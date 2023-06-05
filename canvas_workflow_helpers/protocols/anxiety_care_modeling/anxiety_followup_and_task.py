import arrow
import requests
import json

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import FollowUpRecommendation, ReferRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet

class Anxiety(ValueSet):
    VALUE_SET_NAME = "Anxiety disorder, unspecified"
    ICD10CM = {'F419'}

class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}

TELEHEALTH_NOTE_TYPE_CODE = '448337001'
CARE_NAVIGATION_GROUP_ID = "1df2aa9a-c816-4419-942f-c13ef4a54b0e"
CANVAS_BOT_ID = "5eede137ecfe4124b8b773040e33be14"

APPOINTMENT_CANCELLED_STATUSES = [
    "cancelled",
    "noshowed",
    "entered-in-error",
    "noshow"
]

class FollowUpAnxiety(ClinicalQualityMeasure):

    class Meta:
        title = "Follow Up: Anxiety"
        version = "2023-v01"
        description = "This protocol recommends a follow-up appointment for patients with anxiety along witha Task to schedule the follow up"

        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.APPOINTMENT]
        authors = ["Canvas Example Medical Association (CEMA)"]

        notification_only = True # If True the protocol will no recompute on upload

        condition_date = None

    def get_fhir_api_token(self):
        """ Given the Client ID and Client Secret for authentication to FHIR,
        return a bearer token """

        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET

        token_response = requests.request(
            "POST",
            f'https://{self.instance_name}.canvasmedical.com/auth/token/',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
        )

        if token_response.status_code != 200:
            raise Exception('Unable to get a valid FHIR bearer token')

        return token_response.json().get('access_token')

    def get_care_team_lead(self):
        key = None
        care_teams = self.patient.patient.get('careTeamMemberships', [])
        for care_team in self.patient.patient.get('careTeamMemberships', []):
            if care_team.get('lead'):
                key = care_team.get('staff', {}).get('key')

        return {
            "owner": {
                "reference": f"Practitioner/{key}"
            }
        } if key else {}

    def create_fhir_task(self):
        """ Create a Task to schedule Follow UP"""
        payload = json.dumps({
            "resourceType": "Task",
            "extension": [
                {
                  "url": "http://schemas.canvasmedical.com/fhir/extensions/task-group",
                  "valueReference": {
                    "reference": f"Group/{CARE_NAVIGATION_GROUP_ID}"
                  }
                }
            ],
            "status": "requested",
            "description": "Schedule anxiety follow up",
            "for": {
                "reference": f"Patient/{self.patient.patient_key}"
            },
            "requester": {
                "reference": f"Practitioner/{CANVAS_BOT_ID}"
            },
            **self.get_care_team_lead(),
            "input": [
                {
                  "type": {
                    "text": "label"
                  },
                  "valueString": "Urgent"
                }
            ],
            "restriction": {
                "period": {
                  "end": f'{arrow.now().shift(days=1).format("YYYY-MM-DD")}T00:00:00+00:00'
                }
            }
        })
        response = requests.request(
            "POST",
            f"https://fhir-{self.instance_name}.canvasmedical.com/Task",
            headers={
                'Authorization': f'Bearer {self.token}',
                'accept': 'application/json'
            },
            data=payload
        )

        if response.status_code != 201:
            raise Exception(f"Failed to create FHIR Task status {response.status_code} and payload {payload}")

    def get_fhir_task(self, task_id):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        response = requests.get(
            f"https://fhir-{self.instance_name}.canvasmedical.com/Task?_id={task_id}",
            headers={
                'Authorization': f'Bearer {self.token}',
                'accept': 'application/json'
            }
        )

        if response.status_code != 200:
            raise Exception('Failed to get FHIR Task')

        resources = response.json().get("entry", [])
        if len(resources) == 0:
            return None

        return resources[0].get("resource")

    def update_fhir_task(self, task_id, payload):
        """ Given a Task ID and payload, we will want to mark as complete
        and send it to the FHIR Task Update Endpoint """

        payload['status'] = 'completed'
        if 'note' in payload:
            del payload['note']

        response = requests.request(
            "PUT",
            f'https://fhir-{self.instance_name}.canvasmedical.com/Task/{task_id}',
            headers={
                'Authorization': f'Bearer {self.token}',
                'accept': 'application/json'
            },
            data=json.dumps(payload)
        )

        if response.status_code != 200:
            raise Exception(f"Failed to mark Task as completed with {response.status_code} and payload {payload}")


    def get_follow_up_task(self):
        return self.patient.tasks.filter(
            status='OPEN', title="Schedule anxiety follow up")

    def close_task(self):
        open_tasks = self.get_follow_up_task()
        for task in open_tasks:
            task_id = task['externallyExposableId']
            task_payload = self.get_fhir_task(task_id)
            if task_payload:
                self.update_fhir_task(task_id, task_payload)

    def get_fhir_appointments(self):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        date_string = self.condition_date.format('YYYY-MM-DD')
        response = requests.get(
            (f"https://fhir-{self.instance_name}.canvasmedical.com/"
             f"Appointment?date=ge{date_string}&patient=Patient/{self.patient.patient_key}"),
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            }
        )

        if response.status_code != 200:
            raise Exception("Failed to search Appointments")

        return response.json()

    def in_denominator(self):
        """
        Patients diagnosed with anxiety
        """
        anxiety_condition = self.patient.conditions.find(Anxiety).filter(clinicalStatus='active')

        if len(anxiety_condition):
            self.condition_date = arrow.get(anxiety_condition[-1]['created'])
            return True

        return False

    def in_numerator(self):
        # Patients that have a follow-up appointment scheduled in the future
        telehealth_appts = self.patient.upcoming_appointments.filter(
            startTime__gt=self.condition_date, noteType__code=TELEHEALTH_NOTE_TYPE_CODE
        )

        if any(
            appt
            for appt in telehealth_appts
            if appt.get("status") not in APPOINTMENT_CANCELLED_STATUSES
        ):
            return True

        # if there are no upcoming appointments, we need to make sure they dont have a completed
        # appointment after diagnosis was recorded
        appointments = self.get_fhir_appointments()

        for apt in appointments.get('entry', []):
            apt_code = apt['resource']['appointmentType']['coding'][0]['code']
            start_time = arrow.get(apt['resource']['start'])
            status = apt['resource']['status']
            if (apt_code == TELEHEALTH_NOTE_TYPE_CODE and
                start_time > self.condition_date and
                status not in APPOINTMENT_CANCELLED_STATUSES):
                return True

    def check_if_field_changed(self, model_name, field_name):
        if self.field_changes.get("model_name") != model_name:
            return False

        return field_name in self.field_changes.get("fields", {})

    def compute_results(self):
        """ """
        result = ProtocolResult()

        self.instance_name = self.settings.INSTANCE_NAME
        self.token = self.get_fhir_api_token()

        # Check if a patient has anxiety
        if self.in_denominator():

            if self.in_numerator():
                result.status = STATUS_SATISFIED

                # Let's make sure we mark the Task as Done as well
                self.close_task()
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has been diagnosed with Anxiety"
                result.add_narrative(narrative)

                follow_up_recommendation = FollowUpRecommendation(
                    key="RECOMMEND_FOLLOW_UP",
                    rank=1,
                    button="Follow up",
                    patient=self.patient,
                    title=f"Schedule a One Week Follow Up",
                    narrative=narrative,
                    context={
                        "requested_date": arrow.now().shift(days=7).format("YYYY-MM-DD"),
                        "internal_comment": "Reassess anxiety",
                        "requested_note_type": TELEHEALTH_NOTE_TYPE_CODE,
                    },
                )
                result.add_recommendation(follow_up_recommendation)

                if (self.check_if_field_changed(model_name='condition', field_name='committer_id') and
                    not self.get_follow_up_task()):
                    self.create_fhir_task()

        # if anxiety command was EIE make sure any task is closed
        elif self.check_if_field_changed(model_name='condition', field_name='entered_in_error_id'):
            self.close_task()


        return result

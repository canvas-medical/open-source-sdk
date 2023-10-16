import arrow
import requests
import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import FollowUpRecommendation, ReferRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}


TELEHEALTH_NOTE_TYPE_CODE = '448337001'
CARE_COORDINATION_GROUP_ID = "e3fabb40-1ccc-4bb4-9e64-e813f27bf2e2"
CANVAS_BOT_ID = "5eede137ecfe4124b8b773040e33be14"
APPOINTMENT_CANCELLED_STATUSES = [
    "cancelled",
    "noshowed",
    "entered-in-error",
    "noshow"
]

class FollowUpElevatedPHQ9(ClinicalQualityMeasure):
    class Meta:
        title = "Follow Up: Elevated PHQ-9"
        version = "2023-v01"
        description = "This protocol recommends a follow-up appointment for patients with a PHQ9 score >= 10"
        information = "https://link_to_protocol_information"
        types = ["FollowUp"]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.APPOINTMENT]

        score = None
        interview_time = None

        notification_only = True # If True the protocol will no recompute on upload

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
                    "reference": f"Group/{CARE_COORDINATION_GROUP_ID}"
                  }
                }
            ],
            "status": "requested",
            "description": "Schedule PHQ-9 follow up for patient",
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
        response = self.fhir.create("Task", payload)

        if response.status_code != 201:
            raise Exception(f"Failed to create FHIR Task status {response.status_code} and payload {payload} {response.text} {response.headers}")

    def get_fhir_task(self, task_id):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        response = self.fhir.search("Task", {"_id": task_id})

        if response.status_code != 200:
            raise Exception(f'Failed to get FHIR Task {response.text} {response.headers}')

        resources = response.json().get("entry", [])
        if not len(resources):
            return None

        return resources[0].get("resource")

    def update_fhir_task(self, task_id, payload):
        """ Given a Task ID and payload, we will want to mark as complete
        and send it to the FHIR Task Update Endpoint """

        payload['status'] = 'completed'
        if 'note' in payload:
            del payload['note']

        response = self.fhir.update("Task", task_id, payload)

        if response.status_code != 200:
            raise Exception(f"Failed to mark Task as completed with {response.status_code} and payload {payload} {response.text} {respponse.headers}")

    def get_follow_up_task(self):
        return self.patient.tasks.filter(
            status='OPEN', title="Schedule PHQ-9 follow up for patient")

    def close_task(self):
        open_tasks = self.get_follow_up_task()
        for task in open_tasks:
            task_id = task['externallyExposableId']
            task_payload = self.get_fhir_task(task_id)
            if task_payload:
                self.update_fhir_task(task_id, task_payload)

    def get_fhir_appointments(self):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        response = self.fhir.search("Appointment", 
            {"date": f"ge{self.interview_time[:10]}",
             "patient": f"Patient/{self.patient.patient_key}"}),

        if response.status_code != 200:
            raise Exception(f"Failed to search Appointments {response.text} {response.headers}")

        return response.json()

    def in_denominator(self):
        """
        Patients with most recent PHQ9 score >= 10

        """
        phq9_ques = self.patient.interviews.find(QuestionnairePhq9).last()
        if not phq9_ques:
            return False

        score = next(
            (
                result.get("score")
                for result in phq9_ques.get("results", [])
                if result.get("score") and result.get("score") >= 10
            ),
            None,
        )
        self.score = score
        self.interview_time = phq9_ques['noteTimestamp']
        return bool(score)

    def in_numerator(self):
        # Patients that have a follow-up appointment scheduled in the future
        telehealth_appts = self.patient.upcoming_appointments.filter(
            startTime__gt=self.interview_time, noteType__code=TELEHEALTH_NOTE_TYPE_CODE
        )

        if any(
            appt
            for appt in telehealth_appts
            if appt.get("status") not in APPOINTMENT_CANCELLED_STATUSES
        ):
            return True

        # if there are no upcoming appointments, we need to make sure they dont have a completed
        # appointment after the PHQ-9 was filled out
        appointments = self.get_fhir_appointments()

        for apt in appointments.get('entry', []):
            apt_code = apt['resource']['appointmentType']['coding'][0]['code']
            start_time = arrow.get(apt['resource']['start'])
            status = apt['resource']['status']
            if (apt_code == TELEHEALTH_NOTE_TYPE_CODE and
                start_time > arrow.get(self.interview_time) and
                status not in APPOINTMENT_CANCELLED_STATUSES):
                return True


    def compute_results(self):
        """ """
        result = ProtocolResult()

        self.fhir = FumageHelper(self.settings)
        fhir.get_fhir_api_token()

        # Check if a patient has an elevated PHQ-9
        if self.in_denominator():

            if (self.field_changes.get('model_name') == 'appointment' and
                not self.field_changes.get('created')):
                return result

            if self.in_numerator():
                result.status = STATUS_SATISFIED

                # Let's make sure we mark the Task as Done as well
                self.close_task()
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has completed a PHQ-9 with an elevated score"
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
                        "internal_comment": "Reassess PHQ-9",
                        "requested_note_type": TELEHEALTH_NOTE_TYPE_CODE,
                        "reason_for_visit": "Follow Up Visit"
                    },
                )
                result.add_recommendation(follow_up_recommendation)

                if not self.get_follow_up_task():
                    self.create_fhir_task()


        return result

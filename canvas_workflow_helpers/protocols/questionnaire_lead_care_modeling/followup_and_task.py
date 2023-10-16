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
from canvas_workflow_kit.fhir import FumageHelper

OFFICE_VISIT_NOTE_TYPE_CODE = '308335008'
CARE_COORDINATION_GROUP_ID = "4dfcb0f8-3594-4195-8870-32464756ae47"
CANVAS_BOT_ID = "5eede137ecfe4124b8b773040e33be14"

APPOINTMENT_CANCELLED_STATUSES = [
    "cancelled",
    "noshowed",
    "entered-in-error",
    "noshow"
]

class QuestionnaireIntakeChecklist(ValueSet):
    VALUE_SET_NAME = "Intake Checklist"
    INTERNAL = {"999-999"}

class ScheduleInitialOfficeVisit(ClinicalQualityMeasure):

    class Meta:
        title = "Schedule Initial Visit"
        version = '2023-08-28'
        description = "This protocol recommends a follow-up appointment for patients based on questionnaire responses"

        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.APPOINTMENT]
        authors = ["Canvas Example Medical Association (CEMA)"]

        notification_only = False # If True the protocol will no recompute on upload

        interview_date = None

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
            "description": "Schedule Initial Visit",
            "for": {
                "reference": f"Patient/{self.patient.patient_key}"
            },
            "requester": {
                "reference": f"Practitioner/{CANVAS_BOT_ID}"
            },
            "input": [
                {
                  "type": {
                    "text": "label"
                  },
                  "valueString": "Routine"
                }
            ],
            "restriction": {
                "period": {
                  "end": f'{arrow.now().shift(days=1).isoformat()}'
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
            raise Exception(f'Failed to get FHIR Task {task_id} {response.text} {response.headers}')

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

        response = self.fhir.update("Task", task_id, payload)

        if response.status_code != 200:
            raise Exception(f"Failed to mark Task as completed with {response.status_code} and payload {payload} {response.text} {response.headers}")


    def get_follow_up_task(self):
        return self.patient.tasks.filter(
            status='OPEN', title="Schedule Office Visit")

    def close_task(self):
        open_tasks = self.get_follow_up_task()
        for task in open_tasks:
            task_id = task['externallyExposableId']
            task_payload = self.get_fhir_task(task_id)
            if task_payload:
                self.update_fhir_task(task_id, task_payload)

    def get_fhir_appointments(self):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        date_string = self.interview_date.format('YYYY-MM-DD')
        response = self.fhir.search("Appointment", 
                {"patient": f"Patient/{self.patient.patient_key}",
                 "date": f"ge{date_string}"})

        if response.status_code != 200:
            raise Exception(f"Failed to search Appointments {response.text} {response.headers}")

        return response.json()

    def in_denominator(self):
        """
        Patients have answered Yes to all the questions on the Intake Checklist Questionnaire
        """
        interviews = self.patient.interviews.find(QuestionnaireIntakeChecklist).filter(status='AC')

        if len(interviews):
            most_recent = max(interviews, key=lambda x: x['noteTimestamp'])

            # check that all the response's values are `Yes`
            if not all([r['value'] == 'Yes' for r in most_recent['responses']]):
                return False

            self.interview_date = arrow.get(most_recent['noteTimestamp'])
            return True

        return False

    def in_numerator(self):
        # Patients that have a follow-up appointment scheduled in the future
        office_apts = self.patient.upcoming_appointments.filter(
            startTime__gt=self.interview_date, noteType__code=OFFICE_VISIT_NOTE_TYPE_CODE
        )

        if any(
            appt
            for appt in office_apts
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
            if (apt_code == OFFICE_VISIT_NOTE_TYPE_CODE and
                start_time > self.interview_date and
                status not in APPOINTMENT_CANCELLED_STATUSES):
                return True

    def check_if_field_changed(self, model_name, field_name):
        if self.field_changes.get("model_name") != model_name:
            return False

        return field_name in self.field_changes.get("fields", {})

    def compute_results(self):
        """ """
        result = ProtocolResult()

        self.fhir = FumageHelper(self.settings)
        self.fhir.get_fhir_api_token()

        if self.in_denominator():

            if self.in_numerator():
                result.status = STATUS_SATISFIED

                # Let's make sure we mark the Task as Done as well
                self.close_task()
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                follow_up_recommendation = FollowUpRecommendation(
                    key="RECOMMEND_FOLLOW_UP",
                    rank=1,
                    button="Follow up",
                    patient=self.patient,
                    title=f"Schedule patient for their initial visit",
                    narrative="",
                    context={
                        "requested_date": arrow.now().shift(days=7).format("YYYY-MM-DD"),
                        "requested_note_type": OFFICE_VISIT_NOTE_TYPE_CODE,
                        "reason_for_visit_coding": "INIV30"
                    },
                )
                result.add_recommendation(follow_up_recommendation)

                if not self.get_follow_up_task():
                    self.create_fhir_task()

        # if questionnnaire command was EIE make sure any task is closed
        elif self.check_if_field_changed(model_name='interview', field_name='entered_in_error_id'):
            self.close_task()


        return result

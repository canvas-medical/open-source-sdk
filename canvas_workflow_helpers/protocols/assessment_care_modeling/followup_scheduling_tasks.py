import arrow
import requests

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.internal.integration_messages import create_task_payload
from canvas_workflow_kit.value_set.value_set import ValueSet

class ReAssessment(ValueSet):
    VALUE_SET_NAME = 'Patient Re-Assessment'
    INTERNAL = {'Patient Re-Assessment'}

class SemiAnnualAssessmentFollowUpSchedulingTasks(ClinicalQualityMeasure):

    class Meta:
        title = 'Semi-Annual Assessment Follow Up Scheduling Tasks'
        version = '2023-08-18'
        description = 'Upon Check-In of Semi-Annual Assessment, Create Task for IDT Coordination Team to schedule Goal Alignment and Care Planning Meeting'
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

        notification_only = True

    # This is a hard-coded team identifier that is always responsible calling patients
    # You can normally get this ID from our FHIR Group Search endpoint
    TEAM_IDENTIFIER = '5425152c-d390-4498-9948-fe1eef711fbd'

    CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'

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

    def get_fhir_appointment(self, apt_id):
        """ Given a Apt ID we can perform a FHIR Appointment Read Request"""
        response = requests.get(
            f"https://fhir-{self.instance_name}.canvasmedical.com/Appointment/{apt_id}",
            headers={
                'Authorization': f'Bearer {self.token}',
                'accept': 'application/json'
            }
        )

        if response.status_code != 200:
            raise Exception('Failed to get FHIR Appointment: ', apt_id)

        return response.json()

    def get_checked_in_appointment(self):
        note_change_id = self.field_changes['canvas_id']

        for apt in self.patient.appointments:
            if apt['state']['id'] == note_change_id and apt['state']['state'] == 'CVD':
                return apt['externallyExposableId']


    def get_new_field_value(self, field_name):
        change_context_fields = self.field_changes.get('fields', {})
        if field_name not in change_context_fields:
            return None
        return change_context_fields[field_name][1]

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        changed_model = self.field_changes.get('model_name', '')
        if changed_model == 'notestatechangeevent' and self.get_new_field_value('state') == 'CVD':

            appointment_id = self.get_checked_in_appointment()

            if not appointment_id:
                return result

            self.instance_name = self.settings.INSTANCE_NAME
            self.token = self.get_fhir_api_token()

            fhir_apt = self.get_fhir_appointment(appointment_id)

            if fhir_apt['appointmentType']['coding'][0]['code'] == "Canvas Semi-Annual Assessment":

                payload = dict(
                    patient_key=self.patient.patient['key'],
                    created_by_key=self.CANVAS_BOT_KEY,
                    status="OPEN", # This can be anything from the list ["COMPLETED", "CLOSED", "OPEN"]
                    team_identifier=self.TEAM_IDENTIFIER,
                    due=arrow.now().shift(weeks=1).isoformat(),
                    created=arrow.now().isoformat(),
                    tag=None,
                    labels=["Routine"]
                )

                self.set_updates([
                    create_task_payload(**payload, title=f'Schedule Goal Alignment Session'),
                    create_task_payload(**payload, title=f'Schedule Care Planning Session')
                ])

        return result

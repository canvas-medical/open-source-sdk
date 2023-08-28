import arrow
import requests

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          STATUS_DUE,
                                          STATUS_SATISFIED,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.value_set.value_set import ValueSet
from canvas_workflow_kit.recommendation import InterviewRecommendation


class UMCriteria(ValueSet):
    VALUE_SET_NAME = 'UM Criteria'
    INTERNAL = {'888-123'}

class PayorSpecificQuestionnaireRecommendation(ClinicalQualityMeasure):

    class Meta:
        title = 'Humana UM Criteria'
        version = '2023-08-28'
        description = 'Upon Check-In of Office Visit, recommend a questionnaire based on patient coverage'
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT, CHANGE_TYPE.INTERVIEW]
        notification_only = True

    dates = []

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

    def search_fhir_appointment(self):
        """ Given a Apt ID we can perform a FHIR Appointment Read Request"""
        response = requests.get(
            (f"https://fhir-{self.instance_name}.canvasmedical.com/"
             f"Appointment?patient=Patient/{self.patient.patient_key}"),
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            }
        )

        if response.status_code != 200:
            raise Exception("Failed to search Appointments")

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

    def patient_has_coverage(self, name, _type):
        for coverage in self.patient.patient['coverages']:
            if coverage['isActive'] and coverage['transactorName'] == name and coverage['transactorType'] == _type:
                return True

        return False


    def in_denominator(self):
        """ Patient's that have an appointment/note in a checked-in status """
        appointments = self.search_fhir_appointment()

        dates = []
        for apt in appointments['entry']:
            if apt['resource']['status'] == 'checked-in':
                dates.append(arrow.get(apt['resource']['start']))

        self.dates = dates
        return len(self.dates)

    def in_numerator(self):
        """ Patient's that have the questionnaire in notes in checked-in """
        interviews = self.patient.interviews.find(UMCriteria)

        return any([arrow.get(i['noteTimestamp']) in self.dates for i in interviews])

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE


        changed_model = self.field_changes.get('model_name', '')

        if (changed_model == 'interview' and
            len(self.patient.interviews.find(UMCriteria).filter(
                id=self.field_changes['canvas_id'], status='AC'))
        ):
            # if the Questionnaire was just filled out then mark as satisfied
            result.status = STATUS_SATISFIED
            return result


        # only want to perform recommendation if the patient has a specific coverage
        if self.patient_has_coverage(name="Humana", _type='commercial'):


            self.instance_name = self.settings.INSTANCE_NAME
            self.token = self.get_fhir_api_token()

            # trigger only on a check in action of an appointment
            if changed_model == 'notestatechangeevent' and self.get_new_field_value('state') == 'CVD':

                appointment_id = self.get_checked_in_appointment()
                if not appointment_id:
                    return result

                fhir_apt = self.get_fhir_appointment(appointment_id)

                # if the appointment checked in is an Office Visit
                if fhir_apt['appointmentType']['coding'][0]['code'] == "308335008":

                    # confirm this note doesn't already have this questionnaire
                    interviews = self.patient.interviews.find(UMCriteria)
                    if not any([arrow.get(i['noteTimestamp']) == arrow.get(fhir_apt['start']) for i in interviews]):
                        result.due_in = -1
                        result.status = STATUS_DUE

                        interview_recommendation = InterviewRecommendation(
                                    key='RECOMMEND_UM_CRITERIA',
                                    rank=1,
                                    button='Interview',
                                    patient=self.patient,
                                    questionnaires=[UMCriteria],
                                    title='Complete this form to satisfy Humana’s UM criteria for this patient'
                        )
                        result.add_recommendation(interview_recommendation)
                    else:
                        result.status = STATUS_SATISFIED

                    return result


            # find if this patient has an checked-in notes without the questionnaire
            if self.in_denominator():
                if self.in_numerator():
                    result.status = STATUS_SATISFIED
                    return result
                else:
                    result.due_in = -1
                    result.status = STATUS_DUE

                    interview_recommendation = InterviewRecommendation(
                                key='RECOMMEND_UM_CRITERIA',
                                rank=1,
                                button='Interview',
                                patient=self.patient,
                                questionnaires=[UMCriteria],
                                title='Complete this form to satisfy Humana’s UM criteria for this patient'
                    )
                    result.add_recommendation(interview_recommendation)

        return result

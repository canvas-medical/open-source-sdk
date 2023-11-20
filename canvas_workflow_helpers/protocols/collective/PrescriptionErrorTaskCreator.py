import json
import requests
import arrow

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.internal.integration_messages import create_task_payload

class PrescriptionErrorTaskCreator(ClinicalQualityMeasure):
    class Meta:

        title = 'Prescription error task creator'
        version = '1.0.0'
        description = 'Listens for prescription errors and creates a task.'
        types = ['Notification']
        compute_on_change_types = [CHANGE_TYPE.PRESCRIPTION]
        notification_only = True

    # Replace this with the instance name
    instance_name = 'healthcareinaction'

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

    def get_fhir_medicationrequest(self, prescription_id):
        """ Read FHIR MedicationRequest using prescription ID"""
        response = requests.get(
            (f"https://fumage-{self.instance_name}.canvasmedical.com/"
             f"MedicationRequest/{prescription_id}"),
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            }
        )

        if response.status_code != 200:
            raise Exception("Failed to search MedicationRequest")

        return response.json()

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        # Get the name of the prescription
        prescription_id = self.field_changes.get('external_id')
        sdk_prescription = self.patient.prescriptions.filter(externallyExposableId=prescription_id)
        
        prescription_name = sdk_prescription.records[0]['coding'][0].get('display')
        for d in sdk_prescription.records[0]['coding']:
            if d.get('system') == 'http://www.fdbhealth.com/':
                prescription_name = d.get('display')

        # Get the prescriber key
        fhir_medrequest = self.get_fhir_medicationrequest(prescription_id)
        requester_key = fhir_medrequest['requester']['reference'].split('/')[1]

        # Create a task if the prescription error-ed
        status_change = self.field_changes.get('fields').get('status')

        if status_change and status_change[1] == 'error':
            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=requester_key,
                status="OPEN",
                title= f"Prescription for {prescription_name} encountered an error.",
                assignee_identifier=requester_key,
                due=arrow.now().isoformat(),
                created=arrow.now().isoformat(),
                tag=None,
                labels=[],
            )

            self.set_updates([task_payload])

        return result

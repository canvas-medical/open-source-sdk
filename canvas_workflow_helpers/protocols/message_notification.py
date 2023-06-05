import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification
import requests


class MessageNotification(ClinicalQualityMeasure):
    class Meta:
        title = 'Message Notification'
        version = 'v0.0.1'
        description = 'Listens for message submission and sends a notification.'
        types = ['Notification']
        compute_on_change_types = [CHANGE_TYPE.MESSAGE]
        notification_only = True

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

    def get_fhir_communication(self, message_id):
        """ Given a Communication ID we can perform a FHIR Communication Search Request"""
        request = (f"https://fhir-{self.instance_name}.canvasmedical.com/"
             f"Communication?_id={message_id}")
        response = requests.get(
            request,
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            })

        if response.status_code != 200:
            raise Exception(f"Failed to retrieve FHIR Communicaton with {request}")

        return response.json()['entry'][0]['resource']

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.field_changes['model_name'] == 'messagetransmission':
            self.instance_name = self.settings.INSTANCE_NAME
            self.token = self.get_fhir_api_token()

            canvas_id = self.field_changes.get('fields', {}).get('message_id', None)
            if canvas_id:
                message = self.patient.messages.filter(id=canvas_id[1]).records
                if message:
                    message_id = message[-1]['externallyExposableId']
                    fhir_record = self.get_fhir_communication(message_id)
                    if fhir_record['sender']['reference'].startswith("Practitioner"):
                        send_notification(
                            'https://webhook.site/0a8f7cb1-fcc5-421c-8a99-9c87533cf678',
                            json.dumps(self.get_fhir_communication(message_id)),
                            headers={'Content-Type': 'application/json'})

        return result

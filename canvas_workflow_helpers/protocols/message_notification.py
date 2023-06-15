import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification

class MessagesListener(ClinicalQualityMeasure):
    class Meta:

        title = 'Message Notification'
        version = 'v0.0.1'
        description = 'Listens for message from both staff and patients and sends a notification.'
        types = ['Notification']
        compute_on_change_types = [CHANGE_TYPE.MESSAGE]

        notification_only = True

    # REPLACE this url with your server url which should receive these notifications
    notification_url = 'https://webhook.site/2a5d6d49-f2d3-4cd9-a9e5-273992d81913'
    headers = {'Content-Type': 'application/json'}

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

        # only care about when the record is created for the first time to reduce noise
        if self.field_changes.get("created"):

            model_name = self.field_changes.get("model_name")

            # Message tranmissions only happen when Staff is sending to a patient
            if model_name == 'messagetransmission':
                message_id = (self.field_changes.get('fields')).get('message_id')
                canvas_id = message_id[1]
                message = self.patient.messages.filter(id=canvas_id)[0]
                self.base_payload = {
                    'canvas_patient_key': self.patient.patient['key'],
                    'message_info': message,
                    'fhir_payload': self.get_fhir_communication(message['externallyExposableId'])

                }
                send_notification(self.notification_url, json.dumps(self.base_payload), self.headers)

            # We need to confirm that we are only getting messages patient send to staff
            elif model_name == 'message':
                canvas_id = self.field_changes.get("canvas_id")
                message = self.patient.messages.filter(id=canvas_id)[0]
                if message['sender']['type'] == 'Patient':
                    self.base_payload = {
                        'canvas_patient_key': self.patient.patient['key'],
                        'message_info': message,
                        'fhir_payload': self.get_fhir_communication(message['externallyExposableId'])

                    }
                    send_notification(self.notification_url, json.dumps(self.base_payload), self.headers)

        return result

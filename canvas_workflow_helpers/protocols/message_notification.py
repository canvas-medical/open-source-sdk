import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.fhir import FumageHelper

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

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        # only care about when the record is created for the first time to reduce noise
        if self.field_changes.get("created"):

            model_name = self.field_changes.get("model_name")

            fhir = FumageHelper(self.settings)

            # Message tranmissions only happen when Staff is sending to a patient
            if model_name == 'messagetransmission':
                message_id = (self.field_changes.get('fields')).get('message_id')
                canvas_id = message_id[1]
                message = self.patient.messages.filter(id=canvas_id)[0]

                response = fhir.search("Communication", {'_id': message['externallyExposableId']})
                if response.status_code != 200:
                    raise Exception(f"Failed to find communication {message['externallyExposableId']} {response.text}")

                self.base_payload = {
                    'canvas_patient_key': self.patient.patient['key'],
                    'message_info': message,
                    'fhir_payload': response.json()

                }
                send_notification(self.notification_url, json.dumps(self.base_payload), self.headers)

            # We need to confirm that we are only getting messages patient send to staff
            elif model_name == 'message':
                canvas_id = self.field_changes.get("canvas_id")
                message = self.patient.messages.filter(id=canvas_id)[0]
                if message['sender']['type'] == 'Patient':
                    response = fhir.search("Communication", {'_id': message['externallyExposableId']})
                    if response.status_code != 200:
                        raise Exception(f"Failed to find communication {message['externallyExposableId']} {response.text}")

                    self.base_payload = {
                        'canvas_patient_key': self.patient.patient['key'],
                        'message_info': message,
                        'fhir_payload': response.json()
                    }
                    send_notification(self.notification_url, json.dumps(self.base_payload), self.headers)

        return result

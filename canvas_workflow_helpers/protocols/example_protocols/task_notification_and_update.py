import arrow
import requests
import json

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification

class SyncTask(ClinicalQualityMeasure):
    class Meta:
        title = 'Task Notification'
        version = 'v1.0.0'
        description = 'Listens for the creation of a task and sends a notification to a webhook, on successful notification update the task via FHIR with a comment'
        compute_on_change_types = [CHANGE_TYPE.TASK]
        notification_only = True

    # TODO change these
    URL = 'https://webhook.site/de73cb04-077e-489d-abca-3c31f29ac28d'
    INSTANCE_NAME = 'CHANGE-ME' # change this for the instance you are working on

    def get_fhir_api_token(self):
        """ Given the Client ID and Client Secret for authentication to FHIR,
        return a bearer token """

        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET

        token_response = requests.request(
            "POST",
            f'https://{self.INSTANCE_NAME}.canvasmedical.com/auth/token/',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
        )

        return token_response.json().get('access_token')

    def get_fhir_task(self, task_id):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        return requests.get(
            f"https://fhir-{self.INSTANCE_NAME}.canvasmedical.com/Task?_id={task_id}",
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            }
        )

    def update_fhir_task(self, task_id, payload):
        """ Given a Task ID and payload, we will add an additional comment to the Task
        and send it to the FHIR Task Update Endpoint """

        new_note = {
            "authorReference": {
                "reference": payload['requester']['reference']
            },
            "time": f'{arrow.now()}',
            "text": (f"Task successfuly synced: {self.URL}/{self.patient.patient_key}/view")
        }

        if payload.get('note'):
            payload['note'].append(new_note)
        else:
            payload.update({'note': [new_note]})

        requests.request(
            "PUT",
            f'https://fhir-{self.INSTANCE_NAME}.canvasmedical.com/Task/{task_id}',
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            },
            data=json.dumps(payload)
        )


    def compute_results(self):
        result = ProtocolResult()

        # lets only check and send notification if the Task is created for the first time
        if self.field_changes.get('model_name') == 'task' and self.field_changes.get('created'):

            # field changes will contain the Task ID we can use in FHIR
            task_id = self.field_changes.get('external_id')

            fhir_response = self.get_fhir_task(task_id).json()['entry'][0]['resource']

            # Build the payload we want sent to our webhook
            # We are demoing what a Task looks like in both FHIR and our SDK
            payload = {
                'patient_key': self.patient.patient['key'],
                'patient_name': f"{self.patient.patient['firstName']} {self.patient.patient['lastName']}",
                'fhir_response': fhir_response,
                'sdk_object': self.patient.tasks.filter(externallyExposableId=task_id)[0]
            }
            notification_response = send_notification(
                self.URL, json.dumps(payload), {'Content-Type': 'application/json'})

            if notification_response.status_code == 200:
                # We want to update the task with a comment that the payload was successfully sent
                self.update_fhir_task(task_id, fhir_response)

        return result

from typing import Optional
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    ProtocolResult,
)
from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
import arrow

from canvas_workflow_kit.utils import send_notification
from requests import Response

# Replace with your endpoint URL for a third-party service,
# along with whatever headers are required
ENDPOINT_URL = ''
ENDPOINT_HEADERS = {'Content-Type': 'application/json'}

CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = '3b161f0b-d377-4580-8f7b-d1f9440199cd'


class MessageTriage(ClinicalQualityMeasure):
    class Meta:
        title = 'Message Triage'
        description = (
            'This protocol triggers when a patient sends a message.'
            'This message is sent to a third-party endpoint for processing.'
            'Depending on the response, a task may be created, if the message'
            'is deemed urgent.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/collective'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.MESSAGE]
        references = []

    def get_message_for_change(self) -> Optional[str]:
        '''Gets the message that triggered the protocol, if it was created.'''
        if self.field_changes.get('created'):
            model_name = self.field_changes.get('model_name')
            if model_name == 'message':
                message_id = self.field_changes.get('fields').get('id')
                canvas_id = message_id[1]
                return self.patient.messages.filter(id=canvas_id)[0].get(
                    'content'
                )
        return None

    def send_message_to_endpoint(self, message: str) -> Response:
        # Replace with a payload that matches the endpoint's requirements
        payload = {}
        return send_notification(
            url=ENDPOINT_URL,
            payload=payload,
            headers=ENDPOINT_HEADERS,
        )

    def create_task(self):
        '''Create a task for the patient's care team to triage the message.'''
        task_payload = create_task_payload(
            patient_key=self.patient.patient['key'],
            created_by_key=CANVAS_BOT_KEY,
            status='OPEN',
            title=(
                f'{self.patient.first_name} has sent a potentially '
                f'urgent message.'
            ),
            team_identifier=TEAM_IDENTIFIER,
            due=arrow.now().isoformat(),
            created=arrow.now().isoformat(),
            tag=None,
            labels=['Urgent'],
        )
        self.set_updates([task_payload])

    def post_fumage_communication(self, message: str) -> Response:
        '''Post a message to the patient using the fumage endpoint.'''
        payload = {
            'resourceType': 'Communication',
            'status': 'unknown',
            'sent': arrow.now().isoformat(),
            'received': arrow.now().isoformat(),
            'recipient': [
                {'reference': f"Patient/{self.patient.patient['key']}"}
            ],
            'sender': {'reference': f'Practitioner/{CANVAS_BOT_KEY}'},
            'payload': [
                {
                    'contentString': message,
                }
            ],
        }

        fumage = FumageHelper(self.settings)
        response = fumage.create('Communication', payload)
        if response.status_code != 201:
            raise Exception(
                f"Failed to create Communication with {response.text} and"
                f"correlation-id {response.headers['fumage-correlation-id']}"
            )
        return response

    def process_endpoint_response(
        self, response: Response, result: ProtocolResult
    ) -> None:
        '''
        Insert logic here to process the response from the endpoint
        and determine whether to create a task or send a message
        back to the patient. We are just searching for keywords in the
        message content for the sake of this example.
        '''

        content = self.get_message_for_change() or ''
        if 'hurt' in content:
            self.create_task()
            result.add_narrative(
                'Created a task for the care team to triage the message.'
            )
        elif 'thanks' in content:
            message = 'You are welcome!'
            self.post_fumage_communication(message)
            result.add_narrative('Automatically replied to patient message.')

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        # Uncomment the following line to send the message to the endpoint
        # endpoint_response = self.send_message_to_endpoint(last_message)
        endpoint_response = None

        self.process_endpoint_response(endpoint_response, result)
        return result

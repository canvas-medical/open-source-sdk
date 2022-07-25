import json

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification


class MessageNotification(ClinicalQualityMeasure):
    """
    Protocol that listens for messages and sends a notification once the 'send' button is clicked in the UI.
    """

    class Meta:

        title = 'Message Notification'

        version = 'v0.0.1'

        description = 'Listens for message submission and sends a notification.'

        information = 'https://canvasmedical.com/'

        identifiers = ['MessageNotification']

        types = ['Notification']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.MESSAGE]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

        notification_only = True

    # REPLACE this url with your server url which should receive these notifications
    notification_url = 'https://webhook.site/360e0615-d7c0-430a-9b11-7d781390da36'
    headers = {'Content-Type': 'application/json'}

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE


        if self.field_changes['model_name'] == 'messagetransmission':
            canvas_id = self.field_changes.get('fields', {}).get('message_id', None)
            if canvas_id:
                self.base_payload = {
                    'canvas_patient_key': self.patient.patient['key'],
                    'message_info': self.patient.messages.filter(id=canvas_id[1]).records
                }
                send_notification(self.notification_url, json.dumps(self.base_payload), self.headers)

        return result

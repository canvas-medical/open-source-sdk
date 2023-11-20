import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_NOT_APPLICABLE,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.utils import send_notification


class CommunicateDisqualification(ClinicalQualityMeasure):
    class Meta:
        title = 'Communicate program disqualification'
        version = '1.0.0'
        description = (
            'If program status is updated to disqualified, sends a webhook.'
        )
        types = []
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        notification_only = True

    webhook_url = 'https://webhook.site/93c3e08b-8cee-4c5c-a6ee-63ad8b0b6c1f'

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        interview_id = self.field_changes['canvas_id']

        interview = self.patient.interviews.filter(id=interview_id)[0]

        for response in interview['responses']:
            if (
                response['code'] == 'a214'
                and response['codeSystem'] == 'INTERNAL'
            ):
                payload = {
                    'patient_key': self.patient.patient['key'],
                    'program_status': 'disqualified',
                }
                send_notification(
                    self.webhook_url,
                    json.dumps(payload),
                    headers={'Content-Type': 'application/json'},
                )

        return result

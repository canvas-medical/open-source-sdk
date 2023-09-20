import json

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_NOT_APPLICABLE,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.utils import send_notification


class LabOrderWebhook(ClinicalQualityMeasure):
    class Meta:
        title = 'Send webhook for new lab orders'
        version = '1.0.1'
        description = (
            'If new lab order committed, send a webhook to '
            'home phlebotomy vendor.'
        )
        types = []
        compute_on_change_types = [CHANGE_TYPE.LAB_ORDER]
        notification_only = True

    webhook_url = 'https://webhook.site/93c3e08b-8cee-4c5c-a6ee-63ad8b0b6c1f'

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.field_changes['created'] is True:
            lab_order_id = self.field_changes['canvas_id']

            lab_order = self.patient.lab_orders.filter(id=lab_order_id)[0]

            send_notification(
                self.webhook_url,
                json.dumps(lab_order),
                headers={'Content-Type': 'application/json'},
            )

        return result

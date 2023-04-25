from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention


class EMBannerAlert(ClinicalQualityMeasure):
    """
    A Banner alert that warns the user if they are billing with a 9920* new patient code if there exists a previous note with a 9920* new patient code.
    """

    class Meta:
        title = "E&M New Patient Banner Alert"

        version = "2023-v01"

        description = "A Banner alert that warns the user if they are billing with a 9920* new patient code if there exists a previous note with a 9920* new patient code.."

        information = "https://link_to_protocol_information"

        identifiers = ["EMBannerAlert"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.BILLING_LINE_ITEM]

        authors = ["Canvas Example Medical Association (CEMA)"]

    def has_previous_new_pt_code(self):
        return len(self.patient.billing_line_items.filter(cpt__startswith="9920")) > 1

    def compute_results(self):
        result = ProtocolResult()
        if self.has_previous_new_pt_code():
            result.due_in = -1
            result.status = STATUS_DUE
            result.recommendations.append(
                BannerAlertIntervention(
                    narrative="A new patient E&M code 9920* has been previously billed. Please update the billing footer",
                    placement=[AlertPlacement.ALERT_PLACEMENT_TIMELINE.value],
                    intent=AlertIntent.ALERT_INTENT_ALERT.value,
                )
            )
        return result

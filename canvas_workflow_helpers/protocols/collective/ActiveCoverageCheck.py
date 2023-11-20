from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.constants import AlertIntent, AlertPlacement


class CoverageCheck(ClinicalQualityMeasure):
    class Meta:
        title = 'Active Coverage Check'
        description = (
            'This protocol checks for active coverage for each patient. If '
            'a patient does not have active coverage, a banner will be '
            'displayed on their patient summary and profile.'
        )
        version = '1.0.3'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.COVERAGE]
        references = []

    def in_denominator(self) -> bool:
        """All patients are considered."""
        return True

    def in_numerator(self) -> bool:
        """Check if a patient has active insurance coverage."""
        return any(
            (coverage['isActive'] for coverage in self.patient.coverages)
        )

    def remainder_tasks(self, result: ProtocolResult):
        result.add_recommendation(
            BannerAlertIntervention(
                narrative=(
                    f'{self.patient.first_name} does not have active coverage.'
                ),
                placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value],
                intent=AlertIntent.ALERT_INTENT_WARNING.value,
            )
        )
        result.status = STATUS_DUE
        result.add_narrative('The patient does not have active coverage.')

    def numerator_tasks(self, result: ProtocolResult):
        result.status = STATUS_SATISFIED
        result.add_narrative('The patient has active coverage.')

    def excluded_tasks(self, result: ProtocolResult):
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

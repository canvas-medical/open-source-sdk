from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import HyperlinkRecommendation
from canvas_workflow_kit.value_set.v2021.diagnosis import Diabetes


class GuidelinesLink(ClinicalQualityMeasure):
    class Meta:
        title = 'Guidelines link'
        description = (
            'This protocol recommends providing a hyperlink to the ADA '
            + 'Standard of Care for all patients. This is to ensure '
            + 'frictionless access to protocols and standards of care, '
            + 'which can enhance clinician effectiveness.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.EXTERNAL_EVENT]
        references = []

    def in_denominator(self) -> bool:
        """Checks if a patient has diabetes."""
        return bool(
            self.patient.conditions.find(Diabetes).filter(
                clinicalStatus='active'
            )
        )

    def in_numerator(self) -> bool:
        """No exclusions."""
        return False

    def remainder_tasks(self, result: ProtocolResult):
        result.add_recommendation(
            HyperlinkRecommendation(
                key='diabetes_standards_of_care_2023',
                href='https://doi.org/10.2337/dc23-S001',
                title='Access the guidelines',
                button='ADA link',
            )
        )
        result.status = STATUS_DUE
        result.add_narrative(('Diabetes standards of care 2023.'))

    def numerator_tasks(self, result: ProtocolResult):
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol is not applicable as patient does not have '
                + 'diagnosis of diabetes.'
            )
        )
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

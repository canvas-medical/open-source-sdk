from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    STATUS_DUE,
    ClinicalQualityMeasure,
    ProtocolResult,
)

from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.value_set import ValueSet


class WeightLossProgramStatusQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class WeightLossProgramStatusBanner(ClinicalQualityMeasure):
    class Meta:
        title = 'Display Program Status in Banner'
        description = (
            "This protocol displays a patient's program status in a banner "
            + 'alert on the patient summary for general visibility.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.INTERVIEW,
        ]
        references = []

    def in_denominator(self) -> bool:
        return True

    def in_numerator(self) -> bool:
        return False

    def get_current_status(self):
        """
        Return the most recent status if any based on the
        questionnaire "Program status".
        """

        status_coding_to_display = {
            'a211': 'Intake',
            'a212': 'Condition screening',
            'a213': 'Treatment',
            'a214': 'Disqualified',
        }

        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')

        if not status_interviews:
            return None

        most_recent = max(status_interviews, key=lambda x: x['created'])
        response = most_recent['responses'][0]['code']
        return status_coding_to_display[response]

    def remainder_tasks(self, result: ProtocolResult):
        result.status = STATUS_DUE
        current_status = self.get_current_status()
        if current_status is None:
            narrative_text = 'No program status on file'
        else:
            narrative_text = f'Program status: {current_status}'
        result.add_recommendation(
            BannerAlertIntervention(
                narrative=(narrative_text),
                placement=[
                    'profile',
                    'chart',
                ],
                intent='info',
            )
        )

    def numerator_tasks(self, result: ProtocolResult):
        result.status = STATUS_SATISFIED

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

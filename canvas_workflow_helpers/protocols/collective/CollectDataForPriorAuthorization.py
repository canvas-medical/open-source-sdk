from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import InstructionRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2022.intervention import (
    DietaryRecommendations,
    RecommendationToIncreasePhysicalActivity,
)


class WeightLossPaymentMethodQuestionnire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Payment Method Questionnaire'
    INTERNAL = {'i4'}


class CollectPriorAuthData(ClinicalQualityMeasure):
    class Meta:
        title = 'Prior authorization requirements'
        description = (
            'This protocol recommends that patients who are '
            'insured should be instructed to keep a food '
            'journal for 3 months and exercise twice weekly. '
            'This data can be used for prior authorization purposes.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        references = []

    def is_pending_prior_auth(self) -> bool:
        """
        Check if the patient has a pending prior auth based on payment
        questionnaire.

        Answer codes:
            Cash pay	a411
            Insurance - prior auth pending	a412
            Insurance - prior auth complete	a413
        """
        payment_interviews = self.patient.interviews.find(
            WeightLossPaymentMethodQuestionnire
        ).filter(status='AC')
        if not payment_interviews:
            return False
        most_recent = max(payment_interviews, key=lambda x: x['created'])
        return most_recent['responses'][0]['code'] == 'a412'

    def has_had_exercise_intervention(self) -> bool:
        return bool(
            self.patient.instructions.find(
                RecommendationToIncreasePhysicalActivity
            )
        )

    def has_had_dietary_intervention(self) -> bool:
        return bool(self.patient.instructions.find(DietaryRecommendations))

    def in_denominator(self) -> bool:
        return self.is_pending_prior_auth()

    def in_numerator(self) -> bool:
        return False

    def remainder_tasks(self, result: ProtocolResult):
        # Instruct patient to keep a food journal for 3 months.
        result.add_recommendation(
            InstructionRecommendation(
                key='RECOMMENDATION_FOOD_JOURNAL_INSTRUCTION',
                patient=self.patient,
                instruction=DietaryRecommendations,
                title='Food journaling',
            )
        )
        # Instruct patient to exercise twice weekly.
        result.add_recommendation(
            InstructionRecommendation(
                key='RECOMMENDATION_EXERCISE_INSTRUCTION',
                patient=self.patient,
                instruction=RecommendationToIncreasePhysicalActivity,
                title='Exercise',
            )
        )
        result.add_narrative(
            (
                'Prior authorization requires three months of '
                'food journaling and twice-weekly exercise.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient has been instructed to keep a food '
                'journal for 3 months and exercise twice weekly.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol is not applicable for patients who are not insured.'
        )
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

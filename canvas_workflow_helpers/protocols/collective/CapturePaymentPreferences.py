from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import InterviewRecommendation
from canvas_workflow_kit.value_set import ValueSet


class WeightLossProgramStatusQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class WeightLossPaymentMethodQuestionnire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Payment Method Questionnaire'
    INTERNAL = {'i4'}


class WeightLossPaymentMethod(ClinicalQualityMeasure):
    class Meta:
        title = 'Capture payment preferences'

        description = (
            'This protocol ensures that patients\' payment '
            'preferences are captured.'
        )

        version = '1.0.2'

        information = 'https://canvasmedical.com/gallery'

        identifiers = []

        types = []

        compute_on_change_types = [
            CHANGE_TYPE.INTERVIEW
        ]

    def in_denominator(self):
        """
        Patients whose weight loss status questionnaire
        indicates that they've started treatment.
        """
        # Intake	a211
        # Condition screening	a212
        # Treatment	a213
        # Disqualified	a214
        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')

        if len(status_interviews) == 0:
            return False

        most_recent = max(status_interviews, key=lambda x: x['created'])
        response = most_recent['responses'][0]['code']
        return response == 'a213'

    def in_numerator(self):
        """
        Patients that have already been notified.
        """
        payment_interviews = self.patient.interviews.find(
            WeightLossPaymentMethodQuestionnire
        ).filter(status='AC')

        return bool(payment_interviews)

    def compute_results(self):
        result = ProtocolResult()

        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has been interviewed'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_narrative(
                    f'{self.patient.first_name} has no payment method recorded.'
                )

                result.add_recommendation(
                    InterviewRecommendation(
                        key='WEIGHTLOSS_PAYMENT_INTERVIEW',
                        title='Record payment method',
                        patient=self.patient,
                        button='Interview',
                        questionnaires=[WeightLossPaymentMethodQuestionnire],
                    )
                )
        return result

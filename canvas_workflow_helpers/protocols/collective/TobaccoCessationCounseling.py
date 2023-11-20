from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
    CHANGE_TYPE,
)
from canvas_workflow_kit.recommendation import InstructionRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set.v2021 import (
    TobaccoUseCessationCounseling,
    TobaccoUseScreening,
)
from canvas_workflow_kit.value_set.v2021.diagnosis import Diabetes

SMOKING_QUESTION_CODE = '39240-7'  # Code for smoking status question

'''
Positive response codes for smoking status question:
    Current every day user  449868002
    Current some day user   428041000124106
    Current Heavy tobacco user  428071000124103
    Current Light tobacco user  428061000124105
'''
SMOKING_POSITIVE_RESPONSE_CODES = [
    '449868002',
    '428041000124106',
    '428071000124103',
    '428061000124105',
]


class DiabeticSmokingCessation(ClinicalQualityMeasure):
    class Meta:
        title = 'Smoking Cessation for Diabetics'
        description = (
            'This protocol recommends counseling on smoking cessation every 6 '
            'months for patients who smoke.'
            'This is based on the understanding that smoking cessation '
            'counseling and other forms of treatment should be a routine '
            'component of diabetes care.'
        )
        version = '1.0.12'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.INSTRUCTION,
            CHANGE_TYPE.INTERVIEW,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def in_denominator(self) -> bool:
        if self.patient.conditions.find(Diabetes).filter(
            clinicalStatus='active'
        ):
            return False
        screenings = self.patient.interviews.find(TobaccoUseScreening).filter(
            status='AC'
        )
        if not screenings:
            return False

        most_recent = max(screenings, key=lambda x: x['created'])
        smoking_status_question = next(
            (
                question
                for question in most_recent['questions']
                if question['code'] == SMOKING_QUESTION_CODE
            ),
            None,
        )
        if smoking_status_question is None:
            return False
        else:
            smoking_status_question_id = smoking_status_question[
                'questionResponseId'
            ]

        smoking_status_response = next(
            (
                response
                for response in most_recent['responses']
                if response['questionResponseId'] == smoking_status_question_id
            ),
            None,
        )
        if smoking_status_response is None:
            return False
        else:
            smoking_status_response_code = smoking_status_response['code']
        return smoking_status_response_code in SMOKING_POSITIVE_RESPONSE_CODES

    def in_numerator(self) -> bool:
        last_six_months = Timeframe(self.now.shift(months=-6), self.now)
        counseling_records = self.patient.instructions.find(
            TobaccoUseCessationCounseling
        ).within(last_six_months)
        return bool(counseling_records)

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.add_narrative(
                    (
                        'Patient has been counseled on smoking cessation '
                        'within the last 6 months.'
                    )
                )
                result.status = STATUS_SATISFIED
            else:
                instruction_recommendation = InstructionRecommendation(
                    key='smoking_cessation_counseling',
                    patient=self.patient,
                    instruction=TobaccoUseCessationCounseling,
                    title='Counsel on smoking cessation',
                )
                result.add_recommendation(instruction_recommendation)
                result.status = STATUS_DUE
                result.add_narrative(
                    (
                        f'{self.patient.first_name} is a current smoker and '
                        'should be counseled on smoking cessation.'
                    )
                )
        else:
            result.add_narrative(
                (
                    'Patient is not a current smoker, so smoking '
                    'cessation counseling is not applicable.'
                )
            )
            result.status = STATUS_NOT_APPLICABLE
        return result

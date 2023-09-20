from enum import Enum

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import (
    InterviewRecommendation,
    PerformRecommendation,
    ReferRecommendation,
)
from canvas_workflow_kit.value_set import ValueSet

STOP_BANG_RESPONSE_VALUES = {
    'a311': 0,
    'a312': 1,
    'a321': 0,
    'a322': 1,
    'a331': 0,
    'a332': 1,
    'a341': 0,
    'a342': 1,
    'a351': 0,
    'a352': 1,
    'a361': 0,
    'a362': 1,
    'a371': 0,
    'a372': 1,
    'a381': 0,
    'a382': 1,
}


class WeightLossProgramStatusQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class SleepApnea(ValueSet):
    VALUE_SET_NAME = 'Sleep Apnea'
    ICD10CM = {
        'G4730',  # unspecified
        'G4731',  # Primary central sleep apnea
        'G4732',  # High altitude periodic breathing
        'G4733',  # Obstructive sleep apnea (adult) (pediatric)
        'G4734',  # Idiopathic sleep related nonobstructive hypoventilation
        'G4735',  # Congenital central alveolar hypoventilation syndrome
        'G4736',  # Sleep related hypoventilation
        'G4737',  # Central sleep apnea in conditions classified elsewhere
        'G4739',  # Other
    }


class SleepStudyStatus(Enum):
    NORMAL = 'normal'
    ABNORMAL = 'abnormal'


class SleepStudy(ValueSet):
    """
    All sleep study CPT codes.
    Reference: https://aasm.org/clinical-resources/
    coding-reimbursement/sleep-medicine-codes/
    """

    VALUE_SET_NAME = 'Sleep Study'
    CPT = {
        '95782',
        '95783',
        '95800',
        '95801',
        '95803',
        '95805',
        '95806',
        '95807',
        '95808',
        '95810',
        '95811',
        '94660',
    }


class StopBangQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'STOP-BANG'
    INTERNAL = {'i3'}


class SleepApneaScreening(ClinicalQualityMeasure):
    class Meta:
        title = 'Sleep apnea screening'
        description = (
            'This protocol recommends the use of the STOP-BANG '
            'questionnaire for initial screening of sleep apnea. '
            'If the score is 3 or greater, a sleep study is '
            'recommended. If the sleep study results are abnormal, '
            'a referral to sleep medicine is advised.'
        )
        version = '1.0.13'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.IMAGING_REPORT,
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.REFERRAL_REPORT,
        ]
        references = []

    def stop_bang_score(self):
        last_stop_bang = (
            self.patient.interviews.find(StopBangQuestionnaire)
            .filter(status='AC')
            .last()
        )

        if last_stop_bang:
            stop_bang_score = int(last_stop_bang['results'][0]['narrative'][-1])

            return stop_bang_score

        else:
            return None

    def is_screening(self) -> bool:
        """
        Return the most recent status if any based on the
        questionnaire "Program status".

        Possible values:
            "a211": "Intake",
            "a212": "Condition screening",
            "a213": "Treatment",
            "a214": "Disqualified",
        """

        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')

        if not status_interviews:
            return False

        most_recent = max(status_interviews, key=lambda x: x['created'])
        return most_recent['responses'][0]['code'] == 'a212'

    def had_sleep_study(self) -> bool:
        return bool(self.patient.imaging_reports.find(SleepStudy))

    def has_sleep_apnea(self) -> bool:
        return bool(
            self.patient.conditions.find(SleepApnea).filter(
                clinicalStatus='active'
            )
        )

    def in_denominator(self) -> bool:
        return self.is_screening()

    def in_numerator(self) -> bool:
        stop_bang_score = self.stop_bang_score()
        if stop_bang_score is not None and stop_bang_score <= 3:
            return True
        if self.had_sleep_study() and not self.has_sleep_apnea():
            return True
        return bool(self.patient.referrals.filter(specialty='Sleep Medicine'))

    def remainder_tasks(self, result: ProtocolResult):
        if not self.stop_bang_score() and not self.had_sleep_study():
            result.add_recommendation(
                InterviewRecommendation(
                    key='RECOMMEND_STOP_BANG',
                    patient=self.patient,
                    questionnaires=[StopBangQuestionnaire],
                    narrative=(
                        f'Screen {self.patient.first_name} for sleep apnea '
                        'with the STOP-BANG questionnaire.'
                    ),
                    title='STOP-BANG questionnaire',
                    button='Interview',
                )
            )
        if (
            self.stop_bang_score()
            and self.stop_bang_score() >= 3
            and not self.had_sleep_study()
        ):
            result.add_recommendation(
                PerformRecommendation(
                    key='RECOMMEND_SLEEP_STUDY',
                    patient=self.patient,
                    procedure=SleepStudy,
                    condition=SleepApnea,
                    title='Perform sleep study for STOP-BANG >= 3',
                    narrative=(
                        f'{self.patient.first_name} has a STOP-BANG score of '
                        '3 or greater. Consider performing a sleep study.'
                    ),
                )
            )

        if self.had_sleep_study() and self.has_sleep_apnea():
            result.add_recommendation(
                ReferRecommendation(
                    key='RECOMMEND_REFER_TO_SLEEP_MEDICINE',
                    patient=self.patient,
                    referral=SleepStudy,
                    condition=SleepApnea,
                    title='Refer to Sleep Medicine',
                )
            )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                f'{self.patient.first_name} has been screened for sleep apnea'
                'and either has a low risk or has been referred to '
                'sleep medicine.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative('Protocol not applicable.')
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

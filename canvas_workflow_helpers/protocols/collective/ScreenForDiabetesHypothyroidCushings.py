import arrow
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import LabRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    CushingsSyndrome,
    Diabetes,
    Hyperthyroidism,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class WeightLossProgramStatusQuestionnaire(ValueSet):
    """Questionnaire for Weight Loss Program Status"""

    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class Empty(ValueSet):
    VALUE_SET_NAME = 'Empty'
    CPT = {}


class TSHLaboratoryTest(ValueSet):
    """Tests for TSH (Thyroid Stimulating Hormone)"""

    VALUE_SET_NAME = 'TSH Test'
    CPT = {
        '899',  # TSH
        '36127',  # TSH with Reflex to FT4
        '90896',  # TSH, Pregnancy
    }


class UrineCortisolLaboratoryTest(ValueSet):
    """Tests for Urine Cortisol"""

    VALUE_SET_NAME = 'Urine Cortisol Test'
    CPT = {'82530', '82542'}


class ScreeningForComorbidities(ClinicalQualityMeasure):
    class Meta:
        title = 'Screening for Diabetes, Hypothyroid, and Cushings'
        description = (
            'This protocol recommends screening for diabetes, hypothyroidism, '
            'and Cushings disease in patients who are in the '
            '"Condition screening" status. The recommended tests '
            'are hemoglobin A1c, TSH, and 24-hour urine cortisol, '
            'provided there are no results for these tests from '
            'the past year.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.INTERVIEW,
        ]
        references = []

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

    def missing_tests_in_last_year(self) -> list:
        tests_to_check = [
            Hba1CLaboratoryTest,
            TSHLaboratoryTest,
            UrineCortisolLaboratoryTest,
        ]
        missing_tests = []
        last_year = Timeframe(arrow.now().shift(years=-1), arrow.now())
        for test in tests_to_check:
            had_test = bool(
                self.patient.lab_reports.find(test).within(last_year)
            )
            if not had_test:
                missing_tests.append(test)
        return missing_tests

    def in_denominator(self) -> bool:
        """Patients who are in the "Condition screening" status."""
        return self.is_screening()

    def in_numerator(self) -> bool:
        """Patients who have no missing tests within the past year."""
        return len(self.missing_tests_in_last_year()) == 0

    def remainder_tasks(self, result: ProtocolResult):
        missing_tests = self.missing_tests_in_last_year()
        hg_codes = []
        if Hba1CLaboratoryTest in missing_tests:
            hg_codes.append('496')

        if TSHLaboratoryTest in missing_tests:
            hg_codes.append('899')

        if UrineCortisolLaboratoryTest in missing_tests:
            hg_codes.append('14534')

        result.add_recommendation(
            LabRecommendation(
                key='RECOMMEND_LABS',
                patient=self.patient,
                context={'health_gorilla_order_codes': hg_codes},
                title='Order missing tests',
                condition=Empty,
                lab=Empty
            )
        )
        result.add_narrative(
            (
                'Patient needs screening for poorly controlled diabetes, '
                'hypothyroidism and/or Cushing disease.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient has already been screened for diabetes, '
                'hypothyroidism, and Cushings disease in the past year.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol is not applicable for patients not in '
                '"Condition screening" status.'
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

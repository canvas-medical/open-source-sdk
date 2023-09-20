import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import LabRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import Diabetes


class AlbuminCreatineTest(ValueSet):
    VALUE_SET_NAME = 'Albumin/Creatine Ratio Test'
    LOINC = {'9318-7'}


class LDLTest(ValueSet):
    VALUE_SET_NAME = 'LDL Cholestorol Test'
    LOINC = {'13457-7'}


class PotassiumTest(ValueSet):
    VALUE_SET_NAME = 'Potassium Test'
    LOINC = {'2823-3'}


class DiabeticLabMonitoring(ClinicalQualityMeasure):
    class Meta:
        title = 'Monitoring renal and endocrine labs in diabetics'
        description = (
            'This protocol recommends standard of care lab monitoring '
            'for diabetics including BMP, urine albumin/creatinine '
            'ratio and lipids.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []

        compute_on_change_types = [
            CHANGE_TYPE.LAB_ORDER,
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.CONDITION,
        ]

        references = []

    def missing_tests(self):
        """
        The diabetes tests that the patient has missed.
        """
        missing_tests = []
        tests = [AlbuminCreatineTest, LDLTest, PotassiumTest]
        for test in tests:
            had_test = (
                len(
                    self.patient.lab_reports.find(test).after(
                        arrow.now().shift(years=-1)
                    )
                )
                > 0
            )
            if not had_test:
                missing_tests.append(test)
        return missing_tests

    def in_numerator(self):
        """
        Patients who have no missing tests within the past year.
        """
        return len(self.missing_tests()) == 0

    def in_denominator(self):
        """
        All diabetic patients.
        """
        return self.patient.conditions.find(Diabetes)

    def compute_results(self):
        result = ProtocolResult()

        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has had all their tests.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                missing_tests = self.missing_tests()
                missing_tests_string = ', '.join(
                    [test.VALUE_SET_NAME for test in missing_tests]
                )
                result.add_narrative(
                    (
                        f'{self.patient.first_name} is missing tests: '
                        f'{missing_tests_string}.'
                    )
                )
                for i, missing_test in enumerate(missing_tests):
                    result.add_recommendation(
                        LabRecommendation(
                            key=missing_test.name,
                            patient=self.patient,
                            lab=missing_test,
                            condition=Diabetes,
                            rank=i,
                        )
                    )

        return result

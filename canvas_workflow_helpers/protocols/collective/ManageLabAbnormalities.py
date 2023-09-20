from typing import Optional

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import ReferRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest
from typing import List


class Endocrinology(ValueSet):
    VALUE_SET_NAME = 'Endocrinology'
    SNOMED = {'394583002'}


class TSHLaboratoryTest(ValueSet):
    """Tests for TSH (Thyroid Stimulating Hormone)"""

    VALUE_SET_NAME = 'TSH Test'
    LOINC = {
        '11580-8',
    }


class UrineCortisolLaboratoryTest(ValueSet):
    """Tests for Urine Cortisol"""

    VALUE_SET_NAME = 'Urine Cortisol Test'
    LOINC = {
        '2147-7',
    }


class ManageLabAbnormalities(ClinicalQualityMeasure):
    class Meta:
        title = 'Screening lab abnormalities'
        description = (
            'This protocol outlines the management of patients '
            'with abnormal lab results. If a patient\'s Hemoglobin '
            'A1c is greater than 9, or if their TSH or 24-hour '
            'urine cortisol levels are abnormal, the patient should be '
            'referred back to their primary care provider or a specialist.'
        )
        version = '1.0.2'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
        ]
        references = []

    def last_a1c(self) -> Optional[float]:
        if a1c_tests := self.patient.lab_reports.find(Hba1CLaboratoryTest):
            return float(a1c_tests.last_value())

        return None

    def last_tsh(self) -> Optional[float]:
        if tsh_tests := self.patient.lab_reports.find(TSHLaboratoryTest):
            return float(tsh_tests.last_value())

        return None

    def last_cortisol(self) -> Optional[float]:
        if cortisol_tests := self.patient.lab_reports.find(
            UrineCortisolLaboratoryTest
        ):
            return float(cortisol_tests.last_value())

        return None

    def abnormal_tests(self) -> List[str]:
        abnormal_tests = []
        if last_a1c := self.last_a1c():
            if last_a1c > 9:
                abnormal_tests.append('hemoglobin A1c')
        if last_tsh := self.last_tsh():
            if last_tsh > 5:
                abnormal_tests.append('TSH')
        if last_cortisol := self.last_cortisol():
            if last_cortisol > 100:
                abnormal_tests.append('24-hour urine cortisol')
        return abnormal_tests

    def in_denominator(self) -> bool:
        return len(self.abnormal_tests()) > 0

    def in_numerator(self) -> bool:
        referral_to_pcp_or_alternate_provider = (
            False  # Add referral logic if needed
        )
        return referral_to_pcp_or_alternate_provider

    def remainder_tasks(self, result: ProtocolResult):
        result.add_recommendation(
            ReferRecommendation(
                key='RECOMMEND_REFERRAL_TO_PCP_OR_SPECIALIST',
                referral=Endocrinology,
                patient=self.patient,
                condition=None,
                title='Refer to endocrinologist.',
            )
        )
        result.add_narrative(
            (
                f'{self.patient.first_name} should be referred to an '
                f'endocrinologist for abnormal tests: '
                f'{", ".join(self.abnormal_tests())}.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient with abnormal lab results has been referred '
                'back to PCP or specialist.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol is not applicable to patients with normal lab results.'
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

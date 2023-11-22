from typing import Optional

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
from canvas_workflow_kit.value_set.v2017 import (
    HdlCLaboratoryTest,
    TriglyceridesLaboratoryTest,
)
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Diabetes,
    HeartFailure,
    IschemicHeartDiseaseOrOtherRelatedDiagnoses,
)
from canvas_workflow_kit.value_set.v2021.lab_test import (
    Hba1CLaboratoryTest,
)
from canvas_workflow_kit.value_set.v2021.medication import (
    PharmacologicTherapyForHypertension,
)

HIGH_RISK_RACE_CODES = {
    'American Indian or Alaska Native': '1002-5',
    'Asian': '2028-9',
    'Black or African American': '2054-5',
    'Native Hawaiian or Other Pacific Islander': '2076-8',
    'Hispanic or Latino': '2135-2',
}

HIGH_RISK_ETHNICITY_CODES = {
    '2135-2': 'Hispanic or Latino',
}


class PCOS(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that
    identify patients who have a diagnosis of poly cystic ovary syndrome (PCOS).

    **Data Element Scope:** This value set may use
    the Quality Data Model (QDM) category related to Diagnosis.

    **Inclusion Criteria:** Includes only relevant concepts
    associated with identifying patients who have PCOS.

    **Exclusion Criteria:** None.
    """

    VALUE_SET_NAME = 'PCOS / Polycystic Ovary Syndrome'
    ICD10CM = {'E282', 'N97'}
    SNOMEDCT = {'237055002'}


class FamilialDiabetes(ValueSet):
    """Familial history of diabetes."""

    VALUE_SET_NAME = 'Familial Diabetes'

    ICD10CM = {
        'Z833',
    }


class Prediabetes(ValueSet):
    """
    Characterized by blood glucose levels that are higher than normal but not
    yet high enough to be classed as diabetes.
    Indicates a relatively high risk for the future development of diabetes.
    """

    VALUE_SET_NAME = 'Prediabetes'
    ICD10CM = {'R7303'}
    SNOMEDCT = {'714628002'}


class DiabetesScreening(ClinicalQualityMeasure):
    class Meta:
        title = 'Diabetes screening'

        description = (
            'This protocol recommends screening all '
            'patients over the age of 35 for prediabetes '
            'or diabetes using an A1c test every 3 years, '
            'unless they have a prior diagnosis. Patients '
            'of any age without a prediabetes or diabetes '
            'diagnosis should also be screened if they '
            'meet specific criteria: a BMI of 23 or '
            'higher for Asian Americans, or a BMI of 25 '
            'or more for other populations, combined '
            'with at least one additional risk factor '
            'such as a family history of diabetes, '
            'belonging to a high-risk ethnicity, or '
            'having conditions like cardiovascular '
            'disease or polycystic ovary syndrome. '
            'Regular screenings should begin by age 35, '
            'and for those with normal results, '
            'retesting every 3 years or sooner if risk '
            'factors change, is advised.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.PATIENT,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.VITAL_SIGN,
        ]
        references = ['https://doi.org/10.2337/dc22-S002']

    def get_bmi(self) -> Optional[float]:
        last_weight_oz = self.patient.vital_signs.filter(
            sign='weight'
        ).last_value()
        last_height_in = self.patient.vital_signs.filter(
            sign='height'
        ).last_value()
        if not last_weight_oz or not last_height_in:
            return None
        last_height_in = float(last_height_in)
        last_weight_oz = float(last_weight_oz)
        return (last_weight_oz / last_height_in**2) * 43.9375

    def get_last_lab(self, lab_value_set: ValueSet) -> Optional[str]:
        tests = self.patient.lab_reports.find(lab_value_set)
        return tests.last_value()

    def in_denominator(self) -> bool:
        """
        Determines if a patient should be considered for diabetes
        screening based on a set of criteria.

        The patient should not have been diagnosed with diabetes
        or prediabetes, and should either be above the age of 35, or of any
        age with certain risk factors.

        These risk factors include a BMI of 25 or higher (or 23 or higher
        if of Asian descent), a family history of diabetes, a history of
        cardiovascular disease or high blood pressure, an HDL cholesterol level
        of 35 mg/dL or lower, a triglyceride level of 250 mg/dL or higher,
        having PCOS, or being of certain ethnicities:
        (African American, Hispanic, American Indian,
        Asian American, or Pacific Islander).
        """
        # Check if patient has been diagnosed with diabetes or prediabetes
        if self.patient.conditions.find(Diabetes | Prediabetes).filter(
            clinicalStatus='active'
        ):
            return False
        # Check if patient is above the age of 35
        if self.patient.age > 35:
            return True
        # Check patient BMI, default to True if no BMI is found
        if not self.get_bmi():
            return True
        if (
            self.get_bmi() >= 25
            or (
                self.get_bmi() >= 23
                and self.patient.patient['biologicalRaceCode']
                == HIGH_RISK_RACE_CODES['Asian']
            )
        ) and (
            self.patient.conditions.find(FamilialDiabetes).filter(
                clinicalStatus='active'
            )
            or self.patient.conditions.find(
                IschemicHeartDiseaseOrOtherRelatedDiagnoses
            ).filter(clinicalStatus='active')
            or self.patient.conditions.find(HeartFailure).filter(
                clinicalStatus='active'
            )
            or self.patient.conditions.find(PCOS).filter(
                clinicalStatus='active'
            )
            or self.patient.medications.find(
                PharmacologicTherapyForHypertension
            )
            or (
                float(self.get_last_lab(HdlCLaboratoryTest)) <= 35
                if self.get_last_lab(HdlCLaboratoryTest)
                else False
            )
            or (
                float(self.get_last_lab(TriglyceridesLaboratoryTest)) >= 250
                if self.get_last_lab(TriglyceridesLaboratoryTest)
                else False
            )
            or any(
                self.patient.patient['biologicalRaceCode']
                == high_risk_race_code
                for high_risk_race_code in HIGH_RISK_RACE_CODES.values()
            )
            or any(
                self.patient.patient['culturalEthnicityCode']
                == high_risk_ethnicity_code
                for high_risk_ethnicity_code in HIGH_RISK_ETHNICITY_CODES.values()
            )
        ):
            return True

    def in_numerator(self) -> bool:
        """
        Check if a patient has already had an A1C test in the past 3 years.
        """
        last_three_years = Timeframe(arrow.now().shift(years=-3), arrow.now())
        a1c_tests = self.patient.lab_reports.find(Hba1CLaboratoryTest).within(
            last_three_years
        )
        return bool(a1c_tests)

    def numerator_tasks(self, result: ProtocolResult):
        # Add a narrative to the patient's record
        result.add_narrative(
            (f'{self.patient.first_name} has been screened recently.')
        )
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):
        # Recommend an A1C test to screen for diabetes / prediabetes.
        result.add_recommendation(
            LabRecommendation(
                key='a1c_test',
                patient=self.patient,
                condition=Diabetes,
                lab=Hba1CLaboratoryTest,
                title='Order Hemoglobin A1c',
            )
        )
        result.status = STATUS_DUE
        result.due_in = -1
        result.add_narrative(
            (f'{self.patient.first_name} should be screened for diabetes.')
        )

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            "The patient doesn't need a screening for diabetes / prediabetes."
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

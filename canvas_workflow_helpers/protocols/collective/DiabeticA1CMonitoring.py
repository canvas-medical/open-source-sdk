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
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Cancer,
    CerebrovascularDiseaseStrokeTia,
    ChronicLiverDisease,
    CoronaryArteryDiseaseNoMi,
    Diabetes,
    EndStageRenalDisease,
    HeartFailure,
    MyocardialInfarction,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest
from dateutil.relativedelta import relativedelta


class ChronicKidneyDiseaseStage3Onwards(ValueSet):
    VALUE_SET_NAME = ('Chronic Kidney Disease Stage 3 Onwards',)
    ICD10CM = {'N1830', 'N1831', 'N1832', 'N184', 'N185'}


''' 
Patients with reduced life expectancy include those with age 80+ 
or one of the following diagnoses: 

CKD stage 3 onwards,
coronary artery disease, 
heart failure, 
peripheral vascular disease, 
advanced liver disease, 
or advanced/terminal cancer.'
'''
LimitedLifeExpectancy = (
    HeartFailure
    | ChronicLiverDisease
    | CerebrovascularDiseaseStrokeTia
    | MyocardialInfarction
    | CoronaryArteryDiseaseNoMi
    | EndStageRenalDisease
    | Cancer
    | ChronicKidneyDiseaseStage3Onwards
)


class DiabeticA1CMonitoring(ClinicalQualityMeasure):
    class Meta:
        title = 'A1c Monitoring in Diabetics'
        description = (
            'This protocol outlines the frequency of A1c monitoring in '
            'patients with diabetes. It recommends checking '
            'A1c every 3 months for uncontrolled patients '
            'and every 6 months for controlled patients. '
            'Uncontrolled is defined as A1c >= 7 for standard patients '
            'or A1c >= 8 for patients with '
            'reduced life expectancy, which includes those aged 80+ '
            'or with certain diagnoses.'
        )
        version = '1.0.8'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.PATIENT,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def in_denominator(self) -> bool:
        return bool(self.patient.conditions.find(Diabetes))

    def in_numerator(self) -> bool:
        reduced_life_expectancy = self.patient.age >= 80 or bool(
            self.patient.conditions.find(LimitedLifeExpectancy)
        )
        a1c_tests = self.patient.lab_reports.find(Hba1CLaboratoryTest)
        last_a1c = a1c_tests.last_value()
        if not last_a1c:
            return False
        last_a1c = float(last_a1c)
        if (reduced_life_expectancy and last_a1c >= 8) or (
            not reduced_life_expectancy and last_a1c >= 7
        ):
            return bool(a1c_tests.after(arrow.now() - relativedelta(months=3)))
        else:
            return bool(a1c_tests.after(arrow.now() - relativedelta(months=6)))

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.add_narrative('Protocol satisfied by recent A1C test.')
                result.status = STATUS_SATISFIED
            else:
                result.add_recommendation(
                    LabRecommendation(
                        key='a1c_test',
                        patient=self.patient,
                        condition=Diabetes,
                        lab=Hba1CLaboratoryTest,
                        title='Order Hemoglobin A1c',
                    )
                )
                result.add_narrative(
                    f'{self.patient.first_name} is due for Hemoglobin A1c.'
                )
                result.status = STATUS_DUE
        else:
            result.add_narrative(
                (
                    'Protocol not applicable based on absence '
                    'of diabetes diagnosis.'
                )
            )
            result.status = STATUS_NOT_APPLICABLE
        return result

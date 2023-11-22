import arrow

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import (
    LabRecommendation,
)
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest
from canvas_workflow_kit.value_set.v2022.medication import Antipsychotic

class Lipids(ValueSet):
    VALUE_SET_NAME = 'Lipid panel'
    LOINC = {'13457-7'}

class AntipsychoticBloodwork(ClinicalQualityMeasure):
    class Meta:
        title = 'Routine bloodwork for antipsychotics'
        description = (
            'Recommend ordering yearly A1C and lipid panels for patients on antipsychotics.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.APPOINTMENT,
            CHANGE_TYPE.MEDICATION,
        ]
        references = []

    def is_on_antipsychotics(self) -> bool:
        '''Returns True if the patient is on an antipsychotic medication'''
        return bool(self.patient.medications.find(Antipsychotic).filter(status='active'))

    def has_had_test_within(self, test: ValueSet, timeframe: Timeframe) -> bool:
        '''
        Returns True if the patient has had the given test within the given timeframe.
        '''
        return bool(self.patient.lab_reports.find(test).within(timeframe))

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if not self.is_on_antipsychotics():
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative('Patient is not on antipsychotics.')
            return result

        last_year = Timeframe(arrow.now().shift(years=-1), arrow.now())
        tests = [
            (Hba1CLaboratoryTest, 'RECOMMEND_A1C_LAB', 'Order A1C test', 'A1C Test'),
            (Lipids, 'RECOMMEND_LIPID_PANEL_LAB', 'Order lipid panel', 'Lipid Panel'),
        ]
        if tests_needed := [
            test for test in tests if not self.has_had_test_within(test[0], last_year)
        ]:
            result.status = STATUS_DUE
            for lab, key, title, test_name in tests_needed:
                recommendation = LabRecommendation(
                    key=key,
                    patient=self.patient,
                    lab=lab,
                    condition=Antipsychotic,
                    title=title,
                    button='Order',
                )
                narrative = (
                    f'Patient is on antipsychotics and has not had {test_name} in the last year.'
                )
                result.add_recommendation(recommendation)
                result.add_narrative(narrative)
        else:
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative('Patient has had all relevant bloodwork.')
        return result

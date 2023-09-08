import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes

class Qsymia(ValueSet):
    FDB = {'574991'}

class Contrave(ValueSet):
    FDB = {'582584'}

class Obesity(ValueSet):
    VALUE_SET_NAME = "Obesity, unspecified"
    ICD10CM = {'E669'}

EncounterForObesityCondition = {
    "code": "E669",
    "system": "ICD-10",
    "display": "Obesity, unspecified",
}

class ObesityPrescribeRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Consider prescribing Obesity medication'
        version = '2023-v1'
        description = 'Recommend Prescription for obesity'
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.MEDICATION]
        notification_only = True # add this so your protocol doesn't try to recompute on upload

    condition_date = None

    def in_denominator(self):
        """ Find patient with an active diagnosis for obesity"""
        return len(self.patient.conditions.find(Obesity).filter(clinicalStatus='active'))

    def in_numerator(self):
        """See if they already have an active medication"""
        return len(self.patient.prescriptions.find(Qsymia | Contrave ).filter(status='active'))

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.in_denominator():

            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                result.add_narrative('This patient has been diagnosed with Obesity. Consider one of the following medications.')
                prescribe_recommendation = PrescribeRecommendation(
                        key='RECOMMEND_QSYMIA_PRESCRIPTION',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Qsymia,
                        title='Prescribe Qsymia',
                        context={
                            'conditions': [[EncounterForObesityCondition]],
                            'sig_original_input': 'Take one capsule once a day in the morning',
                            'duration_in_days': 30,
                            'dispense_quantity': 30,
                            'dosage_form': 'capsule',
                            'count_of_refills_allowed': 0,
                            'generic_substitutions_allowed': True,
                    }
                )
                result.add_recommendation(prescribe_recommendation)
                prescribe_recommendation = PrescribeRecommendation(
                        key='RECOMMEND_CONTRAVE_PRESCRIPTION',
                        rank=2,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Contrave,
                        title='Prescribe Contrave',
                        context={
                            'conditions': [[EncounterForObesityCondition]],
                            'sig_original_input': 'Take one tablet once a day in the morning',
                            'duration_in_days': 30,
                            'dispense_quantity': 30,
                            'dosage_form': 'tablet',
                            'count_of_refills_allowed': 0,
                            'generic_substitutions_allowed': True,
                    }
                )
                result.add_recommendation(prescribe_recommendation)

        return result

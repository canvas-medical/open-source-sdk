import json
import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes

class Victoza(ValueSet):
    FDB = {'578861'}

class PHQ9(ValueSet):
    VALUE_SET_NAME = 'PHQ-9'
    LOINC = {'44249-1'}

class DiabetesRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Diabetes Recommendations'
        version = 'v1.0.0'
        description = 'Recommend GLP-1 and PHQ-9 for diabetics'
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.PRESCRIPTION]
        notification_only = True # add this so your protocol doesn't try to recompute on upload

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        now = arrow.now()
        within_three_months = Timeframe(start=now.shift(months=-3), end=now)

        # this patient has been diagnosed with Diabetes
        diabetes_conditions = self.patient.conditions.find(Diabetes)
        if diabetes_conditions:
            presribe_rec_needed = (not self.patient.prescriptions.find(Victoza).filter(status='active'))
            interview_rec_needed = (not self.patient.interviews.find(PHQ9).within(within_three_months))

            # if patient has diabetes and the need either the prescription or interview filled out
            # then they are due for the protocol. If both are filled out then protocol is satisfied
            if presribe_rec_needed or interview_rec_needed:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_narrative(f"{self.patient.patient['firstName']} has been diagnosed with Diabetes. Consider the following steps")
            else:
                result.status = STATUS_SATISFIED
                return result

            # Recommend a Victoza prescribe if patient does not have an active one
            if presribe_rec_needed:

                # create list of diabetes conditions to add to indications on prescribe command
                conditions = []
                for condition in diabetes_conditions:
                    for coding in condition.get('coding', []):
                        if coding.get('system') == 'ICD-10':
                            conditions.append({
                                'code': coding.get('code'),
                                'system': coding.get('system'),
                                'display': coding.get('display')
                            })

                prescribe_recommendation = PrescribeRecommendation(
                        key='RECOMMEND_VICTOZA_PRESCRIPTION',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Victoza,
                        title='Prescribe a GLP-1',
                        context={
                            'conditions': [conditions],
                            'sig_original_input': 'inject 0.6mg daily for 1 week, then increase to 1.2mg daily',
                            'duration_in_days': 30,
                            'dispense_quantity': 1,
                            'dosage_form': '3 mL syringe',
                            'count_of_refills_allowed': 3,
                            'generic_substitutions_allowed': True,
                            'note_to_pharmacist': ''
                    }
                )
                result.add_recommendation(prescribe_recommendation)

            # Want to recommend PHQ-9 questionnaire if one hasnt been filled out in the last 3 months
            if interview_rec_needed:
                interview_recommendation = InterviewRecommendation(
                            key='RECOMMEND_PHQ9_DIABETES',
                            rank=1,
                            button='Interview',
                            patient=self.patient,
                            questionnaires=[PHQ9],
                            title='Diabetes and depression are often co-morbid'
                )
                result.add_recommendation(interview_recommendation)


        return result

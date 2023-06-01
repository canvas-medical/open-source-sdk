import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes

class Fluoxetine(ValueSet):
    FDB = {'287344'}

class Citalopram(ValueSet):
    FDB = {'222717'}

class Sertraline(ValueSet):
    FDB = {'259152'}

class Depression(ValueSet):
    VALUE_SET_NAME = "Depression, unspecified"
    ICD10CM = {'F32A'}

class ReasonForPrescribing(ValueSet):
    VALUE_SET_NAME = 'Reason for Prescribing'
    INTERNAL = {'PRESCCOM'}

EncounterForDepressionCondition = {
    "code": "F32A",
    "system": "ICD-10",
    "display": "Depression, unspecified",
}

class DepressionPrescribeRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Depression: Prescribe Recommendations'
        version = '2023-v1'
        description = 'Recommend Prescription for depression'
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.MEDICATION, CHANGE_TYPE.INTERVIEW]
        notification_only = False # add this so your protocol doesn't try to recompute on upload

    condition_date = None
    prescribed_recommended_meds = False
    prescibed_other_meds = False

    def in_denominator(self):
        """ Find patient with an active diagnosis for depression"""
        diabetes_conditions = self.patient.conditions.find(Depression).filter(clinicalStatus='active')

        if len(diabetes_conditions):
            self.condition_date = arrow.get(diabetes_conditions[-1]['created'])
            return True

        return False

    def in_numerator(self):
        """Look through prescriptions to recomend one or a questionnaire"""
        active_prescriptions = self.patient.prescriptions.filter(status='active')

        # Have any of the active medications been one of the ones we want to recommend?
        prescribed_recommended_meds = active_prescriptions.find(Fluoxetine | Citalopram | Sertraline)

        for med in prescribed_recommended_meds:
            med_id = med['medicationId']
            medication = self.patient.medications.filter(id=med_id)[0]
            if arrow.get(medication['created']) > self.condition_date:
                self.prescribed_recommended_meds = True
                return True

        # Filled out prescribe questionnaire
        interviews = self.patient.interviews.find(ReasonForPrescribing).filter(created__gt=self.condition_date)
        if len(interviews):
            return True

        # Look to see if an active medication was prescribed after the depression diagnosis
        # TODO get the list of specific drugs from Mat

        for active_prescription in active_prescriptions:
            med_id = active_prescription['medicationId']
            medication = self.patient.medications.filter(id=med_id)[0]
            if arrow.get(medication['created']) > self.condition_date:
                self.prescibed_other_meds = True
                return False

        return False


    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.in_denominator():

            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                # recommend a questionnaire to explain why they prescribed other meds
                if self.prescibed_other_meds:
                    result.add_narrative(f'{self.patient.first_name} has been prescribed with a non recommended medication')
                    interview_recommendation = InterviewRecommendation(
                                key='RECOMMEND_PRESCRIBE_REASONING_QUES',
                                rank=1,
                                button='Explain',
                                patient=self.patient,
                                questionnaires=[ReasonForPrescribing],
                                title='Please fill out reasoning'
                    )
                    result.add_recommendation(interview_recommendation)

                # Recommend a Victoza prescribe if patient does not have an active one
                elif not self.prescribed_recommended_meds:
                    result.add_narrative(f'{self.patient.first_name} has been diagnosed with depression, consider prescribing one of the following medications')
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_FLUOXETINE_PRESCRIPTION',
                            rank=1,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Fluoxetine,
                            title='Prescribe Fluoxetine',
                            context={
                                'conditions': [[EncounterForDepressionCondition]],
                                'sig_original_input': 'Take once a day with or without food',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'capsule',
                                'count_of_refills_allowed': 0,
                                'generic_substitutions_allowed': True,
                                'note_to_pharmacist': 'Contact with any questions'
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_CITALOPRAM_PRESCRIPTION',
                            rank=2,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Citalopram,
                            title='Prescribe Citalopram',
                            context={
                                'conditions': [[EncounterForDepressionCondition]],
                                'sig_original_input': 'Take once a day with or without food',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'tablet',
                                'count_of_refills_allowed': 0,
                                'generic_substitutions_allowed': True,
                                'note_to_pharmacist': 'Contact with any questions'
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_SERTRALINE_PRESCRIPTION',
                            rank=3,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Sertraline,
                            title='Prescribe Sertraline',
                            context={
                                'conditions': [[EncounterForDepressionCondition]],
                                'sig_original_input': 'Take once a day with or without food',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'tablet',
                                'count_of_refills_allowed': 0,
                                'generic_substitutions_allowed': True,
                                'note_to_pharmacist': 'Contact with any questions'
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)


        return result

import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes

class Imitrex(ValueSet):
    FDB = {'214702'}

class Nurtec(ValueSet):
    FDB = {'602405'}

class Ubrelvy(ValueSet):
    FDB = {'601775'}

class Migraine(ValueSet):
    VALUE_SET_NAME = "Migraine, unspecified, not intractable, without status migrainosus"
    ICD10CM = {'G43909'}

class MedicationRecQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Medication Recommendations'
    INTERNAL = {'medrec123'}

EncounterForMigraineCondition = {
    "code": "G43909",
    "system": "ICD-10",
    "display": "Migraine, unspecified, not intractable, without status migrainosus",
}

class MigrainePrescribeRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Migraine: Prescribe Recommendations'
        version = '2023-v1'
        description = 'Recommend Prescription for Migraine'
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.INTERVIEW]
        notification_only = False # add this so your protocol doesn't try to recompute on upload

    condition_date = None
    prescribed_recommended_meds = False
    interview_filled_out = False

    def in_denominator(self):
        """ Find patient with an active diagnosis"""
        conditions = self.patient.conditions.find(Migraine).filter(clinicalStatus='active')

        if len(conditions):
            self.condition_date = arrow.get(conditions[-1]['created'])
            return True

        return False

    def in_numerator(self):
        """Look through prescriptions to recomend one or a questionnaire"""
        active_prescriptions = self.patient.prescriptions.filter(status='active')

        # Have any of the active medications been one of the ones we want to recommend?
        prescribed_recommended_meds = active_prescriptions.find(Imitrex | Nurtec | Ubrelvy)

        for med in prescribed_recommended_meds:
            med_id = med['medicationId']
            medication = self.patient.medications.filter(id=med_id)[0]
            if arrow.get(medication['created']) > self.condition_date:
                self.prescribed_recommended_meds = True
                break

        # Filled out prescribe questionnaire
        interviews = self.patient.interviews.find(MedicationRecQuestionnaire).filter(created__gt=self.condition_date)
        if len(interviews):
            self.interview_filled_out = True

        return self.interview_filled_out and self.prescribed_recommended_meds 


    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                result.add_narrative('Patient has recently been diagnosed with migraines. Consider prescribing one of the following medications. ')
                
                if not self.prescribed_recommended_meds:
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_IMITREX_PRESCRIPTION',
                            rank=1,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Imitrex,
                            title='Prescribe Imitrex',
                            context={
                                'conditions': [[EncounterForMigraineCondition]],
                                'sig_original_input': 'Take as needed to relieve migraine symptoms',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'tablet',
                                'count_of_refills_allowed': 1,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_NURTEC_PRESCRIPTION',
                            rank=2,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Nurtec,
                            title='Prescribe Nurtec ODT',
                            context={
                                'conditions': [[EncounterForMigraineCondition]],
                                'sig_original_input': 'Take daily to prevent migraines',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'Tablet',
                                'count_of_refills_allowed': 1,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)
                    prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_UBRELVY_PRESCRIPTION',
                            rank=3,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Ubrelvy,
                            title='Prescribe Ubrelvy',
                            context={
                                'conditions': [[EncounterForMigraineCondition]],
                                'sig_original_input': 'Take as needed to relieve migraine symptoms',
                                'duration_in_days': 30,
                                'dispense_quantity': 30,
                                'dosage_form': 'Tablet',
                                'count_of_refills_allowed': 1,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(prescribe_recommendation)

                
                if not self.interview_filled_out:
                    interview_recommendation = InterviewRecommendation(
                                key='RECOMMEND_PRESCRIBE_REASONING_QUES',
                                rank=4,
                                button='Interview',
                                patient=self.patient,
                                questionnaires=[MedicationRecQuestionnaire],
                                title='Please fill out medication recommendation questionnaire'
                    )
                    result.add_recommendation(interview_recommendation)
        else:
            result.add_narrative('Patient does not have an active migraine diagnosis')


        return result

import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes

class Hydrocodone(ValueSet):
    FDB = {'476332'}

class OswestryQuestionnaire(ValueSet):
    VALUE_SET_NAME = "Oswestry Low Back Pain Disability"
    SNOMEDCT = {'408492009'}

EncounterForLowBackPain = {
    "code": "M5450",
    "system": "ICD-10",
    "display": "Low back pain, unspecified",
}

class PainReliefPrescribeRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Prescribe Pain Relief'
        version = '2023-08-28'
        description = 'Recommend Prescription for pain relief based on questionnnaire results'
        types = []
        compute_on_change_types = [CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.MEDICATION, CHANGE_TYPE.INTERVIEW]
        notification_only = True # add this so your protocol doesn't try to recompute on upload

    def in_denominator(self):
        """ Find patient with severe pain"""
        interviews = self.patient.interviews.find(OswestryQuestionnaire).filter(status='AC')

        if len(interviews):
            most_recent = max(interviews, key=lambda x: x['noteTimestamp'])

            # check the responses for "The pain is the worst imaginable at the moment"
            # or "The pain is very severe at the moment"
            return any([r['value'] in ('The pain is very severe at the moment', 'The pain is the worst imaginable at the moment')
                for r in most_recent['responses']]):

        return False

    def in_numerator(self):
        """Active medication with Hydrocodone"""
        return len(self.patient.prescriptions.find(Hydrocodone).filter(status='active'))


    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.in_denominator():

            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                result.add_narrative(f'Patient has specified a higher than average pain score. Consider prescribing narcotic pain relief.')
                prescribe_recommendation = PrescribeRecommendation(
                        key='RECOMMEND_HYDROCODONE_PRESCRIPTION',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Hydrocodone,
                        title='Prescribe Hydrocodone',
                        context={
                            'conditions': [[EncounterForLowBackPain]],
                            'sig_original_input': 'Take every 4-6 hours as needed to manage pain',
                            'duration_in_days': 5,
                            'dispense_quantity': 20,
                            'dosage_form': 'tablet',
                            'count_of_refills_allowed': 0,
                            'generic_substitutions_allowed': True,
                            'note_to_pharmacist': 'Contact with any questions'
                    }
                )
                result.add_recommendation(prescribe_recommendation)

        return result

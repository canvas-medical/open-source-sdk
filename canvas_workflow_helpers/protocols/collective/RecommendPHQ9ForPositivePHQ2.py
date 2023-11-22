from canvas_workflow_kit.protocol import CHANGE_TYPE, STATUS_DUE, STATUS_NOT_APPLICABLE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult
from canvas_workflow_kit.recommendation import InterviewRecommendation
from canvas_workflow_kit.value_set import ValueSet

class PHQ_9(ValueSet):
    VALUE_SET_NAME = 'PHQ-9'
    LOINC = {'44249-1'}

class PHQ_2(ValueSet):
    VALUE_SET_NAME = 'PHQ-2'
    LOINC = {'58120-7'}

class PHQ2Followup(ClinicalQualityMeasure):
    class Meta:
        title = 'Recommend PHQ-9 for positive PHQ-2 screener'
        description = ('Recommend a PHQ-9 questoinnaire if the if'
        'the patient\'s most recent PHQ-2 score is greater than 2')
        version = '1.0.2'
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        types = []

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        last_phq2 = self.patient.interviews.find(PHQ_2).filter(status='AC').last()
        last_phq9 = self.patient.interviews.find(PHQ_9).filter(status='AC').last()
        if last_phq2 and last_phq2['results'][0]['score'] > 2:
        	if not last_phq9:
        		result.status = STATUS_DUE
        		result.add_recommendation(
        			InterviewRecommendation(
        				key='RECOMMEND_PHQ_9',
        				patient=self.patient,
        				questionnaires=[PHQ_9],
        				title='Administer PHQ-9',
        				button='Interview'
        			)
        		)
        		result.add_narrative('Patient PHQ-2 score is >2, recommend patient take a PHQ-9.')
        	else:
        		result.status = STATUS_SATISFIED
        		result.add_narrative('Patient already has a PHQ-9 on file.')
        else:
        	result.status = STATUS_NOT_APPLICABLE
        	result.add_narrative('No PHQ-2 screener or last PHQ-2 screener negative.')
        return result

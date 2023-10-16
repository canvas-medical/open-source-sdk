# type: ignore
from typing import Dict, Optional

from cached_property import cached_property

from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult
)

from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnaireRisk(ValueSet):
    
    """ 
     This ValueSet will define the specific Questionnaire that is needed to determine patient's priority. 
    """
    
    # VALUE_SET_NAME can be set to a display name for the Questionnaire we are trying to identify
    VALUE_SET_NAME = '@Risk Questionnaire'

    # The name of this variable needs to match the coding system of the questionnaire (i.e. INTERNAL), 
    # while the single value in the set represents the questionnaire's code. These values were passed during Questionnaire Loading
    INTERNAL = {'Risk_Stratification'}


class PatientPriority(ClinicalQualityMeasure):
    """
    Protocol that displays patient priority based on latest risk stratification
    from Internal @Risk questionnaire, if the patient has any.
    """

    SATISFIED_VALUES = ('GREEN', 'YELLOW')

    class Meta:
        title = 'Patient Priority'
        version = '1.0.0'
        description = (
            'Protocol that displays patient priority based on Risk Questionnaire.')
        types = ['']
        compute_on_change_types = [
            ClinicalQualityMeasure.CHANGE_INTERVIEW,
        ]

    def last_interview(self, valueset) -> Optional[Dict]:
        interview = self.patient.interviews.find(valueset).last()

        if not interview:
            return None

        return interview

    @cached_property
    def last_risk(self) -> Optional[Dict]:
        return self.last_interview(
            valueset=QuestionnaireRisk)

    def last_risk_score(self) -> Optional[str]:
        score_string = None
        if self.last_risk:

            responses = self.last_risk.get('responses',[])
            if responses:
                score_string = responses[0].get('value', None)

        return score_string

    def compute_results(self) -> ProtocolResult:

        result = ProtocolResult()
        last_risk_score = self.last_risk_score()
        if last_risk_score:
            if last_risk_score in self.SATISFIED_VALUES:
                result.status = STATUS_SATISFIED
            else:
                result.status = STATUS_DUE

        return result


# type: ignore
from typing import Dict, Optional

from cached_property import cached_property

from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult
)

from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnaireRisk(ValueSet):

    VALUE_SET_NAME = '@Risk Questionnaire'

    INTERNAL = {'Risk_Stratification'}

    

class PatientPriority(ClinicalQualityMeasure):
    """
    Protocol that displays patient priority based on latest risk stratification from Internal @Risk questionnaire, 
    if the patient has any. There is currently no action to take, so no recommendations are made.
    """

    SATISFIED_VALUES = ('GREEN', 'YELLOW')

    class Meta:
        title = 'Patient Priority'

        version = '1.0.0'

        description = (
            'Protocol that displays patient priority based on Risk Questionnaire. '
            'There is currently no action to take, so no recommendations are made.')

        identifiers = ['PatientPriority']

        types = ['CQM']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            'Canvas'
        ]

        compute_on_change_types = [
            ClinicalQualityMeasure.CHANGE_INTERVIEW,
        ]

        funding_source = ''

        references = ['Written by Canvas']

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
      
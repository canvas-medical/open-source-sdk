from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_DUE, STATUS_SATISFIED,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.recommendation import Recommendation
from canvas_workflow_kit.value_set.value_set import ValueSet
"""
This protocol recommends diagnosing certain conditions based on questionnaire responses, 
and the recommendations have one-click commands for inserting the conditions into a Canvas note.
This is also dependent on a Questionnaire called the Diagnostic Assessment Tool with specific 
codings for the questionnaire and each of its questions - the loader data for this Questionnaire is below.
"""


class DiagnosticAssessmentQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Diagnostic Assessment Questionnaire'
    INTERNAL = {'PAT.QUESTIONNAIRE.2'}


class SenilePurpura(ValueSet):
    VALUE_SET_NAME = 'Senile purpura'
    ICD10CM = {'D692'}
    INTERNAL = {'PAT.QUES.8'}


class AhteroscleroticHeartDisease(ValueSet):
    VALUE_SET_NAME = ('Atherosclerotic heart disease of native coronary'
                      'artery with unspecified angina pectoris')
    ICD10CM = {'I25119'}
    INTERNAL = {'PAT.QUES.9'}


class AlcoholDependence(ValueSet):
    VALUE_SET_NAME = 'Alcohol dependence, in remission'
    ICD10CM = {'F1021'}
    INTERNAL = {'PAT.QUES.10'}


class MajorDepressiveDisorder(ValueSet):
    VALUE_SET_NAME = 'Major depressive disorder, single episode, in remission'
    ICD10CM = {'F325'}
    INTERNAL = {'PAT.QUES.11'}


class DiagnosticAssessment(ClinicalQualityMeasure):
    """
    A protocol that recommends diagnosing certain conditions based on questionnaire responses.
    """

    class Meta:

        title = 'Diagnostic Assessment'

        version = 'v1.0.0'

        description = ('A protocol that recommends diagnosing'
                       'certain conditions based on questionnaire responses.')

        information = 'https://canvasmedical.com/'

        identifiers = ['DiagnosticAssessment']

        types = ['Tools']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]
        compute_on_change_types = [
            CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION
        ]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

    most_recent_interview = None
    positive_question_ids = set()
    conditions_to_diagnose = []

    def in_denominator(self):
        """
        Patients whose most recent Diagnostic Assessment Tool questionnaire
        has at least one "Yes" answer.
        """
        # identify all active diagnostic assessment questionnaires for the patient
        # (use the DiagnosticAssessmentQuestionnaire valueset)
        diagnostic_interviews = self.patient.interviews.find(
            DiagnosticAssessmentQuestionnaire).filter(status='AC')

        # if none, return False
        if len(diagnostic_interviews) == 0:
            return False

        # get the most recently completed diagnostic assessment questionnaire by 'created'
        most_recent = max(diagnostic_interviews, key=lambda x: x['created'])
        self.most_recent_interview = most_recent

        # determine which question_ids had a 'yes' response
        positive_question_ids = {
            response['questionResponseId']
            for response in most_recent['responses']
            if response['value'] == 'Yes'
        }
        self.positive_question_ids = positive_question_ids

        # return True if the length of question_ids > 0, otherwise False
        return len(positive_question_ids) > 0

    def in_numerator(self):
        """
        Patients that have already been diagnosed with all recommended conditions.
        """
        # create a set of the codes for positive questions
        questions = self.most_recent_interview['questions']
        positive_question_codes = {
            q['code']
            for q in questions
            if q['questionResponseId'] in self.positive_question_ids
        }

        # map over each value_set and determine (1) if it is associated with any of the
        # positive_question_codes, and (2) if the patient has not been diagnosed with it yet.
        # if both are true, recommend diagnosis

        def value_set_is_positive(value_set):
            value_set_code = list(value_set.values['internal'])[0]
            return value_set_code and value_set_code in positive_question_codes

        def patient_has_condition(value_set):
            return len(
                self.patient.conditions.find(value_set).filter(
                    clinicalStatus='active')) > 0

        def patient_should_be_diagnosed(value_set):
            return value_set_is_positive(
                value_set) and not patient_has_condition(value_set)

        value_sets = [
            SenilePurpura, AhteroscleroticHeartDisease, AlcoholDependence,
            MajorDepressiveDisorder
        ]
        conditions_to_diagnose = [
            v for v in value_sets if patient_should_be_diagnosed(v)
        ]
        self.conditions_to_diagnose = conditions_to_diagnose

        return len(conditions_to_diagnose) == 0

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(
                    f'{self.patient.first_name} responded "Yes" to '
                    f'{len(self.conditions_to_diagnose)} questions in the Diagnostic Assessment '
                    f'Questionnaire, but has not been diagnosed with the associated conditions. '
                    f'Consider updating the Conditions List as clinically appropriate'
                )
                for i, vs in enumerate(self.conditions_to_diagnose):
                    result.add_recommendation(
                        Recommendation(
                            key=
                            f'DiagnosticAssessmentProtocol_RECOMMEND_DIAGNOSE_{vs.name}',
                            rank=i + 1,
                            button='Diagnose',
                            title=vs.name,
                            narrative=result.narrative,
                            command={
                                'type': 'diagnose',
                                'filter': {
                                    'coding': [{
                                        'code':
                                        list(vs.values['icd10cm']),
                                        'system':
                                        'icd10cm'
                                    }]
                                }
                            }))
        return result
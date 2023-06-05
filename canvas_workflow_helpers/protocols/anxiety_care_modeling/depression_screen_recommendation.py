import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set.value_set import ValueSet
from canvas_workflow_kit.recommendation import InterviewRecommendation

class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}

class Anxiety(ValueSet):
    VALUE_SET_NAME = "Anxiety disorder, unspecified"
    ICD10CM = {'F419'}


class AnxietyDepressionScreening(ClinicalQualityMeasure):

    class Meta:
        title = "Anxiety: Depression Screening"
        version = "2023-v01"
        description = "This protocol recommends a depression screening using PHQ-9 if patient is diagnosed with anxiety"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION]
        authors = ["Canvas Example Medical Association (CEMA)"]
        notification_only = True # If True the protocol will no recompute on upload

        condition_date = None

    def in_denominator(self):
        """
        Patients diagnosed with anxiety
        """
        anxiety_condition = self.patient.conditions.find(Anxiety).filter(clinicalStatus='active')

        if len(anxiety_condition):
            self.condition_date = arrow.get(anxiety_condition[-1]['created'])
            return True

        return False

    def in_numerator(self):
        """
        Patients that have filled out the PHQ-9 questionnaire after being diagnoses with anxiety
        """
        interviews = self.patient.interviews.find(QuestionnairePhq9).filter(created__gt=self.condition_date)
        return len(interviews) > 0

    def compute_results(self):
        """ """
        result = ProtocolResult()

        # Find patients diagnoses with Anxiety
        if self.in_denominator():

            # Find if the patient has a recent PHQ-9
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has recently been diagnosed with anxiety"
                result.add_narrative(narrative)

                interview_recommendation = InterviewRecommendation(
                            key='RECOMMEND_PHQ9_QUES',
                            rank=1,
                            button='Interview',
                            patient=self.patient,
                            questionnaires=[QuestionnairePhq9],
                            title='Consider completing a PHQ-9 to screen for depression'
                )
                result.add_recommendation(interview_recommendation)

        return result

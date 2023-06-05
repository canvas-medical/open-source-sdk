from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import DiagnoseRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnaireGAD7(ValueSet):
    VALUE_SET_NAME = "GAD-7 Questionnaire"
    LOINC = {"69737-5"}

class Anxiety(ValueSet):
    VALUE_SET_NAME = "Anxiety disorder, unspecified"
    ICD10CM = {'F419'}


class AnxietyDiagnosis(ClinicalQualityMeasure):

    class Meta:
        title = "Diagnose: Anxiety"
        version = "2023-v01"
        description = "This protocol recommends a diagnosis of anxiety for patients with a GAD7 score > 10"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION]
        authors = ["Canvas Example Medical Association (CEMA)"]

        score = None
        notification_only = True # If True the protocol will no recompute on upload

    def in_denominator(self):
        """
        Patients with most recent GAD7 score > 10

        """
        gad7_ques = self.patient.interviews.find(QuestionnaireGAD7).last()
        if not gad7_ques:
            return False

        score = next(
            (
                result.get("score")
                for result in gad7_ques.get("results", [])
                if result.get("score") > 10
            ),
            None,
        )
        self.score = score
        return bool(score)

    def in_numerator(self):
        """
        Patients diagnoses with anxiety
        """
        return bool(self.patient.conditions.find(Anxiety).filter(clinicalStatus='active'))


    def compute_results(self):
        """ """
        result = ProtocolResult()

        # Find patients with an elevated GAD-7 score
        if self.in_denominator():

            # Find if the patient has a diagnosis of anxiety
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has recently completed an elevated GAD-7, consider diagnosing the patient with the following condition:"
                result.add_narrative(narrative)

                diagnose_recommendation = DiagnoseRecommendation(
                    key='RECOMMEND_ANXIETY_DIAGNOSIS',
                    rank=1,
                    button='Diagnose',
                    patient=self.patient,
                    condition=Anxiety,
                    title=Anxiety.VALUE_SET_NAME,
                )
                result.add_recommendation(diagnose_recommendation)

        return result

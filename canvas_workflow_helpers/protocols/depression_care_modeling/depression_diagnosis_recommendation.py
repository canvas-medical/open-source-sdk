from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import DiagnoseRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}

class Depression(ValueSet):
    VALUE_SET_NAME = "Depression, unspecified"
    ICD10CM = {'F32A'}


class DepressionDiagnosis(ClinicalQualityMeasure):

    class Meta:
        title = "Diagnose: Depression"
        version = "2023-v01"
        description = "This protocol recommends a diagnosis of depression for patients with a PHQ9 score >= 10"
        identifiers = ["DepressionDiagnosis"]
        types = ["CQM"]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION]

        score = None
        notification_only = True # If True the protocol will no recompute on upload

    def in_denominator(self):
        """
        Patients with most recent PHQ9 score >= 10

        """
        phq9_ques = self.patient.interviews.find(QuestionnairePhq9).last()
        if not phq9_ques:
            return False

        score = next(
            (
                result.get("score")
                for result in phq9_ques.get("results", [])
                if result.get("score") >= 10
            ),
            None,
        )
        self.score = score
        return bool(score)

    def in_numerator(self):
        """
        Patients diagnoses with depression
        """
        return bool(self.patient.conditions.find(Depression).filter(clinicalStatus='active'))


    def compute_results(self):
        """ """
        result = ProtocolResult()

        # Find patients with an elevated PHQ-9 score
        if self.in_denominator():

            # Find if the patient has a diagnosis of depression
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has recently completed an elevated PHQ-9, consider diagnosing the patient with the following condition:"
                result.add_narrative(narrative)

                diagnose_recommendation = DiagnoseRecommendation(
                    key='RECOMMEND_DEPRESSION_DIAGNOSIS',
                    rank=1,
                    button='Diagnose',
                    patient=self.patient,
                    condition=Depression,
                    title=Depression.VALUE_SET_NAME,
                )
                result.add_recommendation(diagnose_recommendation)

        return result

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


class QuestionnaireDepressionScale(ValueSet):
    VALUE_SET_NAME = "Edinburgh Postnatal Depression Scale"
    INTERNAL = {"91689009-01"}

class Depression(ValueSet):
    VALUE_SET_NAME = "Postpartum depression"
    ICD10CM = {'F530'}


class PostpartumDepressionDiagnosis(ClinicalQualityMeasure):

    class Meta:
        title = "Diagnose: Postpartum Depression"
        version = "2023-v01"
        description = "This protocol recommends a diagnosis of depression for patients with a Depression score >= 13"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION]

        score = None
        notification_only = True # If True the protocol will no recompute on upload

    def in_denominator(self):
        """
        Patients with most recent Edinburgh Postnatal Depression Scale score >= 13

        """
        questionnaire = self.patient.interviews.find(QuestionnaireDepressionScale).last()
        if not questionnaire:
            return False

        score = next(
            (
                int(result.get("narrative").replace("Score of ", ""))
                for result in questionnaire.get("results", [])
                if "Score of" in result.get("narrative") and int(result.get("narrative").replace("Score of ", "")) >= 13
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

        # Find patients with an elevated EPDS score
        if self.in_denominator():

            # Find if the patient has a diagnosis of depression
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has recently completed an elevated EPDS, consider diagnosing the patient with the following condition:"
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
        else:
            result.add_narrative("Patient does not have a EPDS score >= 13")

        return result

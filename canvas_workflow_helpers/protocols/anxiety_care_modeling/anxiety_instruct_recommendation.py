import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import InstructionRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet

class Anxiety(ValueSet):
    VALUE_SET_NAME = "Anxiety disorder, unspecified"
    ICD10CM = {'F419'}

class AnxietyInstructions(ValueSet):
    VALUE_SET_NAME = "Your child's recent visit"
    SNOMEDCT = {"48694002"}


class AnxietyInstuct(ClinicalQualityMeasure):

    class Meta:
        title = "Instruct: Anxiety"
        version = "2023-v01"
        description = "This protocol recommends an instruction if patient has anxiety"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INSTRUCTION, CHANGE_TYPE.CONDITION]
        authors = ["Canvas Example Medical Association (CEMA)"]

        condition_date = None
        notification_only = True # If True the protocol will no recompute on upload

    def in_denominator(self):
        """Patients with anxiety"""
        conditions = self.patient.conditions.find(Anxiety).filter(clinicalStatus='active')

        if len(conditions):
            self.condition_date = arrow.get(conditions[-1]['created'])
            return True

        return False

    def in_numerator(self):
        """Patients that already have the instruct command"""
        for instuctions in self.patient.instructions.filter(created__gt=self.condition_date):
            for coding in instuctions.get('coding', []):
                if coding.get("display") == AnxietyInstructions.VALUE_SET_NAME:
                    return True

        return False


    def compute_results(self):
        """ """
        result = ProtocolResult()

        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has been diagnosed with Anxiety."
                result.add_narrative(narrative)

                instruct_recommendation = InstructionRecommendation(
                    key='RECOMMEND_ANXIETY_INSTRUCTIONS',
                    rank=1,
                    button='Instruct',
                    patient=self.patient,
                    instruction=AnxietyInstructions,
                    title=AnxietyInstructions.VALUE_SET_NAME,
                )
                result.add_recommendation(instruct_recommendation)

        return result

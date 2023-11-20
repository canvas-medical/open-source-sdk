from typing import Optional
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)

from canvas_workflow_kit.recommendation import InstructionRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class WeightLossProgramStatusQuestionnaire(ValueSet):
    """Questionnaire for Weight Loss Program Status"""

    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class LowCarbDietInstruction(ValueSet):
    """Recommendations for a low-carb diet."""

    VALUE_SET_NAME = 'Low Carb Diet Recommendations'
    SNOMEDCT = {'183065007'}


class GeneralDietEducationInstruction(ValueSet):
    """Recommendations for general diet education."""

    VALUE_SET_NAME = 'General Diet Education Recommendations'
    SNOMEDCT = {'11816003'}


class DietaryPlan(ClinicalQualityMeasure):
    class Meta:
        title = 'Diet planning'
        description = (
            'This protocol recommends a dietary plan for patients in Treatment'
            'phase. If the patient\'s A1c is '
            'over 7, a low-carb diet is suggested.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.INSTRUCTION,
            CHANGE_TYPE.INTERVIEW,
        ]
        references = []

    def last_a1c_level(self) -> Optional[float]:
        last_a1c = self.patient.lab_reports.find(
            Hba1CLaboratoryTest
        ).last_value()
        return float(last_a1c) if last_a1c else None

    def has_dietary_plan_instruction(self) -> bool:
        return bool(
            self.patient.instructions.find(GeneralDietEducationInstruction)
        )

    def is_in_treatment(self) -> bool:
        """
        Return the most recent status if any based on the
        questionnaire "Program status".

        Possible values:
            "a211": "Intake",
            "a212": "Condition screening",
            "a213": "Treatment",
            "a214": "Disqualified",
        """

        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')

        if not status_interviews:
            return False

        most_recent = max(status_interviews, key=lambda x: x['created'])
        return most_recent['responses'][0]['code'] == 'a213'

    def in_denominator(self) -> bool:
        return self.is_in_treatment()

    def in_numerator(self) -> bool:
        """Patients who already have a dietary plan assessment."""
        return self.has_dietary_plan_instruction()

    def remainder_tasks(self, result: ProtocolResult):
        # Recommend general diet education if A1c is not available or is < 7
        if not self.last_a1c_level() or self.last_a1c_level() < 7:
            result.add_recommendation(
                InstructionRecommendation(
                    key='INSTRUCTION_GENERAL_DIET',
                    patient=self.patient,
                    instruction=GeneralDietEducationInstruction,
                    title='General diet education',
                )
            )
        else:
            # Recommend low-carb diet if A1c is > 7
            result.add_recommendation(
                InstructionRecommendation(
                    key='INSTRUCTION_LOW_CARB_DIET',
                    patient=self.patient,
                    instruction=LowCarbDietInstruction,
                    title='Low carb diet education',
                )
            )
        result.add_narrative('Dietary counseling is recommended.')
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Patient has already received dietary instruction.'
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative('Not applicable due to program status.')
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

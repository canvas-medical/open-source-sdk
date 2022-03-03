from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import STATUS_DUE, ClinicalQualityMeasure, ProtocolResult
from canvas_workflow_kit.value_set.v2020 import MorbidObesity
from canvas_workflow_kit.recommendation import (PlanRecommendation)


class PlanCommand(ClinicalQualityMeasure):
    """
    A protocol with a plan button recommendation that inserts a
    completed plan command for patients with obesity
    """

    class Meta:

        title = 'Plan Button'

        version = 'v1.0.0'

        description = 'A protocol w/ a plan button recommendation'

        information = 'https://canvasmedical.com/'

        identifiers = ['Plan']

        types = ['Recommendations']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.CONDITION]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

    def in_denominator(self):
        """
        Patients in the initial population.
        Patients diagnosed with morbid obesity
        """
        return len(
            self.patient.conditions.find(MorbidObesity).filter(
                clinicalStatus='active')) > 0

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            result.due_in = -1
            result.status = STATUS_DUE
            result.add_narrative(
                f"Lets make a plan for {self.patient.first_name}'s weight management"
            )
            result.add_recommendation(
                PlanRecommendation(
                    key='PLAN_COMMAND',
                    rank=1,
                    button='Plan',
                    patient=self.patient,
                    title='Insert a health plan',
                    narrative=
                    'Consult with nutritionist and exercise for 30-60 minutes daily'
                ))
        return result

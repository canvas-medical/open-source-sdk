from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import PlanRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2022.condition import GeneralizedAnxietyDisorder


class GAD(ValueSet):
    VALUE_SET_NAME = 'Generalize Anxiety Disorder'
    ICD10CM = {
        'F410',  # Panic disorder [episodic paroxysmal anxiety]
        'F411',  # Generalized anxiety disorder
        'F413',  # Other mixed anxiety disorders
        'F418',  # Other specified anxiety disorders
        'F419',  # Anxiety disorder, unspecified
    }



from canvas_workflow_kit.timeframe import Timeframe

"""
Protocol to plan anxiety coping mechanisms with patients who have been diagnosed with anxiety disorder.
This protocol is not able to be satisfied.
"""

class PlanProtocol(ClinicalQualityMeasure):

    class Meta:

        title = 'Plan Anxiety Coping Mechanisms'

        description = 'Make a plan with patient to figure out additional ways to cope with anxiety'

        version = '2022-07-18v0'

        information = 'https://www.cdc.gov/tobacco/campaign/tips/diseases/depression-anxiety.html'

        identifiers = ['ACM07']

        types = ['CQM']

        compute_on_change_types = [ #Theres's no event type for plan. There's also no plan record in the patient data so can't actually resolve this recommendation.
            CHANGE_TYPE.CONDITION,
        ]

        references = [
            'https://www.mayoclinic.org/diseases-conditions/anxiety/diagnosis-treatment/drc-20350967'
        ]

    def in_denominator(self):
        """
        Returns true for patients who qualify to receive this recommendation. Specifically, this function returns true if pateints
        have an active diagnosis of generalized anxiety disorder.
        """

        anxiety_conditions = self.patient.conditions.find(GAD).filter(clinicalStatus='active')
        return anxiety_conditions.records != []
        #returns true if the patient has GAD in their records

    def in_numerator(self):
        """
        Determines which patients who are a part of the initial population have already satisfied the recommendation.
        """
        # #a variable to create a timeframe to search for an imaging report in. Because we are interested in whether
        # #a patient has received a yearly bonescan, we search within the timeframe of 1 year ago to present.
        # last_screening_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        # # using the find command, we compare imaging records to the class "BoneScan" and then check that any found records
        # # are within the specified timeframe
        # imaging_completed = self.patient.imaging_reports.find(
        #     BoneScan
        # ).within(last_screening_timeframe)
        # #if imaging completed does not contain any matching records, it will return false.
        # return bool(imaging_completed)
        # #returns true if a full body bone scan has been completed in the last year.
        return False


    def compute_results(self):
        plan_recommendation = PlanRecommendation(
            key='RECOMMEND_ANXIETY_COPING_PLAN',
            rank=1,
            button='Plan',
            patient=self.patient,
            title=f'Plan anxiety coping mechanisms with {self.patient.first_name}',
            narrative='Discuss ways of limiting anxiety'
        )
        result = ProtocolResult()
        if self.in_denominator():
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    plan_recommendation
                )


        return result

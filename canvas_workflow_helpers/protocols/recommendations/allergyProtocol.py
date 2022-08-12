from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import AllergyRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe
from datetime import date

"""
If a patient is diagnosed with an allergy to mammalian meat, recommend adding this allergy to the
allergies list.
"""


class BeefAllergy(ValueSet):
    VALUE_SET_NAME = 'Allergy to beef'
    FDB = {'900124', '1113'}

class MammalMeatAllergy(ValueSet):
    VALUE_SET_NAME = 'Allergy to mammal meat'
    ICD10CM = {'Z91014'}


class AllergyProtocol(ClinicalQualityMeasure):

    class Meta:

        title = 'Add beef meat allergy to allergy list'

        description = 'Since the patient has been diagnosed with an allergy, it should be added to the allergy list.'

        version = '2022-07-22v0'

        information = 'https://ecqi.healthit.gov/ecqm/ep/2021/cms139v9' #TODO

        identifiers = ['ACM14']

        types = ['CQM']

        compute_on_change_types = [ #TODO: ADD AN EVENT THAT MAKES SENSE WITH THE PROTOCOL
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.ALLERGY_INTOLERANCE
        ]

        references = [ #TODO
            'https://www.nih.gov/news-events/nih-research-matters/how-often-should-women-have-bone-tests'
        ]

    def in_denominator(self):
        """
        TODO:DESCRIPTION OF THE PATIENTS INITIALLY QUALIFIED FOR THE PROCEDURE
        """

        allergy_diagnosis = self.patient.conditions.find(MammalMeatAllergy).filter(
            clinicalStatus='active')

        return allergy_diagnosis.records != []
        #if a patient has a mammal meat entry as a diagnosis, return true.

    def in_numerator(self):
        """
        TODO
        """
        # example:
        allergy_recorded = self.patient.allergy_intolerances.find(BeefAllergy)
        print(self.patient.__dict__)
        return bool(allergy_recorded)


    def compute_results(self):
        allergy_recommendation = AllergyRecommendation(
            key='RECOMMEND_BEEF_ALLERGY',
            rank=1,
            button='Allergy',
            allergy=BeefAllergy,
            #title='Beef Products',
            narrative='Swelling of the throat.',
            context={
            'severity': 'mild',
            'onset_date': "2022-08-11"
            }
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already had their allergy recorded.' #TODO
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    allergy_recommendation #TODO: CHANGE TO CORRECT VAR NAME
                )
                result.add_narrative(allergy_recommendation.narrative)


        return result

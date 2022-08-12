from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import ImagingRecommendation #TODO: CHANGE ME TO BE WHATEVER RECOMMENDATION TYPE EX IS FOR
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2022.diagnostic_study import BoneScan #TODO: CHANGE ME TO BE WHATEVER VALUESET IS REQUIRED



from canvas_workflow_kit.timeframe import Timeframe

"""
TODO: DESCRIBE THE PURPOSE OF THE PROTOCOL HERE
"""

#TODO: ADD CLASSES TO STORE THE ACCEPTED VALUESETS IN
class Osteopenia(ValueSet):
    VALUE_SET_NAME = 'Other specified disorders of bone density and structure, unspecified site'
    ICD10CM = {'M8580'}

class BoneScan(ValueSet):
    VALUE_SET_NAME = 'SPECT Whole body Bone'
    LOINC = {'39816-4'}


class ImagingProtocol(ClinicalQualityMeasure): #TODO: CHANGE THE NAME OF THE CLASS

    class Meta:

        title = 'Osteopenia bone density tracking' # TODO: CHANGE TITLE

        description = 'Ensure bone density is stable from year to year' #TODO: CHANGE DESCRIPTION

        version = '2022-07-07v6' #TODO:RESET TO 1

        information = 'https://ecqi.healthit.gov/ecqm/ep/2021/cms139v9' #TODO

        identifiers = ['ACM01'] #TODO: CHANGE TO SOMETHING UNIQUE

        types = ['CQM']

        compute_on_change_types = [ #TODO: ADD AN EVENT THAT MAKES SENSE WITH THE PROTOCOL
            CHANGE_TYPE.ENCOUNTER,
            CHANGE_TYPE.PATIENT,
            CHANGE_TYPE.IMAGING_REPORT
        ]

        references = [ #TODO
            'https://www.nih.gov/news-events/nih-research-matters/how-often-should-women-have-bone-tests'
        ]

    def in_denominator(self):
        """
        TODO:DESCRIPTION OF THE PATIENTS INITIALLY QUALIFIED FOR THE PROCEDURE
        """
        # example:
        # osteopenia_conditions = self.patient.conditions.find(Osteopenia).filter(
        #     clinicalStatus='active')
        #
        # return osteopenia_conditions.records != []
        #returns true if the patient has a condition of osteopenia in their records
        return True

    def in_numerator(self):
        """
        TODO
        """
        # example:
        # last_screening_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        # imaging_completed = self.patient.imaging_reports.find(
        #     BoneScan
        # ).within(last_screening_timeframe)
        # return bool(imaging_completed)
        #returns true if a full body bone scan has been completed in the last year.
        return False

    def compute_results(self):
        imaging_recommendation = ImagingRecommendation( # CHANGE TO CORRECT REC TYPE
            key='RECOMMEND_BONESCAN', #TODO
            rank=1,
            button='Order', #TODO
            patient=self.patient,
            imaging=BoneScan, #TODO
            title='Order a Bonescan', #TODO
            narrative='A bonescan should be ordered for this patient.' #TODO: SEE IF THIS DOES ANYTHING, ALSO CONTEXT
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been imaged this year.' #TODO
                )
            else: 
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    imaging_recommendation #TODO: CHANGE TO CORRECT VAR NAME
                )


        return result

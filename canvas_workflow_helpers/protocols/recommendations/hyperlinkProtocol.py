from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import HyperlinkRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe

"""
TODO: DESCRIBE THE PURPOSE OF THE PROTOCOL HERE
"""

#TODO: ADD CLASSES TO STORE THE ACCEPTED VALUESETS IN


class HyperlinkProtocol(ClinicalQualityMeasure):

    class Meta:

        title = 'Understand Care Protocols' # TODO: CHANGE TITLE

        description = 'Ensure bone density is stable from year to year' #TODO: CHANGE DESCRIPTION

        version = '2022-07-22v0'

        information = 'https://ecqi.healthit.gov/ecqm/ep/2021/cms139v9' #TODO

        identifiers = ['ACM13'] #TODO: CHANGE TO SOMETHING UNIQUE

        types = ['CQM']

        compute_on_change_types = [ #TODO: ADD AN EVENT THAT MAKES SENSE WITH THE PROTOCOL
            CHANGE_TYPE.PROTOCOL_OVERRIDE
        ]

        references = [ #TODO
            'https://www.nih.gov/news-events/nih-research-matters/how-often-should-women-have-bone-tests'
        ]

    def in_denominator(self):
        """
        All patients qualify for this procedure.
        """
        return True

    def in_numerator(self):
        """
        No change types so not sure how to resolve this recommendation.
        """



        return False

    def compute_results(self):
        hyperlink_recommendation = HyperlinkRecommendation(
            key='PROTOCOL_DOCUMENTATION_LINK',
            rank=1,
            button='Documentation',
            href='https://canvas-medical.zendesk.com/hc/en-us/articles/360057232994-Care-Protocols',
            title='Canvas Care Protocols Documentation'
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'This hyperlink has already been recommended.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    hyperlink_recommendation
                )


        return result

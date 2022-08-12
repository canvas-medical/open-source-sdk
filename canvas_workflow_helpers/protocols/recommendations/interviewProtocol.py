from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import InterviewRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021 import Phq9AndPhq9MTools
from canvas_workflow_kit.value_set.v2021 import Diabetes

from canvas_workflow_kit.timeframe import Timeframe

"""
Protocol to remind practitioners to screen patients who have an active diagnosis of diabetes for depression
since these individuals are at an elevated risk.
"""

class PHQ9(ValueSet):
    VALUE_SET_NAME = 'PHQ-9 Depression Screening' #Two in valueset, unlabed. not sure which is which. M is for "modified" and is for teens.
    LOINC = {'44249-1'}
    #from the file assessments_performed.py in v2021 folder. Does not autofill the questionnaire section.


class InterviewProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload imagingProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and interview (anytime an interview or questionnaire
        is conducted)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Yearly PHQ-9 for Individuals with Diabetes'

        description = 'Administer the PHQ-9 to screen individuals with diabetes for depression/determine \
        pre-existing depression severity.'

        version = '2022-07-14v0'

        information = 'https://stacks.cdc.gov/view/cdc/84332'

        identifiers = ['ACM04']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.CONDITION,
        ]

        references = [
            'https://stacks.cdc.gov/view/cdc/84332'
        ]

    def in_denominator(self):
        """
        Determines patients in the initial population. In this case it's patients who have diabetes.
        """

        diabetes_conditions = self.patient.conditions.find(Diabetes).filter(
            clinicalStatus='active')

        return diabetes_conditions.records != []
        #returns true if the patient has a condition of osteopenia in their records


    def in_numerator(self):
        """
        Determines which patients who are a part of the initial population have already satisfied the recommendation.
        Specifically, determines if patients have been given a PHQ9 questionnaire within the last year.
        """

        last_interview_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        interview_completed = self.patient.interviews.find(
            Phq9AndPhq9MTools
        ).within(last_interview_timeframe)
        return bool(interview_completed)
        #THIS PART WORKS IF YOU ENTER IN A PHQ9 BY HAND... because it is a result code that it's looking for (makes sense)


    def compute_results(self):
        """
        An interview recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending an interview, it has been
        set to 'Interview'

        - patient is always going to be set to self.patient

        - questionnaires is a list of ValueSets that contain codings that map to specific interviews. The valueset must be imported. A valid
        coding will result in the interview command being autofilled with this questionnaire. If multiple codes are entered,
        !!!TODO- once figure out what is going on with these codes!!!

        - title is used to display next to the button. It is also used if there is not a matching imaging report
        for the given coding (from the 'imaging' attribute) to generate a display title within the order imaging command.
        If the title starts with 'order a', 'refer for a' or 'perform a', everything after those phrases is kept and saved as
        the imaging order's title. After this text, the coding associated with the imaging class is added in parentheses.
        (e.g. SPECT whole body Bone (CPT: 39820-6))
        ** Note: currently, regardless of which coding system is in use, the display will have the system as CPT.

        - narrative displays under the title of the protocol on the patient's protocols page via line 196
        (result.add_narrative(imaging_recommendation.narrative)). Without this, it will not display on the UI.

        - context is a dictionary that optionally may include a 'conditions' key that maps to another dictionary. Inclusion of a
        pre-existing condition will pre-load the condition into the indications section of the order image command.
        **Note: see the recommendations documentation (https://docs.canvasmedical.com/docs/recommendation-types)for more information
        on adding multiple conditions, and adding conditions a patient has not yet been diagnosed with.

        """
        interview_recommendation = InterviewRecommendation(
            key='RECOMMEND_PHQ9_DIABETES',
            rank=1,
            button='Interview',
            patient=self.patient,
            questionnaires=[PHQ9], #this part isn't working because wrong type of code. need to generate a phq9 using the questionnaire code not a result code.
            title='Patient is due for their PHQ-9 assessment'
        )

        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been interviewed this year.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    interview_recommendation
                )


        return result

from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import StructuredAssessmentRecommendation
from canvas_workflow_kit.value_set import ValueSet



from canvas_workflow_kit.timeframe import Timeframe

"""
This protocol recommends providers perform a structured assessment of osteopenia/osteoporosis symptoms on an annual basis.
"""

class OsteoSA(ValueSet):
    VALUE_SET_NAME = 'Osteo Structured Assessment'
    INTERNAL = {'SA_Osteo'}

class OsteoSAP(ValueSet):
    VALUE_SET_NAME = 'Osteopen Structured Assessment'
    INTERNAL = {'SA_Osteo'}


class Osteopenia(ValueSet): #add osteoporosis in either this val set or it's own when home-app back up
    """
    Creates a class from the Value set that includes the value code and name of the diagnosis.
    This will be used later as the patient.conditions.find() command's parameter to identify if a patient has
    this diagnosis.
    """

    VALUE_SET_NAME = 'Other specified disorders of bone density and structure, \
    unspecified site'
    ICD10CM = {'M8580'}


class StructuredAssessmentProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload structuredAssessmentProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. Supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and interview (it will re-run if a
        questionnaire, structured assessment or physical exam is created or edited.)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Annual Assessment of Osteopenia/Osteoporosis'

        description = 'Routine assessment of Osteopenia/Osteoporosis symptoms'

        version = '2022-07-21v0'

        information = 'https://www.mayoclinic.org/diseases-conditions/copd/symptoms-causes/syc-20353679#:~:text=Overview,(sputum)%20production%20and%20wheezing.'

        identifiers = ['ACM10']

        types = ['CQM']

        # An interview change type will recompute upon creation of or changes made to a Strucutred Assessment
        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.INTERVIEW
        ]

        references = [ #TODO
            'https://www.lung.org/lung-health-diseases/lung-disease-lookup/copd'
        ]

    def in_denominator(self):
        """
        Patients who qualify for this protocol, specifically, patients who have an active diagnosis of Osteopenia or Osteoporosis.
        """
        # example:
        osteo_conditions = self.patient.conditions.find(Osteopenia).filter(
            clinicalStatus='active')

        return osteo_conditions.records != []
        #returns true if the patient has active osteopenia diagnosis


    def in_numerator(self):
        """
        Determines if patients have already satisfied the protocol.
        """
        last_SA_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        SA_completed = self.patient.interviews.find(
            OsteoSA
        ).within(last_SA_timeframe)
        return bool(SA_completed)
        #returns true if a structured assessment of their osteopenia/osteoporosis has been completed in the last year.

    def compute_results(self):
        """
        A structured assessment recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending a structured assessment is completed, it has been
        set to 'assess'

        - patient is always going to be set to self.patient

        - questionnaires is a list of ValuseSets that contains codings that map to specific structured assessments. These valuesets must be imported.
        A valid coding will result in the structured assessment command being generated. If multiple codes are entered,
        TODO: FIGURE OUT WHAT HAPPENS WHEN MULTIPLE CODES ARE ENTERED

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
        structured_assessment_recommendation = StructuredAssessmentRecommendation(
            key='RECOMMEND_OSTEO_STRUCTURED_ASSESSMENT',
            rank=1,
            button='Assess',
            patient=self.patient,
            questionnaires=[OsteoSA, OsteoSAP],
            #title='Assess Osteopenia/Osteoporosis'
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been assessed this year.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    structured_assessment_recommendation
                )


        return result

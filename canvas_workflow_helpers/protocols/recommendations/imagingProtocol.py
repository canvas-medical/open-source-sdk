from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import ImagingRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2022.diagnostic_study import BoneScan
from canvas_workflow_kit import events



from canvas_workflow_kit.timeframe import Timeframe

"""
An example protocol that tests whether an individual diagnosed with osteopenia has recieved
a bone scan in the last year.
"""

#Added Osteopenia and Xray classes to be able to use the find command.
class Osteopenia(ValueSet):
    """
    Creates a class from the Value set that includes the value code and name of the diagnosis.
    This will be used later as the patient.conditions.find() command's parameter to identify if a patient has
    this diagnosis.
    """

    VALUE_SET_NAME = 'Other specified disorders of bone density and structure, \
    unspecified site'
    ICD10CM = {'M8580'}

class BoneScan(ValueSet):
    """
    This is a class that stores the imaging type we want the patient to have performed.
    It is used in several places:
    1. To search whether or not a patient has alread had this imaging done in the given time frame
    (note: for a patient's imaging records to contain this report, it must be signed/reviewed by a
    practitioner)
    2. Upon instantiation of the ImagingRecommendation object, the attribute 'imaging' will be set to this class ('Bonescan')
    which will allow the UI to autofill the correct imaging report within the order imaging command.

    Although a list of codes can be passed in here, we strongly recommend only imputting a single code, as only the first entered
    into the imaging report templates database will be used.
    """
    VALUE_SET_NAME = 'SPECT Whole body Bone'
    LOINC = {'39820-6'}
    # Only the item in the list that was entered into the database first will be
    # used. To ensure you know which code is being used, we suggest only including
    # one code.


class ImagingProtocol(ClinicalQualityMeasure):

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
        condition (so it will re-run if a patient has a new diagnosis) and imaging report (it will re-run if a new
        imaging report has been entered and signed by a practitioner)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Osteopenia bone density tracking'

        description = 'Ensure bone density is stable from year to year'

        version = '2022-07-08v1'

        information = 'https://ecqi.healthit.gov/sites/default/files/EP-EC-Measures-Table-2021-05.pdf'

        identifiers = ['ACM01'] #shows up next to the recommendation on the patient's protocol tab

        types = ['CQM'] #shows up next to the recommendation on the patient's protocol tab

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.IMAGING_REPORT
        ]

        responds_to_event_types = [events.HEALTH_MAINTENANCE, ]

        references = [
            'https://www.nih.gov/news-events/nih-research-matters/how-often-should-women-have-bone-tests'
        ]

    def in_denominator(self):
        """
        Determines patients in the initial population. In this case, all patients with a diagnosis of osteopenia.
        """
        #for testing _upsert_investigative_conditions:
        #same thing as refer-- shows up if you fill everything out. it's not generating a diagnose command anywhere
        return True

        #creates a variable to store a list of matching records from a patient's data
        #searches for a diagnosis matching our created class "Osteopenia", and filters
        #so that only active diagnoses are included.
        osteopenia_conditions = self.patient.conditions.find(Osteopenia).filter(
            clinicalStatus='active')

        #checks to see if there are any records. returns false if an empty list.
        return bool(osteopenia_conditions)
        #returns true if the patient has a condition of osteopenia in their records


    def in_numerator(self):
        """
        Determines which patients who are a part of the initial population have already satisfied the recommendation.
        """
        #a variable to create a timeframe to search for an imaging report in. Because we are interested in whether
        #a patient has received a yearly bonescan, we search within the timeframe of 1 year ago to present.
        last_screening_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        # using the find command, we compare imaging records to the class "BoneScan" and then check that any found records
        # are within the specified timeframe
        imaging_completed = self.patient.imaging_reports.find(
            BoneScan
        ).within(last_screening_timeframe)
        #if imaging completed does not contain any matching records, it will return false.
        return bool(imaging_completed)
        #returns true if a full body bone scan has been completed in the last year.


    def compute_results(self):
        """
        An imaging recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are ordering an image, it has been
        set to 'order'

        - patient is always going to be set to self.patient

        - imaging is a class that contains codings that map to specific imaging orders. The valueset must be imported. A valid
        coding will result in the imaging order command being autofilled with this imaging type. If multiple codes are entered,
        the display will default to the item in the list that was first entered into your practice's database.

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
        imaging_recommendation = ImagingRecommendation(
            key='RECOMMEND_BONESCAN',
            rank=1,
            button='Order',
            patient=self.patient,
            imaging=BoneScan, #if no template with loinc code, it defaults to whatever is after "order a..." and then (cpt: #)
            title='Order a SPECT Whole body Bone', #is this gettign set to be order.display? see normalize_command_codings
            narrative='A bonescan should be ordered for this patient.',
            context={'conditions': [[{ #condition must already exist in the patient or won't show up
                'code': 'M8580',
                'system': 'ICD-10',
                'display': Osteopenia.VALUE_SET_NAME,
            }]]}
        )
        result = ProtocolResult()
        if self.in_denominator(): # Patient has been diagnosed with osteopenia
            if self.in_numerator(): # Has received a full body bone scan within the last year
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been imaged this year.' #Can be found displayed in the inactive protocols list on the patient's page.
                )
            else: # Has not had a bonescan done within a year.
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    imaging_recommendation
                )
                result.add_narrative(imaging_recommendation.narrative)

        return result

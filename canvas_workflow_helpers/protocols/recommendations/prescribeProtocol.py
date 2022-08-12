from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set import ValueSet



from canvas_workflow_kit.timeframe import Timeframe

"""
This protocol generates a recommendation to prescribe tylenol to patients diagnosed with headaches if
it has not already been prescribed.
"""


class ValueSetWithNDC(ValueSet):
    """
    This is a new class type inherited from ValueSet that supports NDC codes in addition to all of the coding
    systems supported by the ValueSet class.
    """
    value_systems = [*ValueSet.value_systems, 'NDC']

class acetNDC(ValueSetWithNDC):
    """
    An NDC valuset class that includes the NDC, FDB and RXNORM codings for tylenol.
    """
    VALUE_SET_NAME = 'acetaminophen 500 mg tablet'
    NDC = {'00450044905'}
    FDB = {206813}
    RXNORM = {'198440'}

class Headaches(ValueSet):
    """
    A valueset that includes the IDC10 coding for headache syndrome.
    """
    VALUE_SET_NAME = 'Periodic Headache Syndrome'
    ICD10CM = {'G43C1'}


class PrescribeProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload prescribeProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis), prescription (it will re-run if a new
        prescription has been entered and signed by a practitioner) and medication (it will rerun if any changes are
        made to medications)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """
        title = 'Prescribe Tylenol for Headaches'

        description = 'Prescribe a pain reliever to manage headache symptoms'

        version = '2022-19-07v0'

        information = 'https://www.cdc.gov/acute-pain/migraine/index.html'

        identifiers = ['ACM08']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.PRESCRIPTION
        ]

        references = [
            'https://www.who.int/news-room/fact-sheets/detail/headache-disorders'
        ]


    headaches = None

    def in_denominator(self):
        """
        Patients who have an active diagnosis of Preiodic Headache Syndrome will return True. All other patients
        will return False.
        """
        #for testing _upsert_investigative_conditions
        #Seems to be working as expected. Doesn't populate indications field. 
        return True

        headache_conditions = self.patient.conditions.find(Headaches).filter(
            clinicalStatus='active')


        if headache_conditions.records != []:
            self.headaches = headache_conditions[0]
            return True
        else:
            return False

    def in_numerator(self):
        """
        Returns True if the medication has already been prescribed and False if it has yet to be prescribed.
        """

        been_prescribed = self.patient.medications.find(
            acetNDC
        ).filter(status="active")
        return bool(been_prescribed)


    def compute_results(self):
        """
        An prescribe recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are prescribing a medication, it has been
        set to 'prescribe'

        - patient is always going to be set to self.patient

        - prescription is a ValueSet that contains codings that map to specific medications. The valueset must be imported. A valid
        coding will result in the command being autofilled with this treatment. NEED TO ADD TO THIS ONCE FIGURE OUT HOW TO AUTOFILL

        - title is used to display next to the button.

        - The context contains several keys that will autofill the prescribe command:
              - `sig_original_input` keys to a string that will autofill the sig field of the command.
              - `duration_in_days` keys to an integer that autofills the "days supply" field
              - `dispense_quantity` keys to an integer that autofills the "quantity to dispense" field
              - `count_of_refills` keys to an integer that autofills the "refills" field
              - `generic_substitutions_allowed` keys to a boolean that autofills the substitutions field as either "allowed" (True)
              or "Not Allowed" (False)
              - `note_to_pharmacist` keys to a string that autofills the "Note to pharmacist" field
              - 'conditions' maps to another dictionary. Inclusion of a pre-existing condition will pre-load the condition into the
              indications section of the prescribe command.
              **Note: see the recommendations documentation (https://docs.canvasmedical.com/docs/recommendation-types)for more information
              on adding multiple conditions, and adding conditions a patient has not yet been diagnosed with.
              ***Note: conditions is required if a valid medication has been included in the recommendation. If it is omitted,
              the prescribe button will be hidden on the recommendation within the UI.
        """

        prescribe_recommendation = PrescribeRecommendation(
            key='RECOMMEND_TYLENOL_MEDICATION',
            rank=1,
            button='Prescribe',
            patient=self.patient,
            prescription=acetNDC,
            title='Recommendation of Tylenol.',
            context={ #this is all working
            'sig_original_input': "This is the sig" ,
            'duration_in_days': 5 ,
            'dispense_quantity': 45 ,
            'count_of_refills_allowed': 4 ,
            'generic_substitutions_allowed': False ,
            'dosage_form': "tablet",
            'note_to_pharmacist': "This is the note to pharmacist",
            'conditions': [[{
                'code': 'G43C1',
                'system': 'ICD-10',
                'display': "Headache Syndrome",
            }]]
            }
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been prescribed tylenol.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    prescribe_recommendation
                )


        return result

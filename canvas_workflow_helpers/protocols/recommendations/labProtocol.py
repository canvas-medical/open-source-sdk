from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import LabRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021 import (
    Diabetes,
    Hba1CLaboratoryTest,
)


from canvas_workflow_kit.timeframe import Timeframe

"""
Patients with diabetes should have their HbA1c tested every 1-2 years. This protocol reminds providers to order a lab
test for their patient with diabetes if it has been more than 2 years since the last one was received.
"""


class HBA1C(ValueSet):
    """
    This class is used as the ValueSet passed in to the lab parameter in the lab recommendation. This code will be used to
    to populate the lab order command on Canvas. Because only one code will be used in the order, we strongly recommend only
    passing in one code to achieve expected behavior.
    """

    VALUE_SET_NAME = 'HbA1c Laboratory Test'
    LOINC = {'4548-4'}
    CPT = {'4548-4'}



class LabProtocol(ClinicalQualityMeasure):


    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload labProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and lab report (it will re-run if a new
        lab report has been entered and signed by a practitioner)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Diabetes HbA1c Lab'

        description = 'Bi-annual HbA1c testing for individuals diagnosed with Diabetes'
        version = '2022-07-14v0'

        information = 'https://www.mayoclinic.org/tests-procedures/a1c-test/about/pac-20384643'

        identifiers = ['ACM05']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.LAB_REPORT
        ]

        references = [
            'https://www.diabetes.org.uk/guide-to-diabetes/managing-your-diabetes/hba1c'
        ]

    def in_denominator(self):
        """
        Determines patients in the initial population. In this case it's patients who have diabetes.
        """
        #for testing _upsert_investigative_conditions
        #autofills automatically but then doesn't save to conditions in patient recordset or say that
        #a condition was diagnosed on the top of the note
        return True

        diabetes_conditions = self.patient.conditions.find(Diabetes).filter(
            clinicalStatus='active')

        return True

        # return diabetes_conditions.records != []

    def in_numerator(self):
        """
        Determines which patients who are a part of the initial population have already satisfied the recommendation.
        In this case, it is individuals who have received a hemoglobin blood test within the last 2 years.
        """

        last_lab_timeframe = Timeframe(self.now.shift(years=-2), self.now)
        lab_completed = self.patient.lab_reports.find(
            Hba1CLaboratoryTest
        ).within(last_lab_timeframe)
        return bool(lab_completed)


    def compute_results(self):
        """
        A lab recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are ordering a lab, it has been
        set to 'order'

        - patient is always going to be set to self.patient

        - condition is a valueset that contains the condition code for the diagnosis tied to this lab report. It is only used to generate a narrative
        if a title is not included. The name of the valueset is utilized in the narrative that is autogenerated when title is absent. This
        Valueset can contain multiple codes since the only thing pulled from it is the name.

        - lab is a class that contains codings that map to specific lab orders. The valueset must be imported. A valid
        coding will result in the lab order command being autofilled with this lab type. If multiple codes are entered,
        the display will default to the item in the list that was first entered into your practice's database. NEED TO INVESTIGATE MORE!!!! TODO

        - title is used to display next to the button. It is also used if there is not a matching lab report
        for the given coding (from the 'lab' attribute) to generate a display title within the order lab command.
        If the title starts with 'order a', 'refer for a' or 'perform a', everything after those phrases is kept and saved as
        the lab order's title. After this text, the coding associated with the lab class is added in parentheses.
        (e.g. SPECT whole body Bone (CPT: 39820-6))
        ** Note: currently, regardless of which coding system is in use, the display will have the system as CPT. TODO:check this is still the case

        - narrative displays under the title of the protocol on the patient's protocols page via line 196
        (result.add_narrative(lab_recommendation.narrative)). Without this, it will not display on the UI.

        - context is a dictionary that optionally may include a 'conditions' key that maps to another dictionary. Inclusion of a
        pre-existing condition will pre-load the condition into the indications section of the order lab command.
        **Note: see the recommendations documentation (https://docs.canvasmedical.com/docs/recommendation-types)for more information
        on adding multiple conditions, and adding conditions a patient has not yet been diagnosed with.

        """
        lab_recommendation = LabRecommendation(
            key='RECOMMEND_HBA1C',
            rank=1,
            button='Order',
            patient=self.patient,
            condition=Diabetes,
            lab=HBA1C,
            title='HbA1c Blood Test',
            context={'conditions': [[{
                'code': 'O2402',
                'system': 'ICD-10',
                'display': "Pre-existing type 1 diabetes mellitus, in childbirth",
            }]]}
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already had their HbA1c tested within the last two years.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    lab_recommendation
                )


        return result

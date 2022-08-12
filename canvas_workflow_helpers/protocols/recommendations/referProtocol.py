from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import ReferRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021 import Colonoscopy, MalignantNeoplasmOfColon


from canvas_workflow_kit.timeframe import Timeframe

"""
This protocol recommends that patients with colon cancer are referred for a colonoscopy yearly until their
condition is no longer active.
"""



class Colonoscopy(ValueSet):
    VALUE_SET_NAME = 'Colonoscopy'
    CPT = {'44388'}


class ReferProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload referProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and referral report (it will re-run if a new
        specialist consult report has been entered and signed by a practitioner)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Yearly Colonoscopy for Colon Cancer Patients'

        description = 'Routine colonoscopy for patients with colon cancer'

        version = '2022-07-20v0'

        information = 'https://www.mayoclinic.org/diseases-conditions/colon-cancer/diagnosis-treatment/drc-20353674'

        identifiers = ['ACM09']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.REFERRAL_REPORT
        ]

        references = [
            'https://www.mountsinai.org/health-library/special-topic/colon-cancer-screening'
        ]


    def in_denominator(self):
        """
        Returns true for any patients who have been diagnosed with colon cancer.
        """
        #for testing _upsert_investigative_conditions
        # this one doesn't show up in indications right away but gets autofilled if you type in the rest of the required fields
        # condition will show up in the recordset but not on the side of the patient chart
        return True

        colon_conditions = self.patient.conditions.find(MalignantNeoplasmOfColon).filter(
            clinicalStatus='active')
        return True
        return colon_conditions.records != []
        #returns true if the patient has a condition of Malignant Neoplasm Of the Colon in their records


    def in_numerator(self):
        """
        Returns true if a patient has been referred for a colonoscopy within the last year.
        """

        last_screening_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        colonoscopy_completed = self.patient.referral_reports.find(
            Colonoscopy
        ).within(last_screening_timeframe)
        return bool(colonoscopy_completed)



    def compute_results(self):
        """
        A refer recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are referring a patient to a specialist, it has been
        set to 'Refer'

        - patient is always going to be set to self.patient

        - referral is a class that contains codings that map to specific referral types. The ValueSet must be imported. Only the name of
        this ValueSet will be utilized to generate a title and narrative if title is not included.

        - condition is a class that contains diagnosis codings. The ValueSet must be imported. Only the name of this ValueSet will be
        utilized to generate a title and narrative if title is not included.

        - title is used to display next to the button.

        - context is a dictionary that optionally may include a 'conditions' key that maps to another dictionary. Inclusion of a
        pre-existing condition will pre-load the condition into the indications section of the refer command.
        **Note: see the recommendations documentation (https://docs.canvasmedical.com/docs/recommendation-types)for more information
        on adding multiple conditions, and adding conditions a patient has not yet been diagnosed with. Context may also include a
        'specialties' key that stores a string. This string will be used to autofill the "Refer to: " box on the refer command.
        It will also be the specialty name for the service provider that is autogenerated from this referral protocol.

        """
        refer_recommendation = ReferRecommendation(
            key='RECOMMEND_REFER_COLONOSCOPY',
            rank=1,
            button='Refer',
            patient=self.patient,
            referral=Colonoscopy,
            condition=MalignantNeoplasmOfColon,
            title='Refer for a Colonoscopy',
            context={
            'specialties': ['Colonoscopy'],
            'conditions': [[{
                'code': 'C186',
                'system': 'ICD-10',
                'display': "Malignant neoplasm of descending colon (C18.6)" ,
            }]]}

        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has been referred for a colonoscopy within the past year'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    refer_recommendation
                )

        return result

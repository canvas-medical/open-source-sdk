from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import FollowUpRecommendation
from canvas_workflow_kit.value_set import ValueSet
from datetime import date


from canvas_workflow_kit.timeframe import Timeframe

"""
A protocol to recommend a follow up when a patient is diagnosed with a concussion.
"""


class Concussion(ValueSet):
    VALUE_SET_NAME = 'Concussion without loss of consciousness, initial encounter'
    ICD10CM = {'S060X0A'}



class FollowUpProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload followUpProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and appointment (it recalculates if a patient
        has an appointment scheduled.)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Concussion Follow Up'

        description = 'Check in on patient post-concussion.'

        version = '2022-08-09v0'

        information = 'https://www.cdc.gov/traumaticbraininjury/index.html'

        identifiers = ['ACM16']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.APPOINTMENT
        ]

        references = [
            'https://www.cdc.gov/traumaticbraininjury/concussion/index.html'
        ]

    def in_denominator(self):
        """
        Determines which patients initially qualify for this protocol. In this case, it returns true
        for patients with an active diagnosis of a concussion.
        """

        concussion_conditions = self.patient.conditions.find(Concussion).filter(
            clinicalStatus='active')

        return concussion_conditions.records != []


    def in_numerator(self):
        """
        Determines if patients have satisfied the protocol. In this case, it returns true if an appointment
        has been scheduled in the future.
        """

        scheduled_appt = self.patient.upcoming_appointments
        return bool(scheduled_appt)



    def compute_results(self):
        """
        A follow up recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending a follow up, it has been
        set to 'follow up'

        - patient is always going to be set to self.patient

        - The text to show on a patient's chart that describes the recommendation. If it is omitted, it will default to "Request
        follow-up appointment"

        -  The text to show on a patient's chart under the title of the recommendation. For this to successfully display, the
        command `add_narrative(diagnose_recommendation.narrative) must be used. If a narrative is not included in the
        recommendation, but the `add_narrative` command is used, it will default to "{patient.name} needs a follow-up appointment."

        - A dictionary that may optionally contain the keys 'requested_date' (keys to a string in the format "YYYY-MM-DD"),
        'reason_for_visit' (keys to a string), 'internal_comment' (keys to a string that will populate the 'scheduling commends'
        field of the Follow Up command) and 'requested_note_type'.  'requested_not_type' keys to a coding of a note type. This note
        type must be scheduleable. To learn more about configurable note types, see this zendesk article:
        https://canvas-medical.zendesk.com/hc/en-us/articles/6623684024083-Note-Types-

        """

        followUp_recommendation = FollowUpRecommendation(
            key='RECOMMEND_FOLLOW_UP',
            rank=1,
            button='Follow up',
            patient=self.patient,
            title=f'Follow Up with {self.patient.first_name}',
            narrative='This is the narrative.',
            context={
                'requested_date':'2022-09-02',
                'reason_for_visit':'Concussion followup',
                'internal_comment':'This is the internal comment.',
                'requested_note_type':'439708006'
            }
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has had an appointment scheduled already.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    followUp_recommendation
                )
                result.add_narrative(followUp_recommendation.narrative)


        return result

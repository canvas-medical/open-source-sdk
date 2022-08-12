from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import VitalSignRecommendation
from canvas_workflow_kit.value_set.v2022.diagnostic_study import BoneScan #TODO: CHANGE ME TO BE WHATEVER VALUESET IS REQUIRED



from canvas_workflow_kit.timeframe import Timeframe

"""
Recommend vitals be taken for a patient upon an office visit.
"""

class VitalSignProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload vitalsProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and vital_sign (it will re-run if new
        vital signs have been entered)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Routine Vital Sign Recommendation'

        description = 'Take a patient\'s vitals at the beginning of an office visit.'

        version = '2022-07-23v0'

        information = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6333367/'

        identifiers = ['ACM12']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.ENCOUNTER,
            CHANGE_TYPE.APPOINTMENT,
            CHANGE_TYPE.VITAL_SIGN
        ]

        references = [
            'https://www.meridian.edu/importance-taking-vital-signs-medical-assisting-guide/'
        ]

    def in_denominator(self):
        """
        If a patient has scheduled an office visit on the current day, they qualify for this protocol, and this
        function will return true
        """
        # example:
        timeframe = Timeframe(self.now, self.now.shift(days=1))
        upcoming_appointment = self.patient.upcoming_appointments.filter(appointmentType= "office", startTime__lte = self.now.shift(days=1))

        return upcoming_appointment.records != []
        #returns true if the patient has a condition of osteopenia in their records
        return True

    def in_numerator(self):
        """
        Patients who have already had their vital signs recorded on a given day have satisfied the requirement, and
        this function will return true. Otherwise, it will return false.
        """
        # example:

        vitals_completed = self.patient.vital_signs.filter(
            dateRecorded__gte= self.now.shift(days=-1))
        return bool(vitals_completed)
        #returns true if vitals have been taken in the last 24 hours.

    def compute_results(self):
        """
        An vital sign recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending vitals be recorded,
        it has been set to 'Vitals'

        - patient is always going to be set to self.patient

        - title is used to display next to the button. If it is not included, it will default to "Collect Vitals"

        - narrative displays under the title of the protocol on the patient's protocols page via
        (result.add_narrative(vital_sign_recommendation.narrative)). Without this, it will not display on the UI.

        """
        vital_sign_recommendation = VitalSignRecommendation(
            key='RECOMMEND_VITAL_SIGN_READING',
            rank=1,
            button='Vitals',
            patient=self.patient,
            title='Recommend Reading Vital Signs',
            narrative=f'{self.patient.first_name} should have their vitals recorded at the beginning of their upcoming appointment.'
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already had their vitals recorded for this visit.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    vital_sign_recommendation
                )
                result.add_narrative(vital_sign_recommendation.narrative)


        return result

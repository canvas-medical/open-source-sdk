import arrow
import requests

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import FollowUpRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}


BEHAVIORAL_HEALTH_NOTE_TYPE_CODE = 'BH'
APPOINTMENT_CANCELLED_STATUSES = [
    "cancelled",
    "noshowed",
    "entered-in-error",
    "noshow"
]


class PHQ9(ClinicalQualityMeasure):
    """
    This protocol recommends a follow-up behavioral appointment for patients with a PHQ9 score >= 10
    """

    class Meta:
        title = "PHQ9 Follow up"

        version = "2023-v01"

        description = "This protocol recommends a follow-up behavioral appointment for patients with a PHQ9 score >= 10"

        information = "https://link_to_protocol_information"

        identifiers = ["PHQ9Appointment"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.APPOINTMENT]

        authors = ["Canvas Example Medical Association (CEMA)"]

        score = None
        interview_time = None

    def get_fhir_api_token(self):
        """ Given the Client ID and Client Secret for authentication to FHIR,
        return a bearer token """

        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET
        instance_name = self.settings.INSTANCE_NAME

        token_response = requests.request(
            "POST",
            f'https://{self.INSTANCE_NAME}.canvasmedical.com/auth/token/',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
        )

        return token_response.json().get('access_token')

    def get_fhir_appointments(self):
        """ Given a Task ID we can perform a FHIR Task Search Request"""
        return requests.get(
            (f"https://fhir-{self.INSTANCE_NAME}.canvasmedical.com/"
            "Appointment?date=ge{self.interview_time[:10]}&patient=Patient/{self.patient.patient_key}"),
            headers={
                'Authorization': f'Bearer {self.get_fhir_api_token()}',
                'accept': 'application/json'
            }
        ).json()

    def in_denominator(self):
        """
        Patients with most recent PHQ9 score >= 10

        """
        phq9_ques = self.patient.interviews.find(QuestionnairePhq9).last()
        if not phq9_ques:
            return False

        score = next(
            (
                result.get("score")
                for result in phq9_ques.get("results", [])
                if result.get("score") >= 10
            ),
            None,
        )
        self.score = score
        self.interview_time = phq9_ques['noteTimestamp']
        return bool(score)

    def in_numerator(self):
        # Patients that have a follow-up behavioral health appointment scheduled in the future
        bh_appts = self.patient.upcoming_appointments.filter(
            startTime__gt=self.interview_time, noteType__code=BEHAVIORAL_HEALTH_NOTE_TYPE_CODE
        )

        if any(
            appt
            for appt in bh_appts
            if appt.get("status") not in APPOINTMENT_CANCELLED_STATUSES
        ):
            return True

        # if there are no upcoming appointments, we need to make sure they dont have a completed
        # appointment after the PHQ-9 was filled out
        appointments = self.get_fhir_appointments()

        for apt in appointments.get('entry', []):
            apt_code = apt['resource']['appointmentType']['coding'][0]['code']
            start_time = arrow.get(apt['resource']['start'])
            status = apt['resource']['status']
            if (apt_code == BEHAVIORAL_HEALTH_NOTE_TYPE_CODE and
                start_time > arrow.get(self.interview_time) and
                status not in APPOINTMENT_CANCELLED_STATUSES):
                return True


    def compute_results(self):
        """ """
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name}'s most recent PHQ-9 score is {self.score}."
                date = arrow.now().shift(days=7).format("YYYY-MM-DD")
                follow_up_recommendation = FollowUpRecommendation(
                    key="RECOMMEND_FOLLOW_UP",
                    rank=1,
                    button="Follow up",
                    patient=self.patient,
                    title=f"Follow Up with {self.patient.first_name}",
                    narrative=narrative,
                    context={
                        "requested_date": date,
                        "internal_comment": "Elevated PHQ-9.",
                        "requested_note_type": BEHAVIORAL_HEALTH_NOTE_TYPE_CODE,
                    },
                )
                result.add_recommendation(follow_up_recommendation)
                result.add_narrative(narrative)

        return result

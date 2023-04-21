import arrow
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


# this pk will vary by database
BEHAVIORAL_HEALTH_NOTE_TYPE_PK = 33
APPOINTMENT_SCHEDULED_STATUSES = [
    "unconfirmed",
    "attempted",
    "confirmed",
    "arrived",
    "roomed",
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

    def in_denominator(self):
        """
        Patients with most recent PHQ9 score >= 10

        """
        phq9_ques = (
            self.patient.interviews.find(QuestionnairePhq9)
            .filter(status="AC", progressStatus="F")
            .last()
        )
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
        return bool(score)

    def in_numerator(self):
        """
        Patients that have a follow-up behavioral health appointment scheduled in the future
        """
        bh_appts = self.patient.upcoming_appointments.filter(
            startTime__gte=arrow.now(), noteType__id=BEHAVIORAL_HEALTH_NOTE_TYPE_PK
        )
        return any(
            appt
            for appt in bh_appts
            if appt.get("status") in APPOINTMENT_SCHEDULED_STATUSES
        )

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name}'s most recent PHQ-9 score is {self.score}."
                follow_up_recommendation = FollowUpRecommendation(
                    key="RECOMMEND_FOLLOW_UP",
                    rank=1,
                    button="Follow up",
                    patient=self.patient,
                    title=f"Follow Up with {self.patient.first_name}",
                    narrative=narrative,
                    context={
                        "requested_date": arrow.now()
                        .shift(days=7)
                        .format("YYYY-MM-DD"),
                        "internal_comment": "Elevated PHQ-9.",
                        "requested_note_type": BEHAVIORAL_HEALTH_NOTE_TYPE_PK,
                    },
                )
                result.add_recommendation(follow_up_recommendation)
                result.add_narrative(narrative)

        return result

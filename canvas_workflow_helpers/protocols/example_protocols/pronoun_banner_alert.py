from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.value_set.value_set import ValueSet


class PronounQuestionnaire(ValueSet):
    VALUE_SET_NAME = "Pronoun Questionnaire"
    INTERNAL = {"PRONOUNS"}


class PronounBannerAlert(ClinicalQualityMeasure):
    """
    Banner alert that displays the patient's response to a pronoun questionnaire
    """

    class Meta:
        title = "Pronoun Banner Alert"

        version = "2023-v01"

        description = "Banner alert that displays the patient's response to a pronoun questionnaire"

        information = "https://link_to_protocol_information"

        identifiers = ["PronounBannerAlert"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]

        authors = ["Canvas Example Medical Association (CEMA)"]

    def get_pronoun_questionnaire(self):
        return (
            self.patient.interviews.find(PronounQuestionnaire)
            .filter(progressStatus="F", status="AC")
            .last()
        )

    def get_pronoun_question_response_id(self, questionnaire):
        if not questionnaire:
            return None
        return next(
            (
                q.get("questionResponseId")
                for q in questionnaire.get("questions", [])
                if q.get("code") == "90778-2"
            ),
            None,
        )

    def get_pronoun_response(self):
        questionnaire = self.get_pronoun_questionnaire()
        question_response_id = self.get_pronoun_question_response_id(questionnaire)
        if not question_response_id:
            return None

        return next(
            (
                r.get("value")
                for r in questionnaire.get("responses", [])
                if r.get("questionResponseId") == question_response_id
            ),
            None,
        )

    def compute_results(self):
        result = ProtocolResult()
        if pronoun := self.get_pronoun_response():
            result.due_in = -1
            result.status = STATUS_DUE
            result.recommendations.append(
                BannerAlertIntervention(
                    narrative=pronoun,
                    placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value],
                    intent=AlertIntent.ALERT_INTENT_INFO.value,
                )
            )
        return result

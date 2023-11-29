from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.value_set.value_set import ValueSet


class Questionnaire(ValueSet):
    INTERNAL = {"QUES_STUDY_ENROLLMENT_Q0"}
    QUESTIONNAIRE_QUESTION_CODE = 'QUES_STUDY_ENROLLMENT_Q2'
    NARRATIVE_TEXT = 'Enrolled in: '


class PronounBannerAlert(ClinicalQualityMeasure):

    class Meta:
        title = "Questionnaire Response Banner Alert"
        version = "2023-v01"
        description = "Banner alert that displays the patient's response to a specific questionnaire"
        identifiers = ["PronounBannerAlert"]
        types = ["CQM"]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]

    def get_questionnaire(self):
        return (
            self.patient.interviews.find(Questionnaire)
            .last()
        )

    def get_question_response_id(self, questionnaire):
        if not questionnaire:
            return None
        return next(
            (
                q.get("questionResponseId")
                for q in questionnaire.get("questions", [])
                if q.get("code") == Questionnaire.QUESTIONNAIRE_QUESTION_CODE
            ),
            None,
        )

    def get_response(self):
        questionnaire = self.get_questionnaire()
        question_response_id = self.get_question_response_id(questionnaire)
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
        if answer := self.get_response():
            result.due_in = -1
            result.status = STATUS_DUE
            result.recommendations.append(
                BannerAlertIntervention(
                    narrative=f"{Questionnaire.NARRATIVE_TEXT}{answer}",
                    placement=[
                        AlertPlacement.ALERT_PLACEMENT_CHART.value,
                        AlertPlacement.ALERT_PLACEMENT_PROFILE.value,
                        AlertPlacement.ALERT_PLACEMENT_TIMELINE.value,
                        AlertPlacement.ALERT_PLACEMENT_APPOINTMENT_CARD.value,
                        AlertPlacement.ALERT_PLACEMENT_SCHEDULING_CARD.value,
                    ],
                    intent=AlertIntent.ALERT_INTENT_INFO.value,
                )
            )
        return result

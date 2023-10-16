from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.value_set.value_set import ValueSet
import arrow


class QuestionnairePhq9(ValueSet):
    VALUE_SET_NAME = "PHQ-9 Questionnaire"
    LOINC = {"44249-1"}


class PHQ9HistoryBannerAlert(ClinicalQualityMeasure):
    class Meta:
        title = "PHQ9 History Banner Alert"
        version = "2023-v01"
        description = "A Banner alert that displays the scores of the patient's last 3 completed PHQ9 questionnaires."
        identifiers = ["PHQ9HistoryBanner"]
        types = ["CQM"]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]

    def get_date_and_score(self, q):
        date = arrow.get(q.get("noteTimestamp")).format("MM/DD/YYYY")
        score = next((r.get("score") for r in q.get("results")), "")
        return f"{date}: {int(score)}"

    def get_last_three_phq9(self):
        return self.patient.interviews.find(QuestionnairePhq9)[-3:][::-1]

    def compute_results(self):
        result = ProtocolResult()
        if phq9s := self.get_last_three_phq9():
            most_recent = phq9s[0]
            if arrow.get(most_recent.get("noteTimestamp")) < arrow.now().shift(
                years=-1
            ):
                result.status = STATUS_SATISFIED
            else:
                scores = "\t".join([self.get_date_and_score(p) for p in phq9s])
                result.due_in = -1
                result.status = STATUS_DUE
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=f"PHQ9 History\n{scores}",
                        placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value],
                        intent=AlertIntent.ALERT_INTENT_INFO.value,
                    )
                )
        return result

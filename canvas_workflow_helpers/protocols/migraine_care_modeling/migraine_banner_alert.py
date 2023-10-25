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


class QuestionnaireMigraineIntake(ValueSet):
    VALUE_SET_NAME = "Migraine Intake"
    INTERNAL = {"migint-123"}

class MigraineIntakeBannerAlert(ClinicalQualityMeasure):
    class Meta:
        title = "Migraine Intake Banner Alert"
        version = "2023-v01"
        description = "After completion of questionnaire display banner alert"
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        types = [""]

    def compute_results(self):
        result = ProtocolResult()
        if self.patient.interviews.find(QuestionnaireMigraineIntake).filter(status='AC'):
            result.due_in = -1
            result.status = STATUS_DUE
            result.recommendations.append(
                BannerAlertIntervention(
                    narrative=f"Migraine Patient, Intake Completed",
                    placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value, AlertPlacement.ALERT_PLACEMENT_PROFILE.value],
                    intent=AlertIntent.ALERT_INTENT_INFO.value,
                )
            )
        else:
            result.add_narrative('Patient has not filled out Migraine Intake Questionnaire')
        return result

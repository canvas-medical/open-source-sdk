import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import TaskRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class QuestionnaireStomachAcheNausea(ValueSet):
    VALUE_SET_NAME = "Stomach Ache/ Nausea"
    INTERNAL = {"12790"}

TASK_TITLE = "Schedule initial visit with mental health team"


class StomachAcheNauseaTask(ClinicalQualityMeasure):

    class Meta:
        title = "Task: Stomach Ache / Nausea"
        version = "2023-v01"
        description = "This protocol recommends task to follow up with a patient based on how they answered the Stomach Ache/ Nausea Questionnaire"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.TASK]
        authors = ["Canvas Example Medical Association (CEMA)"]

        notification_only = True # If True the protocol will no recompute on upload

        questionnaire_time = None

    def in_denominator(self):
        """
        Patients that have answered the Stomach Ache/ Nausea Questionnaire and answered any of these responses:

        Patient exhibits: Shaking/Jitters or Increased heart rate
        Is patient having difficulty sleeping? Yes
        Is patients stomach sensitive to touch? No
        Does pain worsen with coughing, walking, other movements? No
        """
        ques = self.patient.interviews.find(QuestionnaireStomachAcheNausea).last()
        if not ques:
            return False

        self.questionnaire_time = ques['created']

        for response in ques.get("responses", []):
            code = response.get('code')

            if code in ("12795", "12797", "12800", "12804", "12807"):
                return True

        return False

    def in_numerator(self):
        """
        Patients already have a Task associated with the questionnaire
        """
        return bool(self.patient.tasks.filter(
            title=TASK_TITLE,
            created__gt=self.questionnaire_time))

    def compute_results(self):
        """ """
        result = ProtocolResult()

        # Find patients with an elevated GAD-7 score
        if self.in_denominator():

            # Find if the patient has a diagnosis of anxiety
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                narrative = f"{self.patient.first_name} has recently completed a Stomach Ache / Nausea questionnaire"
                result.add_narrative(narrative)

                task_recommendation = TaskRecommendation(
                    patient=self.patient,
                    key='TASK_MEDICATION_RECONCILIATION',
                    rank=1,
                    button='Task',
                    title=TASK_TITLE,
                    context={
                            'labels':['Urgent'],
                            'due_date': arrow.now().shift(days=1).format("YYYY-MM-DD")
                    },
                    narrative="Review responses to recent Stomach Ache / Nausea questionnaire."
                )
                result.add_recommendation(task_recommendation)

        return result

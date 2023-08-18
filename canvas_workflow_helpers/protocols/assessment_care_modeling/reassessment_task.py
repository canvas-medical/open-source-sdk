import arrow

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.internal.integration_messages import create_task_payload
from canvas_workflow_kit.value_set.value_set import ValueSet

class ReAssessment(ValueSet):
    VALUE_SET_NAME = 'Patient Re-Assessment'
    INTERNAL = {'Patient Re-Assessment'}

class ReassessmentQuestionnaireTaskCreator(ClinicalQualityMeasure):

    class Meta:
        title = 'Patient Re-Assessment Questionnaire Task Creator'
        version = '2023-08-18'
        description = 'Create task on completion of Patient Re-Assessment for IDT Coordination team to schedule Semi-Annual visit'
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]

        notification_only = True

    # This is a hard-coded team identifier that is always responsible calling patients
    # You can normally get this ID from our FHIR Group Search endpoint
    TEAM_IDENTIFIER = '5425152c-d390-4498-9948-fe1eef711fbd'

    def get_newly_created_interview(self):
        changed_model = self.field_changes.get('model_name')
        created = self.field_changes.get('created')
        # we only care about interviews that have been created
        if changed_model != 'interview' or not created:
            return False
        return self.field_changes['canvas_id']

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        interview_id = self.get_newly_created_interview()
        if interview_id:
            interview = self.patient.interviews.find(ReAssessment).filter(id=interview_id).records

            if not interview:
                return result

            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key='5eede137ecfe4124b8b773040e33be14',
                status="OPEN", # This can be anything from the list ["COMPLETED", "CLOSED", "OPEN"]
                title=f'Schedule Semi-Annual Visit w/ Patient for Re-Assessment',
                team_identifier=self.TEAM_IDENTIFIER,
                due=arrow.now().shift(days=1).isoformat(),
                created=arrow.now().isoformat(),
                tag=None,
                labels=["Routine"]
            )

            self.set_updates([task_payload])

        return result

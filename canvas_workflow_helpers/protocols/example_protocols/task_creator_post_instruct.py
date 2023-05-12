import json
import arrow

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.internal.integration_messages import create_task_payload

class CreateTaskPostInstruct(ClinicalQualityMeasure):
    class Meta:
        title = 'Instruction Task Creator'
        version = 'v1.0.0'
        description = 'Generates a task after a specific instruct command in completed'
        compute_on_change_types = [CHANGE_TYPE.INSTRUCTION]

    notification_only = True # add this so your protocol doesn't try to recompute on upload

    CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14' # CHANGE FOR GIVEN INSTNACE

    def get_patient_care_team_lead(self):
        """ Find the patient's lead care team member """
        care_teams = self.patient.patient.get('careTeamMemberships', [])
        for care_team in self.patient.patient.get('careTeamMemberships', []):
            if care_team.get('lead'):
                return care_team.get('staff', {}).get('key')

        return ''

    def compute_results(self):
        result = ProtocolResult()

        if self.field_changes.get('model_name') == 'instruction':
            instruct = self.patient.instructions.filter(id=self.field_changes.get('canvas_id')).first()

            # we only want to create this task if the Instructions are for Fasting Labs
            if len(instruct.get('coding', [])) and instruct['coding'][0].get('display') == 'Fasting Labs':

                instruct_date = instruct.get('created')
                created_date = arrow.get(instruct_date).format('MM/DD/YYYY')
                due = arrow.get(instruct_date).shift(days=7).isoformat()

                task_payload = create_task_payload(
                    patient_key=self.patient.patient['key'],
                    created_by_key=self.CANVAS_BOT_KEY,
                    status="OPEN",
                    title=f'Follow up on Hemoglobin A1c order from {created_date}',
                    assignee_identifier=self.get_patient_care_team_lead(),
                    due=due,
                    created=arrow.now().isoformat(),
                    tag=None,
                    labels=[]
                )

                self.set_updates([task_payload])

        return result

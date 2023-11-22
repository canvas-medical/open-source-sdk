from typing import List, Optional

import arrow

from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set import ValueSet
from requests import RequestException


class PHQ_9(ValueSet):
    VALUE_SET_NAME = 'PHQ-9'
    LOINC = {'44249-1'}


CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'


class PHQ9ScreeningAlert(ClinicalQualityMeasure):
    class Meta:
        title = 'PHQ-9 screening alert'
        description = '''
            Alert the care team when a patient's intake screening PHQ-9
            indicates a need for follow-up.
            '''
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        references = []

    def get_if_phq9(self) -> Optional[dict]:
        '''Get the triggering questionnaire if it is a PHQ-9.'''
        questionnaire_id = self.field_changes.get('canvas_id')
        return self.patient.interviews.find(PHQ_9).filter(status='AC', id=questionnaire_id).last()

    def flag_phq_9(self, questionnaire) -> bool:
        '''Flag PHQ-9 if score is 20 or higher or if the answer to Q9 >= 1.'''
        score = float(questionnaire['results'][0]['score'])
        q9_id = [x['code'] for x in questionnaire['questions']]
        q9_id = [
            x['questionResponseId'] for x in questionnaire['questions'] if x['code'] == '44260-8'
        ][0]
        q9_response = [x for x in questionnaire['responses'] if x['questionResponseId'] == q9_id][0]
        return score >= 20 or q9_response['code'] != 'LA6568-5'

    def check_active_task_exists_by_description(
        self, task_description: str
    ) -> Optional[List[dict]]:
        '''
        Check if a task with the specified description exists.
        '''
        fumage = FumageHelper(self.settings)
        response = fumage.search(
            'Task',
            {
                'description': task_description,
                'status': 'requested',
                'patient': f'Patient/{self.patient.patient["key"]}',
            },
        )
        if not response.ok:
            raise RequestException(
                f"Failed to search for Task with {task_description} and"
                f"correlation-id {response.headers['fumage-correlation-id']}"
            )

        return [x['resource'] for x in response.json().get('entry', [])]

    def upsert_task(self) -> bool:
        '''
        Creates a task for a care coordinator to follow-up with the patient.
        '''
        description = 'Patient PHQ-9 score indicates a need for follow-up.'
        if not self.check_active_task_exists_by_description(description):
            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=CANVAS_BOT_KEY,
                status='OPEN',
                title=description,
                team_identifier=TEAM_IDENTIFIER,
                due=arrow.now().isoformat(),
                created=arrow.now().isoformat(),
                tag=None,
                labels=None,
            )
            self.set_updates([task_payload])
            return True
        return False

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        triggering_questionnaire = self.get_if_phq9()
        if bool(triggering_questionnaire):
            if self.flag_phq_9(triggering_questionnaire):
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    'PHQ-9 has been flagged for follow-up. '
                    'A task has been created for the patient.'
                )
                self.upsert_task()
            else:
                result.status = STATUS_NOT_APPLICABLE
                result.add_narrative('No PHQ-9 flagging detected.')
        else:
            result.status = STATUS_UNCHANGED
            result.add_narrative('Triggering questionnaire not PHQ-9.')
        return result

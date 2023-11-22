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

CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'


class BehavioralHealthIntakeQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Behavioral Health Intake Questionnaire'
    INTERNAL = {'iBH'}


class SocialNeedsAlert(ClinicalQualityMeasure):
    class Meta:
        title = 'Social needs alert'
        description = (
            'If an interview has just been completed and it is an intake survey, '
            'then if the patient answered “Yes” to questions on social needs, create a task for '
            'the care coordinator team.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.PATIENT, CHANGE_TYPE.INTERVIEW]
        references = []
        notification_only = True

    def get_if_intake(self) -> Optional[dict]:
        '''Get the triggering questionnaire if it is an intake survey.'''
        questionnaire_id = self.field_changes.get('canvas_id')
        return (
            self.patient.interviews.find(BehavioralHealthIntakeQuestionnaire)
            .filter(status='AC', id=questionnaire_id)
            .last()
        )

    def flag_social_needs(self, questionnaire) -> bool:
        social_needs_codes_positive = {
            'aBH5_1',  # unemployed
            'aBH6_1',  # feels unsafe
            'aBH4_2',  # food insecure
            'aBH3_2',  # worried about housing
        }
        social_need_responses_positive = [
            x for x in questionnaire['responses'] if x['code'] in social_needs_codes_positive
        ]
        return len(social_need_responses_positive) > 0

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
        Creates a task for a care coordinator to follow up with the patient.
        '''
        description = 'Patient has social needs that require follow-up.'
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
        intake_questionnaire = self.get_if_intake()
        if not intake_questionnaire:
            result.status = STATUS_UNCHANGED
            narrative = 'Triggering questionnaire is not a behavioral health intake questionnaire.'
        elif self.flag_social_needs(intake_questionnaire):
            result.status = STATUS_SATISFIED
            narrative = (
                'Patient has social needs that require follow-up. A task has '
                'been created for the patient.'
            )
            self.upsert_task()
        else:
            result.status = STATUS_NOT_APPLICABLE
            narrative = 'No social needs flagging detected.'

        result.add_narrative(narrative)
        return result

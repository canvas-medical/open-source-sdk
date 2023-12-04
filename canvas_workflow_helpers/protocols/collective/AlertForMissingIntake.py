import datetime

from typing import List, Optional, Type

import arrow

from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set import ValueSet
from requests.exceptions import RequestException

TEAM_ID = 'cd002206-7a26-40e0-9363-3f5e93befa83'
CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'


class BehavioralHealthIntakeQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Behavioral Health Intake Questionnaire'
    INTERNAL = {'iBH'}


class AlertForMissingIntake(ClinicalQualityMeasure):
    class Meta:
        title = 'Alert for missing intake'
        description = (
            'If it is less than 72 hours before an appointment and an intake '
            'questionnaire has not been done on a patient, then create a task '
            '"No intake questionnaire uploaded" for a Team (Care coordinators) '
            'to address the issue. First check to make sure such a task has '
            'not already been created, based on the task description.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.PATIENT,
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.APPOINTMENT,
        ]
        references = []

    def has_completed_questionnaire(self, questionnaire: Type[ValueSet]) -> bool:
        return bool(self.patient.interviews.find(questionnaire).filter(status='AC'))

    def get_upcoming_appointments(self) -> List[dict]:
        '''Get the patient's upcoming appointments as a list of dicts.'''
        return [
            appointment
            for appointment in self.patient.upcoming_appointments
            if arrow.get(appointment['startTime']) > arrow.now() 
            and appointment['state']['state'] != 'CLD'
        ]

    def get_next_appointment(self) -> Optional[dict]:
        '''
        Get the next appointment for the patient.
        '''
        upcoming_appointments = self.get_upcoming_appointments()
        return (
            min(
                upcoming_appointments,
                key=lambda x: arrow.get(x['startTime']),
            )
            if bool(upcoming_appointments)
            else None
        )

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
        if entries := response.json().get('entry'):
            return [x['resource'] for x in entries]
        return None

    def upsert_task(
        self,
        task_description: str,
        created_by_key: str,
        team_id: str,
    ) -> bool:
        '''
        Create a task if it does not already exist (by description).
        '''
        if not self.check_active_task_exists_by_description(task_description):
            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=created_by_key,
                status='OPEN',
                title=task_description,
                team_identifier=team_id,
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
        if self.get_next_appointment() and (
            arrow.get(self.get_next_appointment()['startTime']) - arrow.now()
            < datetime.timedelta(hours=72)
        ):
            if self.has_completed_questionnaire(BehavioralHealthIntakeQuestionnaire):
                result.status = STATUS_NOT_APPLICABLE
                result.add_narrative('Patient has completed intake questionnaire.')
            elif self.upsert_task(
                task_description='No intake questionnaire.',
                created_by_key=CANVAS_BOT_KEY,
                team_id=TEAM_ID,
            ):
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    'Patient has not completed intake questionnaire. '
                    'A task has been created for a care coordinator to '
                    'address this.'
                )
            else:
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    'Patient already has a task for a care coordinator to address this.'
                )
        else:
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative('Patient has no upcoming appointments within 72 hours.')
        return result

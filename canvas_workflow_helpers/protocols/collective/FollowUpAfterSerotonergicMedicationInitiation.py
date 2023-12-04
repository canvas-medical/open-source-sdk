import datetime

from typing import List, Optional, Type

import arrow

from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.patient_recordset import (
    PatientRecordSet,
)
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_SATISFIED,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import FollowUpRecommendation
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.value_set.medication_class_path2018 import (
    AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris,
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris,
)
from canvas_workflow_kit.value_set.value_set import ValueSet
from requests import RequestException, Response

SSRIS_SNRIS = (
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris
    | AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris
)
# Replace the following values:
WEBHOOK_URL = 'https://webhook.site/9b855cdb-572f-455e-b73c-a8385d1ef86b'
WEBHOOK_HEADERS = {'Content-Type': 'application/json'}
CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'


class FollowUpAfterSerotonergicMedicationInitiation(ClinicalQualityMeasure):
    class Meta:
        title = 'Follow up after serotonergic medication initiation'
        description = '''
        If patient is started on a medication in SSRI or SNRI class AND 
        have never taken this medication before:
            * Send a webhook with information about the new prescription.
            * Create a task due in 2 weeks for care coordination team to check in with the patient 
                regarding medication tolerability.
            * Recommend a follow-up visit in 4 weeks.
        '''
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.PRESCRIPTION]
        references = []

    def has_taken_medications_before(self, medications: Type[ValueSet]) -> bool:
        '''
        Return true if the patient has taken any of the medications
        in the ValueSet besides the one being prescribed.
        '''
        medication_records = self.patient.medications.find(medications).records
        prescribed_medication_id = self.get_prescribed_medication()[0]['medicationId']
        return any(x['id'] != prescribed_medication_id for x in medication_records)

    def get_prescribed_medication(self) -> PatientRecordSet:
        '''
        Get the current medication being prescribed in the protocol trigger.
        '''
        medication_id = self.field_changes['external_id']
        return self.patient.prescriptions.filter(externallyExposableId=medication_id)

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
        Creates a task for a care coordinator
        to check in with the patient in 2 weeks.
        '''
        description = 'Patient has a new SSRI/SNRI prescription. Check in with them in 2 weeks.'
        if not self.check_active_task_exists_by_description(description):
            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=CANVAS_BOT_KEY,
                status='OPEN',
                title=description,
                team_identifier=TEAM_IDENTIFIER,
                due=arrow.now().shift(weeks=2).isoformat(),
                created=arrow.now().isoformat(),
                tag=None,
                labels=None,
            )
            self.set_updates([task_payload])
            return True
        return False

    def create_follow_up(self, result: ProtocolResult) -> None:
        '''
        Creates a follow up appointment recommendation.
        '''
        result.add_recommendation(
            FollowUpRecommendation(
                key='RECOMMEND_FOLLOW_UP_SSRI_SNRI',
                patient=self.patient,
                title='Follow up in 4 weeks.',
            )
        )

    def send_webhook(self) -> Response:
        '''
        Sends a webhook to the patient portal with instructions and information
        about anxiety / high blood pressure.
        '''
        payload = {'text': 'Some information about SSRIs/SNRIs.'}
        return send_notification(
            url=WEBHOOK_URL,
            payload=payload,
            headers=WEBHOOK_HEADERS,
        )

    def get_upcoming_appointments(self) -> List[dict]:
        '''Get the patient's upcoming appointments as a list of dicts.'''
        return [
            appointment
            for appointment in self.patient.upcoming_appointments
            if arrow.get(appointment['startTime']) > arrow.now() 
            and appointment['state']['state'] != 'CLD'
        ]

    def has_appointment_within(self, time: datetime.timedelta) -> bool:
        '''Return True if the patient has an appointment in the specified time delta from now.'''
        upcoming_appointments = self.get_upcoming_appointments()
        return bool(
            [x for x in upcoming_appointments if arrow.get(x['startTime']) < arrow.now() + time]
        )

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        current_medication = self.get_prescribed_medication()
        if not current_medication.find(SSRIS_SNRIS):
            result.status = STATUS_UNCHANGED
            narrative = 'Patient not prescribed an SSRI/SNRI.'
        elif not self.has_taken_medications_before(SSRIS_SNRIS):
            narrative = (
                'First-time SSRI/SNRI prescription'
            )
            if self.has_appointment_within(datetime.timedelta(weeks=4)):
                result.status = STATUS_SATISFIED
            else:
                result.status = STATUS_DUE
                self.create_follow_up(result)
            self.upsert_task()
            self.send_webhook()
        else:
            result.status = STATUS_UNCHANGED
            narrative = (
                'Patient has a new SSRI/SNRI prescription but has taken '
                'this class of medications before.'
            )

        result.add_narrative(narrative)
        return result

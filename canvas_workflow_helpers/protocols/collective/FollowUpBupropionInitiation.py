from typing import List, Optional, Type

import arrow

from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.patient_recordset import PatientRecordSet
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import FollowUpRecommendation
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.value_set import ValueSet
from requests import RequestException, Response

# Replace the following values:
WEBHOOK_URL = 'https://webhook.site/9b855cdb-572f-455e-b73c-a8385d1ef86b'
WEBHOOK_HEADERS = {'Content-Type': 'application/json'}
CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'


class Bupropion(ValueSet):
    VALUE_SET_NAME = 'Bupropion'
    RXNORM = {
        '1232586',
        '1551469',
        '2611261',
        '42568',
        '835486',
        '316945',
        '317541',
        '1151131',
        '1151133',
        '42347',
        '1551467',
        '2611256',
        '203204',
        '993548',
        '1232591',
        '1551474',
        '2611266',
        '993511',
        '993528',
        '993537',
        '993545',
        '993552',
        '993564',
        '993569',
        '993683',
        '993688',
        '1232587',
        '1551470',
        '2611262',
        '993510',
        '993527',
        '993534',
        '993551',
        '993563',
        '993568',
        '993682',
        '1232588',
        '1551471',
        '2611265',
        '491056',
        '835488',
        '94591',
        '2654526',
        '2655096',
        '2655370',
        '2656765',
        '2656792',
        '2658826',
        '1168564',
        '1168565',
        '1187946',
        '1187947',
        '1232589',
        '1232590',
        '1551472',
        '1551473',
        '2611263',
        '2611264',
        '1232585',
        '1551468',
        '1801289',
        '2611260',
        '993503',
        '993518',
        '993536',
        '993541',
        '993550',
        '993557',
        '993567',
        '993681',
        '993687',
        '993691',
        '1232584',
        '1551462',
        '2611255',
        '993502',
        '993517',
        '993532',
        '993549',
        '993556',
        '993566',
        '993680',
        '993690',
        '1551466',
        '2611259',
        '378233',
        '378354',
        '1151365',
        '1151366',
        '1551464',
        '1551465',
        '2611257',
        '2611258',
    }


class FollowUpBupropionInitiation(ClinicalQualityMeasure):
    class Meta:
        title = 'Follow up bupropion initiation'
        description = '''
            If a patient is prescribed bupropion (bupropion, or wellbutrin, or 
            bupropion XL, or wellbutrin XL), and the patient has not been 
            prescribed bupropion before then:
            * Send webhook to patient portal with instructions and information 
                about monitoring anxiety / high blood pressure
            * Create task due in 1 week for care coordinator to check in with 
                the patient regarding medication tolerability and to request 
                their blood pressure information.
            * Recommend schedule follow up for the patient in 4 weeks
            '''
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.PRESCRIPTION]
        references = []

    def has_taken_medications_before(self, medications: Type[ValueSet]) -> bool:
        '''
        Return True if the patient has taken any of the medications
        in the ValueSet besides the one being prescribed.
        '''
        medication_records = self.patient.medications.find(medications).records
        prescribed_medication_id = self.get_prescribed_medication()[0]['medicationId']
        return any(x['id'] != prescribed_medication_id for x in medication_records)

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
        to check in with the patient in 1 week.
        '''
        description = 'Follow up with patient regarding bupropion prescription.'
        if not self.check_active_task_exists_by_description(description):
            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=CANVAS_BOT_KEY,
                status='OPEN',
                title=description,
                team_identifier=TEAM_IDENTIFIER,
                due=arrow.now().shift(weeks=1).isoformat(),
                created=arrow.now().isoformat(),
                tag=None,
                labels=None,
            )
            self.set_updates([task_payload])
            return True
        return False

    def get_prescribed_medication(self) -> PatientRecordSet:
        '''
        Get the current medication being prescribed in the protocol trigger.
        '''
        medication_id = self.field_changes['external_id']
        return self.patient.prescriptions.filter(externallyExposableId=medication_id)

    def create_follow_up(self, result: ProtocolResult) -> None:
        '''
        Creates a follow up appointment recommendation.
        '''
        result.add_recommendation(
            FollowUpRecommendation(
                key='RECOMMEND_FOLLOW_UP',
                patient=self.patient,
                title='Follow up in 4 weeks.',
            )
        )

    def send_webhook(self) -> Response:
        '''
        Sends a webhook to the patient portal with instructions and information
        about monitoring anxiety / high blood pressure.
        '''
        payload = {'text': 'Some information about monitoring anxiety / high blood pressure.'}
        return send_notification(
            url=WEBHOOK_URL,
            payload=payload,
            headers=WEBHOOK_HEADERS,
        )

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        current_medication = self.get_prescribed_medication()
        if current_medication.find(Bupropion):
            if not self.has_taken_medications_before(Bupropion):
                result.status = STATUS_DUE
                self.upsert_task()
                self.create_follow_up(result)
                self.send_webhook()
                result.add_narrative(
                    'Bupropion therapy initiated'
                )
            else:
                result.status = STATUS_UNCHANGED
                result.add_narrative('Patient has taken this medication before.')
        else:
            result.status = STATUS_UNCHANGED
            result.add_narrative('Patient is not being prescribed bupropion.')
        return result

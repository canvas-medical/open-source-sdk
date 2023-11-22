from typing import Type

from canvas_workflow_kit.patient_recordset import PatientRecordSet
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.medication_class_path2018 import (
    AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris,
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris,
)
from requests import Response

# Replace the following values:
WEBHOOK_URL = 'https://webhook.site/4de5254b-fc30-4c46-be67-d0d9d7d329d8'
WEBHOOK_HEADERS = {'Content-Type': 'application/json'}

SSRIS_SNRIS = (
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris
    | AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris
)


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

class MonitorForSerotoninSyndrome(ClinicalQualityMeasure):
    class Meta:
        title = 'Monitor for serotonin syndrome'
        description = '''
            Ensure patient receives education on monitoring for serotonin 
            syndrome if being prescribed both bupropion and an SSRI / SNRI. 
            Bupropion does have some (minimal) risk of serotonin syndrome, but 
            this appears to be mostly when used in conjunction with other 
            serotonergic medications and not on its own.
            '''
        version = '2.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.PRESCRIPTION]
        references = []
        notification_only = True

    def has_active_medications(self, medications: Type[ValueSet]) -> bool:
        '''Return True if the patient has an active medication in the given ValueSet.'''
        return bool(self.patient.medications.find(medications).filter(status='active'))

    def get_prescribed_medication(self) -> PatientRecordSet:
        '''
        Get the current medication being prescribed in the protocol trigger.
        '''
        external_id = self.field_changes['external_id']
        return self.patient.prescriptions.filter(externallyExposableId=external_id)

    def has_taken_medications_before(self, medications: Type[ValueSet]) -> bool:
        '''
        Return true if the patient has taken any of the medications
        in the ValueSet besides the one being prescribed.
        '''
        medication_records = self.patient.medications.find(medications).records
        prescribed_medication_id = self.get_prescribed_medication()[0]['medicationId']
        return any(x['id'] != prescribed_medication_id for x in medication_records)

    def send_webhook(self) -> Response:
        '''
        Sends a webhook to the patient portal with instructions and information
        about monitoring for serotonin syndrome.
        '''
        payload = {'text': 'Some information about monitoring for serotonin syndrome.'}
        return send_notification(
            url=WEBHOOK_URL,
            payload=payload,
            headers=WEBHOOK_HEADERS,
        )

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        current_medication = self.get_prescribed_medication()
        if (
            current_medication.find(Bupropion)
            and not self.has_taken_medications_before(Bupropion)
            and self.has_active_medications(SSRIS_SNRIS)
        ) or (
            current_medication.find(SSRIS_SNRIS)
            and not self.has_taken_medications_before(SSRIS_SNRIS)
            and self.has_active_medications(Bupropion)
        ):
            result.status = STATUS_SATISFIED
            self.send_webhook()
            result.add_narrative(
                'Webhook sent to patient portal for serotonin syndrome monitoring.'
            )
        else:
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative(
                'Patient is not taking a new combination of bupropion and an SSRI/SNRI.'
            )
        return result

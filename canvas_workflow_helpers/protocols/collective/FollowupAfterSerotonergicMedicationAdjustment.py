from typing import Type

import arrow

from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.patient_recordset import (
    SYSTEM_CODE_MAPPING,
    MedicationRecordSet,
    PatientRecordSet,
)
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_SATISFIED,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set.medication_class_path2018 import (
    AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris,
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris,
)
from canvas_workflow_kit.value_set.value_set import ValueSet

SSRIS_SNRIS = (
    AntidepressantSerotoninNorepinephrineReuptakeInhibitorsSnris
    | AntidepressantSelectiveSerotoninReuptakeInhibitorsSsris
)

CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'


class FollowupAfterSerotonergicMedicationAdjustment(ClinicalQualityMeasure):
    class Meta:
        title = 'Follow-up after serotonergic medication adjustment'
        description = (
            'If dose or active ingredient of SSRI/SNRI is adjusted, then '
            'create a task in 2 weeks for care coordinator to check in with the'
            'patient regarding medication tolerability and ensure they were '
            'able to pick up the medication.'
        )
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
        external_id = self.field_changes['external_id']
        return self.patient.prescriptions.filter(externallyExposableId=external_id)

    @staticmethod
    def medications_to_value_set(
        record_set: MedicationRecordSet, class_name: str
    ) -> Type[ValueSet]:
        '''
        Convert a record set of medications to a ValueSet
        class that can be used to search record sets.
        '''
        # Get a list of tuples of (system, code) from the MedicationRecordSet
        val = [
            (system, code['code'])
            for record in record_set.records
            for code in record['coding']
            for system in SYSTEM_CODE_MAPPING.get(code['system'], [code['system']])
        ]
        # Create the input for the ValueSet class
        value_set_input = {'VALUE_SET_NAME': class_name}
        for system, code in val:
            if system not in value_set_input:
                value_set_input[system.upper()] = set()
            value_set_input[system.upper()].add(code)
        # Create a ValueSet class
        return type(class_name, (ValueSet,), value_set_input)

    def create_task(self) -> None:
        '''
        Creates a task for a care coordinator
        to check in with the patient in 2 weeks.
        '''
        description = (
            'Patient has a new SSRI/SNRI prescription but has a history of taking SSRI/SNRI. '
            'Check in with them in 2 weeks.'
        )
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

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        current_medication = self.get_prescribed_medication()
        CurrentMedicationValueSet = self.medications_to_value_set(
            record_set=current_medication, class_name='CurrentMedication'
        )
        if (
            not current_medication.find(SSRIS_SNRIS)
            or self.has_taken_medications_before(CurrentMedicationValueSet)
            or not self.has_taken_medications_before(SSRIS_SNRIS)
        ):
            result.status = STATUS_UNCHANGED
            narrative = (
                'Patient has not taken an SSRI/SNRI before or has already taken this drug.'
                if current_medication.find(SSRIS_SNRIS)
                else 'Patient not prescribed an SSRI/SNRI.'
            )
            result.add_narrative(narrative)
        else:
            result.status = STATUS_SATISFIED
            result.add_narrative(
                'Patient has not taken this medication before '
                'but has a history of taking SSRIs/SNRIs.'
                'A task has been created to check in with the patient.'
            )
            self.create_task()
        return result

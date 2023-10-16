import json
import arrow

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.internal.integration_messages import create_task_payload


class AppointmentCoverageCheck(ClinicalQualityMeasure):
    class Meta:
        title = 'Appointment Coverage Check'
        version = 'v1.0.0'
        description = 'Listens for appointment creates and generates a task if patient does not have coverage.'
        types = ['Task']
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

        notification_only = True

    def find_provider_key(self):
        appointment_note_id = self.get_new_field_value('note_id')
        if self.patient.upcoming_appointment_notes:
            appointment_note = self.get_record_by_id(
                self.patient.upcoming_appointment_notes, appointment_note_id)
            return appointment_note.get('providerDisplay', {}).get('key')
        return None

    def get_record_by_id(self, recordset, id):
        if recordset is not None:
            recordset_filter = recordset.filter(id=id)
            if recordset_filter:
                return json.loads(json.dumps(recordset_filter[0], default=str))
        return {}

    def get_new_field_value(self, field_name):
        change_context_fields = self.field_changes.get('fields', {})
        if field_name not in change_context_fields:
            return None
        return change_context_fields[field_name][1]

    def is_appointment_and_created(self):
        change_context = self.field_changes
        if not change_context:
            return False

        changed_model = change_context.get('model_name')
        created = change_context.get('created')
        # we only care about appointments that have been created
        if changed_model != 'appointment' or not created:
            return False
        return True

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if len(self.patient.patient['coverages']):
            return result

        if self.is_appointment_and_created():
            appointment_start_time = self.get_new_field_value('start_time')

            provider_key = self.find_provider_key()
            if provider_key is None:
                return result  # not able to assign a task without a provider_key

            first_name = self.patient.first_name
            if appointment_start_time:
                appt_day = arrow.get(appointment_start_time).format(
                    'YYYY - MM - DD')
                due = arrow.get(appointment_start_time).shift(
                    days=-3).isoformat()
            else:
                appt_day = 'unknown date'
                due = 'three days before scheduled appointment'

            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=provider_key,
                status="OPEN", # This can be anything from the list ["COMPLETED", "CLOSED", "OPEN"]
                title=f'{first_name} has no coverage listed and has an appointment on {appt_day}. Please call to verify coverage.',
                assignee_identifier=provider_key,
                due=due,
                created=arrow.now().isoformat(),
                tag=None,
            )

            self.set_updates([task_payload])

            result.add_narrative("successfully created task")
        return result

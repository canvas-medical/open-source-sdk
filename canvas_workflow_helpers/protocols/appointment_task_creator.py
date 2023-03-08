import json
import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.internal.integration_messages import create_task_payload



class AppointmentTaskCreator(ClinicalQualityMeasure):
    """
    Protocol that listens for appointment creates and generates a task.
    """

    class Meta:

        title = 'Appointment Task Creator'

        version = 'v1.0.0'

        description = 'Listens for appointment creates and generates a task.'

        types = ['Task']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

    # This is a hard-coded team identifier that is always responsible calling patients
    # You can normally get this ID from our FHIR Group Search endpoint
    TEAM_IDENTIFIER = '0564c236-9ebe-43e2-8f21-c8e28f6d60c3'

    def get_record(self, recordset, identifiers):
        if recordset is not None:
            recordset_filter = recordset.filter(**identifiers)
            if recordset_filter:
                return json.loads(json.dumps(recordset_filter[0], default=str))
        return {}

    def get_newly_created_appointment(self):
        change_context = self.field_changes
        if not change_context:
            return False

        changed_model = change_context.get('model_name')
        created = change_context.get('created')
        # we only care about appointments that have been created
        if changed_model != 'appointment' or not created:
            return False
        return change_context['canvas_id']

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        apt_id = self.get_newly_created_appointment()
        if apt_id:
            appointment = self.get_record(
                self.patient.upcoming_appointments, {'id': apt_id})

            appointment_note = self.get_record(
                self.patient.upcoming_appointment_notes, {'currentAppointmentId': apt_id})

            if not appointment:
                return result

            provider_key = appointment_note.get('providerDisplay', {}).get('key')
            appointment_start_time = appointment.get('startTime')

            if provider_key is None or appointment_start_time is None:
                return result

            first_name = self.patient.patient['firstName']
            appt_day = arrow.get(appointment_start_time).format('YYYY-MM-DD')
            due = arrow.get(appointment_start_time).shift(days=-3).isoformat()

            task_payload = create_task_payload(
                patient_key=self.patient.patient['key'],
                created_by_key=provider_key,
                status="OPEN", # This can be anything from the list ["COMPLETED", "CLOSED", "OPEN"]
                title=f'{first_name} has an appointment on {appt_day}. Please call to remind!',
                assignee_identifier=provider_key,
                team_identifier=self.TEAM_IDENTIFIER,
                due=due,
                created=arrow.now().isoformat(),
                tag=None,
                labels=["Urgent"]
            )

            self.set_updates([task_payload])

        return result

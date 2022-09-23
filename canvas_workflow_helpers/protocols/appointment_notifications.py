import json

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification


class AppointmentNotification(ClinicalQualityMeasure):
    """
    Protocol that listens for appointment create / update and sends a notification.
    """

    class Meta:

        title = 'Appointment Notification'

        version = 'v1.0.0'

        description = 'Listens for appointment create / update and sends a notification.'

        information = 'https://canvasmedical.com/'

        identifiers = ['AppointmentNotification']

        types = ['Notification']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

        notification_only = True

    def appointment_note_has_a_previously_booked_appointment(
            self, appointment_note_id):
        if self.patient.upcoming_appointment_notes:
            appointment_note = self.get_record_by_id(
                self.patient.upcoming_appointment_notes, appointment_note_id)
            state_history = appointment_note.get('stateHistory', [])
            if len(state_history) >= 2:
                previous_states = [s['state'] for s in state_history][:-1]
                return 'BKD' in previous_states
        return False

    def get_appointment_from_note_id(self, note_id):
        if self.patient.upcoming_appointment_notes:
            appointment_note = self.get_record_by_id(
                self.patient.upcoming_appointment_notes, note_id)
            appointment_id = appointment_note.get('currentAppointmentId')
            return self.get_record_by_id(self.patient.upcoming_appointments,
                                         appointment_id)
        return None

    def get_new_field_value(self, field_name):
        change_context_fields = self.field_changes.get('fields', {})
        if field_name not in change_context_fields:
            return None
        return change_context_fields[field_name][1]

    def get_record_by_id(self, recordset, id):
        if recordset is not None:
            recordset_filter = recordset.filter(id=id)
            if recordset_filter:
                return json.loads(json.dumps(recordset_filter[0], default=str))
        return {}

    def get_appointment_by_note_state_event(self, _id):
        for apt in self.patient.appointments:
            state_id = apt.get('state', {}).get('id')
            if state_id == _id:
                return json.loads(json.dumps(apt, default=str))
        return {}

    @property
    def patient_external_id(self):
        external_identifiers = self.patient.patient.get('externalIdentifiers', [])
        if len(external_identifiers):
            return external_identifiers[0]['value']
        return ''

    @property
    def base_payload(self):
        return {
            'canvas_patient_key': self.patient.patient['key'],
            'external_patient_id': self.patient_external_id
        }

    # REPLACE this url with your server url which should receive these notifications
    notification_url = 'https://webhook.site/a018a2b8-ab4a-4692-8e78-503cb3f2cb9c'
    headers = {'Content-Type': 'application/json'}

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        change_context = self.field_changes
        payload = self.base_payload
        changed_model = change_context.get('model_name', '')

        if changed_model == 'notestatechangeevent':
            state = self.get_new_field_value('state')
            state_map = {
                'CLD': 'cancelled',
                'NSW': 'no_show',
                'RVT': 'reverted',
                'CVD': 'checked_in'
            }

            # we only care about cancelled, no-show, reverted, or check-in state changes
            if state not in state_map:
                return result

            appointment = self.get_appointment_by_note_state_event(self.field_changes['canvas_id'])

            payload = {
                **payload,
                'appointment_external_id': appointment.get('externallyExposableId')
                state_map[state]: True
            }

        elif changed_model == 'appointment':
            appointment_start_time = self.get_new_field_value('start_time')
            payload = {
                **payload,
                'appointment_external_id': change_context.get('external_id'),
                'start_time': appointment_start_time
            }

            created = change_context.get('created')
            if created:
                appointment_note_id = self.get_new_field_value('note_id')
                rescheduled = self.appointment_note_has_a_previously_booked_appointment(
                    appointment_note_id)
            else:
                rescheduled = appointment_start_time is not None

            if rescheduled:
                payload = {**payload, 'rescheduled': True}
            elif created:
                payload = {**payload, 'created': True}

        else:
            return result

        send_notification(self.notification_url, json.dumps(payload),
                          self.headers)

        return result

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
        if hasattr(self.context, 'get'):
            change_context_fields = self.context['change_info']['fields']
            if field_name not in change_context_fields:
                return None
            return change_context_fields[field_name][1]
        return None

    def get_record_by_id(self, recordset, id):
        if recordset is not None:
            recordset_filter = recordset.filter(id=id)
            if recordset_filter:
                return json.loads(json.dumps(recordset_filter[0], default=str))
        return {}

    @property
    def patient_external_id(self):
        external_identifiers = self.patient.patient['externalIdentifiers']
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
    notification_url = 'http://cfc4-76-224-185-72.ngrok.io'

    headers = {'Content-Type': 'application/json'}

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if not hasattr(self.context, 'get'):
            return result
        change_context = self.context.get('change_info')
        payload = self.base_payload
        changed_model = change_context.get('model_name', '')

        if changed_model == 'notestatechangeevent':
            cancelled = self.get_new_field_value('state') == 'CLD'
            # we only care about cancelled state changes
            if not cancelled:
                return result

            appointment = self.get_appointment_from_note_id(
                self.get_new_field_value('note_id'))
            payload = {
                **payload, 'cancelled': True,
                'appointment_external_id':
                appointment.get('externallyExposableId')
            }

        elif changed_model == 'appointment':
            appointment_start_time = self.get_new_field_value('start_time')
            payload = {
                **payload, 'appointment_external_id':
                change_context['external_id'],
                'start_time': appointment_start_time
            }

            created = change_context['created']
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
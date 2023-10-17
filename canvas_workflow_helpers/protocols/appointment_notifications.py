import json
import requests

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.fhir import FumageHelper


class AppointmentNotification(ClinicalQualityMeasure):
    class Meta:

        title = 'Appointment Notification'
        version = 'v1.0.0'
        description = 'Listens for appointment create / update and sends a notification.'
        types = ['Notification']
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]
        notification_only = True

    def get_rescheduled_appointment_id(
            self, appointment):
        for info in appointment.get('supportingInformation', {}):
            if info.get("display") == 'Previously Rescheduled Appointment':
                return info.get("reference").split("/")[1]

        return False

    def get_new_field_value(self, field_name):
        change_context_fields = self.field_changes.get('fields', {})
        if field_name not in change_context_fields:
            return None
        return change_context_fields[field_name][1]

    def get_appointment_by_note_state_event(self, _id):
        for apt in self.patient.appointments:
            state_id = apt.get('state', {}).get('id')
            if state_id == _id:
                return json.loads(json.dumps(apt, default=str))
        return {}

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        payload = {
            'canvas_patient_key': self.patient.patient['key'],
        }
        changed_model = self.field_changes.get('model_name', '')

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
                'appointment_external_id': appointment.get('externallyExposableId'),
                state_map[state]: True
            }

        elif changed_model == 'appointment':
            self.instance_name = self.settings.INSTANCE_NAME

            fhir = FumageHelper(self.settings)

            response = fhir.read("Appointment", self.field_changes.get('external_id'))
            if response.status_code != 200:
                raise Exception("Failed to search Appointments")

            appointment = response.json()

            rescheduled = self.get_rescheduled_appointment_id(appointment)
            created = self.field_changes.get('created')

            payload = {
                **payload,
                'appointment_external_id': self.field_changes.get('external_id'),
                'start_time': appointment.get("start"),
                'end_time': appointment.get("end")
            }

            if created and not rescheduled:
                payload['created'] = True
            elif created and rescheduled:
                payload['rescheduled'] = True
            else:
                return result
        else:
            return result

        # REPLACE this url with your server url which should receive these notifications
        send_notification(
            'https://webhook.site/6bdbe640-9c38-439a-9b89-fd9b4115d017',
            json.dumps(payload),
            headers={'Content-Type': 'application/json'})
        result.add_narrative("successfully sent appointment notification payload")

        return result

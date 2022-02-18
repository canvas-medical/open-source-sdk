import json
import pprint
import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)


class AppointmentTaskCreator(ClinicalQualityMeasure):
    """
    Protocol that listens for appointment creates and generates a task.
    """

    class Meta:

        title = 'Appointment Task Creator'

        version = 'v1.0.0'

        description = 'Listens for appointment creates and generates a task.'

        information = 'https://canvasmedical.com/'

        identifiers = ['AppointmentTaskCreator']

        types = ['Task']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

        notification_only = True

    def get_record_by_id(self, recordset, id):
        print("RECORDS", recordset, type(recordset))
        if recordset is not None:
            # print("ARE WE GETTING HERE")
            recordset_filter = recordset.filter(id=id)
            if len(recordset_filter):
                return json.loads(json.dumps(recordset_filter[0], default=str))

        return {}

    def get_new_field_value(self, field_name):
        # print("ARE WE GETTING", self.context, type(self.context))
        if hasattr(self.context, 'get'):
            change_context_fields = self.context['change_info']['fields']
            # print("ARE WE GETTING", change_context_fields)
            if field_name not in change_context_fields:
                return None
            return change_context_fields[field_name][1]
        return None

    def compute_results(self):
        result = ProtocolResult()
        # print("PROTOCOL", result)
        # pp = pprint.PrettyPrinter(indent=4)
        print("SELF", vars(self))
        result.status = STATUS_NOT_APPLICABLE

        if hasattr(self.context, 'get'):
            change_context = self.context.get('change_info')
            if not change_context:
                return result

            changed_model = change_context['model_name']
            created = change_context['created']

            # we only care about appointments that have been created
            if changed_model != 'appointment' or not created:
                return result

        appointment_start_time = self.get_new_field_value('start_time')
        appointment_note_id = self.get_new_field_value('note_id')
        appointment_note = self.get_record_by_id(
            self.patient.upcoming_appointment_notes, appointment_note_id)

        provider_key = appointment_note.get('providerDisplay', {}).get('key')
        patient_key = self.patient.patient['key']
        first_name = self.patient.patient['firstName']
        appt_day = arrow.get(appointment_start_time).format('YYYY - MM - DD')

        update_payload = {
            'integration_type': 'Task',
            'integration_source': '',
            'patient_identifier': {
                'identifier_type': 'key',
                'identifier': {
                    'key': patient_key
                }
            },
            'integration_payload': {
                'creator': {
                    'identifier_type': 'key',
                    'identifier': {
                        'key': provider_key
                    }
                },
                'assignee': {
                    'identifier_type': 'key',
                    'identifier': {
                        'key': provider_key
                    }
                },
                'title':
                f'{first_name} has an appointment on {appt_day}. Please call to remind!',
                'due':
                arrow.get(appointment_start_time).shift(days=-3).isoformat(),
                'status': 'OPEN'
            }
        }

        self.set_updates([update_payload])

        return result

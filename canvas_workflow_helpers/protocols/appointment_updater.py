from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)


class AppointmentUpdate(ClinicalQualityMeasure):
    """
    Adds a meeting link to an appointment after it is created
    """

    class Meta:
        title = 'Appointment Update'

        version = '2021-v1'

        description = 'Adds a meeting link to an appointment after it is created'

        information = 'https://canvasmedical.com'

        identifiers = []

        types = []

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        notification_only = True

    meeting_link = 'https://www.google.com/search?q=video+call'

    def get_new_field_value(self, field_name):
        change_context_fields = self.context['change_info']['fields']
        if field_name not in change_context_fields:
            return None
        return change_context_fields[field_name][1]

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        change_context = self.context.get('change_info')
        if not change_context:
            return result

        changed_model = change_context['model_name']
        created = change_context['created']
        # we only care about appointments that have been created
        if changed_model != 'appointment' or not created:
            return result

        appointment_external_id = self.get_new_field_value(
            'externally_exposable_id')

        update_payload = {
            'integration_type': 'Update Appointment',
            'integration_source': 'Protocol',
            'patient_identifier': {
                'identifier_type': 'key',
                'identifier': {
                    'key': self.patient.patient['key']
                }
            },
            'integration_payload': {
                'appointment_id': appointment_external_id,
                'meeting_link':
                f'{self.meeting_link}+{appointment_external_id}'
            }
        }

        self.set_updates([update_payload])

        return result
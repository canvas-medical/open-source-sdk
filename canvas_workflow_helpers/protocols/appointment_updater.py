from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE,
                                          ClinicalQualityMeasure,
                                          ProtocolResult)
from canvas_workflow_kit.fhir import FumageHelper


class AppointmentUpdate(ClinicalQualityMeasure):

    class Meta:
        title = 'Appointment Update'
        version = 'v1.0.0'
        description = 'Adds a meeting link to a Telehealth appointment after it is created'
        types = ['Update']
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]
        notification_only = True

    meeting_link = 'https://www.google.com/search?q=video+call'

    def is_appointment_telehealth(self, appointment_external_id):
        appointment = self.patient.upcoming_appointments.filter(externallyExposableId=appointment_external_id)
        if appointment:
            return appointment[0]['noteType']['isTelehealth']

    def compute_results(self):
        result = ProtocolResult()

        changed_model = self.field_changes.get('model_name')
        created = self.field_changes.get('created')
        # we only care about appointments that have been created
        if changed_model != 'appointment' or not created:
            return result

        appointment_external_id = self.field_changes.get('external_id')

        if not self.is_appointment_telehealth(appointment_external_id):
            return result

        fhir = FumageHelper(self.settings)

        response = fhir.read("Appointment", appointment_external_id)
        if response.status_code != 200:
            raise Exception("Failed to search Appointments")

        appointment = response.json()

        if "contained" in appointment:
            supporting_info_id = appointment['contained'][0]['id']
        else:
            supporting_info_id = "appointment-meeting-endpoint"
            appointment['supportingInformation'].append({
                "reference": f"#{supporting_info_id}",
                "type": "Endpoint"
            })

        appointment['contained'] = [{
            "resourceType": "Endpoint",
            "id": supporting_info_id,
            "status": "active",
            "connectionType": {
                "code": "https"
            },
            "payloadType": [{
                "coding":[{
                    "code": "video-call"
                }]
            }],
            "address": f'{self.meeting_link}+{appointment_external_id}'
        }]

        response = fhir.update("Appointment", appointment_external_id, appointment)

        if response.status_code != 200:
            raise Exception(f"Failed to update Appointment response with error: {response.text} headers: {response.headers}")

        result.add_narrative(f"Successfully updated Appointment {appointment_external_id} meeting link")

        return result

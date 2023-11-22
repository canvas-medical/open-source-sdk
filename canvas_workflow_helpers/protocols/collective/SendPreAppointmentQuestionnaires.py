from typing import List
from canvas_workflow_kit.protocol import (
    STATUS_SATISFIED,
    STATUS_NOT_APPLICABLE,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    CHANGE_TYPE,
    ProtocolResult,
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.fhir import FumageHelper
import json
import arrow
from requests import RequestException

# Fill in the following values:
WEBHOOK_URL = 'https://webhook.site/4de5254b-fc30-4c46-be67-d0d9d7d329d8'
WEBHOOK_HEADERS = {'Content-Type': 'application/json'}


class PHQ_9(ValueSet):
    VALUE_SET_NAME = 'PHQ-9'
    LOINC = {'44249-1'}


class GAD_7(ValueSet):
    VALUE_SET_NAME = 'GAD-7'
    LOINC = {'69737-5'}


class SendPreAppointmentQuestionnaires(ClinicalQualityMeasure):
    class Meta:
        title = 'Send pre-appointment questionnaires'
        description = (
            'This protocol is triggered when a patient is scheduled for a new appointment. '
            'If the patient has not completed a PHQ-9/GAD-7 in the past 2 months and the '
            'visit is for anxiety/depression, a webhook is sent.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]
        references = []

    def get_questionnaires(self, questionnaire: ValueSet) -> List[dict]:
        return self.patient.interviews.find(questionnaire).filter(status='AC')

    def has_completed_questionnaire_within_timeframe(
        self, questionnaire: ValueSet, timeframe: Timeframe
    ) -> bool:
        return bool(self.get_questionnaires(questionnaire).within(timeframe))

    def get_triggering_appointment_id(self) -> int:
        return self.field_changes['fields']['externally_exposable_id'][1]

    def get_triggering_appointment(self) -> dict:
        appointment_id = self.get_triggering_appointment_id()
        fumage = FumageHelper(self.settings)
        response = fumage.read('Appointment', appointment_id)
        if not response.ok:
            raise RequestException(
                f"Failed to read Appointment with {appointment_id} and"
                f"correlation-id {response.headers['fumage-correlation-id']}"
            )
        return response.json()

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if not self.field_changes['created'] or self.field_changes['model_name'] != 'appointment':
            result.status = STATUS_UNCHANGED
            result.add_narrative('No appointment created.')
            return result

        triggering_appointment = self.get_triggering_appointment()
        reason_for_visit = triggering_appointment.get('description', '')

        if all(term not in reason_for_visit.lower() for term in ['anxiety', 'depression']):
            result.status = STATUS_UNCHANGED
            result.add_narrative("Patient's upcoming appointment is not for anxiety/depression.")
            return result

        last_2_months = Timeframe(arrow.now().shift(months=-2), arrow.now())
        questionnaires = {PHQ_9: 'PHQ-9', GAD_7: 'GAD-7'}
        narrative_not_completed = (
            'Patient has not completed a {} in the past 2 months and their upcoming visit is for '
            'anxiety/depression.'
        )

        for questionnaire, name in questionnaires.items():
            has_completed = self.has_completed_questionnaire_within_timeframe(
                questionnaire=questionnaire, timeframe=last_2_months
            )
            if not has_completed:
                payload = {'text': narrative_not_completed.format(name)}
                send_notification(
                    WEBHOOK_URL,
                    payload=json.dumps(payload),
                    headers=WEBHOOK_HEADERS,
                )
                result.add_narrative(narrative_not_completed.format(name))
                result.status = STATUS_SATISFIED

        if result.status != STATUS_SATISFIED:
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative('Patient has completed a PHQ-9 and GAD-7 in the past 2 months.')

        return result

import arrow
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)
from canvas_workflow_kit.patient import Patient
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.intervention import BannerAlertIntervention


# Replace with your the group UUID for your team
# (obtain from <your_instance>.canvasmedical.com/admin/api/group/
TEAM_IDENTIFIER = 'cd002206-7a26-40e0-9363-3f5e93befa83'
CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'


class NoShowHandler(ClinicalQualityMeasure):
    class Meta:
        title = 'No Show Handler'
        description = (
            'This protocol outlines the steps to be taken when a '
            'patient does not show up for an appointment. It includes '
            'creating a task for the scheduling team to reschedule '
            'the appointment and adding a banner alert to appointment '
            'cards to warn of prior no-shows.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.APPOINTMENT]
        references = []

    def in_denominator(self, patient: Patient) -> bool:
        if len(patient.appointments) == 0:
            return False
        for appointment in patient.appointments:
            if any(stateChange['state'] == 'NSW'
                for stateChange in appointment['stateHistory']):
                return True

    def in_numerator(self, patient: Patient) -> bool:
        return False

    def numerator_tasks(self, result: ProtocolResult):
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):

        if 'fields' in self.field_changes:
            states = self.field_changes['fields']['state']

            if states[0] != 'NSW' and states[1] == 'NSW':
                task_payload = create_task_payload(
                    patient_key=self.patient.patient['key'],
                    created_by_key=CANVAS_BOT_KEY,
                    status='OPEN',
                    title=f"Reschedule {self.patient.first_name}'s no-show appointment",
                    assignee_identifier=None,
                    team_identifier=TEAM_IDENTIFIER,
                    due=arrow.now().isoformat(),
                    created=arrow.now().isoformat(),
                    tag=None,
                    labels=[],
                )
                self.set_updates([task_payload])

        result.add_recommendation(
            BannerAlertIntervention(
                narrative=(f'{self.patient.first_name} has a prior no-show.'),
                placement=['chart', 'appointment_card'],
                intent='info',
            )
        )
        result.add_narrative(
            (
                'The patient has missed an appointment. A task has been '
                'created for the scheduling team to reschedule the appointment.'
            )
        )
        result.status = STATUS_DUE

    def excluded_tasks(self, result: ProtocolResult):
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator(self.patient):
            if self.in_numerator(self.patient):
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

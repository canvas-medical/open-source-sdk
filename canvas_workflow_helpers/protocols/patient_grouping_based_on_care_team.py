from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.internal.integration_messages import (
    ensure_patient_in_group,
    ensure_patient_not_in_group
)    
from canvas_workflow_kit.protocol import (
    STATUS_NOT_APPLICABLE,
    ClinicalQualityMeasure,
    ProtocolResult
)


class PatientGroupingByCareTeamMember(ClinicalQualityMeasure):

    class Meta:
        title = 'Patient Grouping By Care Team Member'
        version = '1.0.0'
        information = ''
        description = (
            'Protocol that updates a patients membership in a group depending on a given care. '
            'team provider/role ')
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.PATIENT]

    def has_care_team_member(self) -> bool:
        STAFF_KEY = 'e766816672f34a5b866771c773e38f3c'
        STAFF_ROLE = 'Psycho'

        for care_team_member in self.patient.patient['careTeamMemberships']:
            if (care_team_member['staff']['key'] == STAFF_KEY and
                care_team_member['role']['code'] == STAFF_ROLE):
                return True

        return False

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE
       
        patient_key = self.patient.patient['key']

        # Get this UUID from the api_group.externally_exposable_id field
        patient_group_uuid = '173e8abd-7de1-4324-b5c3-4a02089213a1'  # Replace with your group's UUID.

        # a patient should be in the group if they have a specific care team member
        if not self.has_care_team_member():
            group_update = ensure_patient_not_in_group(patient_key, patient_group_uuid)
        else:
            group_update = ensure_patient_in_group(patient_key, patient_group_uuid)

        self.set_updates([group_update])

        return result

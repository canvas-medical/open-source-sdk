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


class PatientGrouping(ClinicalQualityMeasure):
    """
    Protocol that updates a patients membership in a group depending on a given consent. 
    This particular example is of an opt-out based group membership.
    """

    # Consent codes can be found in the Admin view
    CONSENT_CODE = 'A0001'  # replace with your opt-out consent's coding

    class Meta:
        title = 'Patient Grouping'
        version = '1.0.0'
        description = (
            'Protocol that updates a patients membership in a group depending on a given consent. '
            'This particular example is of an opt-out based group membership. ')
        identifiers = ['PatientGrouping']
        types = ['CQM']
        compute_on_change_types = [CHANGE_TYPE.CONSENT]

    def has_opt_out(self) -> bool:
        consents = self.patient.consents.filter(category__code=self.CONSENT_CODE)
        
        if consents:
            state = consents[0]['state']
            return state == 'rejected'

        return False

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE
       
        patient_key = self.patient.patient['key']

        # Get this UUID from the api_group.externally_exposable_id field
        patient_group_uuid = '00000000-0000-0000-0000-000000000000'  # Replace with your group's UUID.

        # This particular group operates on an opt-out policy, so a patient should be 
        # in the group unless they have the opt-out consent
        if self.has_opt_out():
            group_update = ensure_patient_not_in_group(patient_key, patient_group_uuid)
        else:
            group_update = ensure_patient_in_group(patient_key, patient_group_uuid)

        self.set_updates([group_update])

        return result

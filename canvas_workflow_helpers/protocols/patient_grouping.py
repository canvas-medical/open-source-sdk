# type: ignores

from canvas_workflow_kit import events
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

    GROUP_NAME = 'LANES'
    CONSENT_CODE = 'LANES_CONSENT'

    class Meta:
        title = 'Patient Grouping'

        version = '1.0.0'

        information = ''

        description = (
            'Protocol that updates a patients membership in a group depending on a given consent. '
            'This particular example is of an opt-out based group membership. ')

        identifiers = ['PatientGrouping']

        types = ['CQM']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            'Canvas'
        ]

        compute_on_change_types = [
            CHANGE_TYPE.CONSENT
        ]

        funding_source = ''

        references = ['Written by Canvas']


    def has_opt_out(self) -> bool:
        consents = self.patient.consents.filter(category__code=self.CONSENT_CODE)
        
        if consents:
            state = consents[0]['state']
            return True if state == 'rejected' else False

        return False

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE
       
        patient_key = self.patient.patient['key']
        patient_group = self.patient.groups.filter(name=self.GROUP_NAME).records
        
        group_key = ''
        if not patient_group:
            return result

        group_key = patient_group[0]['externallyExposableId']

        # This particular group operates on an opt-out policy, so a patient should be 
        # in the group unless they have the opt out consent
        if self.has_opt_out():
            group_update = ensure_patient_not_in_group(patient_key, group_key)
        else:
            group_update = ensure_patient_in_group(patient_key, group_key)

        self.set_updates([group_update])

        return result

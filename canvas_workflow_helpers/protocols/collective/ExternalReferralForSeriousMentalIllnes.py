from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_UNCHANGED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import ReferRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2018 import BipolarDisorder
from canvas_workflow_kit.value_set.v2019 import SchizophreniaOrPsychoticDisorder

SeriousMentalIllness = BipolarDisorder | SchizophreniaOrPsychoticDisorder


class PsychologyOrPsychiatry(ValueSet):
    VALUE_SET_NAME = 'Psychology or Psychiatry'
    SNOMED = {'722162001', '394587001'}


class ExternalReferralForSeriousMentalIllnes(ClinicalQualityMeasure):
    class Meta:
        title = 'External referral for serious mental illness'
        description = (
            'If a patient has been diagnosed with a serious mental illness, '
            'then create a recommendation to refer the patient to an external '
            'provider.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION]
        references = []

    def is_new_smi_diagnosis(self) -> bool:
        if not self.field_changes['created']:
            return False

        condition_id = self.field_changes.get('canvas_id')
        return bool(self.patient.conditions.filter(id=condition_id).find(SeriousMentalIllness))

    def add_recommendation(self, result: ProtocolResult) -> None:
        result.add_recommendation(
            ReferRecommendation(
                key='RECOMMEND_REFERRAL_FOR_SMI',
                referral=PsychologyOrPsychiatry,
                patient=self.patient,
                condition=SeriousMentalIllness,
                title=('Refer externally'),
            )
        )

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.is_new_smi_diagnosis():
            result.status = STATUS_DUE
            result.add_narrative('Diagnosis of serious mental illness identified')
            self.add_recommendation(result)
        else:
            result.status = STATUS_UNCHANGED
            result.add_narrative(
                'Patient has not received a new diagnosis of a serious mental illness.'
            )
        return result

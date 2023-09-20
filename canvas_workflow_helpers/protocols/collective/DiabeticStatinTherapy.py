from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Diabetes,
    Type1Diabetes,
)
from canvas_workflow_kit.value_set.v2021.medication import (
    HighIntensityStatinTherapy,
    ModerateIntensityStatinTherapy,
)


class Atorvastatin20(ValueSet):
    VALUE_SET_NAME = 'Atorvastatin 20mg'
    FDB = {'163181'}


class Rosuvastatin10(ValueSet):
    VALUE_SET_NAME = 'Rosuvastatin 10mg'
    FDB = {'451294'}


class Type2Diabetes(ValueSet):
    VALUE_SET_NAME = 'Type 2 Diabetes'
    ICD10CM = Diabetes.ICD10CM - Type1Diabetes.ICD10CM


class DiabeticStatinTherapy(ClinicalQualityMeasure):
    class Meta:
        title = 'Statin initiation'
        description = (
            'This protocol recommends starting a statin at '
            'moderate intensity for patients over 40 with type 2 diabetes '
            'who are not already on a statin. High-'
            'intensity statins are recommended for those at higher '
            'cardiovascular risk. This is due to the '
            'increased risk of ASCVD in people with type 2 diabetes, '
            'and the proven benefits of statins in these '
            'patients, regardless of baseline LDL cholesterol levels.'
        )
        version = '1.0.4'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.CONDITION,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def in_denominator(self) -> bool:
        return bool(
            self.patient.conditions.find(Type2Diabetes).filter(
                clinicalStatus='active'
            )
            and self.patient.age > 40
        )

    def in_numerator(self) -> bool:
        moderate_intensity_statin = self.patient.medications.find(
            ModerateIntensityStatinTherapy
        ).filter(status='active')
        high_intensity_statin = self.patient.medications.find(
            HighIntensityStatinTherapy
        ).filter(status='active')
        return bool(moderate_intensity_statin or high_intensity_statin)

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.add_narrative(
                    (
                        'Patient with type 2 diabetes and age > 40 is '
                        'already on a statin.'
                    )
                )
                result.status = STATUS_SATISFIED
            else:
                result.add_recommendation(
                    PrescribeRecommendation(
                        key='rosuvastatin',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Rosuvastatin10,
                        title='Start rosuvastatin',
                        context={
                            'sig_original_input': 'Take one nightly',
                            'duration_in_days': 90,
                            'dispense_quantity': 90,
                            'dosage_form': 'tablet',
                            'count_of_refills_allowed': 3,
                            'generic_substitutions_allowed': True,
                            'note_to_pharmacist': '',
                        },
                    )
                )
                result.add_recommendation(
                    PrescribeRecommendation(
                        key='atorvastatin',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Atorvastatin20,
                        title='Start atorvastatin',
                        context={
                            'sig_original_input': 'Take one nightly',
                            'duration_in_days': 90,
                            'dispense_quantity': 90,
                            'dosage_form': 'tablet',
                            'count_of_refills_allowed': 3,
                            'generic_substitutions_allowed': True,
                            'note_to_pharmacist': '',
                        },
                    )
                )
                result.add_narrative(
                    (
                        'Moderate-intensity statins are recommended for '
                        'patients with type 2 diabetes and age > 40. '
                        'Consider high intensity for '
                        'patients at higher cardiovascular risk.'
                    )
                )
                result.status = STATUS_DUE
        else:
            result.add_narrative(
                'Protocol is not applicable for patients age < 40 '
                'or without type 2 diabetes.'
            )
            result.status = STATUS_NOT_APPLICABLE
        return result

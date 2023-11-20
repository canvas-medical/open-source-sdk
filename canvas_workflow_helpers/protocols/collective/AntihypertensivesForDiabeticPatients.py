from datetime import datetime
from typing import List, NamedTuple, Optional

import arrow
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
from canvas_workflow_kit.value_set.medication_class_path2018 import (
    CalciumChannelBlockers,
    DiureticThiazidesAndRelatedAndCombinations,
)
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Diabetes,
    DiagnosisOfHypertension,
    Proteinuria,
)
from canvas_workflow_kit.value_set.v2021.medication import (
    AceInhibitorOrArbOrArni,
)

BloodPressureReading = NamedTuple(
    'BloodPressureReading',
    [('systolic', float), ('diastolic', float), ('recorded_time', datetime)],
)


class AlbuminCreatinineRatio(ValueSet):
    VALUE_SET_NAME = 'Albumin/creatinine ratio'
    LOINC = {'9318-7'}


class LisinoprilRx(ValueSet):
    VALUE_SET_NAME = 'lisinopril'
    FDB = {'244899'}


class HydrochlorothiazideRx(ValueSet):
    VALUE_SET_NAME = 'hydrochlorothiazide'
    FDB = {'269382'}


class AmlodipineRx(ValueSet):
    VALUE_SET_NAME = 'amlodipine'
    FDB = {'202624'}


class HighDoseACEIARB(ValueSet):
    VALUE_SET_NAME = 'High Dose ACEI/ARB'
    RXNORM = {
        '197884',
        '199352',
        '200096',
        '205305',
        '261962',
        '283317',
        '308962',
        '310140',
        '310793',
        '314203',
        '349200',
        '349405',
        '351292',
        '351293',
        '403854',
        '403855',
        '477130',
        '485471',
        '578330',
        '636042',
        '636045',
        '639537',
        '722131',
        '722137',
        '730866',
        '730872',
        '802749',
        '848135',
        '857187',
        '858810',
        '876519',
        '876529',
        '897853',
        '898346',
        '898359',
        '898719',
        '979464',
        '979471',
        '979480',
        '999986',
        '999991',
        '999996',
        '1000001',
        '1091652',
        '1299859',
        '1299890',
        '1299896',
        '1600716',
    }


class DiabeticHypertensionWithAlbuminuria(ClinicalQualityMeasure):
    class Meta:
        title = 'Antihypertensives in Diabetics'
        description = (
            'This protocol outlines the management of '
            'hypertension in patients with diabetes. It '
            'recommends ACEI/ARB as first-line treatment '
            'for patients with diabetes and albuminuria or '
            'coronary artery disease, adjusted to the '
            'maximum tolerable dose. For other patients, '
            'ACEI/ARB, CCB, or thiazide diuretic are '
            'reasonable first options. If BP remains above '
            '130/80, the protocol advises to uptitrate and '
            'add from the remaining classes until maxed out, '
            'then consider spironolactone as a fourth option.'
        )
        version = '1.0.22'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.VITAL_SIGN,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.LAB_REPORT,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def blood_pressure_readings(
        self,
    ) -> List[BloodPressureReading]:
        bp_readings = self.patient.vital_signs.filter(sign='blood_pressure')
        if not bp_readings:
            return []
        result = []
        for reading in bp_readings:
            if len(reading['value'].split('/')) < 2:
                continue
            systolic, diastolic = reading['value'].split('/')
            recorded_time = arrow.get(reading['dateRecorded'])
            if systolic and diastolic:
                result.append(
                    BloodPressureReading(
                        float(systolic), float(diastolic), recorded_time
                    )
                )
        return result

    def latest_blood_pressure_reading(self) -> Optional[BloodPressureReading]:
        if bp_readings := self.blood_pressure_readings():
            return max(bp_readings, key=lambda x: x.recorded_time)
        else:
            return None

    def acei_arb_prescription(self) -> bool:
        return bool(
            self.patient.medications.find(AceInhibitorOrArbOrArni).filter(
                status='active'
            )
        )

    def thiazide_prescription(self) -> bool:
        return bool(
            self.patient.medications.find(
                DiureticThiazidesAndRelatedAndCombinations
            ).filter(status='active')
        )

    def ccb_prescription(self) -> bool:
        return bool(
            self.patient.medications.find(CalciumChannelBlockers).filter(
                status='active'
            )
        )

    def acei_arb_max_dose(self) -> bool:
        return bool(
            self.patient.medications.find(HighDoseACEIARB).filter(
                status='active'
            )
        )

    def last_alb_creat_ratio(self):
        alb_creat_ratios = self.patient.lab_reports.find(AlbuminCreatinineRatio)

        return (
            float(alb_creat_ratios.last_value()) if alb_creat_ratios else None
        )

    def has_albuminuria(self) -> bool:
        return bool(
            self.patient.conditions.find(Proteinuria).filter(
                clinicalStatus='active'
            )
            or (
                self.last_alb_creat_ratio()
                and self.last_alb_creat_ratio() >= 30
            )
        )

    def has_diabetes(self) -> bool:
        return bool(
            self.patient.conditions.find(Diabetes).filter(
                clinicalStatus='active'
            )
        )

    def has_hypertension(self) -> bool:
        return bool(
            self.patient.conditions.find(DiagnosisOfHypertension).filter(
                clinicalStatus='active'
            )
        )

    def recommend_antihypertensive(self, result, rx_value_set):
        result.add_recommendation(
            PrescribeRecommendation(
                key=rx_value_set.VALUE_SET_NAME,
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=rx_value_set,
                title=f'Start {rx_value_set.VALUE_SET_NAME}',
                context={
                    'sig_original_input': 'Take one daily',
                    'duration_in_days': 30,
                    'dispense_quantity': 30,
                    'dosage_form': 'tablet',
                    'count_of_refills_allowed': 3,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        return result

    def recommend_lisinopril(self, result):
        return self.recommend_antihypertensive(result, LisinoprilRx)

    def recommend_hydrochlorothiazide(self, result):
        return self.recommend_antihypertensive(result, HydrochlorothiazideRx)

    def recommend_amlodipine(self, result):
        return self.recommend_antihypertensive(result, AmlodipineRx)

    def in_denominator(self) -> bool:
        if not self.has_diabetes():
            return False
        if self.has_albuminuria() or self.has_hypertension():
            return True
        bp_readings = self.blood_pressure_readings()
        return any(
            bp_reading.systolic > 130 or bp_reading.diastolic > 80
            for bp_reading in bp_readings
        )

    def in_numerator(self) -> bool:
        if latest_bp := self.latest_blood_pressure_reading():
            return (
                latest_bp.systolic < 100 and latest_bp.diastolic < 60
                if self.has_albuminuria() and not self.acei_arb_max_dose()
                else latest_bp.systolic < 130 and latest_bp.diastolic < 80
            )
        else:
            return False

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol satisfied by blood pressure and/or '
                + 'antihypertensive medications.'
            )
        )
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):
        if self.has_albuminuria() and not self.acei_arb_prescription():
            self.recommend_lisinopril(result)
            result.add_narrative(
                'ACEi/ARB is recommended for diabetics with albuminuria.'
            )
        elif (
            self.has_albuminuria()
            and self.acei_arb_prescription()
            and not self.acei_arb_max_dose()
        ):
            result.add_narrative(
                'Uptitrate ACE/ARB to maximum tolerated dose '
                'for renal protection.'
            )
        else:
            if not self.acei_arb_prescription():
                self.recommend_lisinopril(result)
            if not self.ccb_prescription():
                self.recommend_amlodipine(result)
            if not self.thiazide_prescription():
                self.recommend_hydrochlorothiazide(result)
            result.add_narrative(
                'Increase antihypertensive regimen; target BP is 130/80.'
            )

        result.status = STATUS_DUE

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol not applicable based on diagnoses and blood pressure.'
        )
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

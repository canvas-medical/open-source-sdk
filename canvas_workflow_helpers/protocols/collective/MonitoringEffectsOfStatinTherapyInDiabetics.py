from typing import List, Optional

import arrow
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import (
    LabRecommendation,
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.lab_test import LdlCholesterol
from canvas_workflow_kit.value_set.v2021.medication import (
    HighIntensityStatinTherapy,
    LowIntensityStatinTherapy,
    ModerateIntensityStatinTherapy,
)

StatinTherapy = (
    HighIntensityStatinTherapy
    | LowIntensityStatinTherapy
    | ModerateIntensityStatinTherapy
)


class Lipids(ValueSet):
    VALUE_SET_NAME = 'Lipid panel'
    LOINC = {'13457-7'}


class DiabeticsStatinMonitoring(ClinicalQualityMeasure):
    class Meta:
        title = 'Response to statin therapy'
        description = (
            'This protocol outlines the follow-up process '
            'after initiating statin therapy. It recommends '
            'checking lipid levels 3 months after starting '
            'statin therapy. If lipid levels have not '
            'reduced by at least 30%, the protocol '
            'recommends increasing the statin dose. '
            'High-intensity statin therapy is expected to '
            'achieve a 50% or greater reduction in LDL, '
            'while moderate intensity should reduce LDL by 30-49%.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.MEDICATION,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def on_statin_therapy(self) -> bool:
        return bool(
            self.patient.medications.find(StatinTherapy).filter(status='active')
        )

    def get_medication_start_dates(
        self, medications
    ) -> Optional[List[arrow.Arrow]]:
        if not medications:
            return None
        start_dates = []
        for medication in medications:
            for period in medication['periods']:
                start_date = arrow.get(period['from'])
                start_dates.append(start_date)
        return start_dates

    def current_statins_start_dates(self) -> Optional[List[arrow.Arrow]]:
        current_statins = self.patient.medications.find(StatinTherapy).filter(
            status='active'
        )
        return self.get_medication_start_dates(current_statins)

    def all_statins_start_dates(self) -> Optional[List[arrow.Arrow]]:
        statins = self.patient.medications.find(StatinTherapy)
        return self.get_medication_start_dates(statins)

    def current_statin_is_first(self) -> bool:
        if not self.on_statin_therapy():
            return False
        return set(self.current_statins_start_dates()) == set(
            self.all_statins_start_dates()
        )

    def in_denominator(self) -> bool:
        """
        Patients whose current statin RX is for the first time and started
        at least 3 months ago.
        """
        if not self.current_statin_is_first():
            return False
        return min(self.current_statins_start_dates()) < arrow.now().shift(
            months=-3
        )

    def ldl_reduction(self) -> Optional[float]:
        statin_start_date = min(self.current_statins_start_dates())
        if not statin_start_date:
            return None
        if ldl_before_therapy := (
            self.patient.lab_reports.find(LdlCholesterol)
            .before(statin_start_date)
            .last_value()
        ):
            return (
                (
                    (float(ldl_before_therapy) - float(last_ldl_value))
                    / float(ldl_before_therapy)
                )
                if (
                    last_ldl_value := (
                        self.patient.lab_reports.find(LdlCholesterol)
                        .after(statin_start_date)
                        .last_value()
                    )
                )
                else None
            )
        else:
            return None

    def in_numerator(self) -> bool:
        # Check if patient has started statin therapy
        if not self.on_statin_therapy():
            return False
        # Check if LDL has reduced by at least 30%
        ldl_reduction = self.ldl_reduction()
        return ldl_reduction >= 0.3 if ldl_reduction else False

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol satisfied by checking lipid levels and '
                'achieving at least a 30% reduction.'
            )
        )
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):
        # If lipid panel was not repeated 3 months after starting statin therapy
        current_statins_start_date = min(self.current_statins_start_dates())
        if not self.patient.lab_reports.find(LdlCholesterol).after(
            current_statins_start_date.shift(months=3)
        ):
            # recommend a lipid panel
            result.add_recommendation(
                LabRecommendation(
                    key='RECOMMEND_LIPID_PANEL_LAB',
                    patient=self.patient,
                    lab=Lipids,
                    condition=LdlCholesterol,
                    title='Order lipid panel',
                    button='Order',
                )
            )
            result.add_narrative(
                'Check lipid panel to monitor response to statin therapy.'
            )
        # If lipid panel was repeated but LDL did not reduce by at least 30%
        elif self.ldl_reduction() and self.ldl_reduction() < 0.3:
            result.add_narrative(
                'LDL has not decreased by at least 30% since starting '
                'statin. Consider increasing dose.'
            )
        else:
            result.add_narrative(
                'LDL should decrease by at least 30% on statin therapy.'
            )
        result.status = STATUS_DUE

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol not applicable based on statin therapy status.'
        )
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

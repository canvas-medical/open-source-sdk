from typing import Optional

import arrow
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet


class Dulaglutide(ValueSet):
    VALUE_SET_NAME = 'Dulaglutide'
    RXNORM = {
        '1551295',
        '1551300',
        '1551304',
        '1551306',
        '2395777',
        '2395779',
        '2395783',
        '2395785',
    }


class Liraglutide(ValueSet):
    VALUE_SET_NAME = 'Liraglutide'
    RXNORM = {
        '1598268',
        '1860167',
        '1860172',
        '897122',
        '897126',
    }


class Semaglutide(ValueSet):
    VALUE_SET_NAME = 'Semaglutide'
    RXNORM = {
        '1991306',
        '1991311',
        '1991316',
        '1991317',
        '2200644',
        '2200650',
        '2200652',
        '2200654',
        '2200656',
        '2200658',
        '2398841',
        '2398842',
        '2553501',
        '2553506',
        '2553601',
        '2553603',
        '2553802',
        '2553803',
        '2553901',
        '2553903',
        '2554102',
        '2554104',
        '2599362',
        '2599365',
        '2619152',
        '2619154',
    }


class Canagliflozin(ValueSet):
    VALUE_SET_NAME = 'Canagliflozin'
    RXNORM = {
        '1373463',
        '1373469',
        '1373471',
        '1373473',
        '1545150',
        '1545156',
        '1545157',
        '1545159',
        '1545161',
        '1545163',
        '1545164',
        '1545166',
        '1810997',
        '1810999',
        '1811002',
        '1811003',
        '1811006',
        '1811007',
        '1811010',
        '1811011',
    }


class Tirzepatide(ValueSet):
    VALUE_SET_NAME = 'Tirzepatide'
    RXNORM = {
        '2601761',
        '1601743',
        '2601784',
        '2601767',
        '2601773',
        '2601755',
    }


GLP1Medications = Dulaglutide | Liraglutide | Semaglutide | Tirzepatide


class GLP1Uptitration(ClinicalQualityMeasure):
    class Meta:
        title = 'GLP-1 dose titration'
        description = (
            'This protocol guides the adjustment of GLP-1 dosage '
            'based on weight loss. If weight loss is less than '
            '5% per month, an increase in GLP-1 is recommended.'
            'If weight loss exceeds 5% per week, consider decreasing '
            'or stopping GLP-1. For weight loss rates in between, '
            'maintain the current dose.'
        )
        version = '1.0.0'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.VITAL_SIGN,
            CHANGE_TYPE.MEDICATION,
        ]
        references = []

    def on_glp1(self) -> bool:
        return bool(
            self.patient.medications.find(GLP1Medications).filter(
                status='active'
            )
        )

    def weight_loss_ratio_over_time(
        self, time_period: Timeframe
    ) -> Optional[float]:
        """
        Simple calculation of weight loss rate based on
        earliest / latest measurement. Replace this with a more complicated
        function if desired.
        """
        weight_measurements_oz = self.patient.vital_signs.filter(
            sign='weight'
        ).within(time_period)
        if not weight_measurements_oz or len(weight_measurements_oz) < 2:
            return None
        weight_measurements_by_time = [
            {
                'value': float(measurement['value']),
                'time': arrow.get(measurement['dateRecorded']),
            }
            for measurement in weight_measurements_oz
        ]
        earliest_weight = min(
            weight_measurements_by_time, key=lambda x: x['time']
        )
        latest_weight = max(
            weight_measurements_by_time, key=lambda x: x['time']
        )
        return (
            earliest_weight['value'] - latest_weight['value']
        ) / earliest_weight['value']

    def weight_loss_ratio_over_last_month(self):
        last_month = Timeframe(arrow.now().shift(months=-1), arrow.now())
        return self.weight_loss_ratio_over_time(last_month)

    def weight_loss_ratio_over_last_two_weeks(self):
        last_two_weeks = Timeframe(arrow.now().shift(weeks=-2), arrow.now())
        return self.weight_loss_ratio_over_time(last_two_weeks)

    def in_denominator(self) -> bool:
        """Patients on GLP-1s."""
        return self.on_glp1()

    def in_numerator(self) -> bool:
        """Patients on GLP-1s whose weight loss trend is appropriate."""
        return bool(
            (
                self.weight_loss_ratio_over_last_month()
                and self.weight_loss_ratio_over_last_month() > 0.05
                and self.weight_loss_ratio_over_last_two_weeks()
                and self.weight_loss_ratio_over_last_two_weeks() < 0.05
            )
        )

    def remainder_tasks(self, result: ProtocolResult):
        # If weight loss is less than 5% per month over
        # the past month, recommend increasing GLP-1.
        if (
            self.weight_loss_ratio_over_last_month()
            and self.weight_loss_ratio_over_last_month() < 0.05
        ):
            result.add_narrative(
                f'{self.patient.first_name} has '
                'lost less than 5% body weight over the last month. '
                'Consider increasing GLP-1 dose.'
            )
        # If weight loss is more than 5% per week over the
        # past two weeks, recommend decreasing or stopping GLP-1.
        elif (
            self.weight_loss_ratio_over_last_two_weeks()
            and self.weight_loss_ratio_over_last_two_weeks() > 0.05
        ):
            result.add_narrative(
                f'{self.patient.first_name} has '
                'lost greater than 5% body weight over the last two weeks. '
                'Consider decreasing GLP-1 dose.'
            )
        elif (
            not self.weight_loss_ratio_over_last_month()
            or not self.weight_loss_ratio_over_last_two_weeks()
        ):
            result.add_narrative(
                f'{self.patient.first_name} does not '
                'have sufficient vitals data to calculate weight loss '
                'over last two weeks and one month to determine if GLP-1 '
                'dose titration is needed.'
            )
        # If weight loss is between 5% per week and 5% per month,
        # recommend maintaining the current dose.
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'GLP-1 dose has been adjusted according to the protocol.'
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol is not applicable for patients not on GLP-1.'
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

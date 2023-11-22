from datetime import timedelta
from enum import Enum
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
from canvas_workflow_kit.recommendation import FollowUpRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Diabetes,
    EndStageRenalDisease,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class DiabetesControlLevel(Enum):
    POORLY_CONTROLLED = 1
    VERY_POORLY_CONTROLLED = 2
    WELL_CONTROLLED = 3
    UNKNOWN = 4


class GlucoseLab(ValueSet):
    """List of ICD-10-CM codes for Hypoglycemia"""

    VALUE_SET_NAME = 'Glucose labs'
    LOINC = {
        '2349-9',
        '1558-6',
    }


class ChronicKidneyDiseaseStage3Onwards(ValueSet):
    VALUE_SET_NAME = 'Chronic Kidney Disease Stage 3 Onwards'
    ICD10CM = {'N1830', 'N1831', 'N1832', 'N184', 'N185'}


class EndStageHeartFailure(ValueSet):
    VALUE_SET_NAME = 'End stage heart failure'
    ICD10CM = {'I5084'}


class MetastaticMalignancy(ValueSet):
    ICD10CM = {
        'C77.0',  #  lymph nodes of head, face and neck
        'C77.1',  #  intrathoracic lymph nodes
        'C77.2',  #  intra-abdominal lymph nodes
        'C77.3',  #  axilla and upper limb lymph nodes
        'C77.4',  #  inguinal and lower limb lymph nodes
        'C77.5',  #  intrapelvic lymph nodes
        'C77.8',  #  lymph nodes of multiple regions
        'C77.9',  #  lymph node, unspecified
        'C78.00',  #  unspecified lung
        'C78.01',  #  right lung
        'C78.02',  #  left lung
        'C78.1',  #  mediastinum
        'C78.2',  #  pleura
        'C78.30',  #  unspecified respiratory organ
        'C78.39',  #  other respiratory organs
        'C78.4',  #  small intestine
        'C78.5',  #  large intestine and rectum
        'C78.6',  #  retroperitoneum and peritoneum
        'C78.7',  #  liver and intrahepatic bile duct
        'C78.80',  #  unspecified digestive organ
        'C78.89',  #  other digestive organs
        'C79.00',  #  unspecified kidney and renal pelvis
        'C79.01',  #  right kidney and renal pelvis
        'C79.02',  #  left kidney and renal pelvis
        'C79.10',  #  unspecified urinary organs
        'C79.11',  #  bladder
        'C79.19',  #  other urinary organs
        'C79.2',  #  skin
        'C79.31',  #  brain
        'C79.32',  #  cerebral meninges
        'C79.40',  #  unspecified part of nervous system
        'C79.49',  #  other parts of nervous system
        'C79.51',  #  bone
        'C79.52',  #  bone marrow
        'C79.60',  #  unspecified ovary
        'C79.61',  #  right ovary
        'C79.62',  #  left ovary
        'C79.63',  #  bilateral ovaries
        'C79.70',  #  unspecified adrenal gland
        'C79.71',  #  right adrenal gland
        'C79.72',  #  left adrenal gland
        'C79.81',  #  breast
        'C79.82',  #  genital organs
        'C79.89',  #  other specified sites
        'C79.9',  #  unspecified site'
    }


# Add to this value set as needed
LimitedLifeExpectancy = (
    EndStageHeartFailure | MetastaticMalignancy | EndStageRenalDisease
)


class DiabeticVisitFrequency(ClinicalQualityMeasure):
    class Meta:
        title = 'Diabetes visit frequency'
        description = (
            'This protocol ensures that patients with diabetes have an'
            'upcoming appointment scheduled within the appropriate interval'
            'based on their diabetes control level. '
            'The intervals are: every 1 month for very '
            'poorly controlled diabetics, every 3 months for poorly controlled '
            'diabetics, and every 6 months for well-controlled diabetics. The '
            'protocol should be re-run any time a new lab result is received '
            'or an appointment is changed or updated.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.APPOINTMENT,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

    def has_diabetes(self) -> bool:
        return bool(
            self.patient.conditions.find(Diabetes).filter(
                clinicalStatus='active'
            )
        )

    def upcoming_appointments(self) -> List[arrow.Arrow]:
        return [
            arrow.get(appointment['startTime'])
            for appointment in self.patient.upcoming_appointments
            if arrow.get(appointment['startTime']) > arrow.now()
        ]

    def get_appointment_start_time(self, appointment):
        """
        Return the start time for an appointment, which we define
        as the time that the appointment was checked in.
        """
        return next(
            (
                arrow.get(event['created'])
                for event in appointment['stateHistory']
                if event['state'] == 'CVD'
            ),
            None,
        )

    def past_appointments(self) -> List[arrow.Arrow]:
        """
        Filter to appointments that are either checked in or locked,
        then return the start times for those appointments.
        """
        valid_appointments = [
            appointment
            for appointment in self.patient.appointments
            if appointment['state']['state'] in ('LKD', 'CVD')
        ]
        return [
            self.get_appointment_start_time(appointment)
            for appointment in valid_appointments
        ]

    def last_appointment(self) -> Optional[arrow.Arrow]:
        return (
            max(self.past_appointments())
            if len(self.past_appointments()) > 0
            else None
        )

    def time_between_appointments(self) -> Optional[timedelta]:
        last_appointment = self.last_appointment()
        if not last_appointment:
            return None
        upcoming_appointments = self.upcoming_appointments()
        if not upcoming_appointments:
            return None
        next_appointment = min(upcoming_appointments)
        return next_appointment - last_appointment

    def has_reduced_life_expectancy(self) -> bool:
        return (
            bool(
                self.patient.conditions.find(LimitedLifeExpectancy).filter(
                    clinicalStatus='active'
                )
            )
            or self.patient.age >= 80
        )

    def last_a1c_level(self) -> Optional[float]:
        last_a1c = self.patient.lab_reports.find(
            Hba1CLaboratoryTest
        ).last_value()
        return float(last_a1c) if last_a1c else None

    def hypoglycemic_episodes_in_interval(self, timeframe: Timeframe) -> int:
        """
        Counts level 2 hypoglycemic episodes (glucose readings below 55 mg/dL).
        """
        return len(
            self.patient.lab_reports.find(GlucoseLab)
            .within(timeframe)
            .filter(value__lte=55)
        )

    def diabetes_control_level(self) -> DiabetesControlLevel:
        last_a1c = self.last_a1c_level()
        # Get weekly counts of hypoglycemic incidents for last month
        weekly_hypoglycemic_incidents = []
        for i in range(4):
            interval = Timeframe(
                arrow.now().shift(weeks=-(i + 1)), arrow.now().shift(weeks=-i)
            )
            weekly_hypoglycemic_incidents.append(
                self.hypoglycemic_episodes_in_interval(interval)
            )
        # Look for the maximum number of hypoglycemic incidents last month
        max_hypoglycemic_incidents = max(weekly_hypoglycemic_incidents)

        if not last_a1c:
            return DiabetesControlLevel.UNKNOWN
        if (
            (self.has_reduced_life_expectancy() and last_a1c > 10)
            or (not self.has_reduced_life_expectancy() and last_a1c > 9)
        ) and max_hypoglycemic_incidents >= 3:
            return DiabetesControlLevel.VERY_POORLY_CONTROLLED
        if (
            (self.has_reduced_life_expectancy() and last_a1c > 8)
            or (not self.has_reduced_life_expectancy() and last_a1c > 7)
        ) and max_hypoglycemic_incidents >= 1:
            return DiabetesControlLevel.POORLY_CONTROLLED
        if (
            (self.has_reduced_life_expectancy() and last_a1c < 8)
            or (not self.has_reduced_life_expectancy() and last_a1c < 7)
        ) and max_hypoglycemic_incidents == 0:
            return DiabetesControlLevel.WELL_CONTROLLED
        return DiabetesControlLevel.UNKNOWN

    def recommended_apt_interval(self) -> Optional[timedelta]:
        """
        The time interval in which the patient should be seen.
        Adjust the final "return timedelta(days=180)" to set
        preferred frequency for DiabetesControlLevel.UNKNOWN
        """
        control_level = self.diabetes_control_level()
        if control_level == DiabetesControlLevel.VERY_POORLY_CONTROLLED:
            return timedelta(days=30)
        elif control_level == DiabetesControlLevel.POORLY_CONTROLLED:
            return timedelta(days=90)
        elif control_level == DiabetesControlLevel.WELL_CONTROLLED:
            return timedelta(days=180)
        return timedelta(days=180)

    def in_denominator(self) -> bool:
        """All patients with diabetes who have had at least one appointment."""
        return self.has_diabetes() and self.last_appointment()

    def in_numerator(self) -> bool:
        """
        Patients with an upcoming appointment scheduled within the appropriate
        interval based on their diabetes control level.
        """
        if not self.time_between_appointments():
            return False
        return (
            self.time_between_appointments() < self.recommended_apt_interval()
        )

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'The patient has an upcoming appointment scheduled within the'
                'appropriate interval based on their diabetes control level.'
            )
        )
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):
        last_appointment_date = self.last_appointment().format('MMMM D, YYYY')
        recommended_apt_interval = self.recommended_apt_interval()

        if self.upcoming_appointments():
            result.add_recommendation(
                FollowUpRecommendation(
                    key='RECOMMEND_FOLLOWUP',
                    patient=self.patient,
                    title='Schedule an appointment',
                )
            )
            result.add_narrative(
                f'{self.patient.first_name} has an upcoming appointment, '
                f'but it should be within {recommended_apt_interval.days} '
                'of the last appointment, '
                f'which was on {last_appointment_date}.'
            )
        else:
            result.add_recommendation(
                FollowUpRecommendation(
                    key='RECOMMEND_FOLLOWUP',
                    patient=self.patient,
                    title='Schedule sooner appointment',
                )
            )
            result.add_narrative(
                f'{self.patient.first_name} has no upcoming appointments. '
                'Next appointment should be within '
                f'{recommended_apt_interval.days} of the last appointment,'
                f'which was on {last_appointment_date}.'
            )
        result.status = STATUS_DUE

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative('Patient does not have a diagnosis of diabetes.')
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

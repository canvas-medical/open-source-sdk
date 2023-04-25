from typing import cast

import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    CONTEXT_REPORT,
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.constants import CHANGE_TYPE

# @canvas-adr-0006
from canvas_workflow_kit.value_set.specials import CMS125v6Tomography

# flake8: noqa
from canvas_workflow_kit.value_set.v2018 import (
    AnnualWellnessVisit,
    BilateralMastectomy,
    HomeHealthcareServices,
    Mammography,
    OfficeVisit,
    PreventiveCareServicesEstablishedOfficeVisit18AndUp,
    PreventiveCareServicesInitialOfficeVisit18AndUp,
    StatusPostLeftMastectomy,
    StatusPostRightMastectomy,
    UnilateralMastectomy,
)
from canvas_workflow_kit.value_set.value_set import ValueSet


class MammographyImaging(ValueSet):
    VALUE_SET_NAME = "Mammography Imaging"
    CPT = {"77067"}


EncounterForMammographCondition = {
    "code": "Z1231",
    "system": "ICD-10",
    "display": "Encounter for screening mammogram for malignant neoplasm of breast",
}


class BreastCancerScreening(ClinicalQualityMeasure):
    """
    Breast Cancer Screening

    Description: Percentage of women 50-74 years of age who had a mammogram to screen for breast
    cancer

    Definition: None

    Rationale: Breast cancer is one of the most common types of cancers, accounting for a quarter
    of all new cancer diagnoses for women in the U.S. (BreastCancer.Org, 2011). It ranks as the
    second leading cause of cancer-related mortality in women, accounting for nearly 40,000
    estimated deaths in 2013 (American Cancer Society, 2011).

    According to the National Cancer Institute's Surveillance Epidemiology and End Results program,
    the chance of a woman being diagnosed with breast cancer in a given year increases with age. By
    age 30, it is one in 2,212. By age 40, the chances increase to one in 235, by age 50, it
    becomes one in 54, and, by age 60, it is one in 25. From 2004 to 2008, the median age at the
    time of breast cancer diagnosis was 61 years among adult women (Tangka et al, 2010).

    In the U.S., costs associated with a diagnosis of breast cancer range from $451 to $2,520,
    factoring in continued testing, multiple office visits, and varying procedures. The total costs
    related to breast cancer add up to nearly $7 billion per year in the U.S., including $2 billion
    spent on late-stage treatment (Lavigne et al, 2008; Boykoff et al, 2009).

    Guidance: Patient self-report for procedures as well as diagnostic studies should be recorded
    in 'Procedure, Performed' template or 'Diagnostic Study, Performed' template in QRDA-1. Patient
    self-report is not allowed for laboratory tests.

    This measure evaluates primary screening. Do not count biopsies, breast ultrasounds, MRIs or
    tomosynthesis (3D mammography), because they are not appropriate methods for primary breast
    cancer screening.

    More information: https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS125v6.html
    """

    class Meta:
        title = "Breast Cancer Screening"
        version = "2023v1"

        # 27 months, but we want to ensure it is displayed as 2 years, 3 months
        # 27 * 30 is 2 years, 2 months, and some amount of days
        default_display_interval_in_days = (365 * 2) + (3 * 30)

        description = (
            "Women 50-74 years of age who have not had a mammogram to screen for "
            "breast cancer within the last 27 months."
        )
        information = (
            "https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS125v6.html"
        )

        identifiers = ["BreastCancerScreening"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            "National Committee for Quality Assurance",
        ]

        references = [
            "American Cancer Society. 2010. Cancer Facts & Figures 2010. Atlanta: American Cancer Society.",
            'National Cancer Institute. 2010. "Breast Cancer Screening." http://www.cancer.gov/cancertopics/pdq/screening/breast/healthprofessional',
            "National Business Group on Health. 2011. Pathways to Managing Cancer in the Workplace. Washington: National Business Group on Health.",
            'U.S. Preventive Services Task Force (USPSTF). 2009. 1) "Screening for breast cancer: U.S. Preventive Services Task Force recommendation statement." 2) "December 2009 addendum." Ann Intern Med 151(10):716-726.',
            "BreastCancer.org. 2012. U.S. Breast Cancer Statistics. www.breastcancer.org/symptoms/understand_bc/statistics.jsp",
        ]

        compute_on_change_types = [
            CHANGE_TYPE.PROTOCOL_OVERRIDE,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.IMAGING_REPORT,
            CHANGE_TYPE.PATIENT,
        ]

    _on_date = None
    AGE_RANGE_START = 51
    AGE_RANGE_END = 74
    EXTRA_SCREENING_MONTHS = 15

    def had_mastectomy(self) -> bool:
        if self.patient.conditions.find(BilateralMastectomy).starts_before(
            self.timeframe.end
        ):
            return True

        unilateral_mastectomy = self.patient.conditions.find(
            UnilateralMastectomy
        ).starts_before(self.timeframe.end)
        if 2 == len(unilateral_mastectomy):
            return True

        if unilateral_mastectomy and self.patient.conditions.find(
            StatusPostRightMastectomy
        ).starts_before(self.timeframe.end):
            return True

        if unilateral_mastectomy and self.patient.conditions.find(
            StatusPostLeftMastectomy
        ).starts_before(self.timeframe.end):
            return True

        return False

    def first_due_in(self) -> int | None:
        if (
            self.patient.is_female
            and self.patient.age_at(self.timeframe.end) < self.AGE_RANGE_START
            and not self.had_mastectomy()
        ):
            return cast(
                int,
                (
                    self.patient.birthday.shift(years=self.AGE_RANGE_START)
                    - self.timeframe.end
                ).days,
            )
        return None

    def in_initial_population(self) -> bool:
        """
        Initial population: Women 51-74 years of age with a visit during the measurement period
        """
        return cast(
            bool,
            self.patient.age_at_between(
                self.timeframe.end, self.AGE_RANGE_START, self.AGE_RANGE_END
            )
            and self.patient.is_female
            and (
                self.patient.has_visit_within(
                    self.timeframe,
                    (
                        OfficeVisit
                        | PreventiveCareServicesInitialOfficeVisit18AndUp
                        | PreventiveCareServicesEstablishedOfficeVisit18AndUp
                        | HomeHealthcareServices
                        | AnnualWellnessVisit
                    ),
                )
                if self.context == CONTEXT_REPORT
                else True
            ),
        )

    def in_denominator(self) -> bool:
        """
        Denominator: Equals Initial Population

        Exclusions: Women who had a bilateral mastectomy or who have a history of a bilateral
        mastectomy or for whom there is evidence of a right and a left unilateral mastectomy.

        Exclude patients who were in hospice care during the measurement year.

        Exceptions: None
        """
        if not self.in_initial_population():
            return False

        if self.patient.hospice_within(self.timeframe):
            return False

        if self.had_mastectomy():
            return False

        return True

    def in_numerator(self) -> bool:
        """
        Numerator: Women with one or more mammograms during the measurement period or the 15 months
        prior to the measurement period

        Exclusions: Not Applicable
        """
        if self.period_adjustment:
            period = self.timeframe
        else:
            period = self.timeframe.increased_by(
                months=-1 * self.EXTRA_SCREENING_MONTHS
            )
        record = (
            self.patient.imaging_reports.find(Mammography | CMS125v6Tomography)
            .within(period)
            .last()
        )
        if record:
            self._on_date = arrow.get(record["originalDate"])
            return True

        return False

    def compute_results(self) -> ProtocolResult:
        """
        Clinical recommendation: The U.S. Preventive Services Task Force (USPSTF) recommends
        biennial screening mammography for women aged 50-74 years (B recommendation). The decision
        to start regular, biennial screening mammography before the age of 50 years should be an
        individual one and take patient context into account, including the patient's values
        regarding specific benefits and harms (C recommendation). The Task Force concludes the
        evidence is insufficient to assess the additional benefits and harms of screening
        mammography in women 75 years and older (I statement).

        U.S. Preventive Services Task Force (2009)
        Grade: B recommendation. The USPSTF recommends biennial screening mammography for women
        aged 50 to 74 years.
        Grade: C recommendation. The decision to start regular, biennial screening mammography
        before the age of 50 years should be an individual one and take patient context into
        account, including the patient's values regarding specific benefits and harms.
        Grade: I Statement. The USPSTF concludes that the current evidence is insufficient to
        assess the additional benefits and harms of screening mammography in women 75 years or
        older.
        Grade: D recommendation. The USPSTF recommends against teaching breast self-examination
        (BSE).
        Grade: I Statement. The USPSTF concludes that the current evidence is insufficient to
        assess the additional benefits and harms of clinical breast examination (CBE) beyond
        screening mammography in women 40 years or older.
        Grade: I Statement. The USPSTF concludes that the current evidence is insufficient to
        assess the additional benefits and harms of either digital mammography or magnetic
        resonance imaging (MRI) instead of film mammography as screening modalities for breast
        cancer.
        """
        result = ProtocolResult()

        if self.in_denominator():
            first_name = self.patient.first_name
            extra_months = 0 if self.period_adjustment else self.EXTRA_SCREENING_MONTHS
            if self.in_numerator() and self._on_date:
                result.due_in = (
                    self._on_date.shift(
                        days=self.timeframe.duration, months=extra_months
                    )
                    - self.now
                ).days
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f"{first_name} had a mammography {self.display_date(self._on_date)}."
                )
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative("No relevant exams found.")
                result.add_narrative(self.screening_interval_context())
                result.add_instruction_recommendation(
                    key="PLAN_RECOMMENDATION",
                    rank=1,
                    button="Plan",
                    patient=self.patient,
                    instruction=Mammography,
                    title="Discuss breast cancer screening",
                )
                result.add_imaging_recommendation(
                    key="IMAGING_RECOMMENDATION",
                    rank=2,
                    button="Order",
                    patient=self.patient,
                    imaging=MammographyImaging,
                    title="Order Mammography, screening; bilateral",
                    context={"conditions": [[EncounterForMammographCondition]]},
                )
        else:
            result.due_in = self.first_due_in()

        return result

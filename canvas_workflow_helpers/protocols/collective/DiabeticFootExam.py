from typing import Any, Iterable, Optional

import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult
)
from canvas_workflow_kit.recommendation import InterviewRecommendation
# flake8: noqa
from canvas_workflow_kit.value_set.v2018 import (
    BilateralAmputationOfLegBelowOrAboveKnee,
    LeftUnilateralAmputationAboveOrBelowKnee,
    PulseExamOfFoot,
    RightUnilateralAmputationAboveOrBelowKnee,
    SensoryExamOfFoot,
    UnilateralAmputationBelowOrAboveKneeUnspecifiedLaterality,
    VisualExamOfFoot
)
from .diabetes_quality_measure import DiabetesQualityMeasure


class ClinicalQualityMeasure123v6(DiabetesQualityMeasure):
    """
    Diabetes: Foot Exam

    Description: The percentage of patients 18-75 years of age with diabetes (type 1 and type 2)
    who received a foot exam (visual inspection and sensory exam with mono filament and a pulse
    exam) during the measurement year

    Definition: Foot exam: visual inspection with a sensory exam and a pulse exam.

    Rationale: As the seventh leading cause of death in the U.S., diabetes kills approximately
    75,000 people a year (CDC FastStats 2015). Diabetes is a group of diseases marked by high blood
    glucose levels, resulting from the body's inability to produce or use insulin (CDC Statistics
    2014, ADA Basics 2013). People with diabetes are at increased risk of serious health
    complications including vision loss, heart disease, stroke, kidney failure, amputation of toes,
    feet or legs, and premature death. (CDC Fact Sheet 2014).

    In 2012, diabetes cost the U.S. an estimated $245 billion: $176 billion in direct medical costs
    and $69 billion in reduced productivity. This is a 41 percent increase from the estimated $174
    billion spent on diabetes in 2007 (ADA Economic 2013).

    Complications due to improper or poor quality of foot care in diabetics can include amputations
    of the toe, foot, lower and upper leg. Between 1993 and 2009, the CDC monitored the rates of
    nontraumatic amputations in the diabetic population. Overall, the rates peaked in 1996 with toe
    amputations at 3.7 per 1,000 diabetic population. Amputations for the foot, lower leg, and
    upper leg were 1.5, 2.3, and 1.1 per 1,000 diabetic population, respectively, in 1996. Since
    the late nineties, lower extremity amputation rates in the diabetic population have declined,
    witnessed by the following rates in 2009: for toe amputations (1.8 per 1,000 diabetic
    population), followed by lower leg (0.9), foot (0.5) and upper leg (0.4) amputations (CDC,
    2012).

    Guidance: Only patients with a diagnosis of Type 1 or Type 2 diabetes should be included in the
    denominator of this measure; patients with a diagnosis of secondary diabetes due to another
    condition should not be included.

    More information: https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS123v6.html
    """

    class Meta:
        title = 'Diabetes: Foot Exam'

        version = '2019-02-12v1'

        description = (
            'Patients 18-75 years of age with diabetes who have not received a foot exam in the last year.'  # noqa: E501
        )
        information = 'https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS123v6.html'

        identifiers = ['CMS123v6']

        types = ['CQM']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            'National Committee for Quality Assurance',
        ]

        compute_on_change_types = [
            ClinicalQualityMeasure.CHANGE_PROTOCOL_OVERRIDE,
            ClinicalQualityMeasure.CHANGE_CONDITION,
            ClinicalQualityMeasure.CHANGE_INTERVIEW,
            ClinicalQualityMeasure.CHANGE_PATIENT,
        ]

        references = [
            'American Diabetes Association. Microvascular complications and foot care. Sec. 10. In Standards of Medical Care in Diabetes-2017. Diabetes Care 2017;40(Suppl. 1):S88-S98',  # noqa: E501
            'American Diabetes Association (ADA). 2013. Diabetes Statistics. Retrieved from http://www.diabetes.org/diabetes-basics/diabetes-statistics/.',  # noqa: E501
            'Centers for Disease Control and Prevention (CDC). 2012. CDC\'s Diabetes Program-Data and Trends-Diabetes Surveillance System-Nontraumatic Lower Extremity Amputation with Diabetes by Level of Amputation. Retrieved from http://www.cdc.gov/diabetes/statistics/lealevel/fig8.htm.',  # noqa: E501
            'Centers for Disease Control and Prevention (CDC). 2014. National Diabetes Statistics Report. http://www.cdc.gov/diabetes/pdfs/data/2014-report-estimates-of-diabetes-and-its-burden-in-the-united-states.pdf',  # noqa: E501
            'Centers for Disease Control and Prevention (CDC). 2015. FastStats: Deaths and Mortality. www.cdc.gov/nchs/fastats/deaths.htm.',  # noqa: E501
            'Centers for Disease Control and Prevention. 2014. CDC Features. Diabetes Latest. www.cdc.gov/features/diabetesfactsheet/.',  # noqa: E501
            'American Diabetes Association. 2013. Diabetes Basics. www.diabetes.org/diabetes-basics/?loc=GlobalNavDB',  # noqa: E501
            'American Diabetes Association (ADA). April 2013. Economic Costs of Diabetes in the U.S. in 2012. Diabetes Care. Vol. 36 no. 4 1033-46. http://care.diabetesjournals.org/content/36/4/1033.full',  # noqa: E501
        ]

    @classmethod
    def enabled(cls) -> bool:
        return True

    _on_dates = None

    @property
    def period(self) -> Any:
        if not self._on_dates:
            return 'N/A'
        from_date = min(self._on_dates)
        to_date = max(self._on_dates)
        if from_date == to_date:
            return self.display_date(from_date)
        else:
            return self.display_period(from_date, to_date)

    def in_denominator(self) -> bool:
        """
        Denominator: Equals Initial Population

        Exclusions: Patients who have had either a bilateral amputation above or below the knee, or
        both a left and right amputation above or below the knee before or during the measurement
        period.

        Exclude patients who were in hospice care during the measurement year.

        Exceptions: None
        """
        if not self.in_initial_population():
            return False

        if self.patient.hospice_within(self.timeframe):
            return False

        # bilateral is an exclusion
        conditions = self.patient.conditions.starts_before(self.timeframe.end)

        if conditions.find(BilateralAmputationOfLegBelowOrAboveKnee):
            return False

        # as is two unilateral amputations
        amputations = conditions.find(LeftUnilateralAmputationAboveOrBelowKnee |
                                      RightUnilateralAmputationAboveOrBelowKnee |
                                      UnilateralAmputationBelowOrAboveKneeUnspecifiedLaterality)

        if len(amputations) >= 2:
            return False

        return True

    def in_numerator(self) -> bool:
        """
        Numerator: Patients who received visual, pulse and sensory foot examinations during the
        measurement period

        Exclusions: Not Applicable
        """
        performed = {
            VisualExamOfFoot.OID: False,
            PulseExamOfFoot.OID: False,
            SensoryExamOfFoot.OID: False,
        }
        self._on_dates = []

        interviews = self.patient.interviews.validated().within(self.timeframe)
        for exam_class in [VisualExamOfFoot, PulseExamOfFoot, SensoryExamOfFoot]:
            exams = interviews.find(exam_class)
            if exams and exam_class.OID in performed:
                on_date = max([record['noteTimestamp'] for record in exams])
                self._on_dates.append(arrow.get(on_date))
                performed[exam_class.OID] = True

        return all(performed.values())

    def compute_results(self) -> ProtocolResult:
        """
        Clinical recommendation: American Diabetes Association (2017) Guidelines/ Recommendations:
        Perform annual comprehensive foot examination to identify risk factors predictive of ulcers
        and amputations. The foot examination should include inspection, assessment of foot/leg
        pulses, and testing for loss of protective sensation (10-g monofilament plus testing any
        one of: vibration using 128-Hz tuning fork, pinprick sensation, temperature, ankle
        reflexes, or vibration perception threshold). (Level of evidence: B)
        """
        result = ProtocolResult()

        if self.in_denominator():
            first_name = self.patient.first_name
            if self.in_numerator():
                result.due_in = (
                    min(self._on_dates).shift(days=self.timeframe.duration) - self.now).days
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{first_name} has diabetes and his comprehensive foot exam was done {self.period}.'  # noqa: E501
                )
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(f'{first_name} has diabetes and is due for foot exam.')
                title = (
                    'Conduct comprehensive foot examination '
                    'including assessment of protective sensation, pulses and visual inspection.')

                # we need to make one interview that satisfies all three of these SNOMED codes
                result.add_interview_recommendation(
                    key='CMS123v6_RECOMMEND_FOOT_EXAM',
                    rank=1,
                    button='Plan',
                    patient=self.patient,
                    questionnaires=[VisualExamOfFoot, PulseExamOfFoot, SensoryExamOfFoot],
                    title=title)
        else:
            result.due_in = self.first_due_in()

        return result

from typing import List, Type

import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ExternallyAwareClinicalQualityMeasure,
    ProtocolResult
)
from canvas_workflow_kit.recommendation import (
    PerformRecommendation,
    ReferRecommendation,
    TaskRecommendation
)
from canvas_workflow_kit.timeframe import Timeframe
# flake8: noqa
from canvas_workflow_kit.value_set.v2018 import (
    Diabetes,
    OphthalmologicalServices,
    RetinalOrDilatedEyeExam
)
from canvas_workflow_kit.value_set.value_set import ValueSet
from .diabetes_quality_measure import DiabetesQualityMeasure


class FundusPhotography(ValueSet):

    CPT = {'92250'}


class ClinicalQualityMeasure131v6(ExternallyAwareClinicalQualityMeasure, DiabetesQualityMeasure):
    """
    Diabetes: Eye Exam

    Description: Percentage of patients 18-75 years of age with diabetes who had a retinal or
    dilated eye exam by an eye care professional during the measurement period or a negative
    retinal exam (no evidence of retinopathy) in the 12 months prior to the measurement period

    Definition: None

    Rationale: As the seventh leading cause of death in the U.S., diabetes kills approximately
    75,000 people a year (CDC FastStats 2015). Diabetes is a group of diseases marked by high blood
    glucose levels, resulting from the body's inability to produce or use insulin (CDC Statistics
    2014, ADA Basics 2013). People with diabetes are at increased risk of serious health
    complications including vision loss, heart disease, stroke, kidney failure, amputation of toes,
    feet or legs, and premature death. (CDC Fact Sheet 2014).

    In 2012, diabetes cost the U.S. an estimated $245 billion: $176 billion in direct medical costs
    and $69 billion in reduced productivity. This is a 41 percent increase from the estimated $174
    billion spent on diabetes in 2007 (ADA Economic 2013).

    In 2005-2008, of adults with diabetes aged 40 years or older, 4.2 million (28.5%) people had
    diabetic retinopathy, damage to the small blood vessels in the retina that may result in loss
    of vision. (CDC Statistics, 2014).

    Guidance: Only patients with a diagnosis of Type 1 or Type 2 diabetes should be included in the
    denominator of this measure; patients with a diagnosis of secondary diabetes due to another
    condition should not be included.

    The eye exam must be performed by an ophthalmologist or optometrist.

    More information: https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS131v6.html
    """

    class Meta:

        title = 'Diabetes: Eye Exam'

        version = '2019-08-02v1'

        description = ('Patients 18-75 years of age with diabetes who have not had a retinal or '
                       'dilated eye exam by an eye care professional.')
        information = 'https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS131v6.html'

        identifiers = ['CMS131v6']

        types = ['CQM']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            'National Committee for Quality Assurance',
        ]

        references = [
            'American Diabetes Association. Microvascular complications and foot care. Sec. 10. In Standards of Medical Care in Diabetes 2017. Diabetes Care 2017;40(Suppl. 1):S88-S98',
            'American Diabetes Association. 2009. "Standards of Medical Care in Diabetes-2009." Diabetes Care 2009 32 (Suppl 1):S6-S12. doi:10.2337/dc09-S006.',
            'American Diabetes Association. 2013. Diabetes Basics. www.diabetes.org/diabetes-basics/?loc=GlobalNavDB',
            'American Diabetes Association (ADA). April 2013. Economic Costs of Diabetes in the U.S. in 2012. Diabetes Care. Vol. 36 no. 4 1033-46. http://care.diabetesjournals.org/content/36/4/1033.full',
            'Centers for Disease Control and Prevention (CDC). 2014. National Diabetes Statistics Report. http://www.cdc.gov/diabetes/pdfs/data/2014-report-estimates-of-diabetes-and-its-burden-in-the-united-states.pdf',
            'Centers for Disease Control and Prevention (CDC). 2015. FastStats: Deaths and Mortality. www.cdc.gov/nchs/fastats/deaths.htm.',
            'Centers for Disease Control and Prevention. 2014. CDC Features. Diabetes Latest. www.cdc.gov/features/diabetesfactsheet/.', ]

        compute_on_change_types = [
            ClinicalQualityMeasure.CHANGE_PROTOCOL_OVERRIDE,
            ClinicalQualityMeasure.CHANGE_CONDITION,
            ClinicalQualityMeasure.CHANGE_PATIENT,
            ClinicalQualityMeasure.CHANGE_REFERRAL_REPORT,
        ]

    @classmethod
    def enabled(cls) -> bool:
        return True

    _on_date = None
    _in_period = None
    _finding = None

    @property
    def specific_visits(self) -> Type[ValueSet]:
        return super().specific_visits | OphthalmologicalServices

    def in_denominator(self) -> bool:
        """
        Denominator: Equals Initial Population

        Exclusions: Exclude patients who were in hospice care during the measurement year

        Exceptions: None
        """
        if not self.in_initial_population():
            return False

        if self.patient.hospice_within(self.timeframe):
            return False

        return True

    def in_numerator(self) -> bool:
        """
        Numerator: Patients with an eye screening for diabetic retinal disease. This includes
        diabetics who had one of the following:
        A retinal or dilated eye exam by an eye care professional in the measurement period or a
        negative retinal exam (no evidence of retinopathy) by an eye care professional in the year
        prior to the measurement period

        Exclusions: Not Applicable
        """
        records = (self.patient.referral_reports
                   .find(RetinalOrDilatedEyeExam)
                   .within(self.timeframe))  # yapf: disable

        if records:
            self._in_period = True
        else:
            self._in_period = False

            prior_period = Timeframe(
                start=self.timeframe.start.shift(days=-1 * self.timeframe.duration),
                end=self.timeframe.start)

            records = (self.patient.referral_reports
                       .find(RetinalOrDilatedEyeExam)
                       .within(prior_period))  # yapf: disable

        if records:
            last = records[-1]
            negative_finding = False
            self._finding = ''

            for coding in last['codings']:
                if coding['display'] == 'Findings':
                    self._finding = coding['value']

                if coding['code'] == '721103006':
                    negative_finding = True

            self._on_date = arrow.get(last['originalDate'])

            if self._in_period or negative_finding:
                return True

        return False

    # protocol satisfied
    def craft_satisfied_result(self):
        result = ProtocolResult()
        result.status = STATUS_SATISFIED
        exam_date = self.display_date(self._on_date)

        if self._in_period:
            result.due_in = (self._on_date.shift(days=self.timeframe.duration) - self.now).days
            result.add_narrative(
                f'{self.patient.first_name} has diabetes and a retinal examination was done '
                f'{exam_date}, demonstrating {self._finding}.')
        else:
            result.due_in = (self._on_date.shift(days=self.timeframe.duration) - self.now).days
            next_date = self._on_date.shift(days=self.timeframe.duration).format('M/D/YY')
            result.add_narrative(
                f'{self.patient.first_name} has diabetes and a retinal examination was done '
                f'{exam_date} demonstrating no diabetic eye disease. '
                f'Next examination is due {next_date}.')

        return result

    def craft_unsatisfied_result(self):
        result = ProtocolResult()
        result.due_in = -1
        result.status = STATUS_DUE
        if self._on_date:
            exam_date = self.display_date(self._on_date)
            result.add_narrative(
                f'{self.patient.first_name} has diabetes and a prior abnormal retinal examination '
                f'{exam_date} showing {self._finding}. {self.patient.first_name} is due for '
                'retinal examination.')
        else:
            humanized_timeframe = ((self.now
                                    .shift(months=-1,
                                           days=-self.timeframe.duration)
                                    .humanize(other=self.now,
                                              granularity='month',
                                              only_distance=True))
                                   .replace(' ago', ''))  # yapf: disable
            result.add_narrative(
                f'{self.patient.first_name} has diabetes and no documentation of retinal '
                f'examination in the past {humanized_timeframe}.')

        result.add_recommendation(
            PerformRecommendation(
                key='CMS131v6_RECOMMEND_PERFORM_EYE_EXAM',
                rank=1,
                button='Perform',
                patient=self.patient,
                procedure=FundusPhotography,
                condition=Diabetes,
                title='Perform retinal examination'))

        context_conditions = (self.patient.conditions.find(Diabetes).intersects(
            self.timeframe, still_active=self.patient.active_only))

        codings = [condition['coding'] for condition in context_conditions.records]

        result.add_recommendation(
            ReferRecommendation(
                key='CMS131v6_RECOMMEND_REFER_EYE_EXAM',
                rank=2,
                button='Refer',
                patient=self.patient,
                referral=RetinalOrDilatedEyeExam,
                condition=Diabetes,
                context={
                    'conditions': codings,
                    'specialties': [
                        'Ophthalmology',
                        'Ophthalmology ',  # TODO/BUG: science contacts contains an entry like this
                        'Optometrist',
                        'Optometry',
                    ],
                },
                title='Refer for retinal examination'))

        return result

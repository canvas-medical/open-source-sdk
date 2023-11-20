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
from canvas_workflow_kit.recommendation import InterviewRecommendation
from canvas_workflow_kit.value_set import ValueSet


class GLP1SideEffectsQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'GLP-1 Side Effects Questionnaire'
    INTERNAL = {'i5'}


class GLP1Drugs(ValueSet):
    VALUE_SET_NAME = 'GLP-1 Drugs'
    RXNORM = {
        '2601734',
        '1649570',
        '1151126',
        '2601723',
        '2601746',
        '2601758',
        '2601764',
        '2601770',
        '2601776',
        '2601785',
        '2601745',
        '2601757',
        '2601763',
        '2601769',
        '2601775',
        '2601781',
        '2601737',
        '2601736',
        '2601743',
        '2601755',
        '2601761',
        '2601767',
        '2601773',
        '2601784',
        '2601742',
        '2601754',
        '2601760',
        '2601766',
        '2601772',
        '2601778',
        '2601731',
        '2601730',
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
        '1598268',
        '1860167',
        '1860172',
        '897122',
        '897126',
        '1551295',
        '1551300',
        '1551304',
        '1551306',
        '2395777',
        '2395779',
        '2395783',
        '2395785',
        '1242963',
        '1242968',
        '1544916',
        '1544918',
        '1990866',
        '1990869',
        '847910',
        '847913',
        '847915',
        '847917',
    }


class TreatmentSideEffects(ClinicalQualityMeasure):
    class Meta:
        title = 'GLP-1 side effects screening'
        description = (
            'This protocol recommends a questionnaire to screen '
            'for side effects, mainly nausea, vomiting, diarrhea, '
            'and abdominal bloating, when GLP-1 has been started '
            'or the dose has been changed.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.PATIENT,
        ]
        references = []

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

    def taken_questionnaire(self) -> bool:
        return self.patient.interviews.find(
            GLP1SideEffectsQuestionnaire
        ).filter(status='AC')

    def in_denominator(self) -> bool:
        """Patients who started GLP-1 at least 1 week ago."""
        glp_1_prescriptions = self.patient.medications.find(GLP1Drugs)
        if not self.get_medication_start_dates(glp_1_prescriptions):
            return False
        glp1meds = self.patient.medications.find(GLP1Drugs)
        start_dates = self.get_medication_start_dates(glp1meds)
        one_week_ago = arrow.now().shift(weeks=-1)
        return any((x < one_week_ago for x in start_dates))

    def in_numerator(self) -> bool:
        """Patients who have taken the questionnaire."""
        return self.taken_questionnaire()

    def remainder_tasks(self, result: ProtocolResult):
        result.add_recommendation(
            InterviewRecommendation(
                key='RECOMMEND_GLP1_SIDE_EFFECTS_QUESTIONNAIRE',
                patient=self.patient,
                questionnaires=[GLP1SideEffectsQuestionnaire],
                title='Screen for side effects of GLP-1',
                button='Interview',
            )
        )
        result.add_narrative(
            (
                f'{self.patient.first_name} has '
                'not been screened for side effects since starting GLP-1.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient has completed the questionnaire to screen for '
                'side effects of GLP-1.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol is not applicable as patient is not on a GLP-1.'
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

import arrow
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import ReferRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class PhysicalandOccupationalTherapy(ValueSet):
    VALUE_SET_NAME = "Physical & Occupational Therapy (TBD)"


EncounterForLowBackPain = {
    "code": "M5450",
    "system": "ICD-10",
    "display": "Low back pain, unspecified",
}

class QuestionnaireIntakeChecklist(ValueSet):
    VALUE_SET_NAME = "Intake Checklist"
    INTERNAL = {"999-999"}


class ReferPhysicalTherapyAssessment(ClinicalQualityMeasure):

    class Meta:

        title = 'Refer to Physical Therapy'
        version = '2023-08-28'
        description = ('A protocol that recommends referral to physical therapy'
                       'based on questionnaire responses.')
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.REFERRAL_REPORT]
        authors = ['Canvas Medical']
        references = ['Canvas Medical']
        notification_only = True

    interview_date = None

    def in_denominator(self):
        """
        Patients whose most recent Intake checklist questionnaire
        has answered No to "Has patient provided applicable imaging?"
        """
        interviews = self.patient.interviews.find(QuestionnaireIntakeChecklist).filter(status='AC')

        # if none, return False
        if len(interviews) == 0:
            return False

        # get the most recently completed questionnaire by 'noteTimestamp'
        most_recent = max(interviews, key=lambda x: x['noteTimestamp'])
        self.interview_date = arrow.get(most_recent['noteTimestamp']).date()

        # check the answer to question 3 is no using the code 999-1009
        return any([i['code'] == '999-1009' for i in most_recent['responses']])

    def in_numerator(self):
        """
        Patients that have already had a Referral Report come back after the interview time
        """
        return any([arrow.get(r['originalDate']).date() >= self.interview_date
            for r in self.patient.referral_reports.filter(specialty="Physical & Occupational Therapy")])

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(
                    f'Patient has not completed conservative therapy '
                    'and should be referred per UM guidelines.'
                )

                refer_recommendation = ReferRecommendation(
                    key='RECOMMEND_REFER_PHYSICAL_THERAPY',
                    rank=1,
                    button='Refer',
                    patient=self.patient,
                    referral=PhysicalandOccupationalTherapy,
                    condition=EncounterForLowBackPain,
                    title='Refer for Physical & Occupational Therapy',
                    context={
                    'specialties': ['Physical & Occupational Therapy'],
                    'conditions': [[EncounterForLowBackPain]]}
                )
                result.add_recommendation(refer_recommendation)

        return result

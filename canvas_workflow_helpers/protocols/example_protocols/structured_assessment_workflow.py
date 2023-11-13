from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
    STATUS_NOT_APPLICABLE,
    STATUS_NOT_RELEVANT
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import StructuredAssessmentRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet
import arrow


class ConditionsSA(ValueSet):
    VALUE_SET_NAME = "Conditions"
    INTERNAL = {"INT-1000"}

class KneeSurgery(ValueSet):
    VALUE_SET_NAME = 'Knee Surgery'
    INTERNAL = {'surg_knee001'}

class HipSurgery(ValueSet):
    VALUE_SET_NAME = 'Hip Surgery'
    INTERNAL = {'surg_hip001'}

class BackSurgery(ValueSet):
    VALUE_SET_NAME = 'Back / Neck Surgery'
    INTERNAL = {'surg_back001'}

CODE_SA_MAPPING = {
    'M25561': KneeSurgery,
    'M25562': KneeSurgery,
    'M1711': KneeSurgery,
    'M1712': KneeSurgery,
    'M25551': HipSurgery,
    'M25552': HipSurgery,
    'M1611': HipSurgery,
    'M1612': HipSurgery,
    'M5450': BackSurgery,
    'M542': BackSurgery,
}


class AdditionalSurgicalProcedureDocumentation(ClinicalQualityMeasure):
    class Meta:
        title = "Additional Surgical Procedure Documentation"
        version = "2023-v01"
        description = "When the user selects one of the ICD-10 codes in the conditions structured assessment under the Indications for Surgery, a more specific structured assessment is recommended"
        identifiers = []
        types = ["SA Rec"]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW]
        notification_only = True

    def compute_results(self):
        result = ProtocolResult()

        # find the conditions structured assessment
        interview = self.patient.interviews.find(ConditionsSA).filter(status='AC').last()
        
        if not interview:
            result.status = STATUS_NOT_RELEVANT
            result.add_narrative("Conditions SA not filled out for patient")
            return result

        interview_date = interview['noteTimestamp']
        response_icd_codes = {c['code'] for c in interview['responses']} # icd codes selected in SA
        sa_icd_codes_found = {c for c in response_icd_codes if c in CODE_SA_MAPPING}
        sa_recs = {CODE_SA_MAPPING[code] for code in sa_icd_codes_found}
        rec_needed = False

        if not len(sa_recs):
            result.status = STATUS_NOT_APPLICABLE
            result.add_narrative(
                f"Conditions SA does not contain icd codes that match recommendation list: {', '.join(response_icd_codes)}")
            return result

        for i, rec in enumerate(sa_recs):

            # see if SA is already filled out after the Conditions SA
            sa_found = self.patient.interviews.find(rec).filter(status='AC').after(arrow.get(interview_date)).last()
            if sa_found:
                continue

            rec_needed = True
            structured_assessment_recommendation = StructuredAssessmentRecommendation(
                key=f'RECOMMEND_{rec.VALUE_SET_NAME}_STRUCTURED_ASSESSMENT',
                rank=i+1,
                button='Assess',
                patient=self.patient,
                questionnaires=[rec],
                title=f'Assess {rec.VALUE_SET_NAME}'
            )
            result.add_recommendation(structured_assessment_recommendation)

        if rec_needed:
            result.status = STATUS_DUE
            result.add_narrative(
                f"{self.patient.first_name} has a surgical indication of {', '.join(sa_icd_codes_found)}, "
                "please complete further documentation related to the specific surgical procedure."
            )
        else:
            result.status = STATUS_SATISFIED
            result.add_narrative(
                f"Surgical Procedure SA {', '.join([r.VALUE_SET_NAME for r in sa_recs])} have already been committed "
                f"for {', '.join(sa_icd_codes_found)}")

        return result

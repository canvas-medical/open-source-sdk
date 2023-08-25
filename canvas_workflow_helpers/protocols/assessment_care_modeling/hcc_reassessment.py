import arrow

from cached_property import cached_property
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set.hcc2018 import HCCConditions
from canvas_workflow_kit.value_set.value_set import ValueSet
from canvas_workflow_kit.recommendation import InterviewRecommendation, AssessRecommendation


class ReAssessment(ValueSet):
    VALUE_SET_NAME = 'Patient Re-Assessment' 
    INTERNAL = {'Patient Re-Assessment'}

class SemiAnnualReassessment(ClinicalQualityMeasure):
    class Meta:
        title = "Semi-Annual Reassessment"
        version = "2023-08-17"
        description = "All patients with active HCC conditions not assessed within the last year or filled out questionnaire."
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.INTERVIEW]

    @cached_property
    def active_hcc(self) -> list[dict]:
        hcc_conditions = []

        for record in [
            r
            for r in self.patient.conditions.find(HCCConditions)
            if r["clinicalStatus"] == "active"
        ]:
            if record["lastTimestamps"]["assessed"]:
                last_date = arrow.get(record["lastTimestamps"]["assessed"])
            else:
                last_date = arrow.get(record["noteTimestamp"])

            codes = [c for c in record["coding"] if c["system"] == "ICD-10"]
            if codes:
                hcc_conditions.append(
                    {
                        "ICD10": codes[0]["code"],
                        "date": last_date,
                        "id": record["id"]
                    }
                )
        return hcc_conditions

    @cached_property
    def too_old_hccs(self) -> list:
        return [hcc for hcc in self.active_hcc if hcc["date"] < self.timeframe.start]

    def in_initial_population(self) -> bool:
        return True

    def in_denominator(self) -> bool:
        """
        Patients with active condition in the HCC list
        """
        return bool(self.active_hcc)

    def in_numerator(self) -> bool:
        """
        Patients with active condition in the HCC list
         did not have a prior assessment or diagnosis in past 12 months
         or filled out the questionnaire after the condition was diagnosed
        """
        hccs = self.too_old_hccs
        last_date = max([hcc["date"] for hcc in hccs])
        return bool(hccs) and not self.patient.interviews.find(ReAssessment).filter(created__gte=last_date)

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(
                    f"Please outline IDT members that should be involved in patient re-asssessment"
                )
                for hcc in self.too_old_hccs:
                    condtion_id = hcc["id"]
                    idc10 = hcc["ICD10"]
                    label = HCCConditions.label_idc10_for(idc10)
                    raf = HCCConditions.raf_for(idc10)
                    day = hcc["date"].format("M/D/YY")

                    assess_recommendation = AssessRecommendation(
                      key='RECOMMEND_ASSESS_CONDITION',
                      rank=1,
                      button='Assess',
                      patient=self.patient,
                      title=f'Assess Condition: {label}',
                      context={
                        "condition_id": condtion_id,
                      }
                    )
                    result.add_recommendation(assess_recommendation)

                interview_recommendation = InterviewRecommendation(
                            key='RECOMMEND_REASSESSMENT',
                            rank=1,
                            button='Interview',
                            patient=self.patient,
                            questionnaires=[ReAssessment],
                            title='Patient is due for their Patient Re-Assessment'
                )

                result.add_recommendation(interview_recommendation)
            else:
                result.due_in = (
                    min([hcc["date"] for hcc in self.active_hcc]).shift(
                        days=self.timeframe.duration
                    )
                    - self.now
                ).days
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    "All Significant Condition have been assessed within the last {}.".format(  # noqa: E501
                        self.now.shift(months=-1, days=-1 * self.timeframe.duration).humanize(
                            other=self.now, granularity="month", only_distance=True
                        )
                    ).replace(
                        " ago", ""
                    )
                )
        return result

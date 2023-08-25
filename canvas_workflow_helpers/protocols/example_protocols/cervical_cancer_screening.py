import arrow
from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import LabRecommendation, ReferRecommendation
from canvas_workflow_kit.value_set.v2022.procedure import (
    HysterectomyWithNoResidualCervix,
)
from canvas_workflow_kit.value_set.v2022.laboratory_test import PapTest, HpvTest
from canvas_workflow_kit.value_set.value_set import ValueSet


class ScreeningForCervicalCancer(ValueSet):
    VALUE_SET_NAME = "Screening for cervical cancer"
    ICD10CM = {"Z12.4"}


class HpvTestOrder(ValueSet):
    VALUE_SET_NAME = "HPV DNA, LOW/HIGH RISK"
    CPT = {"87624"}


class PapTestOrder(ValueSet):
    VALUE_SET_NAME = "THINPREP PAP AND HR HPV DNA"
    CPT = {"88142"}


EncounterForPapCondition = {
    "code": "Z12.4",
    "system": "ICD-10",
    "display": "Encounter for screening for malignant neoplasm of cervix",
}


class ScreeningForHPV(ValueSet):
    VALUE_SET_NAME = "Screening for HPV"
    ICD10CM = {"Z11.51"}


EncounterForHPVScreeningCondition = {
    "code": "Z11.51",
    "system": "ICD-10",
    "display": "Encounter for screening for human papillomavirus (HPV)",
}

class Obstetrics_Gynecology(ValueSet):
    VALUE_SET_NAME = "Obstetrics & Gynecology (TBD)"


EncounterForGynecologicalExamCondition = {
    "code": "Z014.19",
    "system": "ICD-10",
    "display": "Encounter for gynecological examination (general) (routine) without abnormal findings",
}


class CervicalCancerScreening(ClinicalQualityMeasure):
    """
    A protocol to screen women for cervical cancer.
    """

    class Meta:
        title = "Cervial Cancer Screening"

        version = "2023-v01"

        description = (
            "A protocol to screen women between ages 21-64 for cervical cancer"
        )

        information = "https://link_to_protocol_information"

        identifiers = ["CervicalCancerScreening"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.PATIENT,
        ]

        authors = ["Canvas Example Medical Association (CEMA)"]

    def in_denominator(self):
        """
        Patient is female between the ages 21-64 without a total hysterectomy past surgical history.

        """
        is_female = self.patient.is_female
        in_age_range = self.patient.age_at_between(arrow.now(), 21, 65)
        no_hysterectomy = (
            len(self.patient.conditions.find(HysterectomyWithNoResidualCervix)) == 0
        )
        return is_female and in_age_range and no_hysterectomy

    def in_numerator(self):
        """
        Patient either:
          - has a pap lab test result within the past 3 years
          - age is between 30-64 and has an HPV lab test result within the past 5 years
        """
        has_pap_lab_test_within_3_years = (
            len(
                self.patient.lab_reports.find(PapTest).after(
                    arrow.now().shift(years=-3)
                )
            )
            > 0
        )

        age_between_30_and_64 = self.patient.age_at_between(arrow.now(), 30, 65)
        has_hpv_lab_test_within_5_years = (
            len(
                self.patient.lab_reports.find(HpvTest).after(
                    arrow.now().shift(years=-5)
                )
            )
            > 0
        )

        return has_pap_lab_test_within_3_years or (
            age_between_30_and_64 and has_hpv_lab_test_within_5_years
        )

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                narrative = f"{self.patient.first_name} is {int(self.patient.age)} years old without a hysterectomy surgical history and should be screened for cervical cancer."
                result.add_narrative(narrative)
                pap_recommendation = LabRecommendation(
                    key="PAP_TEST",
                    rank=1,
                    patient=self.patient,
                    condition=ScreeningForCervicalCancer,
                    title="Order pap test",
                    narrative=result.narrative,
                    lab=PapTestOrder,
                    context={
                        "conditions": [[EncounterForPapCondition]],
                        "health_gorilla_order_codes": ["92089"]
                    },
                )

                result.add_recommendation(pap_recommendation)
                hpv_recommendation = LabRecommendation(
                    key="HPV_TEST",
                    rank=2,
                    patient=self.patient,
                    condition=ScreeningForHPV,
                    title="Order HPV test",
                    narrative=result.narrative,
                    lab=HpvTestOrder,
                    context={
                        "conditions": [[EncounterForHPVScreeningCondition]],
                        "health_gorilla_order_codes": ["36453"],
                    },
                )
                result.add_recommendation(hpv_recommendation)

                refer_recommendation = ReferRecommendation(
                    key='RECOMMEND_REFER_OBGYN',
                    rank=3,
                    button='Refer',
                    patient=self.patient,
                    referral=Obstetrics_Gynecology,
                    condition=EncounterForGynecologicalExamCondition,
                    title='Refer for a Obstetrics & Gynecology',
                    context={
                    'specialties': ['Obstetrics & Gynecology'],
                    'conditions': [[EncounterForGynecologicalExamCondition]]}
                )
                result.add_recommendation(refer_recommendation)



        return result

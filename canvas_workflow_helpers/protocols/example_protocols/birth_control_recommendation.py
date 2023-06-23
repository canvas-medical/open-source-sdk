from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.medication import ContraceptiveMedications


class QuestionnaireBirthControlRequest(ValueSet):
    VALUE_SET_NAME = "Birth Control Request"
    INTERNAL = {"BC"}

class YAZ(ValueSet):
    VALUE_SET_NAME = "YAZ (28) 3 mg-0.02 mg tablet"
    FDB = {'476825'}

class Sprintec(ValueSet):
    VALUE_SET_NAME = "Sprintec (28) 0.25 mg-35 mcg tablet"
    FDB = {'446338'}

class Kariva(ValueSet):
    VALUE_SET_NAME = "Kariva (28) 0.15 mg-0.02 mg (21)/0.01 mg (5) tablet"
    FDB = {'401017'}

class Jolessa(ValueSet):
    VALUE_SET_NAME = "Jolessa 0.15 mg-30 mcg (91) tablets,3 month dose pack"
    FDB = {'546307'}

class Seasonique(ValueSet):
    VALUE_SET_NAME = "Seasonique 0.15 mg-30 mcg (84)/10 mcg(7) tablets,3 month dose pack"
    FDB = {'545786'}

EncounterForSurveiallanceOfContraceptivePills = {
    "code": "Z3041",
    "system": "ICD-10",
    "display": 'Encounter for surveillance of contraceptive pills',
}


class BirthControlPillQuickPicks(ClinicalQualityMeasure):

    class Meta:
        title = "Birth Control Pill Quick Picks"
        version = "2023-v01"
        description = "This protocol recommends birth control prescriptions based on questionnaire responses"
        information = "https://link_to_protocol_information"
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.MEDICATION]
        authors = ["Canvas Example Medical Association (CEMA)"]

        # notification_only = True # If True the protocol will no recompute on upload

        option = None

    def in_denominator(self):
        """
        Patients that have answered the Birth Control Request and answered any of these responses:
            - Q: Have you used birth control before? (BCQ1) = Pill (BCQ1Pill)
            - Q:Were you happy with the birth control option(s) you used previously? (BCQ4) = Yes (BCQ4Y)
            - Q: What other goals do you have or what benefits are you hoping to get from using birth control? (BCQ15) =
                Option I want to skip my periods regularly (BCQ15SKIP)
        """
        ques = self.patient.interviews.find(QuestionnaireBirthControlRequest).last()
        if not ques:
            return False

        code_responses = {response.get('code') for response in ques.get("responses", [])}

        if {"BCQ1Pill", "BCQ4Y"}.issubset(code_responses):
            self.option = 2 if 'BCQ15SKIP' in code_responses else 1
            return True

        return False

    def in_numerator(self):
        """
        Patients already have active Contraceptive Medication
        """
        return bool(self.patient.medications.find(
            ContraceptiveMedications | YAZ | Sprintec | Kariva | Jolessa | Seasonique).filter(
                status='active'))

    def compute_results(self):
        """ """
        result = ProtocolResult()

        # Find patients that have used birth control and are happy with previously used options
        if self.in_denominator():

            # Find if the patient has active contraceptive
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE

                if self.option == 1:
                    narrative = f"The patient indicated that they were happy with their previous pill. Please reference which medication they previously took and prescribe accordingly. Here are some quick picks for the most common options."
                    yaz_prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_YAZ_PRESCRIPTION',
                            rank=1,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=YAZ,
                            title='Prescribe Yaz',
                            context={
                                'conditions': [[EncounterForSurveiallanceOfContraceptivePills]],
                                'sig_original_input': 'Take 1 tablet by mouth daily at the same time',
                                'duration_in_days': 28,
                                'dispense_quantity': 1,
                                'dosage_form': '28 tablet blister pack',
                                'count_of_refills_allowed': 11,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(yaz_prescribe_recommendation)
                    sprintec_prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_SPRINTEC_PRESCRIPTION',
                            rank=2,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Sprintec,
                            title='Prescribe Sprintec',
                            context={
                                'conditions': [[EncounterForSurveiallanceOfContraceptivePills]],
                                'sig_original_input': 'Take 1 tablet by mouth daily at the same time',
                                'duration_in_days': 28,
                                'dispense_quantity': 1,
                                'dosage_form': '28 tablet blister pack',
                                'count_of_refills_allowed': 11,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(sprintec_prescribe_recommendation)
                    kariva_prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_KARIVA_PRESCRIPTION',
                            rank=3,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Kariva,
                            title='Prescribe Kariva',
                            context={
                                'conditions': [[EncounterForSurveiallanceOfContraceptivePills]],
                                'sig_original_input': 'Take 1 tablet by mouth daily at the same time',
                                'duration_in_days': 28,
                                'dispense_quantity': 1,
                                'dosage_form': 'Tablet',
                                'count_of_refills_allowed': 11,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(kariva_prescribe_recommendation)
                else:
                    narrative = f"The patient indicated that they want to reduce the frequency of their periods. Here are some quick picks for the most common options."
                    jolessa_prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_JOLESSA_PRESCRIPTION',
                            rank=1,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Jolessa,
                            title='Prescribe Jolessa',
                            context={
                                'conditions': [[EncounterForSurveiallanceOfContraceptivePills]],
                                'sig_original_input': 'Take 1 tablet by mouth daily at the same time',
                                'duration_in_days': 91,
                                'dispense_quantity': 1,
                                'dosage_form': '91 tablet blister pack',
                                'count_of_refills_allowed': 3,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(jolessa_prescribe_recommendation)
                    seasonique_prescribe_recommendation = PrescribeRecommendation(
                            key='RECOMMEND_SEASONIQUE_PRESCRIPTION',
                            rank=2,
                            button='Prescribe',
                            patient=self.patient,
                            prescription=Seasonique,
                            title='Prescribe Seasonique',
                            context={
                                'conditions': [[EncounterForSurveiallanceOfContraceptivePills]],
                                'sig_original_input': 'Take 1 tablet by mouth daily at the same time',
                                'duration_in_days': 91,
                                'dispense_quantity': 1,
                                'dosage_form': '91 tablet blister pack',
                                'count_of_refills_allowed': 3,
                                'generic_substitutions_allowed': True,
                        }
                    )
                    result.add_recommendation(seasonique_prescribe_recommendation)


                result.add_narrative(narrative)

        return result

import json
from typing import Optional

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_NOT_APPLICABLE,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    EndStageRenalDisease,
    Type1Diabetes,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest
from canvas_workflow_kit.fhir import FumageHelper


class WeightLossProgramStatusQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class WeightLossProgramIntakeQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Program Intake Questionnaire'
    INTERNAL = {'i1'}


class SevereCardioVascularDisease(ValueSet):
    VALUE_SET_NAME = 'Severe Cardiovascular Disease'
    ICD10CM = {'I5084'}


DisqualifyingConditions = (
    Type1Diabetes | EndStageRenalDisease | SevereCardioVascularDisease
)


class TSHLaboratoryTest(ValueSet):
    """Tests for TSH (Thyroid Stimulating Hormone)"""

    VALUE_SET_NAME = 'TSH Test'
    LOINC = {
        '11580-8',
    }


class UrineCortisolLaboratoryTest(ValueSet):
    """Tests for Urine Cortisol"""

    VALUE_SET_NAME = 'Urine Cortisol Test'
    LOINC = {
        '2147-7',
    }


status_coding_to_display = {
    'a211': 'Intake',
    'a212': 'Condition screening',
    'a213': 'Treatment',
    'a214': 'Disqualified',
}

status_display_to_coding = {v: k for k, v in status_coding_to_display.items()}


class UpdateProgramStatus(ClinicalQualityMeasure):
    class Meta:
        title = 'Update program status'
        version = '1.0.0'
        description = (
            'Updates program status based on '
            'questionnaires, conditions, lab results.'
        )
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.PATIENT,
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.CONDITION,
        ]
        notification_only = True

    questionnaire_id = '3ee30e27-a18f-4fc2-bdbc-5af3827590ce'
    link_id = '21ba40f3-0416-48b8-8a96-234592e91b03'
    practitioner_id = '5eede137ecfe4124b8b773040e33be14'

    def get_current_status(self) -> Optional[str]:
        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')
        if not status_interviews:
            return None
        most_recent = max(status_interviews, key=lambda x: x['created'])
        response = most_recent['responses'][0]['code']
        return status_coding_to_display[response]

    def last_a1c(self) -> Optional[float]:
        if a1c_tests := self.patient.lab_reports.find(Hba1CLaboratoryTest):
            return float(a1c_tests.last_value())
        return None

    def last_tsh(self) -> Optional[float]:
        if tsh_tests := self.patient.lab_reports.find(TSHLaboratoryTest):
            return float(tsh_tests.last_value())
        return None

    def last_cortisol(self) -> Optional[float]:
        if cortisol_tests := self.patient.lab_reports.find(
            UrineCortisolLaboratoryTest
        ):
            return float(cortisol_tests.last_value())
        return None

    def has_abnormal_tests(self) -> bool:
        if last_a1c := self.last_a1c():
            if last_a1c > 9:
                return True
        if last_tsh := self.last_tsh():
            if last_tsh > 5:
                return True
        if last_cortisol := self.last_cortisol():
            if last_cortisol > 100:
                return True
        return False

    def has_missing_tests(self) -> bool:
        tests_to_check = [
            Hba1CLaboratoryTest,
            TSHLaboratoryTest,
            UrineCortisolLaboratoryTest,
        ]
        return any(
            not self.patient.lab_reports.find(test) for test in tests_to_check
        )

    def compute_correct_status(self) -> str:
        """Compute the correct status for the patient."""
        if not self.patient.interviews.find(
            WeightLossProgramIntakeQuestionnaire
        ):
            return 'Intake'
        if (
            bool(
                self.patient.conditions.find(DisqualifyingConditions).filter(
                    clinicalStatus='active'
                )
            )
            or self.patient.age > 65
        ):
            return 'Disqualified'
        if self.has_missing_tests():
            return 'Condition screening'
        return 'Disqualified' if self.has_abnormal_tests() else 'Treatment'

    def post_fhir_questionnaireresponse(self, status_display):
        payload = {
            'resourceType': 'QuestionnaireResponse',
            'status': 'completed',
            'questionnaire': f'Questionnaire/{self.questionnaire_id}',
            'subject': {'reference': f"Patient/{self.patient.patient['key']}"},
            'author': {'reference': f'Practitioner/{self.practitioner_id}'},
            'item': [
                {
                    'linkId': f'{self.link_id}',
                    'text': 'Current status',
                    'answer': [
                        {
                            'valueCoding': {
                                'system': f'http://schemas.{self.settings.INSTANCE_NAME}.canvasmedical.com/fhir/systems/internal',
                                'code': status_display_to_coding[
                                    status_display
                                ],
                                'display': status_display,
                            }
                        }
                    ],
                }
            ],
        }

        fhir = FumageHelper(self.settings)
        response = fhir.create("QuestionnaireResponse", payload)
        if response.status_code != 201:
            raise Exception(f"Failed to create QuestionnaireResponse with {response.text} and correlation-id {response.headers['fumage-correlation-id']}")

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE
        current_status = self.get_current_status()
        correct_status = self.compute_correct_status()
        if correct_status == current_status:
            return result
        else:
            self.post_fhir_questionnaireresponse(correct_status)

        return result

from pathlib import Path

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (ProtocolResult, STATUS_DUE,
                                          STATUS_NOT_APPLICABLE)
from canvas_workflow_kit.recommendation import (Recommendation)


class SurveyDrivenDiagnosisTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        patient_in_denominator = self.load_patient('full_detailed_patient')
        patient_in_numerator = self.load_patient('partial_detailed_patient')

        self.denominator_class = self.createProtocolClass()(
            patient=patient_in_denominator)
        self.numerator_class = self.createProtocolClass()(
            patient=patient_in_numerator)

    def createProtocolClass(self):
        template_path = Path(
            __file__).parent.parent / 'protocols/survey_driven_diagnosis.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.denominator_class
        self.assertEqual(
            'A protocol that recommends diagnosing'
            'certain conditions based on questionnaire responses.',
            Protocol._meta.description)
        self.assertEqual('Diagnostic Assessment', Protocol._meta.title)
        self.assertEqual('v1.0.0', Protocol._meta.version)
        self.assertEqual('https://canvasmedical.com/',
                         Protocol._meta.information)
        self.assertEqual(['DiagnosticAssessment'], Protocol._meta.identifiers)
        self.assertEqual(['Tools'], Protocol._meta.types)
        self.assertEqual([events.HEALTH_MAINTENANCE],
                         Protocol._meta.responds_to_event_types)
        self.assertEqual([CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.CONDITION],
                         Protocol._meta.compute_on_change_types)
        self.assertEqual(['Canvas Medical'], Protocol._meta.authors)
        self.assertEqual(['Canvas Medical'], Protocol._meta.references)
        self.assertEqual('', Protocol._meta.funding_source)

    def test_denominator_class(self):
        tested = self.denominator_class
        result = tested.compute_results()

        narrative = (
            f'{tested.patient.first_name} responded "Yes" to '
            f'3 questions in the Diagnostic Assessment '
            f'Questionnaire, but has not been diagnosed with the associated conditions. '
            f'Consider updating the Conditions List as clinically appropriate')

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0], Recommendation)
        self.assertEqual(narrative, result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_numerator_class(self):
        tested = self.numerator_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)
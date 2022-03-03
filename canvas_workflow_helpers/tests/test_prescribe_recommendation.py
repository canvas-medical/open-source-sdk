from pathlib import Path

from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (ProtocolResult, STATUS_DUE,
                                          STATUS_SATISFIED,
                                          STATUS_NOT_APPLICABLE)
from canvas_workflow_kit.recommendation import (PrescribeRecommendation)


class PrescribeButtonTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        full_patient = self.load_patient('full_detailed_patient')
        partial_patient = self.load_patient('partial_detailed_patient')
        no_details_patient = self.load_patient('no_details_patient')

        self.in_numerator_class = self.createProtocolClass()(
            patient=full_patient)
        self.in_denominator_class = self.createProtocolClass()(
            patient=partial_patient)
        self.not_applicable_class = self.createProtocolClass()(
            patient=no_details_patient)

    def createProtocolClass(self):
        template_path = Path(
            __file__
        ).parent.parent / 'protocols/prescribe_command_recommendation.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.in_numerator_class
        self.assertEqual('A protocol w/ a prescribe button recommendation',
                         Protocol._meta.description)
        self.assertEqual('Prescribe Button', Protocol._meta.title)
        self.assertEqual('v1.0.0', Protocol._meta.version)
        self.assertEqual('https://canvasmedical.com/',
                         Protocol._meta.information)
        self.assertEqual(['Prescribe'], Protocol._meta.identifiers)
        self.assertEqual(['Orders'], Protocol._meta.types)
        self.assertEqual([events.HEALTH_MAINTENANCE],
                         Protocol._meta.responds_to_event_types)
        self.assertEqual([CHANGE_TYPE.MEDICATION, CHANGE_TYPE.CONDITION],
                         Protocol._meta.compute_on_change_types)
        self.assertEqual(['Canvas Medical'], Protocol._meta.authors)
        self.assertEqual(['Canvas Medical'], Protocol._meta.references)
        self.assertEqual('', Protocol._meta.funding_source)

    def test_in_numerator_class(self):
        tested = self.in_numerator_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_SATISFIED, result.status)
        self.assertEqual(result.recommendations, [])
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_in_denominator_class(self):
        tested = self.in_denominator_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              PrescribeRecommendation)
        self.assertEqual(
            'Review medical history and consider Zofran prescription.',
            result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertIsNone(result.next_review)

    def test_not_applicable_class(self):
        tested = self.not_applicable_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual(result.recommendations, [])
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

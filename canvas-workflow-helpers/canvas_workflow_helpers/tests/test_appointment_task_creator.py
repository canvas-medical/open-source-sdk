import pathlib

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_helpers.protocols import appointment_task_creator
from canvas_workflow_kit import events
from pathlib import Path
from canvas_workflow_kit.protocol import (ProtocolResult, STATUS_DUE,
                                          STATUS_SATISFIED,
                                          STATUS_NOT_APPLICABLE)


class AppointmentTaskCreatorTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = pathlib.Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        patient = self.load_patient('patient')
        print("PATIENT", patient.patient)
        self.base_class = self.createProtocolClass({})(patient=patient)
        self.satisfied_class = self.createProtocolClass({
            'denominator':
            'return True',
            'numerator':
            'return True'
        })(patient=patient)
        self.due_class = self.createProtocolClass({
            'denominator': 'return True',
            'numerator': 'return False'
        })(patient=patient)

    def createProtocolClass(self, fields={}):
        template_fields = {**fields}
        # Path(__file__).parent.parent / 'builtin_cqms/stub_template_user.py.txt'
        # currentDir = pathlib.Path(__file__).parent.parent.resolve()
        template_path = pathlib.Path(
            __file__).parent.parent / 'protocols/appointment_task_creator.py'
        # print("TEMPLATE PATH", template_path)
        template = template_path.open('r').read()
        # print("TEMPLATE", template, type(template))

        # content = template.format(template_fields)
        return parse_class_from_python_source(template)

    def test_base_fields(self):
        Protocol = self.base_class
        self.assertEqual(
            'Listens for appointment creates and generates a task.',
            Protocol._meta.description)
        self.assertEqual('Appointment Task Creator', Protocol._meta.title)
        self.assertEqual('v1.0.0', Protocol._meta.version)
        self.assertEqual('https://canvasmedical.com/',
                         Protocol._meta.information)
        self.assertEqual(['AppointmentTaskCreator'],
                         Protocol._meta.identifiers)
        self.assertEqual(['Task'], Protocol._meta.types)
        self.assertEqual([events.HEALTH_MAINTENANCE],
                         Protocol._meta.responds_to_event_types)
        self.assertEqual([CHANGE_TYPE.APPOINTMENT],
                         Protocol._meta.compute_on_change_types)
        self.assertEqual(['Canvas Medical'], Protocol._meta.authors)
        self.assertEqual(['Canvas Medical'], Protocol._meta.references)
        self.assertEqual('', Protocol._meta.funding_source)

    def test_base_result(self):
        tested = self.base_class

        print("BASE CLASS", vars(tested))
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    # def test_satisfied_numerator(self):
    #     tested = self.satisfied_class

    #     numerator = tested.in_numerator()
    #     self.assertTrue(numerator)

    # def test_satisfied_denominator(self):
    #     tested = self.satisfied_class

    #     denominator = tested.in_denominator()
    #     self.assertTrue(denominator)

    # def test_satisfied_result(self):
    #     tested = self.satisfied_class

    #     result = tested.compute_results()
    #     self.assertIsInstance(result, ProtocolResult)
    #     self.assertEqual(STATUS_SATISFIED, result.status)
    #     self.assertEqual([], result.recommendations)
    #     self.assertEqual('', result.narrative)
    #     self.assertIsNone(result.due_in)
    #     self.assertEqual(30, result.days_of_notice)
    #     self.assertIsNone(result.next_review)

    # def test_due_numerator(self):
    #     tested = self.due_class

    #     numerator = tested.in_numerator()
    #     self.assertFalse(numerator)

    # def test_due_denominator(self):
    #     tested = self.due_class

    #     denominator = tested.in_denominator()
    #     self.assertTrue(denominator)

    # # def test_due_result(self):
    # #     tested = self.due_class

    # #     result = tested.compute_results()
    # #     self.assertIsInstance(result, ProtocolResult)
    # #     self.assertEqual(STATUS_DUE, result.status)
    # #     self.assertEqual(
    # #         'Nicolas has at least two eGFR measurements < 60 ml/min over the last two years suggesting renal disease. There is no associated condition on the Conditions List.',
    # #         result.narrative)
    # #     self.assertEqual(-1, result.due_in)
    # #     self.assertEqual(30, result.days_of_notice)
    # #     self.assertIsNone(result.next_review)
    # #     self.assertEqual(len(result.recommendations), 1)

    # # def test_due_result_recommendation(self):
    # #     tested = self.due_class

    # #     result = tested.compute_results()
    # #     recommendation = result.recommendations[0]
    # #     self.assertEqual(recommendation.key, 'HCC002v2_RECOMMEND_DIAGNOSE')
    # #     self.assertEqual(recommendation.rank, 1)
    # #     self.assertEqual(recommendation.button, 'Diagnose')
    # #     self.assertEqual(
    # #         recommendation.title,
    # #         'Consider updating the Conditions List to include kidney related problems as clinically appropriate'
    # #     )
    # #     self.assertEqual(
    # #         recommendation.narrative,
    # #         'Nicolas has at least two eGFR measurements < 60 ml/min over the last two years suggesting renal disease. There is no associated condition on the Conditions List.'
    # #     )
    # #     self.assertEqual(recommendation.command, {'type': 'diagnose'})

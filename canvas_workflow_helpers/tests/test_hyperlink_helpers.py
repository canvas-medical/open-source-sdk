from cgitb import reset
from pathlib import Path
from unittest.mock import create_autospec

from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (ProtocolResult, STATUS_DUE)
from canvas_workflow_kit.recommendation import (Recommendation,
                                                HyperlinkRecommendation)


class HyperlinkHelpersTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        patient = self.load_patient('patient_has_appointments')
        patient_without_appointments = self.load_patient(
            'patient_no_appointments')

        self.base_class = self.createProtocolClass()(patient=patient)
        self.no_appointments_class = self.createProtocolClass()(
            patient=patient_without_appointments)

    def createProtocolClass(self):
        template_path = Path(
            __file__).parent.parent / 'protocols/hyperlink_helpers.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.base_class
        self.assertEqual(
            'Creates external dynamic hyperlinks at the top of the protocol list',
            Protocol._meta.description)
        self.assertEqual('External Links', Protocol._meta.title)
        self.assertEqual('v1.0.0', Protocol._meta.version)
        self.assertEqual('https://canvasmedical.com/',
                         Protocol._meta.information)
        self.assertEqual(['ExternalLinks'], Protocol._meta.identifiers)
        self.assertEqual(['Links'], Protocol._meta.types)
        self.assertEqual([events.HEALTH_MAINTENANCE],
                         Protocol._meta.responds_to_event_types)
        self.assertEqual(['Canvas Medical'], Protocol._meta.authors)
        self.assertEqual(['Links to external resources about the patient'],
                         Protocol._meta.references)
        self.assertEqual('', Protocol._meta.funding_source)
        self.assertEqual(False, Protocol._meta.can_be_snoozed)

    def test_appointment_class_result(self):
        tested = self.base_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              HyperlinkRecommendation)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_patient_external_id(self):
        patient_with_appointments = self.base_class
        expecting_id = patient_with_appointments.patient_external_id()
        patient_no_appointments = self.no_appointments_class
        expecting_empty_string = patient_no_appointments.patient_external_id()

        self.assertEqual(expecting_id, '72342334')
        self.assertEqual(expecting_empty_string, '')

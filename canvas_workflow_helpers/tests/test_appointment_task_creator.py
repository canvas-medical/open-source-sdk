from pathlib import Path

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (ProtocolResult,
                                          STATUS_NOT_APPLICABLE)


class AppointmentTaskCreatorTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        patient_has_appointments = self.load_patient(
            'patient_appointments/patient_has_appointments')
        patient_no_appointments = self.load_patient(
            'patient_appointments/patient_no_appointments')

        self.appointment_class = self.createProtocolClass()(
            patient=patient_has_appointments)
        self.no_appointment_class = self.createProtocolClass()(
            patient=patient_no_appointments)

    def createProtocolClass(self):
        template_path = Path(
            __file__).parent.parent / 'protocols/appointment_task_creator.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.appointment_class
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

    def test_appointment_class_result(self):
        tested = self.appointment_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_no_appointment_class_result(self):
        tested = self.no_appointment_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    """
    The rest of these functions tested depend on context = {}
    Currently there is a bug where context = 'report', but the pr is almost ready to merge
    Once fix is merged, add more tests
    For now, just test that these do not error
    """

    def test_get_record_by_id(self):
        tested_no_appointments = self.no_appointment_class
        empty_given_none = tested_no_appointments.get_record_by_id(None, None)

        self.assertEqual({}, empty_given_none)

    def test_get_new_field_value(self):
        tested_no_appointments = self.no_appointment_class
        none_given_none = tested_no_appointments.get_new_field_value(None)

        self.assertIsNone(none_given_none)

    def test_is_appointment_and_created(self):
        tested_no_appointments = self.no_appointment_class
        no_appointments = tested_no_appointments.is_appointment_and_created()

        self.assertEqual(False, no_appointments)

    def test_find_provider_key(self):
        tested_no_appointments = self.no_appointment_class
        no_expected_provider = tested_no_appointments.find_provider_key()

        self.assertIsNone(no_expected_provider)

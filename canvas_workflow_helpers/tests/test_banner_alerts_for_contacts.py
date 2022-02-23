from cgitb import reset
from pathlib import Path

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.utils import parse_class_from_python_source
from .base import WorkflowHelpersBaseTest
from canvas_workflow_kit import events
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.protocol import (ProtocolResult,
                                          STATUS_NOT_APPLICABLE, STATUS_DUE)


class BannerAlertsTest(WorkflowHelpersBaseTest):

    def setUp(self):
        super().setUp()
        currentDir = Path(__file__).parent.resolve()
        self.mocks_path = f'{currentDir}/mock_data/'

        patient_with_contacts = self.load_patient('patient_has_appointments')
        patient_without_contacts = self.load_patient('patient_no_appointments')

        self.contact_class = self.createProtocolClass()(
            patient=patient_with_contacts)
        self.no_contacts_class = self.createProtocolClass()(
            patient=patient_without_contacts)

    def createProtocolClass(self):
        template_path = Path(
            __file__).parent.parent / 'protocols/banner_alerts_for_contacts.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.contact_class
        self.assertEqual('Reminders about patients over the age of 70',
                         Protocol._meta.description)
        self.assertEqual('Banner Alert Contacts', Protocol._meta.title)
        self.assertEqual('v1.0.0', Protocol._meta.version)
        self.assertEqual('https://canvasmedical.com/',
                         Protocol._meta.information)
        self.assertEqual(['BannerAlertContacts'], Protocol._meta.identifiers)
        self.assertEqual(['Alerts'], Protocol._meta.types)
        self.assertEqual([events.HEALTH_MAINTENANCE],
                         Protocol._meta.responds_to_event_types)
        self.assertEqual([CHANGE_TYPE.PATIENT],
                         Protocol._meta.compute_on_change_types)
        self.assertEqual(['Canvas Medical'], Protocol._meta.authors)
        self.assertEqual(['Canvas Medical'], Protocol._meta.references)
        self.assertEqual('', Protocol._meta.funding_source)

    def test_contact_class(self):
        tested = self.contact_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_no_contact_class(self):
        tested = self.no_contacts_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              BannerAlertIntervention)
        self.assertEqual('', result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    """
    The rest of these functions tested depend on context = {}
    Currently there is a bug where context = 'report', but the pr is almost ready to merge
    Once fix is merged, add more tests
    For now, just test that these do not error
    """

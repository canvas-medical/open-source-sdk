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

        multiple_contacts_73yo = self.load_patient(
            'patient_contacts/multiple_contacts_73yo')
        no_contacts_13yo = self.load_patient(
            'patient_contacts/no_contacts_13yo')
        no_contacts_72yo = self.load_patient(
            'patient_contacts/no_contacts_72yo')
        one_contact_73yo = self.load_patient(
            'patient_contacts/one_contact_73yo')

        self.multiple_contact_class = self.createProtocolClass()(
            patient=multiple_contacts_73yo)

        self.no_contacts_class_13yo = self.createProtocolClass()(
            patient=no_contacts_13yo)

        self.no_contacts_class_72yo = self.createProtocolClass()(
            patient=no_contacts_72yo)

        self.one_contact_73yo = self.createProtocolClass()(
            patient=one_contact_73yo)

    def createProtocolClass(self):
        template_path = Path(
            __file__).parent.parent / 'protocols/banner_alerts_for_contacts.py'
        template = template_path.open('r').read()

        return parse_class_from_python_source(template)

    def test_fields(self):
        Protocol = self.multiple_contact_class
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

    def test_no_contacts_under_70(self):
        tested = self.no_contacts_class_13yo
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_NOT_APPLICABLE, result.status)
        self.assertEqual([], result.recommendations)
        self.assertEqual('', result.narrative)
        self.assertIsNone(result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_no_contacts_over_70(self):
        tested = self.no_contacts_class_72yo
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              BannerAlertIntervention)
        self.assertEqual('', result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_multiple_contacts_over_70(self):
        tested = self.multiple_contact_class
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              BannerAlertIntervention)
        self.assertEqual('', result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_one_contact_over_70(self):
        tested = self.one_contact_73yo
        result = tested.compute_results()

        self.assertIsInstance(result, ProtocolResult)
        self.assertEqual(STATUS_DUE, result.status)
        self.assertIsInstance(result.recommendations[0],
                              BannerAlertIntervention)
        self.assertEqual('', result.narrative)
        self.assertEqual(-1, result.due_in)
        self.assertEqual(30, result.days_of_notice)
        self.assertIsNone(result.next_review)

    def test_in_denominator(self):
        expected_true = self.one_contact_73yo
        result_true = expected_true.in_denominator()
        expected_false = self.no_contacts_class_13yo
        result_false = expected_false.in_denominator()

        self.assertEqual(result_true, True)
        self.assertEqual(result_false, False)

    def test_get_contact_display(self):
        tested = self.one_contact_73yo
        contact = {
            "name": "Hansen Azamar",
            "relationship": "Husband",
            "phoneNumber": "0000000000",
            "email": "hansen.test@testing.test",
            "emergencyContact": False,
            "authorizedForReleaseOfInformation": False,
            "id": 2
        }
        result = tested.get_contact_display(contact)
        self.assertEqual(result, 'Hansen Azamar (Husband)')

    def test_has_contact_category(self):
        tested = self.multiple_contact_class
        emergency_contacts = []
        release_of_info_contacts = []
        poa_contacts = []

        for contact in self.multiple_contact_class.patient.patient.get(
                'contacts', []):
            categories = contact.get('categories', [])
            if tested.has_contact_category(categories, 'EMC'):
                emergency_contacts.append(contact)
            if tested.has_contact_category(categories, 'ARI'):
                release_of_info_contacts.append(contact)
            if tested.has_contact_category(categories, 'POA'):
                poa_contacts.append(contact)

        self.assertEqual(len(emergency_contacts), 1)
        self.assertEqual(len(release_of_info_contacts), 1)
        self.assertEqual(len(poa_contacts), 1)
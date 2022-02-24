import math

from canvas_workflow_kit import events
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.protocol import STATUS_DUE, ClinicalQualityMeasure, ProtocolResult


class BannerAlertContacts(ClinicalQualityMeasure):
    """
    A protocol that displays banner alerts for patients over the age of 70
    without a single emergency contact, a single contact authorized for release of information,
    and a single Power of Attorney contact
    """

    class Meta:

        title = 'Banner Alert Contacts'

        version = 'v1.0.0'

        description = 'Reminders about patients over the age of 70'

        information = 'https://canvasmedical.com/'

        identifiers = ['BannerAlertContacts']

        types = ['Alerts']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]
        compute_on_change_types = [CHANGE_TYPE.PATIENT]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

    rounded_patient_age = None

    def get_contact_display(self, contact):
        display = contact['name']
        relationship = contact['relationship']
        if relationship and relationship != '':
            display += f' ({relationship})'
        return display

    def in_denominator(self):
        """
        Patients over the age of 70.

        """
        rounded_patient_age = math.floor(self.patient.age)
        self.rounded_patient_age = rounded_patient_age
        return rounded_patient_age >= 70

    def has_contact_category(self, categories, category):
        return next((cat for cat in categories if cat['category'] == category),
                    None) is not None

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            result.status = STATUS_DUE
            result.due_in = -1

            emergency_contacts = []
            release_of_info_contacts = []
            poa_contacts = []
            for contact in self.patient.patient.get('contacts', []):
                categories = contact.get('categories', [])
                if self.has_contact_category(categories, 'EMC'):
                    emergency_contacts.append(contact)
                if self.has_contact_category(categories, 'ARI'):
                    release_of_info_contacts.append(contact)
                if self.has_contact_category(categories, 'POA'):
                    poa_contacts.append(contact)

            num_emergency_contacts = len(emergency_contacts)
            num_release_contacts = len(release_of_info_contacts)
            num_poa_contacts = len(poa_contacts)

            if num_emergency_contacts == 1:
                emergency_contact_display = self.get_contact_display(
                    emergency_contacts[0])
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=(
                            f'{self.patient.first_name} has 1 '
                            f'emergency contact: {emergency_contact_display}'),
                        placement=['timeline', 'appointment_card'],
                        intent='info'))
            if num_release_contacts == 1:
                release_contact_display = self.get_contact_display(
                    release_of_info_contacts[0])
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} has 1 '
                        f'contact authorized for release of info: {release_contact_display}'
                    ),
                                            placement=[
                                                'timeline', 'appointment_card'
                                            ],
                                            intent='info'))
            if num_poa_contacts == 1:
                poa_contact_display = self.get_contact_display(poa_contacts[0])
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} has 1 '
                        f'contact with Power of Attorney: {poa_contact_display}'
                    ),
                                            placement=[
                                                'timeline', 'appointment_card'
                                            ],
                                            intent='info'))

            if num_emergency_contacts > 1:
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} has {num_emergency_contacts} '
                        'emergency contacts listed. Please reduce to 1.'),
                                            placement=['profile'],
                                            intent='warning'))
            if num_release_contacts > 1:
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} has {num_release_contacts} '
                        'contacts authorized for release of info. Please reduce to 1.'
                    ),
                                            placement=['profile'],
                                            intent='warning'))
            if num_poa_contacts > 1:
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} has {num_poa_contacts} '
                        'contacts with Power of Attorney. Please reduce to 1.'
                    ),
                                            placement=['profile'],
                                            intent='warning'))

            if num_emergency_contacts == 0:
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=
                        (f'{self.patient.first_name} is {self.rounded_patient_age} '
                         'and has no emergency contacts listed'),
                        placement=['appointment_card', 'scheduling_card'],
                        intent='alert',
                        href=
                        f'http://localhost:8000/patient/{self.patient.patient_key}/edit#'
                    ))
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} is {self.rounded_patient_age} '
                        'and has no emergency contacts listed'),
                                            placement=['profile', 'chart'],
                                            intent='alert'))
            if num_release_contacts == 0:
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=
                        (f'{self.patient.first_name} is {self.rounded_patient_age} '
                         'and has no contacts authorized for release of info'),
                        placement=['appointment_card', 'scheduling_card'],
                        intent='alert',
                        href=
                        f'http://localhost:8000/patient/{self.patient.patient_key}/edit#'
                    ))
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} is {self.rounded_patient_age} '
                        'and has no contacts authorized for release of info'),
                                            placement=['profile', 'chart'],
                                            intent='alert'))
            if num_poa_contacts == 0:
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=
                        (f'{self.patient.first_name} is {self.rounded_patient_age} '
                         'and has no contacts with Power of Attorney'),
                        placement=['appointment_card', 'scheduling_card'],
                        intent='alert',
                        href=
                        f'http://localhost:8000/patient/{self.patient.patient_key}/edit#'
                    ))
                result.recommendations.append(
                    BannerAlertIntervention(narrative=(
                        f'{self.patient.first_name} is {self.rounded_patient_age} '
                        'and has no contacts with Power of Attorney'),
                                            placement=['profile', 'chart'],
                                            intent='alert'))
        return result
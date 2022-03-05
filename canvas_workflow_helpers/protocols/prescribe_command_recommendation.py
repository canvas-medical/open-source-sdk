from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (ClinicalQualityMeasure,
                                          ProtocolResult, STATUS_DUE,
                                          STATUS_SATISFIED)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set.value_set import ValueSet


class ValueSetWithNDC(ValueSet):
    value_systems = [*ValueSet.value_systems, 'NDC']


class Zofran(ValueSetWithNDC):
    VALUE_SET_NAME = 'Zofran 8 mg tablet'
    NDC = {'00078067615'}
    RXNORM = {'312086'}
    FDB = {221962}


class Nausea(ValueSet):
    VALUE_SET_NAME = 'Nausea with vomiting, unspecified'
    ICD10CM = {'R112'}


class PrescribeButton(ClinicalQualityMeasure):
    """
    A protocol with a prescribe button recommendation that inserts a 
    completed prescribe command
    """

    class Meta:

        title = 'Prescribe Button'

        version = 'v1.0.0'

        description = 'A protocol w/ a prescribe button recommendation'

        information = 'https://canvasmedical.com/'

        identifiers = ['Prescribe']

        types = ['Orders']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION, CHANGE_TYPE.CONDITION
        ]

        authors = ['Canvas Medical']

        references = ['Canvas Medical']

        funding_source = ''

    nausea = None

    def in_denominator(self):
        """
        Patients with nausea.
        """
        nausea_conditions = self.patient.conditions.find(Nausea).filter(
            clinicalStatus='active')
        if not nausea_conditions:
            return False

        self.nausea = nausea_conditions[0]
        return True

    def in_numerator(self):
        """
        Patients that have already been prescribed zofran
        """
        return len(
            self.patient.medications.find(Zofran).filter(status='active')) > 0

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(
                    'Review medical history and consider Zofran prescription.')
                title = 'Zofran 8 mg tablet'
                prescribe_recommendation = PrescribeRecommendation(
                    key='RECOMMEND_ZOFRAN',
                    rank=1,
                    button='Prescribe',
                    patient=self.patient,
                    prescription=Zofran,
                    title=title,
                    narrative=result.narrative)
                conditions = [
                    coding for coding in self.nausea['coding']
                    if coding['system'] == 'ICD-10'
                ]
                prescribe_recommendation.context = {
                    'conditions': [conditions],
                    'dosage_form': 'tablet',
                    'sig_original_input': '1 tab po bid',
                    'duration_in_days': 10,
                    'dispense_quantity': 20,
                    'dosage_form': 'tablet',
                    'count_of_refills_allowed': 2,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': 'hello, have a great day!'
                }
                result.add_recommendation(prescribe_recommendation)

        return result

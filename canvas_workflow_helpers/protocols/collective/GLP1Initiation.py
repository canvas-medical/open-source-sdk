from typing import Optional

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set import ValueSet


class WeightLossPaymentMethodQuestionnire(ValueSet):
    VALUE_SET_NAME = 'Weight Loss Payment Method Questionnaire'
    INTERNAL = {'i4'}


class Wegovy(ValueSet):
    """Wegovy (semaglutide)"""

    VALUE_SET_NAME = 'Wegovy'
    RXNORM = {
        '2553502',
        '1649570',
        '1151126',
        '1991302',
        '2553506',
        '2553603',
        '2553803',
        '2553903',
        '2554104',
        '2553503',
        '2553602',
        '2553608',
        '2553902',
        '2554103',
        '2553504',
        '2553505',
        '2553501',
        '2553601',
        '2553802',
        '2553901',
        '2554102',
        '2553400',
        '2553600',
        '2553606',
        '2553900',
        '2554101',
        '2553500',
        '1991304',
    }


class Mounjaro(ValueSet):
    """Mounjaro (semaglutide)"""

    VALUE_SET_NAME = 'Mounjaro'
    RXNORM = {
        '2601734',
        '1649570',
        '1151126',
        '2601723',
        '2601746',
        '2601758',
        '2601764',
        '2601770',
        '2601776',
        '2601785',
        '2601745',
        '2601757',
        '2601763',
        '2601769',
        '2601775',
        '2601781',
        '2601737',
        '2601736',
        '2601743',
        '2601755',
        '2601761',
        '2601767',
        '2601773',
        '2601784',
        '2601742',
        '2601754',
        '2601760',
        '2601766',
        '2601772',
        '2601778',
        '2601731',
        '2601730',
    }


class Saxenda(ValueSet):
    """Saxenda (liraglutide)"""

    VALUE_SET_NAME = 'Saxenda'

    RXNORM = {
        '1649571',
        '1151126',
        '475968	',
        '1598268',
        '1598265',
        '1653600',
        '1598267',
        '897122',
        '897120',
        '1653594',
        '1163230',
    }


class WegovyRx(ValueSet):
    VALUE_SET_NAME = 'Wegovy'
    FDB = {'606783'}


class MounjaroRx(ValueSet):
    VALUE_SET_NAME = 'Mounjaro'
    FDB = {'611114'}


class SaxendaRx(ValueSet):
    VALUE_SET_NAME = 'Saxenda'
    FDB = {'584911'}


class Pancreatitis(ValueSet):
    """Pancreatitis"""

    VALUE_SET_NAME = 'Pancreatitis'
    ICD10CM = {
        'K850',
        'K8500',
        'K8501',
        'K8502',
        'K851',
        'K8510',
        'K8511',
        'K8512',
        'K852',
        'K8520',
        'K8521',
        'K8522',
        'K853',
        'K8530',
        'K8531',
        'K8532',
        'K858',
        'K8580',
        'K8581',
        'K8582',
        'K859',
        'K8590',
        'K8591',
        'K8592',
    }


class Gallstones(ValueSet):
    """Gallstones"""

    VALUE_SET_NAME = 'Gallstones'
    ICD10CM = {
        'K800',
        'K8000',
        'K8001',
        'K801',
        'K8010',
        'K8011',
        'K8012',
        'K8013',
        'K8018',
        'K8019',
        'K802',
        'K8020',
        'K8021',
        'K803',
        'K8030',
        'K8031',
        'K8032',
        'K8033',
        'K8034',
        'K8035',
        'K8036',
        'K8037',
        'K804',
        'K8040',
        'K8041',
        'K8042',
        'K8043',
        'K8044',
        'K8045',
        'K8046',
        'K8047',
        'K805',
        'K8050',
        'K8051',
        'K806',
        'K8060',
        'K8061',
        'K8062',
        'K8063',
        'K8064',
        'K8065',
        'K8066',
        'K8067',
        'K807',
        'K8070',
        'K8071',
        'K808',
        'K8080',
        'K8081',
    }


class MedullaryThyroidCancer(ValueSet):
    """Medullary Thyroid Cancer"""

    VALUE_SET_NAME = 'MedullaryThyroidCancer'
    ICD10CM = {'C73'}


class GLP1Initiation(ClinicalQualityMeasure):
    class Meta:
        title = 'Initiation of GLP-1 for Overweight Patients'
        description = (
            'This protocol recommends the initiation of GLP-1 '
            'agonists (Wegovy, Mounjaro, or Saxenda) for '
            'patients with a BMI over 30, who are self-pay '
            'or have insurance with prior authorization '
            'approved, and have no contraindications. '
            'Contraindications include a history of '
            'pancreatitis, gallstones with gallbladder, or '
            'medullary thyroid cancer (personal or family history).'
        )
        version = '1.0.10'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.COVERAGE,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.INTERVIEW,
            CHANGE_TYPE.VITAL_SIGN,
            CHANGE_TYPE.MEDICATION,
        ]
        references = []

    def is_on_medication(self, medication: ValueSet) -> bool:
        return bool(
            self.patient.medications.find(medication).filter(status='active')
        )

    def get_bmi(self) -> Optional[float]:
        last_weight_oz = self.patient.vital_signs.filter(
            sign='weight'
        ).last_value()
        last_height_in = self.patient.vital_signs.filter(
            sign='height'
        ).last_value()
        if not last_weight_oz or not last_height_in:
            return None
        last_height_in = float(last_height_in)
        last_weight_oz = float(last_weight_oz)
        return (last_weight_oz / last_height_in**2) * 43.9375

    def has_history_of_condition(self, condition: ValueSet) -> bool:
        return bool(self.patient.conditions.find(condition))

    def has_contraindications(self) -> bool:
        return self.has_history_of_condition(
            Pancreatitis | Gallstones | MedullaryThyroidCancer
        )

    def is_self_pay_or_prior_auth(self) -> bool:
        """
        Get payment status from most recent payment questionnaire.

        Answer codes:
            Cash pay	a411
            Insurance - prior auth pending	a412
            Insurance - prior auth complete	a413
        """
        if payment_interviews := self.patient.interviews.find(
            WeightLossPaymentMethodQuestionnire
        ).filter(status='AC'):
            most_recent = max(payment_interviews, key=lambda x: x['created'])
            response = most_recent['responses'][0]['code']
            return response in ['a411', 'a413']
        return False

    def recommend_glp(self, result, rx_value_set, rx_dosage_form):
        result.add_recommendation(
            PrescribeRecommendation(
                key=rx_value_set.VALUE_SET_NAME,
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=rx_value_set,
                title=f'Start {rx_value_set.VALUE_SET_NAME}',
                context={
                    'sig_original_input': 'Inject weekly.',
                    'duration_in_days': 30,
                    'dispense_quantity': 1,
                    'dosage_form': rx_dosage_form,
                    'count_of_refills_allowed': 0,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        return result

    def in_denominator(self) -> bool:
        if not self.get_bmi():
            return False
        if self.get_bmi() <= 30:
            return False
        if self.has_contraindications():
            return False
        return self.is_self_pay_or_prior_auth()

    def in_numerator(self) -> bool:
        return self.is_on_medication(Wegovy | Mounjaro | Saxenda)

    def remainder_tasks(self, result: ProtocolResult):
        self.recommend_glp(result, WegovyRx, '0.5 mL syringe')
        self.recommend_glp(result, MounjaroRx, '0.5 mL syringe')
        self.recommend_glp(result, SaxendaRx, '3 mL syringe')
        result.add_narrative('Consider starting GLP-1 agonist.')
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Patient is already on a GLP-1 agonist for weight management.'
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol is not applicable for patients with BMI <'
                '30, not self-pay or without insurance prior auth, '
                'or with contraindications.'
            )
        )
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

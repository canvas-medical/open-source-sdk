from enum import Enum
from typing import Optional

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    STATUS_DUE,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    Diabetes,
    EndStageRenalDisease,
    HeartFailure,
    Type1Diabetes,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class Type2Diabetes(ValueSet):
    VALUE_SET_NAME = 'Type 2 Diabetes'
    ICD10CM = Diabetes.ICD10CM - Type1Diabetes.ICD10CM


class GlucoseLevelCategory(Enum):
    NORMAL = 'Normal'
    ELEVATED = 'Elevated'
    SEVERELY_ELEVATED = 'Severely Elevated'


class Metformin(ValueSet):
    """Metformin RXNORM codes.
    Source: https://mor.nlm.nih.gov/RxNav/search?searchBy=String&searchTerm=metFORMIN
    """

    VALUE_SET_NAME = 'Metformin'
    RXNORM = {
        '1372692',
        '1372706',
        '1372730',
        '1372738',
        '151827',
        '1545151',
        '1592713',
        '1664316',
        '1992686',
        '2359280',
        '2371726',
        '284743',
        '352450',
        '352764',
        '405304',
        '541766',
        '602411',
        '645109',
        '316945',
        '316946',
        '316968',
        '317541',
        '1151131',
        '1151133',
        '1151137',
        '6809',
        '1007411',
        '1008476',
        '1043562',
        '1243019',
        '1368384',
        '1486436',
        '1545149',
        '1664314',
        '1992684',
        '2117292',
        '2281864',
        '285129',
        '352381',
        '607999',
        '614348',
        '729717',
        '802646',
        '235743',
        '1043567',
        '1043574',
        '1043582',
        '1243026',
        '1243033',
        '1243040',
        '1243833',
        '1243843',
        '1243848',
        '1368391',
        '1368398',
        '1545156',
        '1545159',
        '1545163',
        '1545166',
        '1593775',
        '1593831',
        '1593833',
        '1593835',
        '1664321',
        '1664325',
        '1664328',
        '1665369',
        '1796091',
        '1796096',
        '1810999',
        '1811003',
        '1811007',
        '1811011',
        '1862688',
        '1862692',
        '1862697',
        '1862701',
        '1940498',
        '1992691',
        '1992695',
        '1992700',
        '1992703',
        '2200520',
        '2359285',
        '2359290',
        '2359353',
        '2359358',
        '2371736',
        '860977',
        '860983',
        '860998',
        '861002',
        '861006',
        '861008',
        '861012',
        '861015',
        '861018',
        '861027',
        '861733',
        '861747',
        '861752',
        '861757',
        '861762',
        '861771',
        '861785',
        '861808',
        '861818',
        '861821',
        '861824',
        '899993',
        '1043565',
        '1043572',
        '1043580',
        '1243022',
        '1243029',
        '1243036',
        '1243829',
        '1368387',
        '1368394',
        '1545152',
        '1545158',
        '1545162',
        '1545165',
        '1592722',
        '1593826',
        '1593828',
        '1593830',
        '1664317',
        '1664324',
        '1664327',
        '1665368',
        '1796095',
        '1862686',
        '1862696',
        '1940497',
        '1992687',
        '1992694',
        '1992699',
        '1992702',
        '2359281',
        '2359289',
        '2359352',
        '2359357',
        '2371735',
        '860976',
        '860982',
        '860997',
        '861001',
        '861005',
        '861011',
        '861014',
        '861017',
        '861026',
        '861732',
        '861745',
        '861750',
        '861755',
        '861761',
        '861770',
        '861784',
        '861807',
        '861817',
        '861820',
        '861823',
        '899991',
        '1043566',
        '1243037',
        '1243839',
        '1368395',
        '1545153',
        '1593774',
        '1664318',
        '1796090',
        '1810998',
        '1862687',
        '1992688',
        '2200519',
        '2359282',
        '2371728',
        '368254',
        '406257',
        '541768',
        '647241',
        '731442',
        '757603',
        '802051',
        '806287',
        '849585',
        '861756',
        '899992',
        '1167810',
        '1167811',
        '1169920',
        '1169923',
        '1171244',
        '1171245',
        '1171248',
        '1171249',
        '1171254',
        '1171255',
        '1172629',
        '1172630',
        '1172860',
        '1172861',
        '1175016',
        '1175021',
        '1185049',
        '1185325',
        '1185326',
        '1185624',
        '1243038',
        '1243039',
        '1368396',
        '1368397',
        '1545154',
        '1545155',
        '1592716',
        '1592717',
        '1664319',
        '1664320',
        '1992689',
        '1992690',
        '2359283',
        '2359284',
        '2371729',
        '2371730',
        '1043563',
        '1043570',
        '1043578',
        '1243020',
        '1243027',
        '1243034',
        '1243827',
        '1243842',
        '1243846',
        '1368385',
        '1368392',
        '1545150',
        '1545157',
        '1545161',
        '1545164',
        '1593058',
        '1593068',
        '1593070',
        '1593072',
        '1664315',
        '1664323',
        '1664326',
        '1665367',
        '1796089',
        '1796094',
        '1807888',
        '1807894',
        '1807915',
        '1807917',
        '1810997',
        '1811002',
        '1811006',
        '1811010',
        '1862685',
        '1862691',
        '1862695',
        '1862700',
        '1940496',
        '1992685',
        '1992693',
        '1992698',
        '1992701',
        '2200518',
        '2359279',
        '2359288',
        '2359351',
        '2359356',
        '2371734',
        '860975',
        '860981',
        '860999',
        '861004',
        '861007',
        '861010',
        '861021',
        '861025',
        '861731',
        '861736',
        '861740',
        '861743',
        '861748',
        '861753',
        '861760',
        '861763',
        '861769',
        '861783',
        '861787',
        '861790',
        '861795',
        '861806',
        '861816',
        '861819',
        '861822',
        '899989',
        '860974',
        '860980',
        '860995',
        '861009',
        '861020',
        '861024',
        '861730',
        '1043561',
        '1243018',
        '1243826',
        '1368383',
        '1545148',
        '1593057',
        '1664313',
        '1796088',
        '1810996',
        '1862684',
        '1992683',
        '2200517',
        '2359278',
        '2371724',
        '372803',
        '372804',
        '374635',
        '378729',
        '378730',
        '406082',
        '577093',
        '700516',
        '802742',
        '899988',
        '1156197',
        '1161597',
        '1161598',
        '1161599',
        '1161600',
        '1161603',
        '1161604',
        '1161605',
        '1161606',
        '1161607',
        '1161608',
        '1161609',
        '1161610',
        '1161611',
        '1165205',
        '1165206',
        '1165845',
        '1243016',
        '1243017',
        '1368381',
        '1368382',
        '1545146',
        '1545147',
        '1592709',
        '1592710',
        '1664311',
        '1664312',
        '1992681',
        '1992682',
        '2359276',
        '2359277',
        '2371722',
        '2371723',
    }


class Dulaglutide(ValueSet):
    VALUE_SET_NAME = 'Dulaglutide'
    RXNORM = {
        '1551295',
        '1551300',
        '1551304',
        '1551306',
        '2395777',
        '2395779',
        '2395783',
        '2395785',
    }


class Liraglutide(ValueSet):
    VALUE_SET_NAME = 'Liraglutide'
    RXNORM = {
        '1598268',
        '1860167',
        '1860172',
        '897122',
        '897126',
    }


class Semaglutide(ValueSet):
    VALUE_SET_NAME = 'Semaglutide'
    RXNORM = {
        '1991306',
        '1991311',
        '1991316',
        '1991317',
        '2200644',
        '2200650',
        '2200652',
        '2200654',
        '2200656',
        '2200658',
        '2398841',
        '2398842',
        '2553501',
        '2553506',
        '2553601',
        '2553603',
        '2553802',
        '2553803',
        '2553901',
        '2553903',
        '2554102',
        '2554104',
        '2599362',
        '2599365',
        '2619152',
        '2619154',
    }


class Canagliflozin(ValueSet):
    VALUE_SET_NAME = 'Canagliflozin'
    RXNORM = {
        '1373463',
        '1373469',
        '1373471',
        '1373473',
        '1545150',
        '1545156',
        '1545157',
        '1545159',
        '1545161',
        '1545163',
        '1545164',
        '1545166',
        '1810997',
        '1810999',
        '1811002',
        '1811003',
        '1811006',
        '1811007',
        '1811010',
        '1811011',
    }


class Empaglifozin(ValueSet):
    VALUE_SET_NAME = 'Empaglifozin'
    RXNORM = {
        '1545658',
        '1545664',
        '1545666',
        '1545668',
        '1602109',
        '1602115',
        '1602118',
        '1602120',
        '1664315',
        '1664321',
        '1664323',
        '1664325',
        '1664326',
        '1664328',
        '1665367',
        '1665369',
        '1862685',
        '1862688',
        '1862691',
        '1862692',
        '1862695',
        '1862697',
        '1862700',
        '1862701',
        '2359279',
        '2359285',
        '2359288',
        '2359290',
        '2359351',
        '2359353',
        '2359356',
        '2359358',
    }


class Dapagliflozin(ValueSet):
    VALUE_SET_NAME = 'Dapagliflozin'
    RXNORM = {
        '1486977',
        '1486981',
        '1488569',
        '1488574',
        '1593058',
        '1593068',
        '1593070',
        '1593072',
        '1593775',
        '1593831',
        '1593833',
        '1593835',
        '1925498',
        '1925504',
        '1940496',
        '1940498',
        '2169274',
        '2169276',
        '2371734',
        '2371736',
    }


class Tirzepatide(ValueSet):
    VALUE_SET_NAME = 'Tirzepatide'
    RXNORM = {
        '2601761',
        '1601743',
        '2601784',
        '2601767',
        '2601773',
        '2601755',
    }


# Value sets for prescription


class DulaglutideRx(ValueSet):
    VALUE_SET_NAME = 'Dulaglutide'
    FDB = {'582681'}


class LiraglutideRx(ValueSet):
    VALUE_SET_NAME = 'Liraglutide'
    FDB = {'560349'}


class SemaglutideRx(ValueSet):
    VALUE_SET_NAME = 'Semaglutide'
    FDB = {'595028'}


class CanaglifozinRx(ValueSet):
    VALUE_SET_NAME = 'Canagliflozin'
    FDB = {'577707'}


class EmpaglifozinRx(ValueSet):
    VALUE_SET_NAME = 'Empaglifozin'
    FDB = {'582251'}


class DapagliflozinRx(ValueSet):
    VALUE_SET_NAME = 'Dapagliflozin'
    FDB = {'580680'}


class TirzepatideRx(ValueSet):
    VALUE_SET_NAME = 'Tirzepatide'
    FDB = {'611097'}


class MetforminRx(ValueSet):
    VALUE_SET_NAME = 'Metformin'
    FDB = {'467971'}


GLP1Medications = Dulaglutide | Liraglutide | Semaglutide | Tirzepatide

SGLT2Medications = Empaglifozin | Canagliflozin | Dapagliflozin

GlucoseLoweringTherapy = GLP1Medications | SGLT2Medications | Metformin


class ChronicKidneyDiseaseStage3Onwards(ValueSet):
    VALUE_SET_NAME = 'Chronic Kidney Disease Stage 3 Onwards'
    ICD10CM = {'N1830', 'N1831', 'N1832', 'N184', 'N185'}


class EndStageHeartFailure(ValueSet):
    VALUE_SET_NAME = 'End stage heart failure'
    ICD10CM = {'I5084'}


class MetastaticMalignancy(ValueSet):
    ICD10CM = {
        'C77.0',  #  lymph nodes of head, face and neck
        'C77.1',  #  intrathoracic lymph nodes
        'C77.2',  #  intra-abdominal lymph nodes
        'C77.3',  #  axilla and upper limb lymph nodes
        'C77.4',  #  inguinal and lower limb lymph nodes
        'C77.5',  #  intrapelvic lymph nodes
        'C77.8',  #  lymph nodes of multiple regions
        'C77.9',  #  lymph node, unspecified
        'C78.00',  #  unspecified lung
        'C78.01',  #  right lung
        'C78.02',  #  left lung
        'C78.1',  #  mediastinum
        'C78.2',  #  pleura
        'C78.30',  #  unspecified respiratory organ
        'C78.39',  #  other respiratory organs
        'C78.4',  #  small intestine
        'C78.5',  #  large intestine and rectum
        'C78.6',  #  retroperitoneum and peritoneum
        'C78.7',  #  liver and intrahepatic bile duct
        'C78.80',  #  unspecified digestive organ
        'C78.89',  #  other digestive organs
        'C79.00',  #  unspecified kidney and renal pelvis
        'C79.01',  #  right kidney and renal pelvis
        'C79.02',  #  left kidney and renal pelvis
        'C79.10',  #  unspecified urinary organs
        'C79.11',  #  bladder
        'C79.19',  #  other urinary organs
        'C79.2',  #  skin
        'C79.31',  #  brain
        'C79.32',  #  cerebral meninges
        'C79.40',  #  unspecified part of nervous system
        'C79.49',  #  other parts of nervous system
        'C79.51',  #  bone
        'C79.52',  #  bone marrow
        'C79.60',  #  unspecified ovary
        'C79.61',  #  right ovary
        'C79.62',  #  left ovary
        'C79.63',  #  bilateral ovaries
        'C79.70',  #  unspecified adrenal gland
        'C79.71',  #  right adrenal gland
        'C79.72',  #  left adrenal gland
        'C79.81',  #  breast
        'C79.82',  #  genital organs
        'C79.89',  #  other specified sites
        'C79.9',  #  unspecified site'
    }


# Add to this value set as needed
LimitedLifeExpectancy = (
    EndStageHeartFailure | MetastaticMalignancy | EndStageRenalDisease
)


class DiabeticInitialGlucoseLoweringTherapy(ClinicalQualityMeasure):
    class Meta:
        title = 'Initial medications for diabetes'
        description = (
            'This protocol outlines the initial glucose-lowering '
            'therapy for patients with type 2 diabetes. The '
            'treatment algorithm is based on the patient\'s A1c '
            'level, presence of renal or heart failure, ASCVD '
            'risk, and BMI. The protocol recommends different '
            'therapies such as SGLT-2 inhibitors, GLP-1 receptor '
            'agonists, and metformin, depending on the patient\'s '
            'specific conditions and needs.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.VITAL_SIGN,
        ]

        references = ['Standards of Care in Diabetes (2023)']

    def in_denominator(self) -> bool:
        """Patients with type 2 diabetes."""
        return bool(
            self.patient.conditions.find(Type2Diabetes).filter(
                clinicalStatus='active'
            )
        )

    def in_numerator(self) -> bool:
        """Patients who are already on a glucose-lowering therapy."""
        return bool(
            self.patient.medications.find(GlucoseLoweringTherapy).filter(
                status='active'
            )
        )

    def has_chronic_kidney_disease(self) -> bool:
        return bool(
            self.patient.conditions.find(
                ChronicKidneyDiseaseStage3Onwards
            ).filter(clinicalStatus='active')
        )

    def has_heart_failure(self) -> bool:
        return bool(
            self.patient.conditions.find(HeartFailure).filter(
                clinicalStatus='active'
            )
        )

    def has_reduced_life_expectancy(self) -> bool:
        return (
            bool(
                self.patient.conditions.find(LimitedLifeExpectancy).filter(
                    clinicalStatus='active'
                )
            )
            or self.patient.age >= 80
        )

    def last_a1c(self):
        if a1c_tests := self.patient.lab_reports.find(Hba1CLaboratoryTest):
            return float(a1c_tests.last_value())
        return None

    def a1c_elevation(self) -> Optional[GlucoseLevelCategory]:
        """Return the glucose level category based on the patient's A1c.
        For patients with reduced life expectancy, the thresholds are
        higher.
        """
        if not self.last_a1c():
            return None
        if self.has_reduced_life_expectancy():
            if self.last_a1c() >= 10:
                return GlucoseLevelCategory.SEVERELY_ELEVATED
            elif self.last_a1c() >= 8.0:
                return GlucoseLevelCategory.ELEVATED
            else:
                return GlucoseLevelCategory.NORMAL
        elif self.last_a1c() >= 9.0:
            return GlucoseLevelCategory.SEVERELY_ELEVATED
        elif self.last_a1c() >= 7.0:
            return GlucoseLevelCategory.ELEVATED
        else:
            return GlucoseLevelCategory.NORMAL

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

    def get_ascvd_risk(self) -> Optional[float]:
        # Insert preferred ASCVD risk score method
        return 0

    def recommend_metformin(self, result):
        result.add_recommendation(
            PrescribeRecommendation(
                key='metformin',
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=MetforminRx,
                title='Start metformin',
                context={
                    'sig_original_input': (
                        'Take one daily for 1 week, '
                        'two daily for 1 week, '
                        'then two twice a day, as tolerated.'
                    ),
                    'duration_in_days': 30,
                    'dispense_quantity': 90,
                    'dosage_form': 'tablet',
                    'count_of_refills_allowed': 3,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        return result

    def recommend_sglt2(self, result):
        result.add_recommendation(
            PrescribeRecommendation(
                key='Canaglifozin',
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=CanaglifozinRx,
                title='Start canagliflozin',
                context={
                    'sig_original_input': 'Take 1 daily',
                    'duration_in_days': 30,
                    'dispense_quantity': 30,
                    'dosage_form': 'tablet',
                    'count_of_refills_allowed': 3,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        return result

    def recommend_glp1(self, result):
        result.add_recommendation(
            PrescribeRecommendation(
                key='semaglutide',
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=SemaglutideRx,
                title='Start semaglutide',
                context={
                    'sig_original_input': 'Inject weekly.',
                    'duration_in_days': 30,
                    'dispense_quantity': 1,
                    'dosage_form': '1.5 mL syringe',
                    'count_of_refills_allowed': 0,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        return result

    def remainder_tasks(self, result: ProtocolResult):
        result.status = STATUS_DUE

        if self.a1c_elevation() == GlucoseLevelCategory.ELEVATED:
            if self.has_chronic_kidney_disease() or self.has_heart_failure():
                self.recommend_sglt2(result)
                result.add_narrative(
                    (
                        'Consider SGLT-2 in patients with '
                        'heart failure or chronic kidney disease.'
                    )
                )
            elif self.get_ascvd_risk() > 0.15:
                self.recommend_glp1(result)
                self.recommend_sglt2(result)
                result.add_narrative(
                    'Based on ASCVD risk, consider either GLP-1 or SGLT-2.'
                )
            elif self.get_bmi() and self.get_bmi() >= 27:
                self.recommend_glp1(result)
                result.add_narrative('Based on BMI, consider GLP-1.')
            else:
                self.recommend_metformin(result)
                result.add_narrative(
                    (
                        'In the absence of indications '
                        'for GLP-1 or SGLT-2, metformin is a reasonable option.'
                    )
                )

        elif self.a1c_elevation() == GlucoseLevelCategory.SEVERELY_ELEVATED:
            if self.get_ascvd_risk() > 0.15 or (
                self.get_bmi()
                and self.get_bmi() >= 27
                and (
                    self.has_heart_failure()
                    or self.has_chronic_kidney_disease()
                )
            ):
                self.recommend_glp1(result)
                self.recommend_sglt2(result)
                result.add_narrative(
                    (
                        'Consider starting both a GLP1 and SGLT-2 in '
                        'patients with severely elevated hemoglobin A1c '
                        'with elevated ASCVD risk score and '
                        'heart failure or CKD.'
                    )
                )
            elif self.has_heart_failure() or self.has_chronic_kidney_disease():
                self.recommend_metformin(result)
                self.recommend_sglt2(result)
                result.add_narrative(
                    (
                        'Consider starting both metformin and SGLT-2 in '
                        'patients with severely elevated hemoglobin A1c '
                        'with heart failure or CKD.'
                    )
                )
            else:
                self.recommend_metformin(result)
                self.recommend_glp1(result)
                result.add_narrative(
                    (
                        'Consider starting both metformin and GLP-1 in '
                        'patients with severely elevated hemoglobin A1c '
                        'without other indications for SGLT-2.'
                    )
                )
        else:
            self.recommend_metformin(result)
            result.add_narrative(
                (
                    'In the absence of indications '
                    'for GLP-1 or SGLT-2, metformin is a reasonable option.'
                )
            )

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient with type 2 diabetes is already on a '
                'glucose-lowering therapy.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Protocol is not applicable for patients without type 2 diabetes.'
        )
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self):
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

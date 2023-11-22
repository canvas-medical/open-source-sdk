from enum import Enum
from typing import Optional

from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.recommendation import (
    PrescribeRecommendation,
    Recommendation,
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import (
    ChronicKidneyDiseaseStage5,
    Diabetes,
    EndStageRenalDisease,
    HeartFailure,
    Type1Diabetes,
)
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class GlucoseLevelCategory(Enum):
    NORMAL = 'Normal'
    ELEVATED = 'Elevated'
    SEVERELY_ELEVATED = 'Severely Elevated'


# Drug value sets
class Insulin(ValueSet):
    """
    OID: 2.16.840.1.113762.1.4.1078.434
    Clinical Focus: This value set intends to capture generic \
        and brand codes for all Insulins
    Data Element Scope:	DRUG_CLASS_MEMBERS: PHARMACOLOGIC:
    Inclusion Criteria:	All generics (with different strengths) , \
        brands (with different strengths) for Insulin
    Exclusion Criteria:	None
    """

    VALUE_SET_NAME = 'Insulin'
    RXNORM = {
        '1007184',
        '1008501',
        '106892',
        '1157459',
        '1157460',
        '1157461',
        '1157462',
        '1157463',
        '1157464',
        '1160696',
        '1164824',
        '1167934',
        '1168563',
        '1171289',
        '1171291',
        '1171997',
        '1172691',
        '1172692',
        '1175624',
        '1178119',
        '1178120',
        '1178125',
        '1178127',
        '1178128',
        '135805',
        '1372723',
        '1372741',
        '1372744',
        '139825',
        '1543200',
        '1543202',
        '1543203',
        '1543206',
        '1543207',
        '1544488',
        '1544490',
        '1604538',
        '1604539',
        '1604540',
        '1604541',
        '1604543',
        '1604544',
        '1605101',
        '1650256',
        '1650260',
        '1650262',
        '1650264',
        '1651313',
        '1651315',
        '1652237',
        '1652238',
        '1652239',
        '1652240',
        '1652241',
        '1652242',
        '1652639',
        '1652640',
        '1652643',
        '1652644',
        '1652645',
        '1652646',
        '1653104',
        '1653106',
        '1653195',
        '1653196',
        '1653197',
        '1653198',
        '1653201',
        '1653202',
        '1653203',
        '1653204',
        '1653207',
        '1653209',
        '1653497',
        '1653499',
        '1653506',
        '1653897',
        '1653899',
        '1654190',
        '1654192',
        '1654651',
        '1654855',
        '1654861',
        '1654862',
        '1654863',
        '1654909',
        '1654910',
        '1654911',
        '1654912',
        '1670007',
        '1670008',
        '1670009',
        '1670010',
        '1670011',
        '1670012',
        '1670013',
        '1670014',
        '1670015',
        '1670016',
        '1670020',
        '1670021',
        '1670022',
        '1670023',
        '1727493',
        '1731314',
        '1731315',
        '1731316',
        '1731317',
        '1736859',
        '1736860',
        '1736861',
        '1736862',
        '1736863',
        '1798387',
        '1798388',
        '1858992',
        '1858993',
        '1858994',
        '1858995',
        '1858996',
        '1858997',
        '1858998',
        '1858999',
        '1859000',
        '1860165',
        '1860166',
        '1860167',
        '1860168',
        '1860169',
        '1860170',
        '1860171',
        '1860172',
        '1862101',
        '1862102',
        '1926331',
        '1926332',
        '1986350',
        '1986351',
        '1986352',
        '1986353',
        '1986354',
        '1986355',
        '1986356',
        '1992165',
        '1992166',
        '1992167',
        '1992168',
        '1992169',
        '1992170',
        '1992171',
        '2002419',
        '2002420',
        '2049379',
        '2049380',
        '2100028',
        '2100029',
        '2107519',
        '2107520',
        '2107521',
        '2107522',
        '2108525',
        '2108527',
        '213442',
        '2179742',
        '2179743',
        '2179744',
        '2179745',
        '2179746',
        '2179747',
        '2179748',
        '2179749',
        '2205453',
        '2205454',
        '2206090',
        '2206091',
        '2206092',
        '2206098',
        '2206099',
        '2268064',
        '2268065',
        '2376838',
        '2377130',
        '2377131',
        '2377132',
        '2377133',
        '2377134',
        '2377230',
        '2377231',
        '2380230',
        '2380231',
        '2380232',
        '2380233',
        '2380234',
        '2380235',
        '2380236',
        '2380240',
        '2380253',
        '2380254',
        '2380255',
        '2380256',
        '2380259',
        '2380260',
        '2380267',
        '2380268',
        '242120',
        '249220',
        '253181',
        '253182',
        '2563969',
        '2563970',
        '2563971',
        '2563972',
        '2563973',
        '2563976',
        '2563977',
        '2589006',
        '2589007',
        '2589008',
        '2589010',
        '2589011',
        '2589012',
        '2589013',
        '2589014',
        '259111',
        '260265',
        '261542',
        '261551',
        '2621571',
        '2621572',
        '274783',
        '284810',
        '285018',
        '311026',
        '311027',
        '311028',
        '311033',
        '311034',
        '311036',
        '311040',
        '311041',
        '311048',
        '340325',
        '340327',
        '343076',
        '343079',
        '343083',
        '343101',
        '343211',
        '343226',
        '343263',
        '343663',
        '351297',
        '351859',
        '351926',
        '360342',
        '362585',
        '362622',
        '363221',
        '363534',
        '365573',
        '365672',
        '365677',
        '365679',
        '376915',
        '378841',
        '378857',
        '378864',
        '378914',
        '378928',
        '378966',
        '379056',
        '400008',
        '400560',
        '484320',
        '484321',
        '484322',
        '485208',
        '485209',
        '485210',
        '51428',
        '573330',
        '573331',
        '575068',
        '575141',
        '575142',
        '575146',
        '575148',
        '575151',
        '575628',
        '575679',
        '607583',
        '616236',
        '616237',
        '616238',
        '731277',
        '731280',
        '731281',
        '752386',
        '752388',
        '803192',
        '803193',
        '803194',
        '816726',
        '847187',
        '847189',
        '847191',
        '847199',
        '847211',
        '847213',
        '847230',
        '847232',
        '847239',
        '847241',
        '847252',
        '847254',
        '847259',
        '847261',
        '86009',
        '865097',
        '865098',
        '92880',
        '92881',
        '93558',
        '93560',
        '977838',
        '977840',
        '977841',
        '977842',
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


GLP1Medications = Dulaglutide | Liraglutide | Semaglutide | Tirzepatide

SGLT2Medications = Empaglifozin | Canagliflozin | Dapagliflozin

# Condition value sets


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


class Type2Diabetes(ValueSet):
    VALUE_SET_NAME = 'Type 2 Diabetes'
    ICD10CM = Diabetes.ICD10CM - Type1Diabetes.ICD10CM


class DiabeticAdjustingTherapy(ClinicalQualityMeasure):
    class Meta:
        title = 'Adjusting Glucose Lowering Therapy in Type 2 Diabetes'
        description = (
            'This protocol outlines the adjustment of glucose-lowering '
            'therapy in patients with type 2 diabetes. It recommends '
            'starting or switching to a GLP-1 for patients with a BMI > 27'
            'who are not already on a GLP-1. For '
            'patients with heart failure or chronic kidney disease, '
            'it recommends starting or switching to an SGLT-2. '
            'The protocol also advises titrating therapy to the '
            'maximum tolerable dose before adding additional therapy.'
            'For persistently elevated fasting blood glucose '
            'levels or A1c, the addition of basal insulin is suggested.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.CONDITION,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

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
        """
        Return the glucose level category based on the patient's A1c.
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

    def on_glp1(self) -> bool:
        return bool(
            self.patient.medications.find(GLP1Medications).filter(
                status='active'
            )
        )

    def on_sglt2(self) -> bool:
        return bool(
            self.patient.medications.find(SGLT2Medications).filter(
                status='active'
            )
        )

    def on_max_dose_therapy(self) -> bool:
        """Patients on therapy at max dose."""
        # TODO treatment logic
        return False

    def on_insulin(self) -> bool:
        """
        Patients who have had basal insulin added to therapy based on A1c/FBG.
        """
        # TODO treatment logic
        return False

    def has_t2diabetes(self) -> bool:
        return bool(
            self.patient.conditions.find(Type2Diabetes).filter(
                clinicalStatus='active'
            )
        )

    def is_on_treatment(self) -> bool:
        # TODO treatment logic
        return False

    def in_denominator(self) -> bool:
        """Patients who have type 2 diabetes and are on some kind of therapy."""
        return bool(self.has_diabetes() and self.is_on_treatment())

    def in_numerator(self) -> bool:
        """Patients who have:
        - BMI > 27 and is not already on a GLP-1/SGLT-2
        - Patients on therapy at max dose
        - Have had basal insulin added to therapy based on A1c/FBG
        """
        return bool(
            ((self.on_glp1() or self.on_sglt2()) and self.get_bmi() > 27)
            or self.on_max_dose_therapy()
            or self.on_insulin()
        )

    def remainder_tasks(self, result: ProtocolResult):
        # If patient has BMI > 27 and is not already on a GLP-1,
        # recommend starting or switching to a GLP-1.
        if self.get_bmi() > 27 and not self.on_glp1():
            result.add_recommendation(
                PrescribeRecommendation(
                    key='RECOMMEND_START_GLP1',
                    patient=self.patient,
                    prescription=GLP1Medications,
                )
            )
            result.add_narrative(
                (
                    'Patient has BMI > 27 and is not already on a GLP-1, '
                    'recommending starting or switching to a GLP-1.'
                )
            )
        # If patient has heart failure or chronic kidney disease and is not
        # already on a SGLT-2, recommend starting or switching to an SGLT-2.
        if (
            self.patient.has_condition(HeartFailure)
            or self.patient.has_condition(ChronicKidneyDiseaseStage5)
        ) and not self.on_sglt2():
            result.add_recommendation(
                PrescribeRecommendation(
                    key='RECOMMEND_START_SGLT2',
                    patient=self.patient,
                    prescription=SGLT2Medications,
                )
            )
            result.add_narrative(
                (
                    'Patient has heart failure or chronic kidney disease '
                    'and is not already on a SGLT-2, recommending starting '
                    'or switching to an SGLT-2.'
                )
            )
        # If A1c elevated according to previous descriptions, generic
        # recommendation for increasing doses / additional agents.
        if self.a1c_elevation() != GlucoseLevelCategory.NORMAL:
            result.add_recommendation(
                Recommendation(
                    key='RECOMMEND_INCREASE_DOSE',
                    patient=self.patient,
                    title='Increase dose / add additional agents',  # TODO: Add context
                )
            )
            result.add_narrative(
                (
                    'A1c is elevated, recommending increasing doses / '
                    'additional agents.'
                )
            )
        # TODO: What happens otherwise?
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient\'s glucose-lowering therapy has been adjusted '
                'according to protocol.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol is not applicable for patients without type '
                '2 diabetes or who are not already on some kind of therapy.'
            )
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

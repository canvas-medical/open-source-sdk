import arrow
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
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import Diabetes


class GlucagonUseInstruction(ValueSet):
    """Instructions for use of glucagon in hypoglycaemia"""

    VALUE_SET_NAME = 'Advice given about use of glucagon in hypoglycaemia'
    SNOMEDCT = {'196521000000105'}


class GlucagonRx(ValueSet):
    VALUE_SET_NAME = 'Glucagon'
    FDB = {'600811'}


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


class Sulfonylureas(ValueSet):
    VALUE_SET_NAME = 'Sulfonylureas'
    RXNORM = {
        '19773',
        '88140',
        '86175',
        '31053',
        '88141',
        '73146',
        '15359',
        '64723',
        '73145',
        '19924',
        '15384',
        '136149',
        '19749',
        '31510',
        '86556',
        '31400',
        '86557',
        '31048',
        '20583',
        '86173',
        '86174',
        '31049',
        '20582',
        '19829',
    }


class Glinides(ValueSet):
    VALUE_SET_NAME = 'Glinides'
    RXNORM = {
        '31191',
        '28453',
        '31414',
        '28452',
        '86178',
        '86179',
        '21321',
        '20025',
    }


class Glucagon(ValueSet):
    VALUE_SET_NAME = 'Glucagon'
    RXNORM = {
        '151823',
        '2180667',
        '2199300',
        '1649570',
        '1649574',
        '1739329',
        '721656',
        '1151126',
        '1151130',
        '4832',
        '253170',
        '261716',
        '153095',
        '2180671',
        '2199304',
        '2199308',
        '2199312',
        '2199316',
        '2587361',
        '1865730',
        '2180668',
        '2199301',
        '1653348',
        '2180669',
        '2199302',
        '2199311',
        '2587360',
        '1171240',
        '2180670',
        '2199303',
        '2180666',
        '2199299',
        '2199307',
        '2199310',
        '2199315',
        '2587358',
        '310497',
        '1865728',
        '2180663',
        '2199297',
        '1653345',
        '2180665',
        '2199298',
        '2199309',
        '1165209',
        '2180664',
    }


class Hypoglycemia(ValueSet):
    """List of ICD-10-CM codes for Hypoglycemia"""

    VALUE_SET_NAME = 'Hypoglycemia'
    ICD10CM = {
        'E16.1',  # Other hypoglycemia
        'E16.2',  # Hypoglycemia, unspecified
    }


class CognitiveImpairment(ValueSet):
    """List of ICD-10-CM codes for Cognitive Impairment
    Source:
    https://www.medrxiv.org/content/medrxiv/early/2022/02/17/
    2022.02.16.22271085/DC1/embed/media-1.pdf?download=true
    """

    VALUE_SET_NAME = 'Cognitive Impairment'
    ICD10CM = {
        'F04',
        'F1026',
        'F1027',
        'F1096',
        'F1097',
        'F1326',
        'F1327',
        'F1396',
        'F1397',
        'F0150',
        'F0151',
        'F0152',
        'F015',
        'A8100',
        'E710',
        'E752',
        'E7523',
        'E7529',
        'F1827',
        'F1897',
        'G10',
        'G20',
        'G300',
        'G3185',
        'G231',
        'G3',
        'G310',
        'G318',
        'G31',
        'F039',
        'F03A',
        'F03B',
        'F03C',
    }


class GlucoseLab(ValueSet):
    """List of ICD-10-CM codes for Hypoglycemia"""

    VALUE_SET_NAME = 'Glucose labs'
    LOINC = {
        '2349-9',
        '1558-6',
    }


class HypoglycemiaRiskReduction(ClinicalQualityMeasure):
    class Meta:
        title = 'Hypoglycemia risk reduction'
        description = (
            'This protocol recommends prescribing glucagon and providing '
            'instructions on its use for any patient with diabetes on '
            'insulin, sulfonylureas or glinides with two or more episodes '
            'of hypoglycemia (<70 mg/dL) per week or impaired cognitive '
            'function. Glucagon is used to acutely raise blood glucose '
            'in a hypoglycemic emergency.'
        )
        version = '1.0.6'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.LAB_REPORT,
        ]
        references = ['Standards of Care in Diabetes (2023)']

    def has_diabetes(self) -> bool:
        return self.patient.conditions.find(Diabetes).filter(
            clinicalStatus='active'
        )

    def has_hypoglycemia(self) -> bool:
        if self.patient.conditions.find(Hypoglycemia).filter(
            clinicalStatus='active'
        ):
            return True
        return any(
            (
                float(glucose['value']) < 70.0
                for glucose in self.patient.lab_reports.find(GlucoseLab).after(
                    arrow.now().shift(months=-3)
                )
            )
        )

    def has_impaired_cognitive_function(self) -> bool:
        return self.patient.conditions.find(CognitiveImpairment).filter(
            clinicalStatus='active'
        )

    def on_insulin(self) -> bool:
        return self.patient.medications.find(Insulin).filter(status='active')

    def on_sulfonylureas(self) -> bool:
        return self.patient.medications.find(Sulfonylureas).filter(
            status='active'
        )

    def on_glinides(self) -> bool:
        return self.patient.medications.find(Glinides).filter(status='active')

    def in_denominator(self) -> bool:
        """
        Patient has diabetes and is on insulin, sulfonylureas or glinides
        or has hypoglycemia or impaired cognitive function
        """
        if not self.has_diabetes():
            return False
        return (
            False
            if not self.on_insulin()
            and not self.on_sulfonylureas()
            and not self.on_glinides()
            else self.has_hypoglycemia()
            or self.has_impaired_cognitive_function()
        )

    def in_numerator(self) -> bool:
        """Patient already prescribed glucagon"""
        return bool(
            self.patient.prescriptions.find(Glucagon).filter(status='active')
        )

    def remainder_tasks(self, result: ProtocolResult):
        result.add_recommendation(
            PrescribeRecommendation(
                key='RECOMMENDATION_PRESCRIBE_GLUCAGON',
                rank=1,
                button='Prescribe',
                patient=self.patient,
                prescription=GlucagonRx,
                title='Prescribe glucagon',
                context={
                    'sig_original_input': 'Take one daily',
                    'duration_in_days': 90,
                    'dispense_quantity': 1,
                    'dosage_form': '0.2 mL syringe',
                    'count_of_refills_allowed': 3,
                    'generic_substitutions_allowed': True,
                    'note_to_pharmacist': '',
                },
            )
        )
        result.add_narrative(
            (
                'Glucagon is recommended for patients on insulin '
                'sulfonylureas or glinides with episodes of hypoglycemia or '
                'impaired cognitive function.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Patient with diabetes on insulin and/or '
                'sulfonylureas/glinides who has a history of ER visits '
                'or hospitalization for hypoglycemia, two or more '
                'episodes of hypoglycemia (<70 mg/dL) per week, any '
                'history of severe level 3 hypoglycemia, concerns '
                'about hypoglycemic unawareness, or impaired cognitive '
                'function is already prescribed glucagon.'
            )
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol is not applicable for patients without '
                'diabetes or not on insulin and/or sulfonylureas/glinides.'
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

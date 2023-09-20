from datetime import timedelta
from typing import Optional

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
    InstructionRecommendation,
    LabRecommendation,
    PrescribeRecommendation,
)
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021.diagnosis import Diabetes
from canvas_workflow_kit.value_set.v2021.lab_test import Hba1CLaboratoryTest


class LifestyleChangeReDietInstruction(ValueSet):
    VALUE_SET_NAME = 'Lifestyle Change Recommendation Re: Diet'
    SNOMEDCT = {'443288003'}


class GestationalDiabetes(ValueSet):
    VALUE_SET_NAME = 'Gestational Diabetes'
    ICD10CM = {'O244'}


class FastingGlucoseLaboratoryTest(ValueSet):
    """Fasting glucose LOINC codes.

    Reference: https://loinc.org/search/?s=fasting%20glucose&t=1&o=%20&f%5B
    Status%5D%5B%5D=%3Dstatus%3AACTIVE&f%5BClassType%5D%5B%5D=%3Dclasstype%3ALab
    """

    VALUE_SET_NAME = 'Fasting Glucose Laboratory Test'
    LOINC = {
        '95102-0',  # Glucose post fasting and meal stimulation panel
        '63382-6',  # Glucose^post CFst
        '16913-6',  # Glucose^post CFst
        '53114-5',  # Glucose^post CFst
        '76629-5',  # Glucose^post CFst
        '1555-2',  # Glucose^post 12H CFst
        '1557-8',  # Glucose^post CFst
        '6764-5',  # Glucose^post CFst
        '101476-0',  # Glucose^post CFst
        '14771-0',  # Glucose^post CFst
        '10450-5',  # Glucose^post 10H CFst
        '1554-5',  # Glucose^post 12H CFst
        '17865-7',  # Glucose^post 8H CFst
        '1556-0',  # Glucose^post CFst
        '41604-0',  # Glucose^post CFst
        '1558-6',  # Glucose^post CFst
        '14770-2',  # Glucose^post CFst
        '1493-6',  # Glucose^1.5H post 0.05-0.15 U insulin/kg IV post 12H CFst
        '77145-1',  # Glucose^post CFst
        '1550-3',  # Glucose^pre 12H CFst
        '14769-4',  # Glucose^pre 12H CFst
        '1523-0',  # Glucose^30M post 0.05-0.15 U insulin/kg IV post 12H CFst
        '1500-8',  # Glucose^1H post 0.05-0.15 U insulin/kg IV post 12H CFst
    }


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


class MetforminRx(ValueSet):
    VALUE_SET_NAME = 'Metformin'
    FDB = {'467971'}


class PrediabetesManagement(ClinicalQualityMeasure):
    class Meta:
        title = 'Prediabetes Management'
        description = (
            'This protocol outlines the management of patients '
            'who screen positive for prediabetes (A1c between 5.7'
            'and 6.4). It recommends lifestyle changes and a '
            'follow-up A1c test in 6 months. Exceptions include '
            'patients with a BMI over 35, a history of gestational '
            'diabetes, fasting glucose of 110 mg/dL or higher, '
            'or A1c over 6%, who should be offered metformin immediately .'
            'If lifestyle changes have been previously recommended '
            'and the A1c remains in the prediabetic range after '
            '6 months, metformin should be started.'
        )
        version = '1.0.1'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.LAB_REPORT,
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.VITAL_SIGN,
            CHANGE_TYPE.INSTRUCTION,
        ]
        references = [
            'Standards of Care in Diabetes (2023), https://doi.org/10.2337/dc23-Srev'
        ]

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
                    'sig_original_input': 'Take one daily for 1 week, '
                    'two daily for 1 week, '
                    'then two twice a day, as tolerated.',
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

    def last_a1c_level(self) -> Optional[float]:
        last_a1c = self.patient.lab_reports.find(
            Hba1CLaboratoryTest
        ).last_value()
        return float(last_a1c) if last_a1c else None

    def last_a1c_date(self) -> Optional[arrow.Arrow]:
        last_a1c = self.patient.lab_reports.find(Hba1CLaboratoryTest).last()
        return arrow.get(last_a1c['originalDate']) if last_a1c else None

    def bmi(self) -> Optional[float]:
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

    def has_gestational_diabetes_history(self) -> bool:
        return bool(self.patient.conditions.find(GestationalDiabetes))

    def last_fasting_glucose_value(self) -> Optional[float]:
        glucose_tests = self.patient.lab_reports.find(
            FastingGlucoseLaboratoryTest
        )
        return float(glucose_tests.last_value()) if glucose_tests else None

    def last_lifestyle_instructions_date(self) -> Optional[arrow.Arrow]:
        last_lifestyle_instructions = self.patient.instructions.find(
            LifestyleChangeReDietInstruction
        ).last()
        return (
            arrow.get(last_lifestyle_instructions['noteTimestamp'])
            if last_lifestyle_instructions
            else None
        )

    def had_lifestyle_instructions_within_six_months(self) -> bool:
        if not self.last_lifestyle_instructions_date():
            return False
        six_months_ago = arrow.now().shift(months=-6)
        return self.last_lifestyle_instructions_date() > six_months_ago

    def on_metformin(self) -> bool:
        return bool(
            self.patient.medications.find(Metformin).filter(status='active')
        )

    def needs_metformin_risk_factors(self) -> bool:
        if (
            (self.bmi() and self.bmi() > 35)
            or self.has_gestational_diabetes_history()
            or (
                self.last_fasting_glucose_value()
                and self.last_fasting_glucose_value() >= 110
            )
            or (self.last_a1c_level() and self.last_a1c_level() > 6)
        ):
            return True
        return False

    def needs_metformin_time_based(self) -> bool:
        six_months_ago = arrow.now().shift(months=-6)
        if (
            (
                self.last_lifestyle_instructions_date()
                and self.last_lifestyle_instructions_date() < six_months_ago
            )
            and (self.last_a1c_level() and 5.7 <= self.last_a1c_level() <= 6.4)
            and (
                (self.last_a1c_date() - self.last_lifestyle_instructions_date())
                >= timedelta(days=6 * 30)
            )
        ):
            return True
        return False

    def in_denominator(self) -> bool:
        """Patients with most recent A1c level between 5.7 and 6.4."""
        last_a1c_level = self.last_a1c_level()
        return 5.7 <= last_a1c_level <= 6.4 if last_a1c_level else False

    def in_numerator(self) -> bool:
        """
        Patients who have been instructed on lifestyle changes
        or started on metformin within the past six months.
        """
        six_months_ago = arrow.now().shift(months=-6)
        if (
            self.needs_metformin_risk_factors()
            or self.needs_metformin_time_based()
        ) and not self.on_metformin():
            return False

        elif not self.had_lifestyle_instructions_within_six_months():
            return False

        elif not self.last_a1c_date() or self.last_a1c_date() < six_months_ago:
            return False

        return True

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                'Protocol satisfied by either instruction on lifestyle changes '
                'or prescription of metformin.'
            )
        )
        result.status = STATUS_SATISFIED

    def remainder_tasks(self, result: ProtocolResult):
        six_months_ago = arrow.now().shift(months=-6)
        narratives = []
        # Recommend lifestyle changes if not already recommended
        if not self.had_lifestyle_instructions_within_six_months():
            result.add_recommendation(
                InstructionRecommendation(
                    key='RECOMMEND_INSTRUCT_LIFESTYLE_CHANGES',
                    patient=self.patient,
                    instruction=LifestyleChangeReDietInstruction,
                    title='Lifestyle changes for prediabetes',
                )
            )
            narratives.append(
                'Patients should be instructed on'
                ' lifestyle changes every 6 months.'
            )
        # Recommend an A1C test if not done in last 6 months
        if not self.last_a1c_date() or self.last_a1c_date() < six_months_ago:
            result.add_recommendation(
                LabRecommendation(
                    key='RECOMMEND_A1C_TEST',
                    patient=self.patient,
                    condition=Diabetes,
                    lab=Hba1CLaboratoryTest,
                    title='Order Hemoglobin A1c',
                )
            )
            narratives.append(
                'Hemoglobin A1c should be checked every 6 months.'
            )
        # If patient has a BMI > 35, a history of gestational diabetes,
        # fasting glucose 110 mg/dL or greater, or A1c > 6%, recommend starting
        # metformin immediately
        if not self.on_metformin():
            if self.needs_metformin_risk_factors():
                self.recommend_metformin(result)
                narratives.append(
                    'Metformin should be started in the '
                    'presence of risk factors or if A1c remains in prediabetic '
                    'range 6 months after lifestyle changes.'
                )
            # If patient has already been instructed with lifestyle changes and
            # A1c is still in pre-diabetic range at 6 months, recommend starting
            # metformin
            elif self.needs_metformin_time_based():
                self.recommend_metformin(result)
                narratives.append(
                    'Metformin should be started in the '
                    'presence of risk factors or if A1c remains in prediabetic '
                    'range 6 months after lifestyle changes.'
                )
        result.add_narrative(' '.join(narratives))
        result.status = STATUS_DUE

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative('Protocol not applicable based on hemoglobin A1c.')
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

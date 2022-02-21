from ..value_set import ValueSet


class AcuteInpatient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts related to acute inpatient visits.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an acute inpatient setting. This is a grouping value set of CPT and SNOMED codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1083'
    VALUE_SET_NAME = 'Acute Inpatient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99221',
        '99222',
        '99223',
        '99231',
        '99232',
        '99233',
        '99238',
        '99239',
        '99251',
        '99252',
        '99253',
        '99254',
        '99255',
        '99291'
    }

    SNOMEDCT = {
        '112689000',
        '1505002',
        '15584006',
        '183450002',
        '183481006',
        '183487005',
        '183488000',
        '183489008',
        '183491000',
        '183492007',
        '183493002',
        '183494008',
        '183495009',
        '183496005',
        '183497001',
        '183498006',
        '183499003',
        '183500007',
        '183501006',
        '183502004',
        '183503009',
        '183504003',
        '183505002',
        '183506001',
        '183507005',
        '183508000',
        '183509008',
        '183510003',
        '183511004',
        '183512006',
        '235313004',
        '25986004',
        '287927002',
        '304566005',
        '305337004',
        '305338009',
        '305341000',
        '305342007',
        '305350003',
        '305354007',
        '305355008',
        '305356009',
        '305357000',
        '305358005',
        '305359002',
        '305360007',
        '305361006',
        '305362004',
        '305363009',
        '305364003',
        '305365002',
        '305366001',
        '305367005',
        '305368000',
        '305369008',
        '305370009',
        '305371008',
        '305372001',
        '305374000',
        '305375004',
        '305376003',
        '305377007',
        '305378002',
        '305379005',
        '305380008',
        '305382000',
        '305383005',
        '305384004',
        '305385003',
        '305386002',
        '305387006',
        '305388001',
        '305389009',
        '305390000',
        '305391001',
        '305392008',
        '305393003',
        '305394009',
        '305395005',
        '305396006',
        '305397002',
        '305399004',
        '305400006',
        '305401005',
        '305402003',
        '305403008',
        '305404002',
        '305405001',
        '305406000',
        '305407009',
        '305408004',
        '305409007',
        '305410002',
        '305411003',
        '305412005',
        '305413000',
        '305414006',
        '305415007',
        '305416008',
        '305417004',
        '305418009',
        '305419001',
        '305420007',
        '305421006',
        '305422004',
        '305423009',
        '305424003',
        '305425002',
        '305426001',
        '305427005',
        '305428000',
        '305429008',
        '305430003',
        '305431004',
        '305432006',
        '305433001',
        '305434007',
        '305435008',
        '306732000',
        '306803007',
        '306967009',
        '308251003',
        '308252005',
        '308253000',
        '310361003',
        '3241000175106',
        '32485007',
        '373113001',
        '397769005',
        '398162007',
        '405614004',
        '417005',
        '432621000124105',
        '442281000124108',
        '447941000124106',
        '448421000124105',
        '448431000124108',
        '448441000124103',
        '448851000124103',
        '4563007',
        '45702004',
        '47348005',
        '48183000',
        '51032003',
        '51501005',
        '5161006',
        '52748007',
        '60059000',
        '63551005',
        '699124006',
        '70755000',
        '71290004',
        '76193006',
        '76464004',
        '81672003',
        '82942009',
        '8715000'
    }

class CareServicesInLongTermResidentialFacility(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients living in assisted living, domiciliary care or rest homes who have had an interaction with a member of their medical team.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with services provided to new and established patients living in assisted living, domiciliary care or rest home. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes visits in settings other than assisted living, domiciliary care or rest homes.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1014'
    VALUE_SET_NAME = 'Care Services in Long-Term Residential Facility'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337'
    }

    SNOMEDCT = {
        '209099002',
        '210098006'
    }

class ClinicalOralEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who had a clinical oral evaluation.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with periodic, limited (problem focused

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.125.12.1003'
    VALUE_SET_NAME = 'Clinical Oral Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDT = {
        'D0120',
        'D0140',
        'D0145',
        'D0150',
        'D0160',
        'D0170',
        'D0180'
    }

class ContactOrOfficeVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent contact and office visits for new and established patients, and includes in-person, telephone, online, and other visit types related to depression encounters.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with outpatient contact and office visits in which a patient may be evaluated for depression. This groups CPT and HCPCS codes.

    **Exclusion Criteria:** Excludes inpatients for purposes of the index event. The majority of CPT codes are specified for outpatient visit types; however psychiatry and psychotherapy visits can be used in the inpatient setting.
    """

    OID = '2.16.840.1.113762.1.4.1080.5'
    VALUE_SET_NAME = 'Contact or Office Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90791',
        '90792',
        '90832',
        '90834',
        '90837',
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99211',
        '99212',
        '99213',
        '99214',
        '99215',
        '99421',
        '99422',
        '99423',
        '99441',
        '99442',
        '99443',
        '99444'
    }

    HCPCSLEVELII = {
        'G0402',
        'G0438',
        'G0439',
        'G2061',
        'G2062',
        'G2063'
    }

class DetoxificationVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent detoxification visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying alcohol and drug detoxification. This is a grouping of SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1059'
    VALUE_SET_NAME = 'Detoxification Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '182969009',
        '20093000',
        '23915005',
        '414054004',
        '414056002',
        '56876005',
        '61480009',
        '64297001',
        '67516001',
        '87106005'
    }

class DischargeServicesHospitalInpatient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent inpatient hospital discharge services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying hospital discharge day management. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1007'
    VALUE_SET_NAME = 'Discharge Services - Hospital Inpatient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99238',
        '99239'
    }

class DischargeServicesHospitalInpatientSameDayDischarge(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent inpatient hospital same day discharge services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying observation or inpatient care for the evaluation and management of a patient that results in discharge on the same date of admission. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1006'
    VALUE_SET_NAME = 'Discharge Services - Hospital Inpatient Same Day Discharge'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99234',
        '99235',
        '99236'
    }

class DischargeServicesNursingFacility(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have been discharged from a nursing facility.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with discharge from a nursing facility, including a final examination, instructions for continuing care and preparation of discharge records, prescriptions, and referral forms. Discharge services encounters can be less than or over 30 minutes. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes discharges from settings other than a nursing facility.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1013'
    VALUE_SET_NAME = 'Discharge Services - Nursing Facility'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99315',
        '99316'
    }

class DischargeServicesNursingFacility_1065(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have been discharged from a nursing facility.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with discharge from a nursing facility, including a final examination, instructions for continuing care and preparation of discharge records, prescriptions, and referral forms. Discharge services encounters can be less than or over 30 minutes. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes discharges from settings other than a nursing facility.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.11.1065'
    VALUE_SET_NAME = 'Discharge Services - Nursing Facility'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99315',
        '99316'
    }

class Ed(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts related to an ED visit.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an ED. This is a grouping value set of CPT and SNOMED codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1085'
    VALUE_SET_NAME = 'ED'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99281',
        '99282',
        '99283',
        '99284',
        '99285'
    }

    SNOMEDCT = {
        '4525004'
    }

class EmergencyDepartmentVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had an interaction with a member of their medical care team in the emergency department.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with care provided to new and established patients in the emergency department. This is a value set grouping that includes CPT and SNOMED CT codes.

    **Exclusion Criteria:** Excludes services not performed in the emergency department, including critical care and observation services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1010'
    VALUE_SET_NAME = 'Emergency Department Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99281',
        '99282',
        '99283',
        '99284',
        '99285'
    }

    SNOMEDCT = {
        '4525004'
    }

class FrailtyEncounter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nursing care services provided to frail patients.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with nursing care and home care services provided to frail patients. This is a grouping of CPT, HCPCS, and SNOMEDCT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1088'
    VALUE_SET_NAME = 'Frailty Encounter'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99504',
        '99509'
    }

    HCPCSLEVELII = {
        'G0162',
        'G0299',
        'G0300',
        'G0493',
        'G0494',
        'S0271',
        'S0311',
        'S9123',
        'S9124',
        'T1000',
        'T1001',
        'T1002',
        'T1003',
        'T1004',
        'T1005',
        'T1019',
        'T1020',
        'T1021',
        'T1022',
        'T1030',
        'T1031'
    }

    SNOMEDCT = {
        '413467001'
    }

class HomeHealthcareServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had a home health visit by a provider for the evaluation or management of a new or existing patient.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with home visits for the evaluation and management of a new or established patient. This is a grouping value set of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1016'
    VALUE_SET_NAME = 'Home Healthcare Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99341',
        '99342',
        '99343',
        '99344',
        '99345',
        '99347',
        '99348',
        '99349',
        '99350'
    }

    SNOMEDCT = {
        '185460008',
        '185462000',
        '185466002',
        '185467006',
        '185468001',
        '185470005',
        '225929007',
        '315205008',
        '439708006',
        '698704008',
        '704126008'
    }

class HospitalInpatientVisitInitial(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent inpatient hospital visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with initial hospital care for the evaluation and management of a patient. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1004'
    VALUE_SET_NAME = 'Hospital Inpatient Visit - Initial'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99221',
        '99222',
        '99223'
    }

class HospitalObservationCareInitial(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent initial inpatient hospital observation care.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with initial observation care for the evaluation and management of a patient. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1002'
    VALUE_SET_NAME = 'Hospital Observation Care - Initial'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99218',
        '99219',
        '99220'
    }

class MedicalDisabilityExam(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent work related or medical disability examinations.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with work related or medical disability examinations. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.11.1233'
    VALUE_SET_NAME = 'Medical Disability Exam'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99455',
        '99456'
    }

class NonacuteInpatient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts related to nonacute inpatient visits.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in a nonacute inpatient setting. This is a grouping value set of CPT and SNOMED codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1084'
    VALUE_SET_NAME = 'Nonacute Inpatient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337'
    }

    SNOMEDCT = {
        '112690009',
        '183430001',
        '183921001',
        '304567001',
        '304568006',
        '305336008',
        '305340004',
        '305381007',
        '306804001',
        '36723004',
        '449411000124106',
        '449421000124103',
        '449431000124100'
    }

class NursingFacilityVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had an interaction with a member of their medical team on admission to a nursing facility.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with services provided to new and established patients in a nursing facility (skilled, intermediate and long-term care facilities).

    **Exclusion Criteria:** Excludes visits in settings other than a nursing facility.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1012'
    VALUE_SET_NAME = 'Nursing Facility Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318'
    }

    SNOMEDCT = {
        '18170008',
        '207195004'
    }

class Observation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts related to observation visits.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an observation care setting. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1086'
    VALUE_SET_NAME = 'Observation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99217',
        '99218',
        '99219',
        '99220'
    }

class OfficeVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had an office or other outpatient visit.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an office or outpatient facility. Patient can be presenting with problems that are minor to high severity. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes non-office visits, including telehealth services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1001'
    VALUE_SET_NAME = 'Office Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215'
    }

    SNOMEDCT = {
        '185463005',
        '185464004',
        '185465003',
        '30346009',
        '3391000175108',
        '37894004',
        '439740005'
    }

class Outpatient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts related to outpatient visits.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an outpatient setting. This is a grouping value set of CPT and HCPCS codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1087'
    VALUE_SET_NAME = 'Outpatient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99211',
        '99212',
        '99213',
        '99214',
        '99215',
        '99241',
        '99242',
        '99243',
        '99244',
        '99245',
        '99341',
        '99342',
        '99343',
        '99344',
        '99345',
        '99347',
        '99348',
        '99349',
        '99350',
        '99381',
        '99382',
        '99383',
        '99384',
        '99385',
        '99386',
        '99387',
        '99391',
        '99392',
        '99393',
        '99394',
        '99395',
        '99396',
        '99397',
        '99401',
        '99402',
        '99403',
        '99404',
        '99411',
        '99412',
        '99429',
        '99455',
        '99456',
        '99483'
    }

    HCPCSLEVELII = {
        'G0402',
        'G0438',
        'G0439',
        'G0463',
        'T1015'
    }

class OutpatientConsultation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had an outpatient interaction at an office with a member of their medical care team.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive history, evaluation, and management of a patient in an office or outpatient facility. Patient can be presenting with problems that are minor to high severity. This is a grouping value set of CPT and SNOMED CT codes.

    **Exclusion Criteria:** Excludes non-office visits, including telehealth services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1008'
    VALUE_SET_NAME = 'Outpatient Consultation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99241',
        '99242',
        '99243',
        '99244',
        '99245'
    }

    SNOMEDCT = {
        '281036007',
        '77406008'
    }

class PreventiveCareEstablishedOfficeVisit0To17(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent initial comprehensive preventive medical evaluation, including regular preventive care or care of small problem or preexisting condition that requires no extra work, to be associated with patients 0-17 years of age, that received prior outpatient professional services from the physician practice in the last 3 years.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with ages 0-17, and indicating initial comprehensive preventive medical evaluation, including regular preventive care or care of small problem or preexisting condition that requires no extra work, for a patient that received prior outpatient professional services from the physician practice in the last 3 years. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes codes that are not for comprehensive preventive medical evaluations and codes that are for patients who have not been seen in the last 3 years.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1024'
    VALUE_SET_NAME = 'Preventive Care, Established Office Visit, 0 to 17'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99391',
        '99392',
        '99393',
        '99394'
    }

class PreventiveCareServicesEstablishedOfficeVisit18AndUp(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients over the age of 18 who have had an established preventive care office visit.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive preventive medicine reevaluation and management of an individual the age of 18 years or over. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes non-office visits, including telehealth services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1025'
    VALUE_SET_NAME = 'Preventive Care Services - Established Office Visit, 18 and Up'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99395',
        '99396',
        '99397'
    }

class PreventiveCareServicesGroupCounseling(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent group counseling services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying preventive medicine counseling and/or risk factor reduction intervention(s) provided to individuals in a group setting.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1027'
    VALUE_SET_NAME = 'Preventive Care Services - Group Counseling'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99411',
        '99412'
    }

class PreventiveCareServicesIndividualCounseling(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have received preventive medicine counseling and/or risk factor reduction interventions.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with counseling, anticipatory guidance, and risk factor reduction interventions. Preventative care and individual counseling encounters can be 15 to 60 minutes. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes codes for services performed in the emergency department, including critical care and observation services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1026'
    VALUE_SET_NAME = 'Preventive Care Services-Individual Counseling'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99401',
        '99402',
        '99403',
        '99404'
    }

class PreventiveCareServicesInitialOfficeVisit0To17(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent initial comprehensive preventive medical evaluation, including regular preventive care or care of small problem or preexisting condition that requires no extra work, to be associated with patients 0-17 years of age, that have no prior outpatient professional services from the physician practice in the last 3 years.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with ages 0-17, and that indicate initial comprehensive preventive medical evaluation, including regular preventive care or care of small problem or preexisting condition that requires no extra work, for a patient that has no prior outpatient professional services from the physician practice in the last 3 years. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes codes that are not for comprehensive preventive medical evaluations and codes that are for patients who have been seen in the last 3 years.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1022'
    VALUE_SET_NAME = 'Preventive Care Services, Initial Office Visit, 0 to 17'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99381',
        '99382',
        '99383',
        '99384'
    }

class PreventiveCareServicesInitialOfficeVisit18AndUp(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients over the age of 18 who have had an initial preventive care office visit.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with comprehensive preventive medicine reevaluation and management of an individual the age of 18 years or over. This is a grouping value set of CPT codes.

    **Exclusion Criteria:** Excludes non-office visits, including telehealth services.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1023'
    VALUE_SET_NAME = 'Preventive Care Services-Initial Office Visit, 18 and Up'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99385',
        '99386',
        '99387'
    }

class PreventiveCareServicesOther(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent unlisted preventive medicine services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with unlisted preventive medicine services. This is a grouping of a CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1030'
    VALUE_SET_NAME = 'Preventive Care Services - Other'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99429'
    }

class PsychotherapyAndPharmacologicManagement(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent psychotherapy services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying psychotherapy services.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1055'
    VALUE_SET_NAME = 'Psychotherapy and Pharmacologic Management'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90845',
        '90847',
        '90849',
        '90853',
        '90875',
        '90876'
    }

class TelehealthServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent telehealth services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying telehealth services, including telephone and online evaluation and management services.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1031'
    VALUE_SET_NAME = 'Telehealth Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '98966',
        '98967',
        '98968',
        '99441',
        '99442',
        '99443'
    }

class TelephoneEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent telephone evaluations.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying evaluation and management services to a patient by telephone. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes telephone evaluation and management services that last for less than five minutes.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1082'
    VALUE_SET_NAME = 'Telephone Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99441',
        '99442',
        '99443'
    }

class TelephoneManagement(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent telephone management.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant codes used to identify assessment and management services to a patient by telephone. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes telephone assessment and management services that last for less than five minutes.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1053'
    VALUE_SET_NAME = 'Telephone Management'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '98966',
        '98967',
        '98968'
    }

class TelephoneVisits(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent telephone visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying assessment, evaluation and management services to a patient by telephone. This is a grouping of CPT codes.

    **Exclusion Criteria:** Excludes telephone assessment, evaluation and management services that last for less than five minutes.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1080'
    VALUE_SET_NAME = 'Telephone Visits'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '98966',
        '98967',
        '98968',
        '99441',
        '99442',
        '99443'
    }
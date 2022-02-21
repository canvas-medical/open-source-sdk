from ..value_set import ValueSet


class BilateralMastectomy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent bilateral mastectomy procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with a bilateral mastectomy. This is a grouping of SNOMED CT codes.

    **Exclusion Criteria:** Excludes codes that indicate a unilateral mastectomy or are unspecified.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1005'
    VALUE_SET_NAME = 'Bilateral Mastectomy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '0HTV0ZZ'
    }

    ICD9CM = {
        '8542',
        '8544',
        '8546',
        '8548'
    }

    SNOMEDCT = {
        '136071000119101',
        '14693006',
        '14714006',
        '17086001',
        '22418005',
        '27865001',
        '428529004',
        '456903003',
        '52314009',
        '59860000',
        '60633004',
        '726636007',
        '76468001'
    }

class Colonoscopy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent colonoscopy procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts that identify patients who have had a screening or diagnostic colonoscopy. This is a grouping of CPT, HCPCS, and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.108.12.1020'
    VALUE_SET_NAME = 'Colonoscopy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '44388',
        '44389',
        '44390',
        '44391',
        '44392',
        '44394',
        '44401',
        '44402',
        '44403',
        '44404',
        '44405',
        '44406',
        '44407',
        '44408',
        '45378',
        '45379',
        '45380',
        '45381',
        '45382',
        '45384',
        '45385',
        '45386',
        '45388',
        '45389',
        '45390',
        '45391',
        '45392',
        '45393',
        '45398'
    }

    HCPCSLEVELII = {
        'G0105',
        'G0121'
    }

    SNOMEDCT = {
        '12350003',
        '174158000',
        '235150006',
        '235151005',
        '25732003',
        '310634005',
        '34264006',
        '367535003',
        '425672002',
        '425937002',
        '427459009',
        '443998000',
        '444783004',
        '446521004',
        '446745002',
        '447021001',
        '709421007',
        '710293001',
        '711307001',
        '713154003',
        '73761001',
        '8180007',
        '851000119109'
    }

class DeliveryLiveBirths(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent single or multiple live births.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with delivery of one or multiple newborns. This is a grouping of CPT, SNOMED CT and ICD-10-PCS codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.111.12.1015'
    VALUE_SET_NAME = 'Delivery Live Births'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '59400',
        '59409',
        '59410',
        '59510',
        '59514',
        '59515',
        '59610',
        '59612',
        '59614',
        '59618',
        '59620',
        '59622'
    }

    ICD10PCS = {
        '10D00Z0',
        '10D00Z1',
        '10D00Z2',
        '10D07Z3',
        '10D07Z4',
        '10D07Z5',
        '10D07Z6',
        '10D07Z7',
        '10D07Z8',
        '10E0XZZ'
    }

    SNOMEDCT = {
        '10745001',
        '11466000',
        '14119008',
        '15413009',
        '16819009',
        '177141003',
        '177142005',
        '177143000',
        '177152009',
        '177157003',
        '177158008',
        '177161009',
        '177162002',
        '177164001',
        '177167008',
        '177168003',
        '177170007',
        '177173009',
        '177174003',
        '177175002',
        '177176001',
        '177179008',
        '177180006',
        '177181005',
        '177184002',
        '177185001',
        '17860005',
        '18625004',
        '19390001',
        '22633006',
        '236974004',
        '236975003',
        '236976002',
        '236977006',
        '236978001',
        '236980007',
        '236981006',
        '236982004',
        '236983009',
        '236984003',
        '236985002',
        '236986001',
        '236987005',
        '236988000',
        '236989008',
        '236990004',
        '237311001',
        '25296001',
        '25828002',
        '26313002',
        '265639000',
        '274130007',
        '275168001',
        '275169009',
        '28542003',
        '287976008',
        '288042004',
        '288193006',
        '28860009',
        '29613008',
        '302382009',
        '302383004',
        '30476003',
        '306727001',
        '33807004',
        '359940006',
        '359943008',
        '384729004',
        '384730009',
        '38479009',
        '398307005',
        '40219000',
        '40704000',
        '40792007',
        '41059002',
        '416055001',
        '417121007',
        '4504004',
        '450483001',
        '450484007',
        '450798003',
        '45718005',
        '48204000',
        '54973000',
        '5556001',
        '57271003',
        '58705005',
        '61586001',
        '62508004',
        '65243006',
        '69422002',
        '699999008',
        '700000006',
        '709004006',
        '71166009',
        '72492007',
        '734275002',
        '734276001',
        '736018001',
        '736020003',
        '736026009',
        '736118004',
        '75928003',
        '84195007',
        '85403009',
        '89053004',
        '89346004',
        '89849000',
        '90438006'
    }

class DtapVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for diphtheria, tetanus, and whooping cough (pertussis) (DTaP) vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with diphtheria, tetanus, and whooping cough (pertussis) (DTaP) vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1022'
    VALUE_SET_NAME = 'DTaP Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90698',
        '90700',
        '90723'
    }

    SNOMEDCT = {
        '170395004',
        '170396003',
        '170397007',
        '170399005',
        '170400003',
        '170401004',
        '170402006',
        '310306005',
        '310307001',
        '310308006',
        '312870000',
        '313383003',
        '390846000',
        '390865008',
        '399014008',
        '412755006',
        '412756007',
        '412757003',
        '412762002',
        '412763007',
        '412764001',
        '414001002',
        '414259000',
        '414620004',
        '415507003',
        '415712004',
        '428251000124104'
    }

class FlexibleSigmoidoscopy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a flexible sigmoidoscopy.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a flexible sigmoidoscopy. This is a grouping of CPT, HCPCS and SNOMED CT codes.

    **Exclusion Criteria:** Excludes codes that indicate that this test was ordered only, and not necessarily performed.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1010'
    VALUE_SET_NAME = 'Flexible Sigmoidoscopy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '45330',
        '45331',
        '45332',
        '45333',
        '45334',
        '45335',
        '45337',
        '45338',
        '45339',
        '45340',
        '45341',
        '45342',
        '45345',
        '45346',
        '45347',
        '45349',
        '45350'
    }

    HCPCSLEVELII = {
        'G0104'
    }

    SNOMEDCT = {
        '396226005',
        '425634007',
        '44441009',
        '841000119107'
    }

class FluorideVarnishApplicationForChildren(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a fluoride varnish application.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying patients who received a fluoride varnish application.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.125.12.1002'
    VALUE_SET_NAME = 'Fluoride Varnish Application for Children'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDT = {
        'D1206',
        'D1208'
    }

    CPT = {
        '99188'
    }

    SNOMEDCT = {
        '234723000',
        '313042009',
        '35889000',
        '70468009'
    }

class GastricBypassSurgery(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent codes that can be used to identify patients who have undergone a partial or total removal of the stomach by either a laparoscopic or open method.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying procedures for repair or removal of digestive system organs that includes a partial or total removal of the stomach. This is a grouping of CT and SNOMED CT codes.

    **Exclusion Criteria:** Excludes endoscopic excision of tissue of stomach, excision/laparoscopic wedge resection of lesion of stomach and incisional biopsy of stomach.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1050'
    VALUE_SET_NAME = 'Gastric Bypass Surgery'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '43117',
        '43118',
        '43121',
        '43122',
        '43123',
        '43620',
        '43621',
        '43622',
        '43631',
        '43632',
        '43633',
        '43634',
        '43775',
        '43845',
        '48150',
        '48152'
    }

    SNOMEDCT = {
        '10002003',
        '10869008',
        '112860004',
        '116175006',
        '173560002',
        '173714001',
        '173715000',
        '173716004',
        '173720000',
        '173722008',
        '173794002',
        '21538007',
        '235165007',
        '235214008',
        '235215009',
        '235216005',
        '235217001',
        '235218006',
        '235219003',
        '24431004',
        '24506003',
        '24883002',
        '26452005',
        '265340005',
        '265459006',
        '26565004',
        '275007007',
        '275162000',
        '275194005',
        '287809004',
        '287816003',
        '287818002',
        '287819005',
        '287821000',
        '307303006',
        '307304000',
        '359575000',
        '359579006',
        '40234006',
        '427074001',
        '427980007',
        '430715008',
        '43344006',
        '438338008',
        '439878001',
        '445831005',
        '445983004',
        '446650001',
        '46936007',
        '49209004',
        '53442002',
        '68342003',
        '83371007',
        '83857006',
        '83985009',
        '85217002',
        '87604009',
        '90063003',
        '90410003',
        '9102008',
        '91621005'
    }

class HepatitisAVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedure codes for hepatitis A vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with hepatitis A vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1041'
    VALUE_SET_NAME = 'Hepatitis A Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90633'
    }

    SNOMEDCT = {
        '170378007',
        '170379004',
        '170380001',
        '170381002',
        '170434002',
        '170435001',
        '170436000',
        '170437009',
        '243789007',
        '312868009',
        '313188000',
        '313189008',
        '314177003',
        '314178008',
        '314179000',
        '394691002',
        '412742005',
        '412743000'
    }

class HepatitisBVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for hepatitis B vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant hepatitis B vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1042'
    VALUE_SET_NAME = 'Hepatitis B Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90723',
        '90740',
        '90744',
        '90747',
        '90748'
    }

    ICD10PCS = {
        '3E0234Z'
    }

    ICD9CM = {
        '9955'
    }

    SNOMEDCT = {
        '116802006',
        '16584000',
        '170370000',
        '170371001',
        '170372008',
        '170373003',
        '170434002',
        '170435001',
        '170436000',
        '170437009',
        '312868009',
        '396456003'
    }

class HibVaccine3DoseScheduleAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for haemophilus influenzae type b (Hib) vaccine administration (3-dose schedule).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with haemophilus influenzae type b (Hib) vaccine administration codes (3-dose schedule). This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1084'
    VALUE_SET_NAME = 'Hib Vaccine (3 dose schedule) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90647'
    }

    SNOMEDCT = {
        '127787002',
        '170343007',
        '170344001',
        '170345000',
        '170346004'
    }

class HibVaccine4DoseScheduleAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for haemophilus influenzae type b (Hib) vaccine administration (4-dose schedule).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with haemophilus influenzae type b (Hib) vaccine administration codes (4-dose schedule). This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1086'
    VALUE_SET_NAME = 'Hib Vaccine (4 dose schedule) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90644',
        '90648',
        '90698',
        '90748'
    }

    SNOMEDCT = {
        '127787002',
        '170343007',
        '170344001',
        '170345000',
        '170346004',
        '310306005',
        '310307001',
        '310308006',
        '312869001',
        '312870000',
        '414001002',
        '414259000',
        '415507003',
        '415712004'
    }

class HysterectomyWithNoResidualCervix(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that identify hysterectomy procedures that include removal of the patient's cervix.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with total or radical hysterectomies. This is a grouping of CPT, SNOMED CT, ICD-10-PCS and ICD-9-CM codes.

    **Exclusion Criteria:** Excludes partial hysterectomies and hysterectomies that leave the patient's cervix intact.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1014'
    VALUE_SET_NAME = 'Hysterectomy with No Residual Cervix'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '51925',
        '57540',
        '57545',
        '57550',
        '57555',
        '57556',
        '58150',
        '58152',
        '58200',
        '58210',
        '58240',
        '58260',
        '58262',
        '58263',
        '58267',
        '58270',
        '58275',
        '58280',
        '58285',
        '58290',
        '58291',
        '58292',
        '58293',
        '58294',
        '58548',
        '58550',
        '58552',
        '58553',
        '58554',
        '58570',
        '58571',
        '58572',
        '58573',
        '58575',
        '58951',
        '58953',
        '58954',
        '58956',
        '59135'
    }

    ICD10CM = {
        'Z90710',
        'Z90712'
    }

    ICD10PCS = {
        '0UTC0ZZ',
        '0UTC4ZZ',
        '0UTC7ZZ',
        '0UTC8ZZ'
    }

    ICD9CM = {
        '6185',
        '6841',
        '6849',
        '6851',
        '6859',
        '6861',
        '6869',
        '6871',
        '6879',
        '688',
        '75243',
        'V8801',
        'V8803'
    }

    SNOMEDCT = {
        '116140006',
        '116142003',
        '116143008',
        '116144002',
        '176697007',
        '236888001',
        '236891001',
        '24293001',
        '27950001',
        '28301000',
        '287924009',
        '307771009',
        '31545000',
        '35955002',
        '361222003',
        '361223008',
        '387626007',
        '414575003',
        '41566006',
        '440383008',
        '446446002',
        '446679008',
        '46226009',
        '59750000',
        '708877008',
        '708878003',
        '739671004',
        '739672006',
        '739673001',
        '739674007',
        '740514001',
        '740515000',
        '767610009',
        '767611008',
        '767612001',
        '82418001',
        '86477000',
        '88144003'
    }

class InactivatedPolioVaccineIpvAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for inactivated polio vaccine (IPV) administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all inactivated polio vaccine (IPV) administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1045'
    VALUE_SET_NAME = 'Inactivated Polio Vaccine (IPV) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90698',
        '90713',
        '90723'
    }

    SNOMEDCT = {
        '396456003',
        '412762002',
        '414001002',
        '414259000',
        '414619005',
        '414620004',
        '415507003',
        '415712004',
        '416144004',
        '416591003',
        '417211006',
        '417384007',
        '417615007'
    }

class InfluenzaVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for influenza vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant influenza vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1044'
    VALUE_SET_NAME = 'Influenza Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90655',
        '90657',
        '90661',
        '90662',
        '90673',
        '90685',
        '90686',
        '90687',
        '90688'
    }

    SNOMEDCT = {
        '86198006'
    }

class MeaslesMumpsAndRubellaMmrVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures for measles, mumps and rubella (MMR) vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant measles, mumps and rubella (MMR) vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1031'
    VALUE_SET_NAME = 'Measles, Mumps and Rubella (MMR) Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90707',
        '90710'
    }

    SNOMEDCT = {
        '150971000119104',
        '170433008',
        '38598009',
        '432636005',
        '433733003'
    }

class Pci(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures used to define percutaneous coronary intervention (PCI).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed. The intent of this data element is to identify patients who had percutaneous coronary intervention (PCI) during an episode of acute myocardial infarction.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying patients receiving percutaneous coronary intervention (PCI). This is a grouping of ICD-10-PCS and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113762.1.4.1045.67'
    VALUE_SET_NAME = 'PCI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '0270346',
        '027034Z',
        '0270356',
        '027035Z',
        '0270366',
        '027036Z',
        '0270376',
        '027037Z',
        '02703D6',
        '02703DZ',
        '02703E6',
        '02703EZ',
        '02703F6',
        '02703FZ',
        '02703G6',
        '02703GZ',
        '02703T6',
        '02703TZ',
        '02703Z6',
        '02703ZZ',
        '0270446',
        '027044Z',
        '0270456',
        '027045Z',
        '0270466',
        '027046Z',
        '0270476',
        '027047Z',
        '02704D6',
        '02704DZ',
        '02704E6',
        '02704EZ',
        '02704F6',
        '02704FZ',
        '02704G6',
        '02704GZ',
        '02704T6',
        '02704TZ',
        '02704Z6',
        '02704ZZ',
        '0271346',
        '027134Z',
        '0271356',
        '027135Z',
        '0271366',
        '027136Z',
        '0271376',
        '027137Z',
        '02713D6',
        '02713DZ',
        '02713E6',
        '02713EZ',
        '02713F6',
        '02713FZ',
        '02713G6',
        '02713GZ',
        '02713T6',
        '02713TZ',
        '02713Z6',
        '02713ZZ',
        '0271446',
        '027144Z',
        '0271456',
        '027145Z',
        '0271466',
        '027146Z',
        '0271476',
        '027147Z',
        '02714D6',
        '02714DZ',
        '02714E6',
        '02714EZ',
        '02714F6',
        '02714FZ',
        '02714G6',
        '02714GZ',
        '02714T6',
        '02714TZ',
        '02714Z6',
        '02714ZZ',
        '0272346',
        '027234Z',
        '0272356',
        '027235Z',
        '0272366',
        '027236Z',
        '0272376',
        '027237Z',
        '02723D6',
        '02723DZ',
        '02723E6',
        '02723EZ',
        '02723F6',
        '02723FZ',
        '02723G6',
        '02723GZ',
        '02723T6',
        '02723TZ',
        '02723Z6',
        '02723ZZ',
        '0272446',
        '027244Z',
        '0272456',
        '027245Z',
        '0272466',
        '027246Z',
        '0272476',
        '027247Z',
        '02724D6',
        '02724DZ',
        '02724E6',
        '02724EZ',
        '02724F6',
        '02724FZ',
        '02724G6',
        '02724GZ',
        '02724T6',
        '02724TZ',
        '02724Z6',
        '02724ZZ',
        '0273346',
        '027334Z',
        '0273356',
        '027335Z',
        '0273366',
        '027336Z',
        '0273376',
        '027337Z',
        '02733D6',
        '02733DZ',
        '02733E6',
        '02733EZ',
        '02733F6',
        '02733FZ',
        '02733G6',
        '02733GZ',
        '02733T6',
        '02733TZ',
        '02733Z6',
        '02733ZZ',
        '0273446',
        '027344Z',
        '0273456',
        '027345Z',
        '0273466',
        '027346Z',
        '0273476',
        '027347Z',
        '02734D6',
        '02734DZ',
        '02734E6',
        '02734EZ',
        '02734F6',
        '02734FZ',
        '02734G6',
        '02734GZ',
        '02734T6',
        '02734TZ',
        '02734Z6',
        '02734ZZ'
    }

    SNOMEDCT = {
        '11101003',
        '175066001',
        '36969009',
        '397193006',
        '397431004',
        '414089002',
        '415070008',
        '428488008',
        '429499003',
        '429639007',
        '429809004',
        '609153008',
        '609154002',
        '68466008',
        '698740005',
        '707828002',
        '737085003',
        '85053006'
    }

class PneumococcalConjugateVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedure codes for pneumococcal vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all pneumococcal vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1046'
    VALUE_SET_NAME = 'Pneumococcal Conjugate Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90670'
    }

    SNOMEDCT = {
        '434751000124102'
    }

class PneumococcalVaccineAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent administration of pneumococcal vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with administration of the pneumococcal vaccine. This is a grouping of CVX and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1034'
    VALUE_SET_NAME = 'Pneumococcal Vaccine Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90670'
    }

    SNOMEDCT = {
        '12866006',
        '394678003'
    }

class PrimaryThaProcedure(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent primary Total Hip Arthroplasty (THA) procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with codes that identify primary THA procedures. This is a grouping of CPT, HCPCS and SNOMED CT codes.

    **Exclusion Criteria:** Excludes codes for revision or partial hip arthroplasty procedures.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1006'
    VALUE_SET_NAME = 'Primary THA Procedure'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '27130'
    }

    HCPCSLEVELII = {
        'S2118'
    }

    SNOMEDCT = {
        '15163009',
        '179294005',
        '179304004',
        '179305003',
        '19954002',
        '265157000',
        '265158005',
        '265160007',
        '314489006',
        '314491003',
        '426618001',
        '426904006',
        '427728006',
        '429156003',
        '443435007',
        '450813004',
        '52734007',
        '53081006',
        '57589001',
        '76915002'
    }

class PrimaryTkaProcedure(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent primary Total Knee Arthroplasty (TKA) procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with codes that identify primary TKA procedures. This is a grouping of CPT, HCPCS and SNOMED CT codes.

    **Exclusion Criteria:** Excludes codes for revision or partial knee arthroplasty procedures.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1007'
    VALUE_SET_NAME = 'Primary TKA Procedure'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '27447'
    }

    SNOMEDCT = {
        '179344006',
        '179345007',
        '179351002',
        '179352009',
        '265170009',
        '265172001',
        '392237008',
        '443681002',
        '443682009'
    }

class ProceduresDuringPregnancy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures conducted during pregnancy.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with procedures conducted on a patient during pregnancy. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.111.12.1009'
    VALUE_SET_NAME = 'Procedures During Pregnancy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '57022',
        '58600',
        '58605',
        '58970',
        '58974',
        '58976',
        '59000',
        '59001',
        '59012',
        '59015',
        '59020',
        '59025',
        '59030',
        '59050',
        '59051',
        '59070',
        '59072',
        '59074',
        '59076',
        '59100',
        '59120',
        '59121',
        '59130',
        '59135',
        '59136',
        '59140',
        '59150',
        '59151',
        '59160',
        '59200',
        '59300',
        '59320',
        '59325',
        '59350',
        '59412',
        '59414',
        '59430',
        '59525',
        '59812',
        '59820',
        '59821',
        '59830',
        '59840',
        '59841',
        '59850',
        '59851',
        '59852',
        '59855',
        '59856',
        '59857',
        '59866',
        '59870',
        '59871',
        '59897',
        '59898',
        '59899'
    }

    SNOMEDCT = {
        '10455003',
        '10763001',
        '133875007',
        '176833006',
        '176850008',
        '176852000',
        '176854004',
        '176928008',
        '176929000',
        '176996001',
        '177037000',
        '177038005',
        '177039002',
        '177042008',
        '177091002',
        '177100008',
        '177101007',
        '177102000',
        '177106002',
        '177107006',
        '177112007',
        '177122001',
        '177136006',
        '177212000',
        '177222006',
        '17744000',
        '18302006',
        '18489003',
        '215192006',
        '216209009',
        '233560009',
        '233561008',
        '236894009',
        '236912008',
        '236913003',
        '236914009',
        '236915005',
        '236952005',
        '236953000',
        '236954006',
        '236955007',
        '236956008',
        '236966000',
        '236987005',
        '236988000',
        '236992007',
        '236993002',
        '236994008',
        '237017007',
        '237025009',
        '240278000',
        '240284002',
        '240285001',
        '240286000',
        '240288004',
        '240289007',
        '240290003',
        '240291004',
        '240292006',
        '24068006',
        '243773009',
        '243774003',
        '259863001',
        '265082003',
        '265635006',
        '265642006',
        '26578004',
        '274973002',
        '275222009',
        '275223004',
        '28107008',
        '281568006',
        '281570002',
        '28379004',
        '285409006',
        '285416007',
        '285417003',
        '285434006',
        '287954004',
        '288045002',
        '288194000',
        '29682007',
        '302375005',
        '302384005',
        '303720006',
        '309877008',
        '315308008',
        '36708009',
        '386276009',
        '386277000',
        '386639001',
        '386641000',
        '387615001',
        '387616000',
        '387673001',
        '387678005',
        '387709005',
        '387710000',
        '391896006',
        '391897002',
        '391899004',
        '391998006',
        '392000009',
        '398221005',
        '40704000',
        '408804006',
        '408805007',
        '408806008',
        '408807004',
        '408808009',
        '408819007',
        '408840008',
        '408845003',
        '41058005',
        '41059002',
        '41780001',
        '425707001',
        '425939004',
        '426287008',
        '426737000',
        '427230007',
        '427320001',
        '429613009',
        '429737004',
        '43096003',
        '433153009',
        '440148001',
        '443005005',
        '445865006',
        '445912000',
        '446135006',
        '446341008',
        '446934006',
        '447214008',
        '447771005',
        '447972007',
        '448543003',
        '450563004',
        '45460008',
        '46681009',
        '480571000119102',
        '5048009',
        '5191001',
        '52660002',
        '56620000',
        '61893009',
        '62688006',
        '63407004',
        '63596003',
        '65378009',
        '6708002',
        '69621003',
        '700041001',
        '713117007',
        '713120004',
        '714812005',
        '716100006',
        '725927001',
        '726556001',
        '732970000',
        '73341009',
        '737099004',
        '75456002',
        '81130000',
        '81855008',
        '82688001',
        '84275009',
        '85179000',
        '85548006',
        '87431004',
        '87663001',
        '88144003',
        '88362001',
        '90442009',
        '9221009',
        '9724000'
    }

class ProceduresInvolvingContraceptiveDevices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures involving contraceptive devices.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with procedures related to contraceptive devices. This is a grouping of CPT, HCPCS and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.111.12.1010'
    VALUE_SET_NAME = 'Procedures Involving Contraceptive Devices'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '11976',
        '57170',
        '58300',
        '58301'
    }

    HCPCSLEVELII = {
        'S4981'
    }

    SNOMEDCT = {
        '169553002',
        '176749004',
        '176839005',
        '225251006',
        '225256001',
        '225257005',
        '236892008',
        '274042004',
        '275811000',
        '301806003',
        '301807007',
        '440668008',
        '442490009',
        '450836008',
        '46706006',
        '472837007',
        '472838002',
        '58391006',
        '65200003',
        '68254000'
    }

class TotalColectomy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent total colectomy procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with a total colectomy, as an open or laparoscopic procedure. This is a grouping of CPT, SNOMED CT and ICD-10-PCS codes.

    **Exclusion Criteria:** Excludes partial colectomies.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1019'
    VALUE_SET_NAME = 'Total Colectomy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '44150',
        '44151',
        '44155',
        '44156',
        '44157',
        '44158',
        '44210',
        '44211',
        '44212'
    }

    ICD10PCS = {
        '0DTE0ZZ',
        '0DTE4ZZ',
        '0DTE7ZZ',
        '0DTE8ZZ'
    }

    ICD9CM = {
        '4581',
        '4582',
        '4583'
    }

    SNOMEDCT = {
        '119771000119101',
        '26390003',
        '303401008',
        '307666008',
        '307667004',
        '307669001',
        '31130001',
        '36192008',
        '44751009',
        '456004',
        '80294005'
    }

class UnilateralMastectomyLeft(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent unilateral mastectomy of the right breast.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated  with a unilateral mastectomy of the right breast. This is a grouping value set of SNOMEDCT and ICD10PCS codes.

    **Exclusion Criteria:** Excludes concepts that pertain to a left, right or bilateral mastectomy.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1133'
    VALUE_SET_NAME = 'Unilateral Mastectomy Left'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '0HTU0ZZ'
    }

    SNOMEDCT = {
        '12275221000119100',
        '137671000119105',
        '428571003',
        '429009003',
        '451211000124109',
        '726429001',
        '726435001',
        '726437009'
    }

class UnilateralMastectomyRight(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent unilateral mastectomy of the left breast.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with  a unilateral mastectomy of the left breast. This is a grouping value set of SNOMEDCT and ICD10PCS codes

    **Exclusion Criteria:** Excludes concepts that pertain  to a left, right or bilateral mastectomy.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1134'
    VALUE_SET_NAME = 'Unilateral Mastectomy Right'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '0HTT0ZZ'
    }

    SNOMEDCT = {
        '12275171000119105',
        '137681000119108',
        '429242008',
        '429400009',
        '451201000124106',
        '726430006',
        '726434002',
        '726436000'
    }

class VaricellaZosterVaccineVzvAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedure codes for varicella zoster vaccine administration.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with all varicella zoster vaccine administration codes. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1040'
    VALUE_SET_NAME = 'Varicella Zoster Vaccine (VZV) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90710',
        '90716'
    }

    SNOMEDCT = {
        '425897001',
        '428502009',
        '473164004',
        '571611000119101'
    }

class VascularAccessForDialysis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent procedures related to accessing the vascular system for dialysis.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with procedures related to accessing the vascular system for dialysis such as inserting a needle or catheter or creating a shunt. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1011'
    VALUE_SET_NAME = 'Vascular Access for Dialysis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '36800',
        '36810',
        '36815',
        '36818',
        '36819',
        '36820',
        '36821',
        '36831',
        '36832',
        '36833'
    }

    SNOMEDCT = {
        '180272001',
        '180277007',
        '225892009',
        '22800003',
        '233468004',
        '233471007',
        '233472000',
        '233547003',
        '238314006',
        '238315007',
        '271418008',
        '34163007',
        '426340003',
        '427992007',
        '428118009',
        '431418000',
        '431440009',
        '431781000',
        '432509002',
        '432654009',
        '434435000',
        '438341004',
        '438342006',
        '439241008',
        '439322008',
        '439349008',
        '439534001',
        '443683004',
        '448591002',
        '449400003',
        '450865002',
        '54817007',
        '61160002',
        '61740001',
        '63421002',
        '676002',
        '69380006',
        '736919006',
        '736922008',
        '7459007',
        '79827002',
        '80634002'
    }
from ..value_set import ValueSet


class BmiRatio(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a body mass index (BMI) ratio.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with or related to BMI ratio.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1490'
    VALUE_SET_NAME = 'BMI Ratio'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '39156-5'
    }

class CabgPciProcedure(ValueSet):
    """
    **Clinical Focus:** CABG and PCI procedures

    **Data Element Scope:** CABG and PCI procedures

    **Inclusion Criteria:** Codes from 2018_Registry_SingleSource_v2.2

    **Exclusion Criteria:** None
    """

    OID = '2.16.840.1.113762.1.4.1138.566'
    VALUE_SET_NAME = 'CABG, PCI Procedure'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '33510',
        '33511',
        '33512',
        '33513',
        '33514',
        '33516',
        '33517',
        '33518',
        '33519',
        '33521',
        '33522',
        '33523',
        '33533',
        '33534',
        '33535',
        '33536',
        '92920',
        '92924',
        '92928',
        '92933',
        '92937',
        '92941',
        '92943'
    }

    HCPCSLEVELII = {
        'S2205',
        'S2206',
        'S2207',
        'S2208',
        'S2209'
    }

class CabgSurgeries(ValueSet):
    """
    **Clinical Focus:** This value set grouping contains concepts that represent coronary artery bypass (CABG) surgical procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure. The intent of this data element is to identify patients who have a CABG surgical procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with CABG surgical procedures. This is a grouping of SNOMED CT, ICD-9-CM, and ICD-10-CM codes.

    **Exclusion Criteria:** Excludes codes that represent a CABG performed using a scope.
    """

    OID = '2.16.840.1.113883.3.666.5.694'
    VALUE_SET_NAME = 'CABG Surgeries'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '0210083',
        '0210088',
        '0210089',
        '021008C',
        '021008F',
        '021008W',
        '0210093',
        '0210098',
        '0210099',
        '021009C',
        '021009F',
        '021009W',
        '02100A3',
        '02100A8',
        '02100A9',
        '02100AC',
        '02100AF',
        '02100AW',
        '02100J3',
        '02100J8',
        '02100J9',
        '02100JC',
        '02100JF',
        '02100JW',
        '02100K3',
        '02100K8',
        '02100K9',
        '02100KC',
        '02100KF',
        '02100KW',
        '02100Z3',
        '02100Z8',
        '02100Z9',
        '02100ZC',
        '02100ZF',
        '0210483',
        '0210488',
        '0210489',
        '021048C',
        '021048F',
        '021048W',
        '0210493',
        '0210498',
        '0210499',
        '021049C',
        '021049F',
        '021049W',
        '02104A3',
        '02104A8',
        '02104A9',
        '02104AC',
        '02104AF',
        '02104AW',
        '02104J3',
        '02104J8',
        '02104J9',
        '02104JC',
        '02104JF',
        '02104JW',
        '02104K3',
        '02104K8',
        '02104K9',
        '02104KC',
        '02104KF',
        '02104KW',
        '02104Z3',
        '02104Z8',
        '02104Z9',
        '02104ZC',
        '02104ZF',
        '0211083',
        '0211088',
        '0211089',
        '021108C',
        '021108F',
        '021108W',
        '0211093',
        '0211098',
        '0211099',
        '021109C',
        '021109F',
        '021109W',
        '02110A3',
        '02110A8',
        '02110A9',
        '02110AC',
        '02110AF',
        '02110AW',
        '02110J3',
        '02110J8',
        '02110J9',
        '02110JC',
        '02110JF',
        '02110JW',
        '02110K3',
        '02110K8',
        '02110K9',
        '02110KC',
        '02110KF',
        '02110KW',
        '02110Z3',
        '02110Z8',
        '02110Z9',
        '02110ZC',
        '02110ZF',
        '0211483',
        '0211488',
        '0211489',
        '021148C',
        '021148F',
        '021148W',
        '0211493',
        '0211498',
        '0211499',
        '021149C',
        '021149F',
        '021149W',
        '02114A3',
        '02114A8',
        '02114A9',
        '02114AC',
        '02114AF',
        '02114AW',
        '02114J3',
        '02114J8',
        '02114J9',
        '02114JC',
        '02114JF',
        '02114JW',
        '02114K3',
        '02114K8',
        '02114K9',
        '02114KC',
        '02114KF',
        '02114KW',
        '02114Z3',
        '02114Z8',
        '02114Z9',
        '02114ZC',
        '02114ZF',
        '0212083',
        '0212088',
        '0212089',
        '021208C',
        '021208F',
        '021208W',
        '0212093',
        '0212098',
        '0212099',
        '021209C',
        '021209F',
        '021209W',
        '02120A3',
        '02120A8',
        '02120A9',
        '02120AC',
        '02120AF',
        '02120AW',
        '02120J3',
        '02120J8',
        '02120J9',
        '02120JC',
        '02120JF',
        '02120JW',
        '02120K3',
        '02120K8',
        '02120K9',
        '02120KC',
        '02120KF',
        '02120KW',
        '02120Z3',
        '02120Z8',
        '02120Z9',
        '02120ZC',
        '02120ZF',
        '0212488',
        '0212489',
        '021248C',
        '021248F',
        '021248W',
        '0212493',
        '0212498',
        '0212499',
        '021249C',
        '021249F',
        '021249W',
        '02124A3',
        '02124A8',
        '02124A9',
        '02124AC',
        '02124AF',
        '02124AW',
        '02124J3',
        '02124J8',
        '02124J9',
        '02124JC',
        '02124JF',
        '02124JW',
        '02124K3',
        '02124K8',
        '02124K9',
        '02124KC',
        '02124KF',
        '02124KW',
        '02124Z3',
        '02124Z8',
        '02124Z9',
        '02124ZC',
        '02124ZF',
        '0213083',
        '0213088',
        '0213089',
        '021308C',
        '021308F',
        '021308W',
        '0213093',
        '0213098',
        '0213099',
        '021309C',
        '021309F',
        '021309W',
        '02130A3',
        '02130A8',
        '02130A9',
        '02130AC',
        '02130AF',
        '02130AW',
        '02130J3',
        '02130J8',
        '02130J9',
        '02130JC',
        '02130JF',
        '02130JW',
        '02130K3',
        '02130K8',
        '02130K9',
        '02130KC',
        '02130KF',
        '02130KW',
        '02130Z3',
        '02130Z8',
        '02130Z9',
        '02130ZC',
        '02130ZF',
        '0213483',
        '0213488',
        '0213489',
        '021348C',
        '021348F',
        '021348W',
        '0213493',
        '0213498',
        '0213499',
        '021349C',
        '021349F',
        '021349W',
        '02134A3',
        '02134A8',
        '02134A9',
        '02134AC',
        '02134AF',
        '02134AW',
        '02134J3',
        '02134J8',
        '02134J9',
        '02134JC',
        '02134JF',
        '02134JW',
        '02134K3',
        '02134K8',
        '02134K9',
        '02134KC',
        '02134KF',
        '02134KW',
        '02134Z3',
        '02134Z8',
        '02134Z9',
        '02134ZC',
        '02134ZF'
    }

    ICD9CM = {
        '3610',
        '3611',
        '3612',
        '3613',
        '3614',
        '3615',
        '3616',
        '3617',
        '3619'
    }

    SNOMEDCT = {
        '10190003',
        '10326007',
        '119564002',
        '119565001',
        '14323007',
        '17073005',
        '175021005',
        '175029007',
        '175036008',
        '175037004',
        '175038009',
        '175039001',
        '175040004',
        '175066001',
        '232717009',
        '232719007',
        '232720001',
        '232721002',
        '232722009',
        '232723004',
        '232724005',
        '252427007',
        '29819009',
        '309814006',
        '3546002',
        '359597003',
        '359601003',
        '39202005',
        '39724006',
        '405598005',
        '405599002',
        '414088005',
        '418551006',
        '419132001',
        '438530000',
        '440332008',
        '450506009',
        '67166004',
        '736970002',
        '736971003',
        '736972005',
        '736973000',
        '74371005',
        '82247006',
        '8876004',
        '90487008'
    }

class CardiacSurgery(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent cardiac surgery.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with cardiac surgery.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.371'
    VALUE_SET_NAME = 'Cardiac Surgery'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '33140',
        '33510',
        '33511',
        '33512',
        '33513',
        '33514',
        '33516',
        '33533',
        '33534',
        '33535',
        '33536',
        '92920',
        '92924',
        '92928',
        '92933',
        '92937',
        '92941',
        '92943',
        '92980',
        '92981',
        '92982',
        '92984',
        '92995',
        '92996'
    }

    SNOMEDCT = {
        '10326007',
        '119564002',
        '119565001',
        '15256002',
        '174911007',
        '175007008',
        '175008003',
        '175009006',
        '175011002',
        '175021005',
        '175022003',
        '175024002',
        '175025001',
        '175026000',
        '175036008',
        '175037004',
        '175038009',
        '175039001',
        '175040004',
        '175041000',
        '175045009',
        '175047001',
        '175048006',
        '175050003',
        '232717009',
        '232719007',
        '232720001',
        '232721002',
        '232722009',
        '232723004',
        '232724005',
        '265481001',
        '275215001',
        '275216000',
        '275227003',
        '275252001',
        '275253006',
        '287277008',
        '30670000',
        '309814006',
        '3546002',
        '359597003',
        '359601003',
        '39202005',
        '39724006',
        '414088005',
        '418551006',
        '418824004',
        '419132001',
        '48431000',
        '736966005',
        '736967001',
        '736968006',
        '736969003',
        '736970002',
        '736971003',
        '736972005',
        '736973000',
        '74371005',
        '81266008',
        '82247006',
        '90205004'
    }

class CarotidIntervention(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent carotid intervention surgical procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with representing carotid intervention surgical procedures.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.117.1.7.1.204'
    VALUE_SET_NAME = 'Carotid Intervention'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10PCS = {
        '031H09G',
        '031H09J',
        '031H09K',
        '031H09Y',
        '031H0AG',
        '031H0AJ',
        '031H0AK',
        '031H0AY',
        '031H0JG',
        '031H0JJ',
        '031H0JK',
        '031H0JY',
        '031H0KG',
        '031H0KJ',
        '031H0KK',
        '031H0KY',
        '031H0ZG',
        '031H0ZJ',
        '031H0ZK',
        '031H0ZY',
        '031J09G',
        '031J09J',
        '031J09K',
        '031J09Y',
        '031J0AG',
        '031J0AJ',
        '031J0AK',
        '031J0AY',
        '031J0JG',
        '031J0JJ',
        '031J0JK',
        '031J0JY',
        '031J0KG',
        '031J0KJ',
        '031J0KK',
        '031J0KY',
        '031J0ZG',
        '031J0ZJ',
        '031J0ZK',
        '031J0ZY',
        '031K09J',
        '031K09K',
        '031K0AJ',
        '031K0AK',
        '031K0JJ',
        '031K0JK',
        '031K0KJ',
        '031K0KK',
        '031K0ZJ',
        '031K0ZK',
        '031L09J',
        '031L09K',
        '031L0AJ',
        '031L0AK',
        '031L0JJ',
        '031L0JK',
        '031L0KJ',
        '031L0KK',
        '031L0ZJ',
        '031L0ZK',
        '031M09J',
        '031M09K',
        '031M0AJ',
        '031M0AK',
        '031M0JJ',
        '031M0JK',
        '031M0KJ',
        '031M0KK',
        '031M0ZJ',
        '031M0ZK',
        '031N09J',
        '031N09K',
        '031N0AJ',
        '031N0AK',
        '031N0JJ',
        '031N0JK',
        '031N0KJ',
        '031N0KK',
        '031N0ZJ',
        '031N0ZK',
        '035H0ZZ',
        '035H3ZZ',
        '035H4ZZ',
        '035J0ZZ',
        '035J3ZZ',
        '035J4ZZ',
        '035K0ZZ',
        '035K3ZZ',
        '035K4ZZ',
        '035L0ZZ',
        '035L3ZZ',
        '035L4ZZ',
        '035M0ZZ',
        '035M3ZZ',
        '035M4ZZ',
        '035N0ZZ',
        '035N3ZZ',
        '035N4ZZ',
        '037H046',
        '037H04Z',
        '037H056',
        '037H05Z',
        '037H066',
        '037H06Z',
        '037H076',
        '037H07Z',
        '037H0D6',
        '037H0DZ',
        '037H0E6',
        '037H0EZ',
        '037H0F6',
        '037H0FZ',
        '037H0G6',
        '037H0GZ',
        '037H0Z6',
        '037H0ZZ',
        '037H346',
        '037H34Z',
        '037H356',
        '037H35Z',
        '037H366',
        '037H36Z',
        '037H376',
        '037H37Z',
        '037H3D6',
        '037H3DZ',
        '037H3E6',
        '037H3EZ',
        '037H3F6',
        '037H3FZ',
        '037H3G6',
        '037H3GZ',
        '037H3Z6',
        '037H3ZZ',
        '037H446',
        '037H44Z',
        '037H456',
        '037H45Z',
        '037H466',
        '037H46Z',
        '037H476',
        '037H47Z',
        '037H4D6',
        '037H4DZ',
        '037H4E6',
        '037H4EZ',
        '037H4F6',
        '037H4FZ',
        '037H4G6',
        '037H4GZ',
        '037H4Z6',
        '037H4ZZ',
        '037J046',
        '037J04Z',
        '037J056',
        '037J05Z',
        '037J066',
        '037J06Z',
        '037J076',
        '037J07Z',
        '037J0D6',
        '037J0DZ',
        '037J0E6',
        '037J0EZ',
        '037J0F6',
        '037J0FZ',
        '037J0G6',
        '037J0GZ',
        '037J0Z6',
        '037J0ZZ',
        '037J346',
        '037J34Z',
        '037J356',
        '037J35Z',
        '037J366',
        '037J36Z',
        '037J376',
        '037J37Z',
        '037J3D6',
        '037J3DZ',
        '037J3E6',
        '037J3EZ',
        '037J3F6',
        '037J3FZ',
        '037J3G6',
        '037J3GZ',
        '037J3Z6',
        '037J3ZZ',
        '037J446',
        '037J44Z',
        '037J456',
        '037J45Z',
        '037J466',
        '037J46Z',
        '037J476',
        '037J47Z',
        '037J4D6',
        '037J4DZ',
        '037J4E6',
        '037J4EZ',
        '037J4F6',
        '037J4FZ',
        '037J4G6',
        '037J4GZ',
        '037J4Z6',
        '037J4ZZ',
        '037K046',
        '037K04Z',
        '037K056',
        '037K05Z',
        '037K066',
        '037K06Z',
        '037K076',
        '037K07Z',
        '037K0D6',
        '037K0DZ',
        '037K0E6',
        '037K0EZ',
        '037K0F6',
        '037K0FZ',
        '037K0G6',
        '037K0GZ',
        '037K0Z6',
        '037K0ZZ',
        '037K346',
        '037K34Z',
        '037K356',
        '037K35Z',
        '037K366',
        '037K36Z',
        '037K376',
        '037K37Z',
        '037K3D6',
        '037K3DZ',
        '037K3E6',
        '037K3EZ',
        '037K3F6',
        '037K3FZ',
        '037K3G6',
        '037K3GZ',
        '037K3Z6',
        '037K3ZZ',
        '037K446',
        '037K44Z',
        '037K456',
        '037K45Z',
        '037K466',
        '037K46Z',
        '037K476',
        '037K47Z',
        '037K4D6',
        '037K4DZ',
        '037K4E6',
        '037K4EZ',
        '037K4F6',
        '037K4FZ',
        '037K4G6',
        '037K4GZ',
        '037K4Z6',
        '037K4ZZ',
        '037L046',
        '037L04Z',
        '037L056',
        '037L05Z',
        '037L066',
        '037L06Z',
        '037L076',
        '037L07Z',
        '037L0D6',
        '037L0DZ',
        '037L0E6',
        '037L0EZ',
        '037L0F6',
        '037L0FZ',
        '037L0G6',
        '037L0GZ',
        '037L0Z6',
        '037L0ZZ',
        '037L346',
        '037L34Z',
        '037L356',
        '037L35Z',
        '037L366',
        '037L36Z',
        '037L376',
        '037L37Z',
        '037L3D6',
        '037L3DZ',
        '037L3E6',
        '037L3EZ',
        '037L3F6',
        '037L3FZ',
        '037L3G6',
        '037L3GZ',
        '037L3Z6',
        '037L3ZZ',
        '037L446',
        '037L44Z',
        '037L456',
        '037L45Z',
        '037L466',
        '037L46Z',
        '037L476',
        '037L47Z',
        '037L4D6',
        '037L4DZ',
        '037L4E6',
        '037L4EZ',
        '037L4F6',
        '037L4FZ',
        '037L4G6',
        '037L4GZ',
        '037L4Z6',
        '037L4ZZ',
        '037M046',
        '037M04Z',
        '037M056',
        '037M05Z',
        '037M066',
        '037M06Z',
        '037M076',
        '037M07Z',
        '037M0D6',
        '037M0DZ',
        '037M0E6',
        '037M0EZ',
        '037M0F6',
        '037M0FZ',
        '037M0G6',
        '037M0GZ',
        '037M0Z6',
        '037M0ZZ',
        '037M346',
        '037M34Z',
        '037M356',
        '037M35Z',
        '037M366',
        '037M36Z',
        '037M376',
        '037M37Z',
        '037M3D6',
        '037M3DZ',
        '037M3E6',
        '037M3EZ',
        '037M3F6',
        '037M3FZ',
        '037M3G6',
        '037M3GZ',
        '037M3Z6',
        '037M3ZZ',
        '037M446',
        '037M44Z',
        '037M456',
        '037M45Z',
        '037M466',
        '037M46Z',
        '037M476',
        '037M47Z',
        '037M4D6',
        '037M4DZ',
        '037M4E6',
        '037M4EZ',
        '037M4F6',
        '037M4FZ',
        '037M4G6',
        '037M4GZ',
        '037M4Z6',
        '037M4ZZ',
        '037N046',
        '037N04Z',
        '037N056',
        '037N05Z',
        '037N066',
        '037N06Z',
        '037N076',
        '037N07Z',
        '037N0D6',
        '037N0DZ',
        '037N0E6',
        '037N0EZ',
        '037N0F6',
        '037N0FZ',
        '037N0G6',
        '037N0GZ',
        '037N0Z6',
        '037N0ZZ',
        '037N346',
        '037N34Z',
        '037N356',
        '037N35Z',
        '037N366',
        '037N36Z',
        '037N376',
        '037N37Z',
        '037N3D6',
        '037N3DZ',
        '037N3E6',
        '037N3EZ',
        '037N3F6',
        '037N3FZ',
        '037N3G6',
        '037N3GZ',
        '037N3Z6',
        '037N3ZZ',
        '037N446',
        '037N44Z',
        '037N456',
        '037N45Z',
        '037N466',
        '037N46Z',
        '037N476',
        '037N47Z',
        '037N4D6',
        '037N4DZ',
        '037N4E6',
        '037N4EZ',
        '037N4F6',
        '037N4FZ',
        '037N4G6',
        '037N4GZ',
        '037N4Z6',
        '037N4ZZ',
        '039H00Z',
        '039H0ZX',
        '039H0ZZ',
        '039H30Z',
        '039H3ZX',
        '039H3ZZ',
        '039H40Z',
        '039H4ZX',
        '039H4ZZ',
        '039J00Z',
        '039J0ZX',
        '039J0ZZ',
        '039J30Z',
        '039J3ZX',
        '039J3ZZ',
        '039J40Z',
        '039J4ZX',
        '039J4ZZ',
        '039K00Z',
        '039K0ZX',
        '039K0ZZ',
        '039K30Z',
        '039K3ZX',
        '039K3ZZ',
        '039K40Z',
        '039K4ZX',
        '039K4ZZ',
        '039L00Z',
        '039L0ZX',
        '039L0ZZ',
        '039L30Z',
        '039L3ZX',
        '039L3ZZ',
        '039L40Z',
        '039L4ZX',
        '039L4ZZ',
        '039M00Z',
        '039M0ZX',
        '039M0ZZ',
        '039M30Z',
        '039M3ZX',
        '039M3ZZ',
        '039M40Z',
        '039M4ZX',
        '039M4ZZ',
        '039N00Z',
        '039N0ZX',
        '039N0ZZ',
        '039N30Z',
        '039N3ZX',
        '039N3ZZ',
        '039N40Z',
        '039N4ZX',
        '039N4ZZ',
        '03BH0ZX',
        '03BH0ZZ',
        '03BH3ZX',
        '03BH3ZZ',
        '03BH4ZX',
        '03BH4ZZ',
        '03BJ0ZX',
        '03BJ0ZZ',
        '03BJ3ZX',
        '03BJ3ZZ',
        '03BJ4ZX',
        '03BJ4ZZ',
        '03BK0ZX',
        '03BK0ZZ',
        '03BK3ZX',
        '03BK3ZZ',
        '03BK4ZX',
        '03BK4ZZ',
        '03BL0ZX',
        '03BL0ZZ',
        '03BL3ZX',
        '03BL3ZZ',
        '03BL4ZX',
        '03BL4ZZ',
        '03BM0ZX',
        '03BM0ZZ',
        '03BM3ZX',
        '03BM3ZZ',
        '03BM4ZX',
        '03BM4ZZ',
        '03BN0ZX',
        '03BN0ZZ',
        '03BN3ZX',
        '03BN3ZZ',
        '03BN4ZX',
        '03BN4ZZ',
        '03CH0Z6',
        '03CH0ZZ',
        '03CH3Z6',
        '03CH3Z7',
        '03CH3ZZ',
        '03CH4Z6',
        '03CH4ZZ',
        '03CJ0Z6',
        '03CJ0ZZ',
        '03CJ3Z6',
        '03CJ3Z7',
        '03CJ3ZZ',
        '03CJ4Z6',
        '03CJ4ZZ',
        '03CK0Z6',
        '03CK0ZZ',
        '03CK3Z6',
        '03CK3Z7',
        '03CK3ZZ',
        '03CK4Z6',
        '03CK4ZZ',
        '03CL0Z6',
        '03CL0ZZ',
        '03CL3Z6',
        '03CL3Z7',
        '03CL3ZZ',
        '03CL4Z6',
        '03CL4ZZ',
        '03CM0Z6',
        '03CM0ZZ',
        '03CM3Z6',
        '03CM3Z7',
        '03CM3ZZ',
        '03CM4Z6',
        '03CM4ZZ',
        '03CN0Z6',
        '03CN0ZZ',
        '03CN3Z6',
        '03CN3Z7',
        '03CN3ZZ',
        '03CN4Z6',
        '03CN4ZZ',
        '03HH03Z',
        '03HH0DZ',
        '03HH33Z',
        '03HH3DZ',
        '03HH43Z',
        '03HH4DZ',
        '03HJ03Z',
        '03HJ0DZ',
        '03HJ33Z',
        '03HJ3DZ',
        '03HJ43Z',
        '03HJ4DZ',
        '03HK03Z',
        '03HK0DZ',
        '03HK0MZ',
        '03HK33Z',
        '03HK3DZ',
        '03HK3MZ',
        '03HK43Z',
        '03HK4DZ',
        '03HK4MZ',
        '03HL03Z',
        '03HL0DZ',
        '03HL0MZ',
        '03HL33Z',
        '03HL3DZ',
        '03HL3MZ',
        '03HL43Z',
        '03HL4DZ',
        '03HL4MZ',
        '03HM03Z',
        '03HM0DZ',
        '03HM33Z',
        '03HM3DZ',
        '03HM43Z',
        '03HM4DZ',
        '03HN03Z',
        '03HN0DZ',
        '03HN33Z',
        '03HN3DZ',
        '03HN43Z',
        '03HN4DZ',
        '03LH0BZ',
        '03LH0CZ',
        '03LH0DZ',
        '03LH0ZZ',
        '03LH3BZ',
        '03LH3CZ',
        '03LH3DZ',
        '03LH3ZZ',
        '03LH4BZ',
        '03LH4CZ',
        '03LH4DZ',
        '03LH4ZZ',
        '03LJ0BZ',
        '03LJ0CZ',
        '03LJ0DZ',
        '03LJ0ZZ',
        '03LJ3BZ',
        '03LJ3CZ',
        '03LJ3DZ',
        '03LJ3ZZ',
        '03LJ4BZ',
        '03LJ4CZ',
        '03LJ4DZ',
        '03LJ4ZZ',
        '03LK0BZ',
        '03LK0CZ',
        '03LK0DZ',
        '03LK0ZZ',
        '03LK3BZ',
        '03LK3CZ',
        '03LK3DZ',
        '03LK3ZZ',
        '03LK4BZ',
        '03LK4CZ',
        '03LK4DZ',
        '03LK4ZZ',
        '03LL0BZ',
        '03LL0CZ',
        '03LL0DZ',
        '03LL0ZZ',
        '03LL3BZ',
        '03LL3CZ',
        '03LL3DZ',
        '03LL3ZZ',
        '03LL4BZ',
        '03LL4CZ',
        '03LL4DZ',
        '03LL4ZZ',
        '03LM0BZ',
        '03LM0CZ',
        '03LM0DZ',
        '03LM0ZZ',
        '03LM3BZ',
        '03LM3CZ',
        '03LM3DZ',
        '03LM3ZZ',
        '03LM4BZ',
        '03LM4CZ',
        '03LM4DZ',
        '03LM4ZZ',
        '03LN0BZ',
        '03LN0CZ',
        '03LN0DZ',
        '03LN0ZZ',
        '03LN3BZ',
        '03LN3CZ',
        '03LN3DZ',
        '03LN3ZZ',
        '03LN4BZ',
        '03LN4CZ',
        '03LN4DZ',
        '03LN4ZZ',
        '03NH0ZZ',
        '03NH3ZZ',
        '03NH4ZZ',
        '03NJ0ZZ',
        '03NJ3ZZ',
        '03NJ4ZZ',
        '03NK0ZZ',
        '03NK3ZZ',
        '03NK4ZZ',
        '03NL0ZZ',
        '03NL3ZZ',
        '03NL4ZZ',
        '03NM0ZZ',
        '03NM3ZZ',
        '03NM4ZZ',
        '03NN0ZZ',
        '03NN3ZZ',
        '03NN4ZZ',
        '03QH0ZZ',
        '03QH3ZZ',
        '03QH4ZZ',
        '03QJ0ZZ',
        '03QJ3ZZ',
        '03QJ4ZZ',
        '03QK0ZZ',
        '03QK3ZZ',
        '03QK4ZZ',
        '03QL0ZZ',
        '03QL3ZZ',
        '03QL4ZZ',
        '03QM0ZZ',
        '03QM3ZZ',
        '03QM4ZZ',
        '03QN0ZZ',
        '03QN3ZZ',
        '03QN4ZZ',
        '03RH07Z',
        '03RH0JZ',
        '03RH0KZ',
        '03RH47Z',
        '03RH4JZ',
        '03RH4KZ',
        '03RJ07Z',
        '03RJ0JZ',
        '03RJ0KZ',
        '03RJ47Z',
        '03RJ4JZ',
        '03RJ4KZ',
        '03RK07Z',
        '03RK0JZ',
        '03RK0KZ',
        '03RK47Z',
        '03RK4JZ',
        '03RK4KZ',
        '03RL07Z',
        '03RL0JZ',
        '03RL0KZ',
        '03RL47Z',
        '03RL4JZ',
        '03RL4KZ',
        '03RM07Z',
        '03RM0JZ',
        '03RM0KZ',
        '03RM47Z',
        '03RM4JZ',
        '03RM4KZ',
        '03RN07Z',
        '03RN0JZ',
        '03RN0KZ',
        '03RN47Z',
        '03RN4JZ',
        '03RN4KZ',
        '03SH0ZZ',
        '03SH3ZZ',
        '03SH4ZZ',
        '03SJ0ZZ',
        '03SJ3ZZ',
        '03SJ4ZZ',
        '03SK0ZZ',
        '03SK3ZZ',
        '03SK4ZZ',
        '03SL0ZZ',
        '03SL3ZZ',
        '03SL4ZZ',
        '03SM0ZZ',
        '03SM3ZZ',
        '03SM4ZZ',
        '03SN0ZZ',
        '03SN3ZZ',
        '03SN4ZZ',
        '03UH07Z',
        '03UH0JZ',
        '03UH0KZ',
        '03UH37Z',
        '03UH3JZ',
        '03UH3KZ',
        '03UH47Z',
        '03UH4JZ',
        '03UH4KZ',
        '03UJ07Z',
        '03UJ0JZ',
        '03UJ0KZ',
        '03UJ37Z',
        '03UJ3JZ',
        '03UJ3KZ',
        '03UJ47Z',
        '03UJ4JZ',
        '03UJ4KZ',
        '03UK07Z',
        '03UK0JZ',
        '03UK0KZ',
        '03UK37Z',
        '03UK3JZ',
        '03UK3KZ',
        '03UK47Z',
        '03UK4JZ',
        '03UK4KZ',
        '03UL07Z',
        '03UL0JZ',
        '03UL0KZ',
        '03UL37Z',
        '03UL3JZ',
        '03UL3KZ',
        '03UL47Z',
        '03UL4JZ',
        '03UL4KZ',
        '03UM07Z',
        '03UM0JZ',
        '03UM0KZ',
        '03UM37Z',
        '03UM3JZ',
        '03UM3KZ',
        '03UM47Z',
        '03UM4JZ',
        '03UM4KZ',
        '03UN07Z',
        '03UN0JZ',
        '03UN0KZ',
        '03UN37Z',
        '03UN3JZ',
        '03UN3KZ',
        '03UN47Z',
        '03UN4JZ',
        '03UN4KZ',
        '03VH0BZ',
        '03VH0CZ',
        '03VH0DZ',
        '03VH0ZZ',
        '03VH3BZ',
        '03VH3CZ',
        '03VH3DZ',
        '03VH3ZZ',
        '03VH4BZ',
        '03VH4CZ',
        '03VH4DZ',
        '03VH4ZZ',
        '03VJ0BZ',
        '03VJ0CZ',
        '03VJ0DZ',
        '03VJ0ZZ',
        '03VJ3BZ',
        '03VJ3CZ',
        '03VJ3DZ',
        '03VJ3ZZ',
        '03VJ4BZ',
        '03VJ4CZ',
        '03VJ4DZ',
        '03VJ4ZZ',
        '03VK0BZ',
        '03VK0CZ',
        '03VK0DZ',
        '03VK0ZZ',
        '03VK3BZ',
        '03VK3CZ',
        '03VK3DZ',
        '03VK3ZZ',
        '03VK4BZ',
        '03VK4CZ',
        '03VK4DZ',
        '03VK4ZZ',
        '03VL0BZ',
        '03VL0CZ',
        '03VL0DZ',
        '03VL0ZZ',
        '03VL3BZ',
        '03VL3CZ',
        '03VL3DZ',
        '03VL3ZZ',
        '03VL4BZ',
        '03VL4CZ',
        '03VL4DZ',
        '03VL4ZZ',
        '03VM0BZ',
        '03VM0CZ',
        '03VM0DZ',
        '03VM0ZZ',
        '03VM3BZ',
        '03VM3CZ',
        '03VM3DZ',
        '03VM3ZZ',
        '03VM4BZ',
        '03VM4CZ',
        '03VM4DZ',
        '03VM4ZZ',
        '03VN0BZ',
        '03VN0CZ',
        '03VN0DZ',
        '03VN0ZZ',
        '03VN3BZ',
        '03VN3CZ',
        '03VN3DZ',
        '03VN3ZZ',
        '03VN4BZ',
        '03VN4CZ',
        '03VN4DZ',
        '03VN4ZZ',
        '0G560ZZ',
        '0G563ZZ',
        '0G564ZZ',
        '0G570ZZ',
        '0G573ZZ',
        '0G574ZZ',
        '0G580ZZ',
        '0G583ZZ',
        '0G584ZZ',
        '0G9600Z',
        '0G960ZX',
        '0G960ZZ',
        '0G9630Z',
        '0G963ZX',
        '0G963ZZ',
        '0G9640Z',
        '0G964ZX',
        '0G964ZZ',
        '0G9700Z',
        '0G970ZX',
        '0G970ZZ',
        '0G9730Z',
        '0G973ZX',
        '0G973ZZ',
        '0G9740Z',
        '0G974ZX',
        '0G974ZZ',
        '0G9800Z',
        '0G980ZX',
        '0G980ZZ',
        '0G9830Z',
        '0G983ZX',
        '0G983ZZ',
        '0G9840Z',
        '0G984ZX',
        '0G984ZZ',
        '0GB60ZX',
        '0GB60ZZ',
        '0GB63ZX',
        '0GB63ZZ',
        '0GB64ZX',
        '0GB64ZZ',
        '0GB70ZX',
        '0GB70ZZ',
        '0GB73ZX',
        '0GB73ZZ',
        '0GB74ZX',
        '0GB74ZZ',
        '0GB80ZX',
        '0GB80ZZ',
        '0GB83ZX',
        '0GB83ZZ',
        '0GB84ZX',
        '0GB84ZZ',
        '0GC60ZZ',
        '0GC63ZZ',
        '0GC64ZZ',
        '0GC70ZZ',
        '0GC73ZZ',
        '0GC74ZZ',
        '0GC80ZZ',
        '0GC83ZZ',
        '0GC84ZZ',
        '0GN60ZZ',
        '0GN63ZZ',
        '0GN64ZZ',
        '0GN70ZZ',
        '0GN73ZZ',
        '0GN74ZZ',
        '0GN80ZZ',
        '0GN83ZZ',
        '0GN84ZZ',
        '0GQ60ZZ',
        '0GQ63ZZ',
        '0GQ64ZZ',
        '0GQ70ZZ',
        '0GQ73ZZ',
        '0GQ74ZZ',
        '0GQ80ZZ',
        '0GQ83ZZ',
        '0GQ84ZZ',
        '0GT60ZZ',
        '0GT64ZZ',
        '0GT70ZZ',
        '0GT74ZZ',
        '0GT80ZZ',
        '0GT84ZZ',
        'B3060ZZ',
        'B3061ZZ',
        'B306YZZ',
        'B3070ZZ',
        'B3071ZZ',
        'B307YZZ',
        'B3080ZZ',
        'B3081ZZ',
        'B308YZZ',
        'B3160ZZ',
        'B3161ZZ',
        'B316YZZ',
        'B3170ZZ',
        'B3171ZZ',
        'B317YZZ',
        'B3180ZZ',
        'B3181ZZ',
        'B318YZZ'
    }

    ICD9CM = {
        '0061',
        '0062',
        '0063',
        '0064',
        '0065',
        '3802',
        '3812',
        '3822',
        '3830',
        '3831',
        '3832',
        '3842',
        '3922',
        '3928',
        '8841'
    }

    SNOMEDCT = {
        '112823003',
        '15023006',
        '175363002',
        '175364008',
        '175365009',
        '175367001',
        '175373000',
        '175374006',
        '175376008',
        '175379001',
        '175380003',
        '175398004',
        '18674003',
        '22928005',
        '233259003',
        '233260008',
        '233296007',
        '233297003',
        '233298008',
        '233405004',
        '241219006',
        '276949008',
        '276950008',
        '276951007',
        '287606009',
        '302053004',
        '303161001',
        '31573003',
        '34214004',
        '39887009',
        '405326004',
        '405379009',
        '405407008',
        '405408003',
        '405409006',
        '405411002',
        '405412009',
        '405415006',
        '417884003',
        '418405008',
        '418838006',
        '419014003',
        '420026003',
        '420046008',
        '420171008',
        '425611003',
        '427486009',
        '428802000',
        '429287007',
        '431515004',
        '431519005',
        '431535003',
        '431659001',
        '432039002',
        '432785007',
        '433056003',
        '433061001',
        '433591001',
        '433683001',
        '433690006',
        '433711000',
        '433734009',
        '434159001',
        '434378006',
        '434433007',
        '43628009',
        '438615003',
        '440221006',
        '440453000',
        '440518005',
        '449242004',
        '46912008',
        '51382002',
        '53412000',
        '59012002',
        '59109003',
        '66951008',
        '74720005',
        '79507006',
        '80102005',
        '80104006',
        '87314005',
        '90931006',
        '9339002'
    }

class CataractSurgery(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent cataract surgical procedures.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with cataract surgery.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1411'
    VALUE_SET_NAME = 'Cataract Surgery'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '66840',
        '66850',
        '66852',
        '66920',
        '66930',
        '66940',
        '66982',
        '66983',
        '66984'
    }

    SNOMEDCT = {
        '10178000',
        '110473004',
        '112963003',
        '112964009',
        '12163000',
        '231744001',
        '308694002',
        '308695001',
        '313999004',
        '31705006',
        '335636001',
        '336651000',
        '35717002',
        '361191005',
        '385468004',
        '39243005',
        '397544007',
        '404628003',
        '415089008',
        '417493007',
        '418430006',
        '419767009',
        '420260004',
        '420526005',
        '424945000',
        '446548003',
        '46309001',
        '46426006',
        '46562009',
        '50538003',
        '5130002',
        '51839008',
        '54885007',
        '65812008',
        '67760003',
        '69360005',
        '74490003',
        '75814005',
        '79611007',
        '82155009',
        '84149000',
        '85622008',
        '88282000',
        '89153001',
        '9137006'
    }

class ChemotherapyAdministration(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent chemotherapy administration.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with chemotherapy administration.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1027'
    VALUE_SET_NAME = 'Chemotherapy Administration'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '51720',
        '96401',
        '96405',
        '96406',
        '96409',
        '96413',
        '96416',
        '96420',
        '96422',
        '96425',
        '96440',
        '96446',
        '96450',
        '96521',
        '96522',
        '96523',
        '96542',
        '96549'
    }

    SNOMEDCT = {
        '169396008',
        '24977001',
        '265760000',
        '265761001',
        '265762008',
        '266719004',
        '268500004',
        '315601005',
        '31652009',
        '367336001',
        '38216008',
        '394894008',
        '394895009',
        '394935005',
        '4114003',
        '51534007',
        '6872008',
        '716872004',
        '77738002'
    }

class CognitiveAssessment(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent assessments performed for the evaluation of cognition.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with general concepts for assessments used to evaluate cognition.

    **Exclusion Criteria:** Excludes concepts which explicitly reference specific standardized tools used to evaluate cognition.
    """

    OID = '2.16.840.1.113883.3.526.3.1332'
    VALUE_SET_NAME = 'Cognitive Assessment'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '113024001',
        '4719001'
    }

class CounselingForNutrition(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nutrition counseling.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying counseling for nutrition, including codes for medical nutrition therapy, dietetics services, education about diet or different types of diets (e.g., low fat diet, high fiber diet

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.195.12.1003'
    VALUE_SET_NAME = 'Counseling for Nutrition'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '97802',
        '97803',
        '97804'
    }

    SNOMEDCT = {
        '11816003',
        '183059007',
        '183060002',
        '183061003',
        '183062005',
        '183063000',
        '183065007',
        '183066008',
        '183067004',
        '183070000',
        '183071001',
        '226067002',
        '266724001',
        '275919002',
        '281085002',
        '284352003',
        '305849009',
        '305850009',
        '305851008',
        '306163007',
        '306164001',
        '306165000',
        '306626002',
        '306627006',
        '306628001',
        '313210009',
        '370847001',
        '386464006',
        '404923009',
        '408910007',
        '410171007',
        '410177006',
        '410200000',
        '428461000124101',
        '428691000124107',
        '429095004',
        '431482008',
        '441041000124100',
        '441201000124108',
        '441231000124100',
        '441241000124105',
        '441251000124107',
        '441261000124109',
        '441271000124102',
        '441281000124104',
        '441291000124101',
        '441301000124100',
        '441311000124102',
        '441321000124105',
        '441331000124108',
        '441341000124103',
        '441351000124101',
        '443288003',
        '445291000124103',
        '445301000124102',
        '445331000124105',
        '445641000124105',
        '609104008',
        '61310001',
        '698471002',
        '699827002',
        '699829004',
        '699830009',
        '699849008',
        '700154005',
        '700258004',
        '705060005',
        '710881000'
    }

class CounselingForPhysicalActivity(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent physical activity counseling.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying counseling or referrals related to physical activity, including codes related to weight management services.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.118.12.1035'
    VALUE_SET_NAME = 'Counseling for Physical Activity'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '103736005',
        '183073003',
        '281090004',
        '304507003',
        '304549008',
        '304558001',
        '310882002',
        '386291006',
        '386292004',
        '386463000',
        '390864007',
        '390893007',
        '398636004',
        '398752005',
        '408289007',
        '410200000',
        '410289001',
        '410335001',
        '429778002',
        '435551000124105',
        '710849009'
    }

class CtColonography(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent identify a computed tomographic (CT) colonography.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with patients that have had a CT colonography. This is a grouping of CPT and SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.108.12.1038'
    VALUE_SET_NAME = 'CT Colonography'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '60515-4',
        '72531-7',
        '79069-1',
        '79071-7',
        '79101-2',
        '82688-3'
    }

class DialysisEducation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients received dialysis education.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Intervention, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with patients who had dialysis education. This includes only relevant concepts associated with education at home.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1016'
    VALUE_SET_NAME = 'Dialysis Education'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '28812006',
        '385972005',
        '59596005',
        '66402002'
    }

class DialysisServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dialysis services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with patients who had dialysis services.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1013'
    VALUE_SET_NAME = 'Dialysis Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '1019320',
        '90935',
        '90937',
        '90940',
        '90945',
        '90947',
        '90957',
        '90958',
        '90959'
    }

    HCPCSLEVELII = {
        'G0257'
    }

    SNOMEDCT = {
        '108241001',
        '10848006',
        '11932001',
        '14684005',
        '180273006',
        '225230008',
        '225231007',
        '233575001',
        '233576000',
        '233577009',
        '233578004',
        '233579007',
        '233580005',
        '233581009',
        '233582002',
        '233583007',
        '233584001',
        '233585000',
        '233586004',
        '233587008',
        '233588003',
        '233589006',
        '233590002',
        '238316008',
        '238317004',
        '238318009',
        '238319001',
        '238321006',
        '238322004',
        '238323009',
        '265764009',
        '288182009',
        '302497006',
        '34897002',
        '427053002',
        '428648006',
        '439278006',
        '439976001',
        '57274006',
        '676002',
        '67970008',
        '68341005',
        '71192002',
        '714749008'
    }

class DietaryRecommendations(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dietary management.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with dietary management and nutritional education.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1515'
    VALUE_SET_NAME = 'Dietary Recommendations'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    HCPCSLEVELII = {
        'S9452',
        'S9470'
    }

    ICD10CM = {
        'Z713'
    }

    SNOMEDCT = {
        '103699006',
        '11816003',
        '182922004',
        '182954008',
        '182955009',
        '182956005',
        '182960008',
        '183061003',
        '183065007',
        '183070000',
        '183071001',
        '281085002',
        '284071006',
        '284352003',
        '289176001',
        '289177005',
        '304491008',
        '306163007',
        '361231003',
        '370847001',
        '386464006',
        '410114009',
        '410171007',
        '410177006',
        '410270001',
        '413315001',
        '418995006',
        '424753004',
        '437211000124103',
        '437231000124109',
        '437391000124102',
        '437421000124105',
        '438961000124108',
        '443288003',
        '61310001'
    }

class FollowUpForAboveNormalBmi(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent interventions relevant for a follow up for a BMI above normal measurement.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with interventions relevant for a follow-up when BMI is above normal measurement.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1525'
    VALUE_SET_NAME = 'Follow Up for Above Normal BMI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '43644',
        '43645',
        '43659',
        '43770',
        '43771',
        '43772',
        '43773',
        '43774',
        '43842',
        '43843',
        '43845',
        '43846',
        '43847',
        '43848',
        '43886',
        '43888',
        '97802',
        '97803',
        '97804',
        '98960',
        '99078',
        '99401',
        '99402'
    }

    HCPCSLEVELII = {
        'G0270',
        'G0271',
        'G0447',
        'G0473',
        'S9449',
        'S9451',
        'S9452',
        'S9470'
    }

    ICD10CM = {
        'Z713',
        'Z7182'
    }

    SNOMEDCT = {
        '304549008',
        '307818003',
        '361231003',
        '370847001',
        '386291006',
        '386292004',
        '386373004',
        '386463000',
        '386464006',
        '410177006',
        '413315001',
        '418995006',
        '424753004',
        '443288003'
    }

class FollowUpForAdolescentDepression(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent follow-up plans used to document a plan is in place for the treatment of depression that specifically pertains to the adolescent population.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with emotional and coping support as well as mental health management in an attempt to follow up on previously evaluated and diagnosed depression or depressive disorder in the adolescent population.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1569'
    VALUE_SET_NAME = 'Follow Up for Adolescent Depression'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '108313002',
        '1555005',
        '15558000',
        '18512000',
        '229065009',
        '28868002',
        '304891004',
        '372067001',
        '385721005',
        '385724002',
        '385725001',
        '385726000',
        '385727009',
        '385887004',
        '385889001',
        '385890005',
        '386472008',
        '401277000',
        '405780009',
        '410223002',
        '410224008',
        '410225009',
        '410226005',
        '410227001',
        '410228006',
        '410229003',
        '410230008',
        '410231007',
        '410232000',
        '410233005',
        '410234004',
        '425604002',
        '439141002',
        '5694008',
        '75516001',
        '76168009',
        '76740001',
        '81294000',
        '88848003',
        '91310009'
    }

class FollowUpForAdultDepression(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent follow-up plans used to document a plan is in place for the treatment of depression specifically pertaining to the adult population.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with emotional and coping support as well as mental health management in an attempt to follow up on previously evaluated and diagnosed depression or depressive disorder in the adult population.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1568'
    VALUE_SET_NAME = 'Follow Up for Adult Depression'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '108313002',
        '1555005',
        '15558000',
        '18512000',
        '229065009',
        '28868002',
        '304891004',
        '372067001',
        '385721005',
        '385724002',
        '385725001',
        '385726000',
        '385727009',
        '385887004',
        '385889001',
        '385890005',
        '386472008',
        '401277000',
        '405780009',
        '410223002',
        '410224008',
        '410225009',
        '410226005',
        '410227001',
        '410228006',
        '410229003',
        '410230008',
        '410231007',
        '410232000',
        '410233005',
        '410234004',
        '425604002',
        '439141002',
        '5694008',
        '75516001',
        '76168009',
        '76740001',
        '81294000',
        '88848003',
        '91310009'
    }

class FollowUpForBelowNormalBmi(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a follow-up with a BMI below normal measurement.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with a follow-up when BMI is below normal measurement.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1528'
    VALUE_SET_NAME = 'Follow Up for Below Normal BMI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '97802',
        '97803',
        '97804',
        '98960',
        '99078',
        '99401',
        '99402'
    }

    HCPCSLEVELII = {
        'G0270',
        'G0271',
        'S9449',
        'S9452',
        'S9470'
    }

    ICD10CM = {
        'Z713'
    }

    SNOMEDCT = {
        '386464006',
        '410177006',
        '413315001',
        '418995006',
        '424753004',
        '429095004',
        '443288003'
    }

class Hemodialysis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the administration of hemodialysis.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with the administration of hemodialysis.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1083'
    VALUE_SET_NAME = 'Hemodialysis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90951',
        '90952',
        '90953',
        '90954',
        '90955',
        '90956',
        '90957',
        '90958',
        '90959',
        '90960',
        '90961',
        '90962',
        '90963',
        '90964',
        '90965',
        '90966',
        '90967',
        '90968',
        '90969',
        '90970',
        '99512'
    }

    SNOMEDCT = {
        '302497006'
    }

class HospiceCareAmbulatory(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients receiving hospice care outside of a hospital or long term care facility.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Order or Intervention, Order. The intent of this value set is to identify all patients receiving hospice care outside of a hospital or long term care facility.

    **Inclusion Criteria:** Includes only relevant concepts associated with hospice care concepts.

    **Exclusion Criteria:** Excludes concepts for palliative care or comfort measures.
    """

    OID = '2.16.840.1.113762.1.4.1108.15'
    VALUE_SET_NAME = 'Hospice care ambulatory'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '385763009',
        '385765002'
    }

class HospiceCareAmbulatory_1584(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients receiving hospice care outside of a hospital or long term care facility.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Procedure, Order or Intervention, Order. The intent of this value set is to identify all patients receiving hospice care outside of a hospital or long term care facility.

    **Inclusion Criteria:** Includes only relevant concepts associated with hospice care concepts.

    **Exclusion Criteria:** Excludes concepts for palliative care or comfort measures.
    """

    OID = '2.16.840.1.113883.3.526.3.1584'
    VALUE_SET_NAME = 'Hospice Care Ambulatory'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '385763009',
        '385765002'
    }

class HospitalServicesForUrologyCare(ValueSet):
    """
    **Clinical Focus:** This set of values focuses on hospital care, specifically for urology care.

    **Data Element Scope:** The intent of this data element is to define hospital CPT services used for urology care.

    **Inclusion Criteria:** Included CPT codes

    **Exclusion Criteria:** None
    """

    OID = '2.16.840.1.113762.1.4.1164.64'
    VALUE_SET_NAME = 'Hospital Services for urology care'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99217',
        '99218',
        '99219',
        '99220',
        '99221',
        '99222',
        '99223',
        '99231',
        '99232',
        '99233',
        '99234',
        '99235',
        '99236',
        '99238',
        '99239',
        '99251',
        '99281',
        '99282',
        '99283',
        '99284'
    }

class InfluenzaVaccination(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent influenza vaccinations.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with influenza vaccinations that are SNOMED CT, CPT, and HCPCS codes.

    **Exclusion Criteria:** Excludes CVX vaccine codes.
    """

    OID = '2.16.840.1.113883.3.526.3.402'
    VALUE_SET_NAME = 'Influenza Vaccination'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90630',
        '90653',
        '90654',
        '90655',
        '90656',
        '90657',
        '90658',
        '90661',
        '90662',
        '90666',
        '90667',
        '90668',
        '90673',
        '90674',
        '90682',
        '90685',
        '90686',
        '90687',
        '90688',
        '90689',
        '90694',
        '90756'
    }

    HCPCSLEVELII = {
        'G0008',
        'Q2034',
        'Q2035',
        'Q2036',
        'Q2037',
        'Q2038',
        'Q2039'
    }

    SNOMEDCT = {
        '86198006'
    }

class KidneyTransplant(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have undergone kidney transplant.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with kidney transplants.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1012'
    VALUE_SET_NAME = 'Kidney Transplant'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '50300',
        '50320',
        '50340',
        '50360',
        '50365',
        '50370',
        '50380'
    }

    HCPCSLEVELII = {
        'S2065'
    }

    ICD10PCS = {
        '0TY00Z0',
        '0TY00Z1',
        '0TY00Z2',
        '0TY10Z0',
        '0TY10Z1',
        '0TY10Z2'
    }

    SNOMEDCT = {
        '122531000119108',
        '128631000119109',
        '197747000',
        '213150003',
        '236436003',
        '236569000',
        '236570004',
        '236571000',
        '236572007',
        '236573002',
        '236574008',
        '236575009',
        '236576005',
        '236577001',
        '236578006',
        '236579003',
        '236580000',
        '236581001',
        '236582008',
        '236583003',
        '236584009',
        '236587002',
        '236588007',
        '236589004',
        '236614007',
        '277010001',
        '277011002',
        '426136000',
        '428575007',
        '429451003',
        '473195006',
        '58797008',
        '703048006',
        '707148007',
        '713825007'
    }

class LaboratoryTestsForHypertension(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests that are commonly used with patients diagnosed with hypertension.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with laboratory testing for patients diagnosed with hypertension.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1482'
    VALUE_SET_NAME = 'Laboratory Tests for Hypertension'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '24320-4',
        '24321-2',
        '24323-8',
        '24356-8',
        '24357-6',
        '24362-6',
        '2888-6',
        '57021-8',
        '57782-5',
        '58410-2'
    }

class LifestyleRecommendation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the type of interventions relevant to lifestyle needs.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure or Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with the type of lifestyle education, particularly that related to hyperyension.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1581'
    VALUE_SET_NAME = 'Lifestyle Recommendation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '313204009',
        '39155009',
        '443402002'
    }

class OtherServicesRelatedToDialysis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent services related to dialysis.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Intervention, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with other services related to dialysis.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1015'
    VALUE_SET_NAME = 'Other Services Related to Dialysis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '233591003',
        '251000124108',
        '311000124103',
        '3257008',
        '385970002',
        '385971003',
        '385973000',
        '406168002',
        '717738008',
        '718019005',
        '718308002',
        '718330001',
        '718331002',
        '73257006'
    }

class PalliativeOrHospiceCare(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent identifying patients receiving palliative, comfort or hospice care.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying patients receiving palliative, comfort or hospice care.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1579'
    VALUE_SET_NAME = 'Palliative or Hospice Care'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '103735009',
        '133918004',
        '182964004',
        '305284002',
        '305381007',
        '305981001',
        '306237005',
        '306288008',
        '385736008',
        '385763009'
    }

class PeritonealDialysis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the administration of peritoneal dialysis.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with the administration of peritoneal dialysis.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1084'
    VALUE_SET_NAME = 'Peritoneal Dialysis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90945',
        '90947',
        '90951',
        '90952',
        '90953',
        '90954',
        '90955',
        '90956',
        '90957',
        '90958',
        '90959',
        '90960',
        '90961',
        '90962',
        '90963',
        '90964',
        '90965',
        '90966',
        '90967',
        '90968',
        '90969',
        '90970'
    }

    SNOMEDCT = {
        '14684005',
        '225230008',
        '238318009',
        '238319001',
        '238321006',
        '238322004',
        '238323009',
        '428648006',
        '676002',
        '71192002'
    }

class ProstateCancerTreatment(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent prostate cancer treatments.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with interstitial prostate brachytherapy, external beam radiotherapy to the prostate and radical prostatectomy.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.398'
    VALUE_SET_NAME = 'Prostate Cancer Treatment'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '55810',
        '55812',
        '55815',
        '55840',
        '55842',
        '55845',
        '55866',
        '55875',
        '77427',
        '77435',
        '77772',
        '77778',
        '77799'
    }

    SNOMEDCT = {
        '10492003',
        '113120007',
        '116244007',
        '118161009',
        '118162002',
        '118163007',
        '14473006',
        '168922004',
        '169327006',
        '169328001',
        '169329009',
        '169340001',
        '169349000',
        '169359004',
        '176106009',
        '176258007',
        '176260009',
        '176261008',
        '176262001',
        '176263006',
        '176267007',
        '176288003',
        '19149007',
        '21190008',
        '21372000',
        '228677009',
        '228684001',
        '228688003',
        '228690002',
        '228692005',
        '228693000',
        '228694006',
        '228695007',
        '228697004',
        '228698009',
        '228699001',
        '228701001',
        '228702008',
        '236252003',
        '24242005',
        '26294005',
        '271291003',
        '27877006',
        '28579000',
        '30426000',
        '312235007',
        '314202001',
        '359922007',
        '359926005',
        '36253005',
        '37851009',
        '384691004',
        '384692006',
        '38915000',
        '394902000',
        '394918006',
        '399124002',
        '399180008',
        '399315003',
        '41371003',
        '41416003',
        '427541000119103',
        '427985002',
        '433224001',
        '440093006',
        '440094000',
        '57525009',
        '62867004',
        '65381004',
        '65551008',
        '67598001',
        '68986004',
        '72388004',
        '764675000',
        '77613002',
        '81232004',
        '83154001',
        '84755001',
        '85768003',
        '87795007',
        '8782006',
        '90199006',
        '90470006',
        '91531008'
    }

class RadiationTreatmentManagement(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent radiation treatment management.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with radiation treatment management.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1026'
    VALUE_SET_NAME = 'Radiation Treatment Management'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '77427',
        '77431',
        '77432',
        '77435'
    }

    SNOMEDCT = {
        '84755001'
    }

class RecommendationToIncreasePhysicalActivity(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent exercise, education and nutrition.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with promoting exercise and nutrition regimens.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1518'
    VALUE_SET_NAME = 'Recommendation to Increase Physical Activity'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    HCPCSLEVELII = {
        'S9451'
    }

    SNOMEDCT = {
        '281090004',
        '304507003',
        '304549008',
        '386291006',
        '386292004',
        '386373004',
        '386463000',
        '410289001'
    }

class Referral(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a referral for a patient to a practitioner for evaluation, treatment or co-management of a patient's condition.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with referrals and consultations.

    **Exclusion Criteria:** Excludes self referrals.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1046'
    VALUE_SET_NAME = 'Referral'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '103696004',
        '103697008',
        '103698003',
        '103699006',
        '103704003',
        '183515008',
        '183517000',
        '183528001',
        '183529009',
        '183530004',
        '183541002',
        '183555005',
        '183557002',
        '183561008',
        '183567007',
        '183569005',
        '183583007',
        '183591003',
        '183878008',
        '183879000',
        '183880002',
        '183881003',
        '183882005',
        '183884006',
        '183885007',
        '183886008',
        '183887004',
        '183888009',
        '183889001',
        '183890005',
        '183891009',
        '183892002',
        '183893007',
        '183894001',
        '183895000',
        '183896004',
        '183897008',
        '183899006',
        '183900001',
        '183901002',
        '183902009',
        '183903004',
        '183904005',
        '183905006',
        '183906007',
        '183907003',
        '183908008',
        '183909000',
        '183910005',
        '183911009',
        '183913007',
        '183914001',
        '183915000',
        '183916004',
        '266747000',
        '274410002',
        '306241009',
        '306242002',
        '306243007',
        '306245000',
        '306247008',
        '306250006',
        '306252003',
        '306253008',
        '306254002',
        '306255001',
        '306256000',
        '306257009',
        '306258004',
        '306259007',
        '306260002',
        '306261003',
        '306262005',
        '306263000',
        '306264006',
        '306265007',
        '306266008',
        '306267004',
        '306268009',
        '306269001',
        '306270000',
        '306271001',
        '306272008',
        '306273003',
        '306275005',
        '306276006',
        '306277002',
        '306278007',
        '306279004',
        '306280001',
        '306281002',
        '306282009',
        '306284005',
        '306285006',
        '306286007',
        '306287003',
        '306288008',
        '306289000',
        '306290009',
        '306291008',
        '306293006',
        '306294000',
        '306295004',
        '306296003',
        '306297007',
        '306298002',
        '306299005',
        '306300002',
        '306301003',
        '306302005',
        '306303000',
        '306304006',
        '306305007',
        '306306008',
        '306307004',
        '306308009',
        '306309001',
        '306310006',
        '306311005',
        '306312003',
        '306313008',
        '306314002',
        '306315001',
        '306316000',
        '306317009',
        '306318004',
        '306320001',
        '306338003',
        '306341007',
        '306342000',
        '306343005',
        '306351008',
        '306352001',
        '306353006',
        '306354000',
        '306355004',
        '306356003',
        '306357007',
        '306358002',
        '306359005',
        '306360000',
        '306361001',
        '306736002',
        '307063001',
        '307777008',
        '308439003',
        '308447003',
        '308449000',
        '308450000',
        '308451001',
        '308452008',
        '308453003',
        '308454009',
        '308455005',
        '308456006',
        '308459004',
        '308465004',
        '308469005',
        '308470006',
        '308471005',
        '308472003',
        '308473008',
        '308474002',
        '308475001',
        '308476000',
        '308477009',
        '308478004',
        '308479007',
        '308480005',
        '308481009',
        '308482002',
        '308483007',
        '308484001',
        '308485000',
        '309046007',
        '309623006',
        '309626003',
        '309627007',
        '309629005',
        '310515004',
        '312487009',
        '312488004',
        '390866009',
        '401266006',
        '406158007',
        '406159004',
        '408285001',
        '415277000',
        '416116000',
        '416999007',
        '425971006',
        '428441000124100',
        '428451000124103',
        '428461000124101',
        '428471000124108',
        '428481000124106',
        '428491000124109',
        '428541000124104',
        '429365000',
        '433151006',
        '448761000124106',
        '448771000124104',
        '54395008',
        '698563003',
        '698599008',
        '703974003',
        '703975002',
        '703976001',
        '716634006'
    }

class ReferralForAdolescentDepression(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent appropriate referrals specific to the child and adolescent age group for depression management.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with appropriate referrals as specific to the child and adolescent age group for depression management.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1570'
    VALUE_SET_NAME = 'Referral for Adolescent Depression'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183524004',
        '183583007',
        '183851006',
        '183866009',
        '306136006',
        '306137002',
        '306226009',
        '306227000',
        '306252003',
        '306291008',
        '306294000',
        '308459004',
        '308477009',
        '309627007',
        '390866009',
        '703978000',
        '710914003',
        '711281004'
    }

class ReferralForAdultDepression(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent appropriate referrals specific to the adult age group for depression management.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with appropriate referrals as specific to the adult age group for depression management.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1571'
    VALUE_SET_NAME = 'Referral for Adult Depression'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183524004',
        '183528001',
        '183583007',
        '183866009',
        '305922005',
        '306136006',
        '306137002',
        '306138007',
        '306204008',
        '306226009',
        '306227000',
        '306252003',
        '306294000',
        '308459004',
        '308477009',
        '390866009',
        '703978000',
        '710914003',
        '711281004'
    }

class ReferralOrCounselingForAlcoholConsumption(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the type of interventions relevant to alcohol use.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Procedure or Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with indicating the type of education provided, referral to community service or rehabilitation center for alcohol use.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1583'
    VALUE_SET_NAME = 'Referral or Counseling for Alcohol Consumption'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '24165007',
        '38670004',
        '390857005',
        '408947007',
        '413473000',
        '417096006',
        '431260004'
    }

class ReferralToPrimaryCareOrAlternateProvider(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent referrals to an alternate or primary care provider.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with the different types of services and providers.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1580'
    VALUE_SET_NAME = 'Referral to Primary Care or Alternate Provider'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '134403003',
        '183516009',
        '183561008',
        '183856001',
        '306206005',
        '306253008',
        '308470006'
    }

class ReferralsWhereWeightAssessmentMayOccur(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent multiple types of providers and settings for weight assessment.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with multiple providers in different settings performing weight assessments.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1527'
    VALUE_SET_NAME = 'Referrals Where Weight Assessment May Occur'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183515008',
        '183524004',
        '183583007',
        '306136006',
        '306163007',
        '306164001',
        '306165000',
        '306166004',
        '306167008',
        '306168003',
        '306226009',
        '306227000',
        '306252003',
        '306344004',
        '306353006',
        '306354000',
        '308459004',
        '308470006',
        '308477009',
        '390864007',
        '390866009',
        '390893007',
        '408289007',
        '416790000'
    }

class SalvageTherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent salvage therapy procedures.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with salvage therapy procedures.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.399'
    VALUE_SET_NAME = 'Salvage Therapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '51597',
        '55860',
        '55862',
        '55865'
    }

    SNOMEDCT = {
        '236209003',
        '236211007'
    }

class TobaccoUseCessationCounseling(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent various tobacco cessation counseling interventions.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention.

    **Inclusion Criteria:** Includes only relevant concepts associated with various cessation interventions which may include referral to tobacco-related services or providers, education about the benefits of stopping tobacco use, education about the negative side effects of using tobacco, and monitoring for tobacco cessation.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.509'
    VALUE_SET_NAME = 'Tobacco Use Cessation Counseling'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99406',
        '99407'
    }

    SNOMEDCT = {
        '171055003',
        '185795007',
        '185796008',
        '225323000',
        '225324006',
        '310429001',
        '315232003',
        '384742004',
        '395700008',
        '449841000124108',
        '449851000124105',
        '449861000124107',
        '449871000124100',
        '702388001',
        '710081004',
        '711028002',
        '713700008'
    }

class WeightReductionRecommended(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent management and maintenance of weight.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Intervention or Procedure.

    **Inclusion Criteria:** Includes only relevant concepts associated with interventions addressing healthy eating, goal setting, weight management and maintenance.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1510'
    VALUE_SET_NAME = 'Weight Reduction Recommended'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    HCPCSLEVELII = {
        'S9449'
    }

    SNOMEDCT = {
        '170795002',
        '266724001',
        '268523001',
        '408289007',
        '410200000'
    }
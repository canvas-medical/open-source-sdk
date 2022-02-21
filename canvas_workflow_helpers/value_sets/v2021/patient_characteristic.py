from ..value_set import ValueSet


class Ethnicity(ValueSet):
    """
    **Clinical Focus:**

    **Data Element Scope:**

    **Inclusion Criteria:**

    **Exclusion Criteria:**
    """

    OID = '2.16.840.1.114222.4.11.837'
    VALUE_SET_NAME = 'Ethnicity'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDCREC = {
        '2135-2',
        '2186-5'
    }

class Female(ValueSet):
    """
    **Clinical Focus:** Concepts that represent Female when assessing quality measures

    **Data Element Scope:** Gender

    **Inclusion Criteria:** Appropriate female gender concepts

    **Exclusion Criteria:** Concepts representing Male gender
    """

    OID = '2.16.840.1.113883.3.560.100.2'
    VALUE_SET_NAME = 'Female'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ADMINISTRATIVEGENDER = {
        'F'
    }

class FrailtySymptom(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent frailty symptoms.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Symptom.

    **Inclusion Criteria:** Includes only relevant concepts associated with frailty symptoms. This is a grouping of ICD10CM and SNOMEDCT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.113.12.1075'
    VALUE_SET_NAME = 'Frailty Symptom'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10CM = {
        'R260',
        'R261',
        'R262',
        'R2689',
        'R269',
        'R4181',
        'R531',
        'R5381',
        'R5383',
        'R54',
        'R627',
        'R634',
        'R636',
        'R64'
    }

    SNOMEDCT = {
        '102492002',
        '102568007',
        '102891000',
        '102992006',
        '105501005',
        '105503008',
        '105504002',
        '11172006',
        '11237000',
        '126013009',
        '127378008',
        '129567005',
        '129568000',
        '129584004',
        '135834002',
        '13791008',
        '152921000119101',
        '15929301000119104',
        '160681005',
        '160683008',
        '160684002',
        '160685001',
        '160692006',
        '160693001',
        '160734000',
        '160737007',
        '161832001',
        '161873000',
        '161874006',
        '162236007',
        '162239000',
        '163600007',
        '163685000',
        '163686004',
        '163688003',
        '163689006',
        '163690002',
        '163691003',
        '163695007',
        '16419651000119103',
        '165243005',
        '165244004',
        '16973004',
        '18726006',
        '20940004',
        '22090007',
        '22325002',
        '224960004',
        '225612007',
        '22631008',
        '23042008',
        '238108007',
        '248269005',
        '248278004',
        '248279007',
        '249888000',
        '249937002',
        '249938007',
        '249939004',
        '249940002',
        '249941003',
        '249942005',
        '249943000',
        '249946008',
        '250002000',
        '250003005',
        '250004004',
        '250005003',
        '250006002',
        '250008001',
        '250009009',
        '250011000',
        '250012007',
        '250013002',
        '250014008',
        '250015009',
        '250016005',
        '250018006',
        '250019003',
        '250020009',
        '250021008',
        '250023006',
        '250024000',
        '250027007',
        '250028002',
        '250029005',
        '250032008',
        '250033003',
        '250034009',
        '250035005',
        '250036006',
        '250038007',
        '250040002',
        '250042005',
        '250043000',
        '250044006',
        '250045007',
        '250047004',
        '250048009',
        '250049001',
        '250050001',
        '250051002',
        '250052009',
        '250055006',
        '250056007',
        '250057003',
        '250991000119100',
        '25136009',
        '262285001',
        '26544005',
        '267024001',
        '267032009',
        '268964003',
        '271706000',
        '271707009',
        '271795006',
        '271875007',
        '272036004',
        '27253007',
        '275313006',
        '284529003',
        '298283006',
        '300948004',
        '30767006',
        '309249007',
        '309257005',
        '312444006',
        '31464009',
        '35136003',
        '365884000',
        '367391008',
        '371028005',
        '373931001',
        '394616008',
        '397776000',
        '398218008',
        '401211005',
        '40192003',
        '404904002',
        '413121008',
        '414562003',
        '41786007',
        '418073009',
        '422868009',
        '424429009',
        '426977000',
        '428116008',
        '428264009',
        '429091008',
        '429487005',
        '43005009',
        '431524008',
        '432559006',
        '442099003',
        '44227003',
        '443544006',
        '444042007',
        '444932008',
        '4468000',
        '448765001',
        '48304002',
        '50314001',
        '52751000',
        '53626000',
        '55791005',
        '60631000119109',
        '60651000119103',
        '62334008',
        '67141003',
        '69021004',
        '69161000119103',
        '713512009',
        '713514005',
        '713568000',
        '713655003',
        '73514000',
        '75742003',
        '78119002',
        '78691002',
        '79021000119104',
        '79031000119101',
        '84153003',
        '84229001',
        '8461001',
        '8510008',
        '85711000119103',
        '87242005',
        '88471006',
        '89201000119106',
        '89362005',
        '931000119107',
        '9447003',
        '95438009'
    }

class Male(ValueSet):
    """
    **Clinical Focus:** Concepts that represent Male when assessing quality measures

    **Data Element Scope:** Gender

    **Inclusion Criteria:** Appropriate male gender concepts

    **Exclusion Criteria:** concepts representing Female gender
    """

    OID = '2.16.840.1.113883.3.560.100.1'
    VALUE_SET_NAME = 'Male'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ADMINISTRATIVEGENDER = {
        'M'
    }

class MorbidObesity(ValueSet):
    """
    **Clinical Focus:** This set of values focuses on morbid obesity as well as BMI ranges relating to morbid obesity.

    **Data Element Scope:** The intent of this data element is to identify morbid obesity by diagnosis and BMI values.

    **Inclusion Criteria:** Morbid obesity and associated BMI values

    **Exclusion Criteria:** None
    """

    OID = '2.16.840.1.113762.1.4.1164.67'
    VALUE_SET_NAME = 'Morbid Obesity'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10CM = {
        'E6601',
        'E662',
        'Z6841',
        'Z6842',
        'Z6843',
        'Z6844',
        'Z6845'
    }

    SNOMEDCT = {
        '238136002',
        '408512008'
    }

class OncAdministrativeSex(ValueSet):
    """
    **Clinical Focus:** Gender identity restricted to only Male and Female used in administrative situations requiring a restriction to these two categories.

    **Data Element Scope:** Gender

    **Inclusion Criteria:** Male and Female only.

    **Exclusion Criteria:** Any gender identity that is not male or female.
    """

    OID = '2.16.840.1.113762.1.4.1'
    VALUE_SET_NAME = 'ONC Administrative Sex'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ADMINISTRATIVEGENDER = {
        'F',
        'M'
    }

class Race(ValueSet):
    """
    **Clinical Focus:**

    **Data Element Scope:**

    **Inclusion Criteria:**

    **Exclusion Criteria:**
    """

    OID = '2.16.840.1.114222.4.11.836'
    VALUE_SET_NAME = 'Race'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDCREC = {
        '1002-5',
        '2028-9',
        '2054-5',
        '2076-8',
        '2106-3',
        '2131-1'
    }

class TobaccoUser(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent tobacco user status.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute.

    **Inclusion Criteria:** Includes only relevant concepts associated with indicating a patient uses tobacco products, including smoking and smoke-less tobacco products such as chew, snuff, pipe, cigarette, cigar, etc.

    **Exclusion Criteria:** Excludes concepts that may indicate a current tobacco non-user status.
    """

    OID = '2.16.840.1.113883.3.526.3.1170'
    VALUE_SET_NAME = 'Tobacco User'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '110483000',
        '160603005',
        '160604004',
        '160605003',
        '160606002',
        '160619003',
        '228494002',
        '228499007',
        '228504007',
        '228514003',
        '228515002',
        '228516001',
        '228517005',
        '228518000',
        '230059006',
        '230060001',
        '230062009',
        '230063004',
        '230064005',
        '230065006',
        '266920004',
        '428041000124106',
        '428061000124105',
        '428071000124103',
        '43381005',
        '449867007',
        '449868002',
        '449869005',
        '450811000124104',
        '450821000124107',
        '56578002',
        '56771006',
        '59978006',
        '65568007',
        '713914004',
        '77176002',
        '81703003',
        '82302008'
    }

class White(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient's race as white.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Patient Characteristic Race.

    **Inclusion Criteria:** Includes only relevant concepts associated with a code to identify a patient's race as white. This is a grouping of a CDCREC code.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.123.12.1007'
    VALUE_SET_NAME = 'White'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDCREC = {
        '2106-3'
    }
from ..value_set import ValueSet


class ModerateOrSevere(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent severe and moderate levels of severity.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) attribute related to Severity.

    **Inclusion Criteria:** Includes only relevant concepts associated with specific to severe and moderate levels of severity.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1092'
    VALUE_SET_NAME = 'Moderate or Severe'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '24484000',
        '6736007'
    }

class Payer(ValueSet):
    """
    **Clinical Focus:** Categories of types of health care payor entities as defined by the US Public Health Data Consortium SOP code system

    **Data Element Scope:** @code in CCDA r2.1 template Planned Coverage [act: identifier urn:oid:2.16.840.1.113883.10.20.22.4.129 (open)] DYNAMIC

    **Inclusion Criteria:** All codes in the code system

    **Exclusion Criteria:** none
    """

    OID = '2.16.840.1.114222.4.11.3591'
    VALUE_SET_NAME = 'Payer'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SOP = {
        '1',
        '11',
        '111',
        '112',
        '113',
        '119',
        '12',
        '121',
        '122',
        '123',
        '129',
        '13',
        '14',
        '19',
        '191',
        '2',
        '21',
        '211',
        '212',
        '213',
        '219',
        '22',
        '23',
        '25',
        '26',
        '29',
        '291',
        '299',
        '3',
        '31',
        '311',
        '3111',
        '3112',
        '3113',
        '3114',
        '3115',
        '3116',
        '3119',
        '312',
        '3121',
        '3122',
        '3123',
        '313',
        '32',
        '321',
        '3211',
        '3212',
        '32121',
        '32122',
        '32123',
        '32124',
        '32125',
        '32126',
        '32127',
        '32128',
        '322',
        '3221',
        '3222',
        '3223',
        '3229',
        '33',
        '331',
        '332',
        '333',
        '334',
        '34',
        '341',
        '342',
        '343',
        '349',
        '35',
        '36',
        '361',
        '362',
        '369',
        '37',
        '371',
        '3711',
        '3712',
        '3713',
        '372',
        '379',
        '38',
        '381',
        '3811',
        '3812',
        '3813',
        '3819',
        '382',
        '389',
        '39',
        '391',
        '4',
        '41',
        '42',
        '43',
        '44',
        '5',
        '51',
        '511',
        '512',
        '513',
        '514',
        '515',
        '516',
        '517',
        '519',
        '52',
        '521',
        '522',
        '523',
        '524',
        '529',
        '53',
        '54',
        '55',
        '56',
        '561',
        '562',
        '59',
        '6',
        '61',
        '611',
        '612',
        '613',
        '614',
        '619',
        '62',
        '621',
        '622',
        '623',
        '629',
        '7',
        '71',
        '72',
        '73',
        '79',
        '8',
        '81',
        '82',
        '821',
        '822',
        '823',
        '83',
        '84',
        '85',
        '89',
        '9',
        '91',
        '92',
        '93',
        '94',
        '95',
        '951',
        '953',
        '954',
        '959',
        '96',
        '97',
        '98',
        '99',
        '9999'
    }
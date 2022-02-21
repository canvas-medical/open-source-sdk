from ..value_set import ValueSet


class PositiveFinding(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent positive test results. This is intended to be paired with other concepts that identify specific medical tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Result.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a positive test result.

    **Exclusion Criteria:** Excludes concepts that identify a specific type of medical test.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1016'
    VALUE_SET_NAME = 'Positive Finding'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '441773004'
    }

class TobaccoNonUser(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent tobacco non-user status.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Result.

    **Inclusion Criteria:** Includes only relevant concepts associated with indicating a patient does not use tobacco products, including smoking and smoke-less tobacco products such as chew, snuff, pipe, cigarette, cigar, etc.

    **Exclusion Criteria:** Excludes concepts that may indicate a current tobacco user status.
    """

    OID = '2.16.840.1.113883.3.526.3.1189'
    VALUE_SET_NAME = 'Tobacco Non-User'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '105539002',
        '105540000',
        '105541001',
        '160618006',
        '160620009',
        '160621008',
        '228491005',
        '228492003',
        '228493008',
        '228501004',
        '228502006',
        '228503001',
        '228511006',
        '228512004',
        '228513009',
        '266919005',
        '266921000',
        '266922007',
        '266923002',
        '266924008',
        '266925009',
        '266928006',
        '281018007',
        '360890004',
        '360900008',
        '360918006',
        '360929005',
        '405746006',
        '428081000124100',
        '428091000124102',
        '451371000124109',
        '451381000124107',
        '456711000124105',
        '48031000119106',
        '53896009',
        '702975009',
        '702979003',
        '735128000',
        '8392000',
        '8517006',
        '87739003'
    }

class VisualAcuity2040OrBetter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visual acuity findings that are 20/40 or better.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Result.

    **Inclusion Criteria:** Includes only relevant concepts associated with distance vision findings of 20/40 or better.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1483'
    VALUE_SET_NAME = 'Visual Acuity 20/40 or Better'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '422497000',
        '423059004',
        '423364005',
        '423862000',
        '424703005'
    }
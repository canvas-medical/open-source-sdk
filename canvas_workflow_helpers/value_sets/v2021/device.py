from ..value_set import ValueSet


class CardiacPacer(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a cardiac pacer device.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Device.

    **Inclusion Criteria:** Includes only relevant concepts associated with a cardiac pacer device.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1193'
    VALUE_SET_NAME = 'Cardiac Pacer'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '14106009',
        '360127006',
        '360128001',
        '424921004',
        '56961003'
    }

class FrailtyDevice(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent durable medical equipment or devices used by frail patients.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Device.

    **Inclusion Criteria:** Includes only relevant concepts associated with patients that use durable medical equipment or devices for frailty. This is a grouping of HCPCS codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.118.12.1300'
    VALUE_SET_NAME = 'Frailty Device'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '105501005',
        '105503008',
        '105504002',
        '152921000119101',
        '160683008',
        '160684002',
        '160685001',
        '16419651000119103',
        '165243005',
        '165244004',
        '225612007',
        '413121008',
        '429091008',
        '429487005',
        '444932008',
        '60631000119109',
        '60651000119103',
        '713655003',
        '79021000119104',
        '79031000119101',
        '89201000119106',
        '931000119107'
    }
from ..value_set import ValueSet


class MedicalReason(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent medical reasons for when a patient does not receive a therapy or service.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Negation Rationale.

    **Inclusion Criteria:** Includes only relevant concepts associated with medically relevant reasons for not receiving a therapy or service.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1007'
    VALUE_SET_NAME = 'Medical Reason'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183932001',
        '183964008',
        '183966005',
        '266721009',
        '269191009',
        '31438003',
        '35688006',
        '397745006',
        '407563006',
        '410534003',
        '410536001',
        '416098002',
        '428119001',
        '59037007',
        '62014003',
        '79899007'
    }

class PatientDeclined(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a reason for patient refusal.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Negation Rationale.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a patient's reason for refusing treatment.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.791'
    VALUE_SET_NAME = 'Patient Declined'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '105480006',
        '183944003',
        '183945002',
        '413310006',
        '413311005',
        '413312003'
    }

class PatientDeclined_1582(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a reason for patient refusal.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Negation Rationale.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a patient's reason for refusing treatment.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1582'
    VALUE_SET_NAME = 'Patient Declined'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '105480006',
        '183944003',
        '183945002',
        '413310006',
        '413311005',
        '413312003'
    }

class PatientReason(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patient-specific reasons for when a patient does not receive a therapy or service.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Negation Rationale.

    **Inclusion Criteria:** Includes only relevant concepts associated with patient-specific reasons for not receiving a therapy or service.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1008'
    VALUE_SET_NAME = 'Patient Reason'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '105480006',
        '160932005',
        '160934006',
        '182890002',
        '182895007',
        '182897004',
        '182900006',
        '182902003',
        '183944003',
        '183945002',
        '184081006',
        '185479006',
        '185481008',
        '224187001',
        '225928004',
        '266710000',
        '266966009',
        '275694009',
        '275936005',
        '281399006',
        '310343007',
        '373787003',
        '406149000',
        '408367005',
        '413310006',
        '413311005',
        '413312003',
        '416432009',
        '423656007',
        '424739004',
        '443390004',
        '713247000'
    }

class SystemReason(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent system-specific reasons for when a patient does not receive a therapy or service.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) attribute related to Negation Rationale.

    **Inclusion Criteria:** Includes only relevant concepts associated with system-specific reasons for not receiving a therapy or service.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1009'
    VALUE_SET_NAME = 'System Reason'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '107724000',
        '182856006',
        '182857002',
        '185335007',
        '224194003',
        '224198000',
        '224199008',
        '242990004',
        '266756008',
        '270459005',
        '309017000',
        '309846006',
        '419808006',
        '424553001'
    }
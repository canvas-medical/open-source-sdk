from ..value_set import ValueSet


class EggSubstance(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent an allergy or intolerance to an egg substance.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Allergy/Intolerance.

    **Inclusion Criteria:** Includes only relevant concepts associated with an allergy or intolerance to an egg substance.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1537'
    VALUE_SET_NAME = 'Egg Substance'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '102263004',
        '226881001',
        '226885005',
        '229955000',
        '256442007',
        '256443002',
        '286550009',
        '303300008',
        '414074006'
    }
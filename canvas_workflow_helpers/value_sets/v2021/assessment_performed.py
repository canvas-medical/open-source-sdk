from ..value_set import ValueSet


class AverageNumberOfDrinksPerDrinkingDay(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient's number of alcoholic drinks per drinking day.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a quantitative observation of the reported number of alcoholic drinks per drinking day. This is a grouping of a LOINC code.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.106.12.1018'
    VALUE_SET_NAME = 'Average Number of Drinks per Drinking Day'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '11287-0'
    }

class FallsScreening(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent assessment tools or instruments used to quantify fall risk.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with fall risk assessment tools and screening assessments used to evaluate fall risk such as the Get Up and Go Test, Morse falls risk assessment, multidisciplinary team falls assessment, and history of falls. This is a grouping of LOINC and SNOMED CT codes.

    **Exclusion Criteria:** Excludes codes that indicate falls for children or falls that take place in an inpatient setting.
    """

    OID = '2.16.840.1.113883.3.464.1003.118.12.1028'
    VALUE_SET_NAME = 'Falls Screening'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '52552-7',
        '57254-5',
        '59454-9',
        '73830-2'
    }

class HipDysfunctionAndOsteoarthritisOutcomeScoreForJointReplacementHoosjr(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the Hip Dysfunction and Osteoarthritis Outcome Score for Joint Replacement (HOOS Jr.) total interval score.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying the Hip Dysfunction and Osteoarthritis Outcome Score for Joint Replacement (HOOS Jr.) total interval score. This is a grouping of a LOINC code.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.118.12.1210'
    VALUE_SET_NAME = 'Hip Dysfunction and Osteoarthritis Outcome Score for Joint Replacement [HOOSJR]'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '82323-7'
    }

class HistoryOfHipFractureInParent(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a family history of fracture in a parent.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with a patient has a family history of fracture in a parent. This is a grouping of SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.113.12.1040'
    VALUE_SET_NAME = 'History of hip fracture in parent'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '391096007',
        '416072008',
        '445121000124105',
        '445501000124107'
    }

class KneeInjuryAndOsteoarthritisOutcomeScoreForJointReplacementKoosjr(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the Knee Injury and Osteoarthritis Outcome Score for Joint Replacement (KOOS Jr.) total interval score.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with the Knee Injury and Osteoarthritis Outcome Score for Joint Replacement (KOOS Jr.) score. This is a grouping of a LOINC code.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.118.12.1218'
    VALUE_SET_NAME = 'Knee Injury and Osteoarthritis Outcome Score for Joint Replacement [KOOSJR]'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '82324-5'
    }

class Phq9AndPhq9MTools(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the PHQ 9 and PHQ 9M depression assessment scores for  adults and adolescents.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with LOINC codes that indicate a completed PHQ 9 and PHQ 9M depression assessment tool for adults and adolescents with a summary score.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.67.1.101.1.263'
    VALUE_SET_NAME = 'PHQ 9 and PHQ 9M Tools'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '44261-6',
        '89204-2'
    }

class SexuallyActive(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent vaginal intercourse.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Assessment, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with concepts that indicate whether a patient has had vaginal intercourse.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1040'
    VALUE_SET_NAME = 'Sexually Active'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '64728-9'
    }
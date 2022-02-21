from ..value_set import ValueSet


class NegativeDepressionScreening(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent situations in which a depression screen was performed by the health care professional and the finding was negative for depression.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with screening for depression whereby the outcome is negative.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1564'
    VALUE_SET_NAME = 'Negative Depression Screening'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '428171000124102'
    }

class PositiveDepressionScreening(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent situations in which a depression screen was performed by the health care professional and the finding or result was positive for depression.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with screening for depression whereby the outcome is positive.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1565'
    VALUE_SET_NAME = 'Positive Depression Screening'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '428181000124104'
    }

class StandardizedPainAssessmentTool(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent pain assessment tools or instruments used to quantify pain intensity.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with pain assessment tools or instruments used to quantify pain intensity such as 0-10 numerical rating scale, visual analog scale, a categorical scale, pictorial scale, faces pain rating scale, or the Brief Pain Inventory (BPI).

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1028'
    VALUE_SET_NAME = 'Standardized Pain Assessment Tool'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '38208-5',
        '38214-3',
        '38221-8',
        '72514-3',
        '77565-0'
    }

class StandardizedToolsForAssessmentOfCognition(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the total score results for the standardized tools used for the assessment of cognition.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with total score results for the following standardized tools: -Blessed Orientation-Memory-Concentration Test (BOMC) -Montreal Cognitive Assessment (MoCA) -St. Louis University Mental Status Examination (SLUMS) -Mini-Mental State Examination (MMSE) [Note: The MMSE has not been well validated for non-Alzheimer's dementias] -Short Informant Questionnaire on Cognitive Decline in the Elderly (IQCODE) -Ascertain Dementia 8 (AD8) Questionnaire -Minimum Data Set (MDS) Brief Interview of Mental Status (BIMS) [Note: Validated for use with nursing home patients only] -Formal neuropsychological evaluation -Mini-Cog.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1006'
    VALUE_SET_NAME = 'Standardized Tools for Assessment of Cognition'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '58151-2',
        '71492-3',
        '71493-1',
        '71722-3',
        '72106-8',
        '72172-0',
        '72173-8',
        '72233-0'
    }

class TobaccoUseScreening(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent screening for tobacco use.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with screening tools or questions used to obtain a patient's tobacco use status.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1278'
    VALUE_SET_NAME = 'Tobacco Use Screening'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '39240-7',
        '68535-4',
        '68536-2',
        '72166-2'
    }

class UrinaryRetention(ValueSet):
    """
    **Clinical Focus:** This set of values focuses on urinary retention related to drugs or other causes.

    **Data Element Scope:** The intent of this data element is to define urinary retention.

    **Inclusion Criteria:** Urinary retention related to drugs or other causes

    **Exclusion Criteria:** None
    """

    OID = '2.16.840.1.113762.1.4.1164.52'
    VALUE_SET_NAME = 'Urinary retention'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10CM = {
        'R330',
        'R338',
        'R339'
    }

    SNOMEDCT = {
        '12245681000119103',
        '236648008',
        '267064002'
    }
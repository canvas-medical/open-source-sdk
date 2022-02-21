from ..value_set import ValueSet


class BestCorrectedVisualAcuityExamUsingSnellenChart(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent best corrected visual acuity exams using a Snellen chart.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Physical Exam.

    **Inclusion Criteria:** Includes only relevant concepts associated with best corrected visual acuity exams using a Snellen chart.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1560'
    VALUE_SET_NAME = 'Best Corrected Visual Acuity Exam Using Snellen Chart'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '79880-1',
        '79881-9'
    }

class BmiPercentile(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent BMI percentile.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Physical Exam, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying BMI percentile as a result. This is a grouping of LOINC codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1012'
    VALUE_SET_NAME = 'BMI percentile'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '59574-4',
        '59575-1',
        '59576-9'
    }

class HeartRate(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent heart rate.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Physical Exam.

    **Inclusion Criteria:** Includes only relevant concepts associated with obtaining heart rate.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1176'
    VALUE_SET_NAME = 'Heart Rate'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '68999-2',
        '69000-8',
        '69001-6',
        '8867-4'
    }

class Height(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient's height has been measured or observed.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Physical Exam, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying if a patient's height has been measured or observed. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes codes that are expressed as a percentile, stated by a patient, post-partum or estimated.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1014'
    VALUE_SET_NAME = 'Height'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '3137-7',
        '8302-2',
        '8306-3',
        '8307-1',
        '8308-9'
    }

class RetinalOrDilatedEyeExam(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have received a retinal or dilated eye exam.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Physical Exam, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with procedural codes that indicate a retinal and dilated eye exam took place.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.115.12.1088'
    VALUE_SET_NAME = 'Retinal or Dilated Eye Exam'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '252779009',
        '252780007',
        '252781006',
        '252782004',
        '252783009',
        '252784003',
        '252788000',
        '252789008',
        '252790004',
        '274795007',
        '274798009',
        '308110009',
        '314971001',
        '314972008',
        '410451008',
        '410452001',
        '410453006',
        '410455004',
        '420213007',
        '425816006',
        '427478009',
        '6615001',
        '722161008'
    }

class Weight(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent that a patient's weight has been measured.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Physical Exam, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a patient's weight has been measured. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes codes for patient's ideal body weight, estimated body weight and measured/calculated body fat.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1015'
    VALUE_SET_NAME = 'Weight'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '18833-4',
        '29463-7',
        '3141-9',
        '3142-7',
        '8341-0',
        '8349-3',
        '8350-1',
        '8351-9'
    }
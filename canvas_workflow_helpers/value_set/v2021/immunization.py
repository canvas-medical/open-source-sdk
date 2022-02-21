from ..value_set import ValueSet


class DtapVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent diphtheria, tetanus, and whooping cough (pertussis) (DTaP) vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with diphtheria, tetanus, and whooping cough (pertussis) (DTaP) vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1214'
    VALUE_SET_NAME = 'DTaP Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '106',
        '107',
        '110',
        '120',
        '20',
        '50'
    }

class HepatitisAVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent hepatitis A vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant hepatitis A vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1215'
    VALUE_SET_NAME = 'Hepatitis A Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '31',
        '83',
        '85'
    }

class HepatitisBVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent hepatitis B vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant hepatitis B vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1216'
    VALUE_SET_NAME = 'Hepatitis B Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '08',
        '110',
        '44',
        '45',
        '51'
    }

class HibVaccine3DoseSchedule(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent haemophilus influenzae type b (Hib) vaccines (3-dose schedule).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with haemophilus influenzae type b (Hib) vaccine codes (3-dose schedule). This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1083'
    VALUE_SET_NAME = 'Hib Vaccine (3 dose schedule)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '49'
    }

class HibVaccine4DoseSchedule(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent haemophilus influenzae type b (Hib) vaccines (4-dose schedule).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with haemophilus influenzae type b (Hib) vaccine codes (4-dose schedule). This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1085'
    VALUE_SET_NAME = 'Hib Vaccine (4 dose schedule)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '120',
        '148',
        '48',
        '50',
        '51'
    }

class InactivatedPolioVaccineIpv(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent inactivated polio vaccines (IPV).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all inactivated polio vaccine (IPV) codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1219'
    VALUE_SET_NAME = 'Inactivated Polio Vaccine (IPV)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '10',
        '110',
        '120',
        '89'
    }

class InfluenzaVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent influenza vaccine codes.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with influenza vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1218'
    VALUE_SET_NAME = 'Influenza Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '135',
        '140',
        '141',
        '150',
        '153',
        '155',
        '158',
        '161',
        '88'
    }

class InfluenzaVaccine_1254(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent influenza vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Immunization.

    **Inclusion Criteria:** Includes only relevant concepts associated with CVX concepts related to influenza vaccines.

    **Exclusion Criteria:** Excludes HCPCS, SNOMED CT and CPT influenza vaccine codes.
    """

    OID = '2.16.840.1.113883.3.526.3.1254'
    VALUE_SET_NAME = 'Influenza Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '135',
        '140',
        '141',
        '144',
        '150',
        '155',
        '158',
        '161',
        '166',
        '168',
        '171',
        '185',
        '186',
        '197',
        '88'
    }

class MeaslesMumpsAndRubellaMmrVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent measles, mumps and rubella (MMR) vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant measles, mumps and rubella (MMR) Vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1224'
    VALUE_SET_NAME = 'Measles, Mumps and Rubella (MMR) Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '03',
        '94'
    }

class PneumococcalConjugateVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent pneumococcal vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all pneumococcal vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1221'
    VALUE_SET_NAME = 'Pneumococcal Conjugate Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '133',
        '152'
    }

class PneumococcalVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent conjugate and polysaccharide pneumococcal vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable. Includes only relevant concepts associated with the pneumococcal conjugate 13-valent and the pneumococcal polysaccharide 23-valent vaccine. This is a grouping of CVX codes.

    **Exclusion Criteria:** Excludes codes that represent the pneumococcal conjugate 7-valent vaccine.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1027'
    VALUE_SET_NAME = 'Pneumococcal Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '109',
        '133',
        '152',
        '33'
    }

class RotavirusVaccine2DoseScheduleAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent rotavirus (2-dose schedule) vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all rotavirus (2-dose schedule) vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1048'
    VALUE_SET_NAME = 'Rotavirus Vaccine (2 dose schedule) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90681'
    }

    SNOMEDCT = {
        '434741000124104'
    }

class RotavirusVaccine3DoseSchedule(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent rotavirus (3-dose schedule) vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all rotavirus (3-dose schedule) vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1223'
    VALUE_SET_NAME = 'Rotavirus Vaccine (3 dose schedule)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '116',
        '122'
    }

class RotavirusVaccine3DoseScheduleAdministered(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent rotavirus (3-dose schedule) vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all rotavirus (3-dose schedule) vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1047'
    VALUE_SET_NAME = 'Rotavirus Vaccine (3 dose schedule) Administered'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90680'
    }

    SNOMEDCT = {
        '434731000124109'
    }

class VaricellaZosterVaccineVzv(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent varicella zoster vaccines.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Immunization, Administered.

    **Inclusion Criteria:** Includes only relevant concepts associated with all relevant varicella zoster vaccine codes. This is a grouping of CVX codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1170'
    VALUE_SET_NAME = 'Varicella Zoster Vaccine (VZV)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CVX = {
        '21',
        '94'
    }
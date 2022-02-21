from ..value_set import ValueSet


class AntiHepatitisAIggAntigenTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests to detect anti hepatitis A immunoglobulin (IgG) antibodies.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test

    **Inclusion Criteria:** Includes only relevant concepts associated with test codes for IgG antibody to hepatitis A.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1033'
    VALUE_SET_NAME = 'Anti Hepatitis A IgG Antigen Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '32018-4',
        '40724-7',
        '51913-2'
    }

class AntiHepatitisBVirusSurfaceAb(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests to detect anti hepatitis B surface antigen in the blood.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with test codes for anti-surface antibody in the blood related to hepatitis B virus.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1073'
    VALUE_SET_NAME = 'Anti Hepatitis B Virus Surface Ab'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '10900-9',
        '22322-2',
        '39535-0',
        '48070-7',
        '49177-9',
        '75409-3'
    }

class ChlamydiaScreening(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory testing for chlamydia infections.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with tests for chlamydia infection. This is a grouping of LOINC codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1052'
    VALUE_SET_NAME = 'Chlamydia Screening'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '14463-4',
        '14464-2',
        '14467-5',
        '14474-1',
        '14513-6',
        '16600-9',
        '21190-4',
        '21191-2',
        '21613-5',
        '23838-6',
        '31775-0',
        '31777-6',
        '36902-5',
        '36903-3',
        '42931-6',
        '43304-5',
        '43404-3',
        '43405-0',
        '43406-8',
        '44806-8',
        '44807-6',
        '45068-4',
        '45069-2',
        '45075-9',
        '45076-7',
        '45084-1',
        '45091-6',
        '45095-7',
        '45098-1',
        '45100-5',
        '47211-8',
        '47212-6',
        '49096-1',
        '4993-2',
        '50387-0',
        '53925-4',
        '53926-2',
        '557-9',
        '560-3',
        '6349-5',
        '6354-5',
        '6355-2',
        '6356-0',
        '6357-8',
        '80360-1',
        '80361-9',
        '80362-7'
    }

class FecalOccultBloodTestFobt(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a fecal occult blood test.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying tests for occult blood in stool. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes tests for occult blood in other parts of the body. Excludes codes that indicate that this test was ordered only, and not necessarily performed.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1011'
    VALUE_SET_NAME = 'Fecal Occult Blood Test (FOBT)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '12503-9',
        '12504-7',
        '14563-1',
        '14564-9',
        '14565-6',
        '2335-8',
        '27396-1',
        '27401-9',
        '27925-7',
        '27926-5',
        '29771-3',
        '56490-6',
        '56491-4',
        '57905-2',
        '58453-2',
        '80372-6'
    }

class FitDna(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a fecal immunochemical (FIT) DNA test.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying a FIT DNA laboratory test. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes codes that indicate that this test was ordered only, and not necessarily performed.
    """

    OID = '2.16.840.1.113883.3.464.1003.108.12.1039'
    VALUE_SET_NAME = 'FIT DNA'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '77353-1',
        '77354-9'
    }

class GroupAStreptococcusTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests for group A streptococcus.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test.

    **Inclusion Criteria:** Includes only relevant concepts associated with laboratory tests used to identify the presence of group A streptococcus in the throat.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1012'
    VALUE_SET_NAME = 'Group A Streptococcus Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '11268-0',
        '17656-0',
        '17898-8',
        '18481-2',
        '31971-5',
        '49610-9',
        '5036-9',
        '60489-2',
        '626-2',
        '6557-3',
        '6558-1',
        '6559-9',
        '68954-7',
        '78012-2'
    }

class Hba1CLaboratoryTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent hemoglobin A1c laboratory tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying hemoglobin A1c laboratory tests.

    **Exclusion Criteria:** Excludes codes that identify hemoglobin A1c laboratory tests that use the International Federation of Clinical Chemistry and Laboratory Medicine (IFCC)   protocol and Japanese Diabetes Society (JDS)/Japanese Society of Clinical Chemistry (JSCC) protocol.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1013'
    VALUE_SET_NAME = 'HbA1c Laboratory Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '17856-6',
        '4548-4',
        '4549-2'
    }

class HpvTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent identify high-risk human papilloma virus (HPV) tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with high-risk HPV tests performed on cervical samples. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes high-risk HPV tests conducted on non-cervical samples. Excludes codes that indicate that this test was ordered only, and not necessarily performed.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1059'
    VALUE_SET_NAME = 'HPV Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '21440-3',
        '30167-1',
        '38372-9',
        '59263-4',
        '59264-2',
        '59420-0',
        '69002-4',
        '71431-1',
        '75406-9',
        '75694-0',
        '77379-6',
        '77399-4',
        '77400-0',
        '82354-2',
        '82456-5',
        '82675-0'
    }

class HumanImmunodeficiencyVirusHivLaboratoryTestCodesAbAndAg(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests used for Human Immunodeficiency Virus screening.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test. Used for HIV screening.

    **Inclusion Criteria:** Includes only relevant concepts associated with laboratory tests for HIV-1 and HIV-2 antibodies or antigens.

    **Exclusion Criteria:** Excludes tests and procedures that might be associated with HIV infection that are not used for screening or testing to establish an HIV diagnosis, which would include home/self HIV testing, HIV genotyping tests, HIV RNA tests, HIV cultures, clinical codes used to document care provided to HIV-infected patients.
    """

    OID = '2.16.840.1.113762.1.4.1056.50'
    VALUE_SET_NAME = 'Human Immunodeficiency Virus (HIV) Laboratory Test Codes (Ab and Ag)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '10901-7',
        '10902-5',
        '11078-3',
        '11079-1',
        '11080-9',
        '11081-7',
        '11082-5',
        '12855-3',
        '12856-1',
        '12857-9',
        '12858-7',
        '12859-5',
        '12870-2',
        '12871-0',
        '12872-8',
        '12875-1',
        '12876-9',
        '12893-4',
        '12894-2',
        '12895-9',
        '13499-9',
        '13920-4',
        '14092-1',
        '14126-7',
        '16132-3',
        '16974-8',
        '16975-5',
        '16976-3',
        '16977-1',
        '16978-9',
        '16979-7',
        '18396-2',
        '19110-6',
        '21007-0',
        '21331-4',
        '21332-2',
        '21334-8',
        '21335-5',
        '21336-3',
        '21337-1',
        '21338-9',
        '21339-7',
        '21340-5',
        '22356-0',
        '22357-8',
        '22358-6',
        '24012-7',
        '28004-0',
        '28052-9',
        '29327-4',
        '29893-5',
        '30361-0',
        '31072-2',
        '31073-0',
        '31201-7',
        '31430-2',
        '32571-2',
        '32602-5',
        '32827-8',
        '32842-7',
        '33508-3',
        '33660-2',
        '33806-1',
        '33807-9',
        '33866-5',
        '34591-8',
        '34592-6',
        '35437-3',
        '35438-1',
        '35439-9',
        '35440-7',
        '35441-5',
        '35442-3',
        '35443-1',
        '35444-9',
        '35445-6',
        '35446-4',
        '35447-2',
        '35448-0',
        '35449-8',
        '35450-6',
        '35452-2',
        '35564-4',
        '35565-1',
        '40437-6',
        '40438-4',
        '40439-2',
        '40732-0',
        '40733-8',
        '41143-9',
        '41144-7',
        '41145-4',
        '41290-8',
        '42339-2',
        '42600-7',
        '42627-0',
        '42768-2',
        '43008-2',
        '43009-0',
        '43010-8',
        '43011-6',
        '43012-4',
        '43013-2',
        '43185-8',
        '43599-0',
        '44531-2',
        '44532-0',
        '44533-8',
        '44607-0',
        '44872-0',
        '44873-8',
        '45212-8',
        '47029-4',
        '48345-3',
        '48346-1',
        '49483-1',
        '49580-4',
        '49718-0',
        '49905-3',
        '49965-7',
        '51786-2',
        '51866-2',
        '5220-9',
        '5221-7',
        '5222-5',
        '5223-3',
        '5224-1',
        '5225-8',
        '53379-4',
        '53601-1',
        '54086-4',
        '56888-1',
        '57974-8',
        '57975-5',
        '57976-3',
        '57977-1',
        '57978-9',
        '58900-2',
        '62456-9',
        '68961-2',
        '69668-2',
        '73905-2',
        '73906-0',
        '75622-1',
        '75666-8',
        '77685-6',
        '7917-8',
        '7918-6',
        '7919-4',
        '80203-3',
        '80387-4',
        '81641-3',
        '83101-6',
        '85037-0',
        '85686-4',
        '86233-4',
        '86657-4',
        '89365-1',
        '89374-3',
        '9660-2',
        '9661-0',
        '9662-8',
        '9663-6',
        '9664-4',
        '9665-1',
        '9666-9',
        '9667-7',
        '9668-5',
        '9669-3',
        '9821-0'
    }

class LabTestsDuringPregnancy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent lab tests conducted during pregnancy (e.g., tests conducted on amniotic fluid).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test.

    **Inclusion Criteria:** Includes only relevant concepts associated with laboratory tests conducted during pregnancy. This is a grouping of LOINC codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.111.12.1007'
    VALUE_SET_NAME = 'Lab Tests During Pregnancy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '15019-3',
        '1832-5',
        '1834-1',
        '19171-8',
        '19176-7',
        '19177-5',
        '20403-2',
        '20404-0',
        '31993-9',
        '33773-3',
        '34493-7',
        '34656-9',
        '34718-7',
        '35457-1',
        '41273-4',
        '41274-2',
        '42316-0',
        '43798-8',
        '45273-0',
        '45331-6',
        '45332-4',
        '46731-6',
        '46989-0',
        '48030-1',
        '48039-2',
        '48781-9',
        '49246-2',
        '49318-9',
        '64088-8',
        '64094-6'
    }

class LabTestsForSexuallyTransmittedInfections(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests for sexually transmitted infections.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test, Order.

    **Inclusion Criteria:** Includes only relevant concepts associated with laboratory tests for sexually transmitted infections in females. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes codes that indicate lab tests for sexually transmitted infections in male patients.
    """

    OID = '2.16.840.1.113883.3.464.1003.110.12.1051'
    VALUE_SET_NAME = 'Lab Tests for Sexually Transmitted Infections'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '10705-2',
        '11083-3',
        '11084-1',
        '11481-9',
        '11597-2',
        '12222-6',
        '12223-4',
        '14499-8',
        '14500-3',
        '14502-9',
        '14503-7',
        '14504-5',
        '14506-0',
        '16280-0',
        '17398-9',
        '17399-7',
        '17400-3',
        '17401-1',
        '17402-9',
        '17403-7',
        '17404-5',
        '17405-2',
        '17406-0',
        '17407-8',
        '17408-6',
        '17409-4',
        '17410-2',
        '17411-0',
        '17412-8',
        '17723-8',
        '17724-6',
        '17725-3',
        '17726-1',
        '17727-9',
        '17728-7',
        '17729-5',
        '20507-0',
        '20508-8',
        '21414-8',
        '21415-5',
        '21416-3',
        '21440-3',
        '21441-1',
        '22461-8',
        '22462-6',
        '22587-0',
        '22590-4',
        '22592-0',
        '22594-6',
        '24110-9',
        '24111-7',
        '24312-1',
        '26009-1',
        '29311-8',
        '30167-1',
        '31147-2',
        '31905-3',
        '31906-1',
        '32198-4',
        '32199-2',
        '32705-6',
        '34147-9',
        '34382-2',
        '38372-9',
        '40679-3',
        '40680-1',
        '42481-2',
        '43305-2',
        '43403-5',
        '44543-7',
        '44544-5',
        '44546-0',
        '44547-8',
        '44549-4',
        '44550-2',
        '47236-5',
        '47237-3',
        '47238-1',
        '47387-6',
        '48560-7',
        '49891-5',
        '49896-4',
        '5028-6',
        '50388-8',
        '50690-7',
        '51838-1',
        '51839-9',
        '5291-0',
        '5292-8',
        '53605-2',
        '53762-1',
        '53879-3',
        '5392-6',
        '53927-0',
        '5393-4',
        '5394-2',
        '55299-2',
        '57032-5',
        '59263-4',
        '59264-2',
        '59420-0',
        '61372-9',
        '61373-7',
        '61374-5',
        '61375-2',
        '61376-0',
        '61377-8',
        '61378-6',
        '61379-4',
        '61380-2',
        '61381-0',
        '61382-8',
        '61383-6',
        '61384-4',
        '61385-1',
        '61386-9',
        '61387-7',
        '61388-5',
        '61389-3',
        '61390-1',
        '61391-9',
        '61392-7',
        '61393-5',
        '61394-3',
        '61395-0',
        '61396-8',
        '63464-2',
        '6487-3',
        '6488-1',
        '6489-9',
        '6510-2',
        '6511-0',
        '6514-4',
        '6516-9',
        '6561-5',
        '6562-3',
        '660-1',
        '688-2',
        '690-8',
        '69002-4',
        '691-6',
        '692-4',
        '693-2',
        '698-1',
        '71431-1',
        '71793-4',
        '73732-0',
        '73752-8',
        '73959-9',
        '7975-6',
        '8041-6'
    }

class LdlCholesterol(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent lab tests commonly used for low-density lipoproteins (LDL) cholesterol measurement.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Laboratory Test. The intent of this data element is to identify patients who had a lab test on a source of serum or plasma.

    **Inclusion Criteria:** Includes only relevant concepts associated with LDL-C tests using the source of serum or plasma based on a measurement scale of mass per volume.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1573'
    VALUE_SET_NAME = 'LDL Cholesterol'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '13457-7',
        '18261-8',
        '18262-6',
        '2089-1',
        '43394-6',
        '49132-4',
        '50193-2',
        '55440-2',
        '86911-5',
        '90364-1',
        '91105-7',
        '91106-5',
        '91107-3',
        '91108-1',
        '91109-9',
        '91110-7',
        '91111-5'
    }

class MeaslesAntibodyTestIggAntibodyPresence(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent test results related to IgG antibodies and measles. A positive test conveys immunologic protection against measles.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying positive antibody tests for measles IgG In the serum, cerebrospinal fluid or body fluid.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1060'
    VALUE_SET_NAME = 'Measles Antibody Test (IgG Antibody presence)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '20479-2',
        '35275-7',
        '40648-8',
        '41132-2',
        '53536-9'
    }

class MeaslesAntibodyTestIggAntibodyTiter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests for the  titre (or amount) of IgG antibodies to measles.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with test codes for measles IgG antibody titres in the serum, or cerebrospinal fluid.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1059'
    VALUE_SET_NAME = 'Measles Antibody Test (IgG Antibody Titer)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '21500-4',
        '21501-2',
        '22501-1',
        '22502-9'
    }

class MumpsAntibodyTestIggAntibodyPresence(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent test results for presence of mumps IgG antibody.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying positive antibody tests for mumps IgG.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1062'
    VALUE_SET_NAME = 'Mumps Antibody Test (IgG Antibody presence)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '22415-4',
        '39011-2',
        '40737-9',
        '6476-6',
        '74422-7'
    }

class MumpsAntibodyTestIggAntibodyTiter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent test results for titre (amount) of mumps IgG antibody.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying titres for mumps antibody IgG in serum and by immunofluorescence in cerebrospinal fluid or serum.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1061'
    VALUE_SET_NAME = 'Mumps Antibody Test (IgG Antibody Titer)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '21401-5',
        '22416-2',
        '22417-0',
        '6477-4'
    }

class PapTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent identify cervical cytology tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Order or Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with cervical cytology tests. This is a grouping of LOINC codes.

    **Exclusion Criteria:** Excludes cytology performed on non-cervical samples. Excludes codes that indicate that this test was ordered only, and not necessarily performed.
    """

    OID = '2.16.840.1.113883.3.464.1003.108.12.1017'
    VALUE_SET_NAME = 'Pap Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '10524-7',
        '18500-9',
        '19762-4',
        '19764-0',
        '19765-7',
        '19766-5',
        '19774-9',
        '33717-0',
        '47527-7',
        '47528-5'
    }

class PregnancyTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent urine, serum, or plasma pregnancy tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Order.

    **Inclusion Criteria:** Includes only relevant concepts associated with conducting a pregnancy test. This is a grouping of LOINC codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.111.12.1011'
    VALUE_SET_NAME = 'Pregnancy Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '19080-1',
        '19180-9',
        '20415-6',
        '20994-0',
        '2106-3',
        '2107-1',
        '2110-5',
        '2111-3',
        '2112-1',
        '2113-9',
        '2114-7',
        '2115-4',
        '2118-8',
        '2119-6',
        '21198-7',
        '25372-4',
        '25373-2',
        '34670-0',
        '45194-8',
        '55869-2',
        '55870-0',
        '56497-1',
        '80384-1',
        '83086-9'
    }

class ProstateSpecificAntigenTest(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent prostate specific antigen (PSA) test.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Laboratory Test.

    **Inclusion Criteria:** Includes only relevant concepts associated with prostate specific antigen (PSA) tests.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.401'
    VALUE_SET_NAME = 'Prostate Specific Antigen Test'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '10508-0',
        '10886-0',
        '12841-3',
        '15323-9',
        '15324-7',
        '15325-4',
        '19195-7',
        '19201-3',
        '2857-1',
        '33667-7',
        '34611-4',
        '35741-8'
    }

class RubellaAntibodyTestIggAntibodyPresence(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests for the presence of rubella IgG antibody in serum.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with testing the presence of rubella IgG antibody.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1064'
    VALUE_SET_NAME = 'Rubella Antibody Test (IgG Antibody presence)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '25514-1',
        '39013-8',
        '40667-8',
        '40668-6',
        '63462-6',
        '74415-1'
    }

class RubellaAntibodyTestIggAntibodyTiter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests for the titre (amount) of rubella IgG antibody in serum.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with testing to identify titres for rubella IgG antibody.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1063'
    VALUE_SET_NAME = 'Rubella Antibody Test (IgG Antibody Titer)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '41763-4',
        '46110-3'
    }

class UrineProteinTests(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent urine protein tests.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying urine protein tests, including those that look for albumin, microalbumin, and protein.

    **Exclusion Criteria:** Excludes codes that identify urine protein tests that would be taken from a fetus.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1024'
    VALUE_SET_NAME = 'Urine Protein Tests'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '11218-5',
        '12842-1',
        '13705-9',
        '13801-6',
        '13986-5',
        '13992-3',
        '14956-7',
        '14957-5',
        '14958-3',
        '14959-1',
        '1753-3',
        '1754-1',
        '1755-8',
        '1757-4',
        '17819-4',
        '18373-1',
        '20454-5',
        '20621-9',
        '21059-1',
        '21482-5',
        '26801-1',
        '27298-9',
        '2887-8',
        '2888-6',
        '2889-4',
        '2890-2',
        '29946-1',
        '30000-4',
        '30001-2',
        '30003-8',
        '32209-9',
        '32294-1',
        '32551-4',
        '34366-5',
        '35663-4',
        '40486-3',
        '40662-9',
        '40663-7',
        '43605-5',
        '43606-3',
        '43607-1',
        '44292-1',
        '47558-2',
        '49002-9',
        '49023-5',
        '50209-6',
        '50561-0',
        '50949-7',
        '51190-7',
        '53121-0',
        '53525-2',
        '53530-2',
        '53531-0',
        '53532-8',
        '56553-1',
        '57369-1',
        '57735-3',
        '5804-0',
        '58448-2',
        '58992-9',
        '59159-4',
        '60678-0',
        '63474-1',
        '6941-9',
        '6942-7',
        '76401-9',
        '77253-3',
        '77254-1',
        '77940-5',
        '9318-7'
    }

class VaricellaZosterAntibodyTestIggAntibodyPresence(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests measuring the presence of IgG antibody to varicella zoster in serum, cerebrospinal fluid (CSF

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with tests measuring the presence of IgG antibody to varicella zoster in serum, CSF and body fluids.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1067'
    VALUE_SET_NAME = 'Varicella Zoster Antibody Test (IgG Antibody Presence)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '15410-4',
        '19162-7',
        '41512-5',
        '42537-1',
        '53534-4'
    }

class VaricellaZosterAntibodyTestIggAntibodyTiter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent laboratory tests measuring the titre of IgG antibody to varicella zoster in serum and cerebrospinal fluid (CSF).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Laboratory Test, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated with tests measuring the titre or amount of IgG antibody to varicella zoster in serum or CSF.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1066'
    VALUE_SET_NAME = 'Varicella Zoster Antibody Test (IgG Antibody Titer)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '21595-4',
        '22601-9',
        '22602-7',
        '6569-8'
    }
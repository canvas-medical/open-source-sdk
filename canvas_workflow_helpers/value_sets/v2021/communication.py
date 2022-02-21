from ..value_set import ValueSet


class ConsultantReport(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent consultant reports.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Communication.

    **Inclusion Criteria:** Includes only relevant concepts associated with written consultant reports.

    **Exclusion Criteria:** Excludes reports that are conducted via telephone calls or verbal communication.
    """

    OID = '2.16.840.1.113883.3.464.1003.121.12.1006'
    VALUE_SET_NAME = 'Consultant Report'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    LOINC = {
        '11488-4',
        '34099-2',
        '34100-8',
        '34101-6',
        '34102-4',
        '34103-2',
        '34104-0',
        '34749-2',
        '34756-7',
        '34758-3',
        '34760-9',
        '34761-7',
        '34764-1',
        '34776-5',
        '34777-3',
        '34779-9',
        '34781-5',
        '34783-1',
        '34785-6',
        '34788-0',
        '34791-4',
        '34795-5',
        '34797-1',
        '34798-9',
        '34800-3',
        '34803-7',
        '34805-2',
        '34807-8',
        '34810-2',
        '34812-8',
        '34814-4',
        '34816-9',
        '34820-1',
        '34822-7',
        '34824-3',
        '34826-8',
        '34828-4',
        '34831-8',
        '34833-4',
        '34837-5',
        '34839-1',
        '34841-7',
        '34845-8',
        '34847-4',
        '34849-0',
        '34851-6',
        '34853-2',
        '34855-7',
        '34879-7',
        '51845-6',
        '51846-4',
        '51854-8',
        '64056-5',
        '64068-0',
        '64072-2',
        '64076-3',
        '64080-5',
        '68469-6',
        '68486-0',
        '68551-1',
        '68566-9',
        '68570-1',
        '68575-0',
        '68586-7',
        '68590-9',
        '68597-4',
        '68619-6',
        '68633-7',
        '68639-4',
        '68648-5',
        '68651-9',
        '68661-8',
        '68670-9',
        '68681-6',
        '68685-7',
        '68694-9',
        '68705-3',
        '68716-0',
        '68727-7',
        '68746-7',
        '68757-4',
        '68765-7',
        '68787-1',
        '68802-8',
        '68812-7',
        '68821-8',
        '68837-4',
        '68846-5',
        '68852-3',
        '68864-8',
        '68869-7',
        '68874-7',
        '68879-6',
        '68892-9',
        '68897-8',
        '72555-6',
        '73575-3',
        '75424-2',
        '75465-5',
        '77403-4',
        '77429-9',
        '78250-8',
        '78251-6',
        '78252-4',
        '78253-2',
        '78254-0',
        '78405-8',
        '78406-6',
        '78496-7',
        '78498-3',
        '78567-5',
        '78568-3',
        '78726-7',
        '78732-5',
        '78738-2',
        '79428-9',
        '80396-5',
        '80575-4',
        '80664-6',
        '80666-1',
        '80673-7',
        '80736-2',
        '80801-4',
        '81191-9',
        '81192-7',
        '81193-5',
        '81196-8',
        '82356-7',
        '82359-1',
        '83570-2',
        '83578-5',
        '83609-8',
        '83621-3',
        '83653-6',
        '83685-8',
        '83720-3',
        '83722-9',
        '83868-0',
        '83873-0',
        '83888-8',
        '83909-2',
        '83912-6',
        '83926-6',
        '83931-6',
        '83941-5',
        '83960-5',
        '83967-0',
        '83984-5',
        '83992-8',
        '83996-9',
        '84035-5',
        '84071-0',
        '84115-5',
        '84126-2',
        '84131-2',
        '84142-9',
        '84145-2',
        '84152-8',
        '84173-4',
        '84190-8',
        '84213-8',
        '84231-0',
        '84241-9',
        '84280-7',
        '84292-2',
        '84303-7',
        '84312-8',
        '84324-3',
        '84349-0',
        '84352-4',
        '84358-1',
        '84394-6',
        '84398-7',
        '85174-1',
        '85208-7',
        '85222-8',
        '85232-7',
        '85237-6',
        '85238-4',
        '85517-1',
        '85519-7',
        '85866-2',
        '85871-2',
        '85882-9',
        '85884-5',
        '85886-0',
        '85890-2',
        '85899-3',
        '86451-2',
        '87233-3',
        '87254-9',
        '87627-6',
        '88351-2',
        '88640-8',
        '88644-0',
        '89031-9',
        '89032-7',
        '89033-5',
        '89216-6',
        '89227-3',
        '89446-9',
        '89447-7',
        '89551-6',
        '90006-8',
        '90012-6',
        '90343-5',
        '90354-2',
        '90709-7',
        '90710-5',
        '90712-1',
        '90714-7',
        '90715-4',
        '90717-0',
        '90771-7'
    }

    SNOMEDCT = {
        '371530004',
        '371531000',
        '371545006'
    }

class InfluenzaVaccinationDeclined(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient declining an influenza vaccination.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Communication.

    **Inclusion Criteria:** Includes only relevant concepts associated with a patient declining an influenza vaccination.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1255'
    VALUE_SET_NAME = 'Influenza Vaccination Declined'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '315640000'
    }

class LevelOfSeverityOfRetinopathyFindings(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the level of severity of retinopathy.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Communication, or could be used as a Diagnosis, or as an attribute to represent exam findings.

    **Inclusion Criteria:** Includes only relevant concepts associated with mild non-proliferative, moderate non-proliferative, severe non-proliferative, very severe non-proliferative, and proliferative diabetic retinopathy.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1283'
    VALUE_SET_NAME = 'Level of Severity of Retinopathy Findings'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '312903003',
        '312904009',
        '312905005',
        '399876000',
        '59276001'
    }

class MacularEdemaFindingsPresent(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the presence of macular edema.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Communication, or Diagnosis, or as an attribute to represent exam findings.

    **Inclusion Criteria:** Includes only relevant concepts associated with the presence of macular edema.

    **Exclusion Criteria:** Concepts that do not indicate macular edema are excluded from this value set.
    """

    OID = '2.16.840.1.113883.3.526.3.1320'
    VALUE_SET_NAME = 'Macular Edema Findings Present'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '193350004',
        '193387007',
        '232020009',
        '312911008',
        '312912001',
        '312920004',
        '312921000',
        '312922007',
        '314010006',
        '314011005',
        '314014002',
        '314015001',
        '37231002',
        '399864000',
        '420486006',
        '421779007',
        '432789001'
    }

class PatientReasonForAceInhibitorOrArbDecline(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient reason for declining angiotensin-converting enzyme (ACE) inhibitor or angiotensin ii receptor blocker (ARB) therapy.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Communication, or may be used as an attribute.

    **Inclusion Criteria:** Includes only relevant concepts associated with patient reason declining ACE inhibitor or ARB therapy.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1140'
    VALUE_SET_NAME = 'Patient Reason for ACE Inhibitor or ARB Decline'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '134397009',
        '401084003'
    }

class PreviousReceiptOfInfluenzaVaccine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent a patient reporting a previous receipt of an influenza vaccine.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Communication or Assessment.

    **Inclusion Criteria:** Includes only relevant concepts associated with a patient reporting a previous receipt of an influenza vaccine.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1185'
    VALUE_SET_NAME = 'Previous Receipt of Influenza Vaccine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '185900003',
        '185901004',
        '185902006',
        '416928007'
    }
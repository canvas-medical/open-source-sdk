from ..value_set import ValueSet


class AlcoholAndDrugDependenceTreatment(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent treatment for alcohol and drug dependence.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with assessment, management, and both psychosocial and pharmacological treatment of alcohol and drug dependence. This is a grouping of SNOMED CT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.106.12.1005'
    VALUE_SET_NAME = 'Alcohol and Drug Dependence Treatment'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '171047005',
        '20093000',
        '23915005',
        '24165007',
        '266707007',
        '310653000',
        '313071005',
        '370881007',
        '370884004',
        '385989002',
        '386448003',
        '386449006',
        '386450006',
        '386451005',
        '408933008',
        '408934002',
        '408935001',
        '408936000',
        '408941008',
        '408942001',
        '408943006',
        '408944000',
        '408945004',
        '408947007',
        '408948002',
        '410419007',
        '413473000',
        '423416000',
        '424148004',
        '424407005',
        '424589009',
        '426928008',
        '429291000124102',
        '56876005',
        '60112009',
        '707166002',
        '720174008',
        '720175009',
        '720176005',
        '720177001',
        '737363002'
    }

class Ambulatory(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent encounters in an ambulatory setting.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with care in an ambulatory setting.

    **Exclusion Criteria:** Excludes patients who had ambulatory hospice care.
    """

    OID = '2.16.840.1.113883.3.464.1003.122.12.1003'
    VALUE_SET_NAME = 'Ambulatory'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '255327002',
        '440655000',
        '722171005'
    }

class AnnualWellnessVisit(ValueSet):
    """
    **Clinical Focus:** This value set grouping contains concepts that represent annual wellness visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter. The intent of this data element is to identify patients who have had an annual wellness visit.

    **Inclusion Criteria:** Includes only relevant concepts associated with encounters specific to annual wellness visits.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1240'
    VALUE_SET_NAME = 'Annual Wellness Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    HCPCSLEVELII = {
        'G0438',
        'G0439'
    }

    SNOMEDCT = {
        '444971000124105',
        '456201000124103'
    }

class AudiologyVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent assessment tools or instruments used to quantify hearing.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with hearing assessment tools and instruments used to quantify hearing such as basic vestibular evaluation, spontaneous and positional nystagmus testing, and computerized dynamic posturography. This is a grouping of CPT codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1066'
    VALUE_SET_NAME = 'Audiology Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '92540',
        '92541',
        '92542',
        '92548'
    }

class BehavioralHealthFollowUpVisit(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who have had a behavioral health follow-up visit.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with health and behavior assessment or intervention, or education and training for patient self-management by a physician or other qualified health care professional.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.12.1054'
    VALUE_SET_NAME = 'Behavioral Health Follow-up Visit'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '98960',
        '98961',
        '98962',
        '99078',
        '99510'
    }

class BehavioralneuropsychAssessment(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for assessments for neuropsychological assessments.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with applicable neuropsychological assessments for behavioral health.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1023'
    VALUE_SET_NAME = 'Behavioral/Neuropsych Assessment'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '96116'
    }

    SNOMEDCT = {
        '307808008'
    }

class EncounterInfluenza(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits during which an influenza vaccine may be administered.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with face-to-face encounters during which an influenza vaccine may be administered.

    **Exclusion Criteria:** Excludes telehealth encounters.
    """

    OID = '2.16.840.1.113883.3.526.3.1252'
    VALUE_SET_NAME = 'Encounter-Influenza'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215',
        '99241',
        '99242',
        '99243',
        '99244',
        '99245',
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337',
        '99341',
        '99342',
        '99343',
        '99344',
        '99345',
        '99347',
        '99348',
        '99349',
        '99350',
        '99381',
        '99382',
        '99383',
        '99384',
        '99385',
        '99386',
        '99387',
        '99391',
        '99392',
        '99393',
        '99394',
        '99395',
        '99396',
        '99397',
        '99401',
        '99402',
        '99403',
        '99404',
        '99411',
        '99412',
        '99429'
    }

    HCPCSLEVELII = {
        'G0438',
        'G0439'
    }

    SNOMEDCT = {
        '18170008',
        '185460008',
        '185462000',
        '185463005',
        '185464004',
        '185465003',
        '185466002',
        '185467006',
        '185468001',
        '185470005',
        '207195004',
        '209099002',
        '210098006',
        '225929007',
        '281036007',
        '30346009',
        '315205008',
        '3391000175108',
        '37894004',
        '439708006',
        '439740005',
        '698704008',
        '704126008',
        '77406008'
    }

class EncounterInpatient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent the most common inpatient encounter types.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter. The intent of this data element is to identify patients who have had an inpatient encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with SNOMED CT codes representing inpatient encounter.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.666.5.307'
    VALUE_SET_NAME = 'Encounter Inpatient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183452005',
        '32485007',
        '8715000'
    }

class EncounterToDocumentMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent multiple types of encounters that include documentation of current medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying types of encounters associated with documentation of medications reviewed, updated or transcribed as the current medication list.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1834'
    VALUE_SET_NAME = 'Encounter to Document Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '59400',
        '59510',
        '59610',
        '59618',
        '90791',
        '90792',
        '90832',
        '90834',
        '90837',
        '90839',
        '92002',
        '92004',
        '92012',
        '92014',
        '92507',
        '92508',
        '92526',
        '92537',
        '92538',
        '92540',
        '92541',
        '92542',
        '92544',
        '92545',
        '92547',
        '92548',
        '92550',
        '92557',
        '92567',
        '92568',
        '92570',
        '92585',
        '92588',
        '92626',
        '96116',
        '96156',
        '96158',
        '97129',
        '97161',
        '97162',
        '97163',
        '97164',
        '97165',
        '97166',
        '97167',
        '97168',
        '97802',
        '97803',
        '97804',
        '98960',
        '98961',
        '98962',
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215',
        '99221',
        '99222',
        '99223',
        '99236',
        '99281',
        '99282',
        '99283',
        '99284',
        '99285',
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337',
        '99339',
        '99340',
        '99341',
        '99342',
        '99343',
        '99344',
        '99345',
        '99347',
        '99348',
        '99349',
        '99350',
        '99385',
        '99386',
        '99387',
        '99395',
        '99396',
        '99397',
        '99495',
        '99496'
    }

    HCPCSLEVELII = {
        'G0101',
        'G0108',
        'G0270',
        'G0402',
        'G0438',
        'G0439'
    }

    SNOMEDCT = {
        '10197000',
        '108220007',
        '108221006',
        '108224003',
        '108311000',
        '13607009',
        '14736009',
        '165171009',
        '18091003',
        '18512000',
        '185349003',
        '185463005',
        '185465003',
        '209099002',
        '210098006',
        '225967005',
        '252592009',
        '252624005',
        '270427003',
        '270430005',
        '273643004',
        '274803000',
        '277404009',
        '284015009',
        '308335008',
        '34651001',
        '35025007',
        '36228007',
        '370803007',
        '385973000',
        '386372009',
        '390906007',
        '405096004',
        '406547006',
        '408983003',
        '410155007',
        '410157004',
        '410158009',
        '410160006',
        '410170008',
        '439708006',
        '439952009',
        '440524004',
        '46662001',
        '48423005',
        '50357006',
        '53555003',
        '54290001',
        '63547008',
        '66902005',
        '78318003',
        '83607001',
        '8411005',
        '86013001',
        '90526000',
        '91573000'
    }

class EncounterToEvaluateBmi(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent multiple types of encounters for body mass index (BMI) assessment.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with multiple types of encounters that enable BMI measurement.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1751'
    VALUE_SET_NAME = 'Encounter to Evaluate BMI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDT = {
        'D7111',
        'D7140',
        'D7210',
        'D7220',
        'D7230',
        'D7240',
        'D7241',
        'D7250',
        'D7251'
    }

    CPT = {
        '90791',
        '90792',
        '90832',
        '90834',
        '90837',
        '96156',
        '96158',
        '96159',
        '97161',
        '97162',
        '97163',
        '97165',
        '97166',
        '97167',
        '97802',
        '97803',
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215',
        '99236',
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337',
        '99339',
        '99340',
        '99385',
        '99386',
        '99387',
        '99395',
        '99396',
        '99397',
        '99401',
        '99402'
    }

    HCPCSLEVELII = {
        'G0101',
        'G0108',
        'G0270',
        'G0271',
        'G0402',
        'G0438',
        'G0439',
        'G0447',
        'G0473'
    }

    SNOMEDCT = {
        '10197000',
        '108220007',
        '108221006',
        '108224003',
        '108311000',
        '13607009',
        '14736009',
        '165171009',
        '18512000',
        '185349003',
        '185463005',
        '185465003',
        '225967005',
        '270427003',
        '270430005',
        '308335008',
        '35025007',
        '386372009',
        '390906007',
        '406547006',
        '410155007',
        '410157004',
        '410158009',
        '410160006',
        '410170008',
        '410172000',
        '46662001',
        '55162003',
        '68381003',
        '78318003',
        '83607001',
        '8411005',
        '86013001',
        '90526000'
    }

class EncounterToScreenForBloodPressure(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent multiple types of encounters where blood pressure measurement screening can be performed.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with encounters where the actual procedure of taking a blood pressure is performed.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1920'
    VALUE_SET_NAME = 'Encounter to Screen for Blood Pressure'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CDT = {
        'D7111',
        'D7140',
        'D7210',
        'D7220',
        'D7230',
        'D7240',
        'D7241',
        'D7250',
        'D7251'
    }

    CPT = {
        '90791',
        '90792',
        '92002',
        '92004',
        '92012',
        '92014',
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215',
        '99236',
        '99281',
        '99282',
        '99283',
        '99284',
        '99285',
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337',
        '99339',
        '99340',
        '99341',
        '99342',
        '99343',
        '99344',
        '99345',
        '99347',
        '99348',
        '99349',
        '99350',
        '99385',
        '99386',
        '99387',
        '99395',
        '99396',
        '99397'
    }

    HCPCSLEVELII = {
        'G0101',
        'G0402',
        'G0438',
        'G0439'
    }

    SNOMEDCT = {
        '103705002',
        '108220007',
        '108221006',
        '108224003',
        '12843005',
        '13607009',
        '14736009',
        '18170008',
        '185349003',
        '185463005',
        '185465003',
        '207195004',
        '209099002',
        '210098006',
        '270427003',
        '270430005',
        '306677009',
        '308335008',
        '35025007',
        '390906007',
        '406547006',
        '439708006',
        '4525004',
        '46662001',
        '50357006',
        '76464004',
        '78318003',
        '83607001',
        '86013001',
        '90526000'
    }

class EncounterToScreenForDepression(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts in which a depression screen could be assessed and documented through an exam, assessment, interview or evaluation.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with wellness visits, annual visits, therapy evaluations, or primary or specialist physician office visits where a depression screen could be conducted.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1916'
    VALUE_SET_NAME = 'Encounter to Screen for Depression'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '59400',
        '59510',
        '59610',
        '59618',
        '90791',
        '90792',
        '90832',
        '90834',
        '90837',
        '92625',
        '96105',
        '96110',
        '96112',
        '96116',
        '96125',
        '96136',
        '96138',
        '96156',
        '96158',
        '97165',
        '97166',
        '97167',
        '99078',
        '99201',
        '99202',
        '99203',
        '99204',
        '99205',
        '99212',
        '99213',
        '99214',
        '99215',
        '99304',
        '99305',
        '99306',
        '99307',
        '99308',
        '99309',
        '99310',
        '99315',
        '99316',
        '99318',
        '99324',
        '99325',
        '99326',
        '99327',
        '99328',
        '99334',
        '99335',
        '99336',
        '99337',
        '99339',
        '99340',
        '99384',
        '99385',
        '99386',
        '99387',
        '99394',
        '99395',
        '99396',
        '99397',
        '99401',
        '99402',
        '99403',
        '99404',
        '99483',
        '99484',
        '99492',
        '99493'
    }

    HCPCSLEVELII = {
        'G0101',
        'G0402',
        'G0438',
        'G0439',
        'G0444'
    }

    SNOMEDCT = {
        '10197000',
        '108220007',
        '108221006',
        '108224003',
        '108311000',
        '13607009',
        '14736009',
        '165171009',
        '171207006',
        '18512000',
        '185349003',
        '185463005',
        '185465003',
        '252603000',
        '270427003',
        '270430005',
        '302440009',
        '308335008',
        '35025007',
        '370803007',
        '390906007',
        '406547006',
        '410155007',
        '410157004',
        '46662001',
        '53555003',
        '78318003',
        '83607001',
        '8411005',
        '86013001',
        '90526000'
    }

class EsrdMonthlyOutpatientServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent patients who had ESRD monthly outpatient services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying patients who had ESRD monthly outpatients services.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.109.12.1014'
    VALUE_SET_NAME = 'ESRD Monthly Outpatient Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90951',
        '90952',
        '90953',
        '90954',
        '90955',
        '90956',
        '90957',
        '90958',
        '90959',
        '90960',
        '90961',
        '90962',
        '90963',
        '90964',
        '90965',
        '90966',
        '90967',
        '90968',
        '90969',
        '90970',
        '90989',
        '90993',
        '90997',
        '90999',
        '99512'
    }

class FollowUpWithin4Weeks(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent capturing the follow-up encounter within four weeks of the initial encounter.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter. Intention to represent follow-up visits within a 4-week period.

    **Inclusion Criteria:** Includes only relevant concepts associated with capturing the follow-up between 1 day to 1 month of the initial finding.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1578'
    VALUE_SET_NAME = 'Follow Up Within 4 Weeks'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183617005',
        '183618000',
        '183619008',
        '183620002',
        '183621003',
        '183622005',
        '183623000'
    }

class FollowUpWithinOneYear(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent capturing the follow-up encounter within one year of the initial encounter.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter. Intention to represent follow-up visits within a one-year period.

    **Inclusion Criteria:** Includes only relevant concepts associated with capturing the follow-up between 1 day to 12 month of the initial finding.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1579'
    VALUE_SET_NAME = 'Follow Up Within One Year'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '183617005',
        '183618000',
        '183619008',
        '183620002',
        '183621003',
        '183622005',
        '183623000',
        '183624006',
        '183625007',
        '183626008',
        '183627004',
        '183628009',
        '300042001'
    }

class GroupPsychotherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits during which group psychotherapy is performed.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with group psychotherapy.

    **Exclusion Criteria:** Excludes family psychotherapy or individual psychotherapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1187'
    VALUE_SET_NAME = 'Group Psychotherapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90853'
    }

    SNOMEDCT = {
        '76168009'
    }

class OccupationalTherapyEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for evaluations for occupational therapy services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with applicable codes for occupational therapy evaluations.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1011'
    VALUE_SET_NAME = 'Occupational Therapy Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '97165',
        '97166',
        '97167',
        '97168'
    }

    SNOMEDCT = {
        '410155007',
        '410157004'
    }

class OphthalmologicServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent ophthalmological visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with relevant encounters during which the patient sees an eye care professional.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.101.11.1206'
    VALUE_SET_NAME = 'Ophthalmologic Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '92002',
        '92004',
        '92012',
        '92014'
    }

class OphthalmologicalServices(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent ophthalmological visits.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with encounters during which the patient sees an eye care professional.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1285'
    VALUE_SET_NAME = 'Ophthalmological Services'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '92002',
        '92004',
        '92012',
        '92014'
    }

    SNOMEDCT = {
        '359960003',
        '36228007',
        '66902005',
        '78831002'
    }

class OutpatientEncountersForPreventiveCare(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent outpatient encounters.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with evaluation and management of a new or established patient through an encounter for annual visit, preventive evaluation, follow-up, or periodic re-evaluations that would occur in the outpatient setting.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1576'
    VALUE_SET_NAME = 'Outpatient Encounters for Preventive Care'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '108219001',
        '108220007',
        '108221006',
        '108224003',
        '14736009',
        '185349003',
        '185389009',
        '270427003',
        '270430005',
        '281036007',
        '308335008',
        '390906007',
        '410187005',
        '78318003',
        '86013001',
        '90526000'
    }

class PalliativeCareEncounter(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent identifying patients receiving palliative, comfort or hospice care.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with identifying patients receiving palliative, comfort or hospice care.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.600.1.1575'
    VALUE_SET_NAME = 'Palliative Care Encounter'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    ICD10CM = {
        'Z515'
    }

class PatientProviderInteraction(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent provider interactions with patients that include both face-to-face and virtual types of encounters.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with provider interactions with patients that are conducted in an office or care setting, as well as interactions which may occur via virtual methods, such as telephone calls, emails, and letters.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1012'
    VALUE_SET_NAME = 'Patient Provider Interaction'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    SNOMEDCT = {
        '185316007',
        '185317003',
        '185318008',
        '185320006',
        '185321005',
        '185349003',
        '185463005',
        '185465003',
        '270424005',
        '270427003',
        '270430005',
        '308335008',
        '308720009',
        '386473003',
        '390906007',
        '401267002',
        '401271004',
        '406547006',
        '438515009',
        '438516005',
        '445450000',
        '448337001',
        '87790002',
        '90526000'
    }

class PhysicalTherapyEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for evaluations for physical therapy services.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with applicable codes for physical therapy evaluations.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1022'
    VALUE_SET_NAME = 'Physical Therapy Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '97161',
        '97162',
        '97163'
    }

    SNOMEDCT = {
        '33849009'
    }

class PsychVisitDiagnosticEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits during which a psychiatric diagnostic evaluation is completed.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with visits with the completion of psychiatric diagnostic evaluations.

    **Exclusion Criteria:** Excludes group psychotherapy or family psychotherapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1492'
    VALUE_SET_NAME = 'Psych Visit - Diagnostic Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90791',
        '90792'
    }

    SNOMEDCT = {
        '10197000',
        '165172002',
        '68338001',
        '79094001'
    }

class PsychVisitFamilyPsychotherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits during which family psychotherapy is performed.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with family psychotherapy.

    **Exclusion Criteria:** Excludes group psychotherapy or individual psychotherapy visits.
    """

    OID = '2.16.840.1.113883.3.526.3.1018'
    VALUE_SET_NAME = 'Psych Visit - Family Psychotherapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90846',
        '90847'
    }

    SNOMEDCT = {
        '108313002'
    }

class PsychVisitPsychotherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for psychotherapy.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with visits for individual psychotherapy services.

    **Exclusion Criteria:** Excludes group psychotherapy or family psychotherapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1496'
    VALUE_SET_NAME = 'Psych Visit - Psychotherapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90832',
        '90834',
        '90837'
    }

    SNOMEDCT = {
        '183381005',
        '183382003',
        '183383008',
        '18512000',
        '302242004',
        '304820009',
        '304822001',
        '314034001',
        '38678006',
        '401157001',
        '443730003',
        '75516001',
        '90102008'
    }

class Psychoanalysis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for psychoanalysis.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with psychoanalysis.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1141'
    VALUE_SET_NAME = 'Psychoanalysis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '90845'
    }

    SNOMEDCT = {
        '28988002',
        '61436009'
    }

class SpeechAndHearingEvaluation(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent visits for speech and hearing evaluation.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Encounter.

    **Inclusion Criteria:** Includes only relevant concepts associated with evaluation of speech and/or hearing related abilities.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1530'
    VALUE_SET_NAME = 'Speech and Hearing Evaluation'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    CPT = {
        '92521',
        '92522',
        '92523',
        '92524',
        '92540',
        '92557',
        '92625'
    }

    SNOMEDCT = {
        '26342005',
        '41375007',
        '77837000',
        '91515000'
    }
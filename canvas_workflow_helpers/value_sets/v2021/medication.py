from ..value_set import ValueSet


class AceInhibitorOrArbIngredient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent angiotensin-converting enzyme (ACE) inhibitor and angiotensin-receptor blocker (ARB) ingredients.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Allergy/Intolerance.

    **Inclusion Criteria:** Includes only relevant concepts associated with prescribable angiotensin-converting enzyme (ACE) inhibitor and angiotensin-receptor blocker (ARB) ingredients only.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1489'
    VALUE_SET_NAME = 'ACE Inhibitor or ARB Ingredient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '18867',
        '1998',
        '214354',
        '29046',
        '30131',
        '321064',
        '35208',
        '35296',
        '3827',
        '38454',
        '50166',
        '52175',
        '54552',
        '69749',
        '73494',
        '83515',
        '83818'
    }

class AceInhibitorOrArbOrArni(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent angiotensin-converting enzyme (ACE) inhibitor, angiotensin-receptor blocker (ARB
    ARNI) therapies.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs concepts associated with component, form and strength); generic; prescribable; ACE inhibitor, ARB therapy, combination drugs such as ACEI plus diuretic, ARB plus neprilysin inhibitor (ARNI

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.526.3.1139'
    VALUE_SET_NAME = 'ACE Inhibitor or ARB or ARNI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000001',
        '1091646',
        '1091652',
        '1235144',
        '1235151',
        '1299859',
        '1299871',
        '1299890',
        '1299896',
        '1299897',
        '1435624',
        '153822',
        '153823',
        '1600716',
        '1600724',
        '1600728',
        '1656340',
        '1656349',
        '1656354',
        '197436',
        '197437',
        '197438',
        '197439',
        '197884',
        '197885',
        '197886',
        '197887',
        '198188',
        '198189',
        '199351',
        '199352',
        '199353',
        '199622',
        '199707',
        '199708',
        '199709',
        '199816',
        '199817',
        '199937',
        '200094',
        '200095',
        '200096',
        '200284',
        '200285',
        '205304',
        '205305',
        '205326',
        '261962',
        '282755',
        '283316',
        '283317',
        '308962',
        '308963',
        '308964',
        '310140',
        '310792',
        '310793',
        '310796',
        '310797',
        '310809',
        '311353',
        '311354',
        '312748',
        '312749',
        '312750',
        '314076',
        '314077',
        '314203',
        '317173',
        '349199',
        '349200',
        '349201',
        '349353',
        '349373',
        '349401',
        '349405',
        '349483',
        '351292',
        '351293',
        '403853',
        '403854',
        '403855',
        '411434',
        '477130',
        '485471',
        '577776',
        '578325',
        '578330',
        '636042',
        '636045',
        '639537',
        '722126',
        '722131',
        '722134',
        '722137',
        '730861',
        '730866',
        '730869',
        '730872',
        '802749',
        '845488',
        '848131',
        '848135',
        '848140',
        '848145',
        '848151',
        '854925',
        '854984',
        '854988',
        '857166',
        '857169',
        '857174',
        '857183',
        '857187',
        '858804',
        '858810',
        '858813',
        '858817',
        '858824',
        '858828',
        '858921',
        '876514',
        '876519',
        '876524',
        '876529',
        '897781',
        '897783',
        '897844',
        '897853',
        '898342',
        '898346',
        '898350',
        '898353',
        '898356',
        '898359',
        '898362',
        '898367',
        '898372',
        '898378',
        '898687',
        '898690',
        '898719',
        '898723',
        '979464',
        '979468',
        '979471',
        '979480',
        '979485',
        '979492',
        '999967',
        '999986',
        '999991',
        '999996'
    }

class AdhdMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent attention deficit hyperactivity disorder (ADHD) medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active and Medication, Dispensed.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; ADHD medications only.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1171'
    VALUE_SET_NAME = 'ADHD Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1006608',
        '1009145',
        '1013930',
        '1013937',
        '1091133',
        '1091145',
        '1091150',
        '1091152',
        '1091155',
        '1091170',
        '1091185',
        '1091210',
        '1091225',
        '1091322',
        '1091341',
        '1091389',
        '1091392',
        '1091497',
        '1092566',
        '1101926',
        '1101932',
        '1233709',
        '1312583',
        '1425847',
        '1425854',
        '1535454',
        '1535470',
        '1593856',
        '1648183',
        '1727443',
        '1734928',
        '1734951',
        '1806177',
        '1806179',
        '1806181',
        '1806183',
        '1806185',
        '1806187',
        '1806189',
        '1806191',
        '1806193',
        '1806195',
        '1806197',
        '1806200',
        '1806202',
        '1806204',
        '1806206',
        '1806208',
        '1806210',
        '1871456',
        '1871460',
        '1871462',
        '1871464',
        '1871466',
        '1871468',
        '1926840',
        '1926849',
        '1926853',
        '1927610',
        '1927617',
        '1927630',
        '1927637',
        '197745',
        '197746',
        '1995461',
        '2001564',
        '2001565',
        '2001566',
        '2001568',
        '349591',
        '349592',
        '349593',
        '349594',
        '349595',
        '541363',
        '541878',
        '541892',
        '577957',
        '577961',
        '608139',
        '608143',
        '687043',
        '753436',
        '753438',
        '753440',
        '753441',
        '854830',
        '854834',
        '854838',
        '854842',
        '854846',
        '854850',
        '861221',
        '861223',
        '861225',
        '861227',
        '861232',
        '861237',
        '862006',
        '862013',
        '862019',
        '862025',
        '884173',
        '884185',
        '884189',
        '884221',
        '884225',
        '884385',
        '884386',
        '884520',
        '884522',
        '884532',
        '884535',
        '884684',
        '892791',
        '899439',
        '899461',
        '899485',
        '899495',
        '899511',
        '899518',
        '899548',
        '899557',
        '977860',
        '998671',
        '998675',
        '998679'
    }

class AdolescentDepressionMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent medications that are commonly used to treat adolescent depression.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with antidepressant medications as well as other recommended depressive management medications, specific to the child and adolescent age group, for depression management.

    **Exclusion Criteria:** Excludes medications that are not commonly used in the treatment of depression in the child and adolescent age group.
    """

    OID = '2.16.840.1.113883.3.526.3.1567'
    VALUE_SET_NAME = 'Adolescent Depression Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1190110',
        '200371',
        '248642',
        '251200',
        '283406',
        '283407',
        '283485',
        '283672',
        '309313',
        '309314',
        '310384',
        '310385',
        '310386',
        '311725',
        '311726',
        '312938',
        '312940',
        '312941',
        '313580',
        '313581',
        '313582',
        '313583',
        '313584',
        '313585',
        '313586',
        '313989',
        '313990',
        '313995',
        '314111',
        '314277',
        '349332',
        '351249',
        '351250',
        '351285',
        '476809',
        '596926',
        '596930',
        '596934',
        '616402',
        '794947',
        '808744',
        '808748',
        '808751',
        '808753',
        '861064'
    }

class AdultDepressionMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent medications that are commonly used to treat adult depression.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with antidepressant medications as well as other recommended depressive management medications, specific to the adult age group, for depression management.

    **Exclusion Criteria:** Excludes medications that are not commonly used in the treatment of depression in the adult age group.
    """

    OID = '2.16.840.1.113883.3.526.3.1566'
    VALUE_SET_NAME = 'Adult Depression Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000048',
        '1000054',
        '1000058',
        '1000064',
        '1000070',
        '1000076',
        '1000097',
        '103968',
        '1086772',
        '1086778',
        '1086784',
        '1086789',
        '1098608',
        '1098649',
        '1098666',
        '1098670',
        '1098674',
        '1098678',
        '1099288',
        '1099292',
        '1099296',
        '1099300',
        '1099304',
        '1099316',
        '1146690',
        '1190110',
        '1232585',
        '1298857',
        '1298861',
        '1298870',
        '1738483',
        '1738495',
        '1738503',
        '1738511',
        '1738515',
        '1738519',
        '1738523',
        '1738527',
        '1738803',
        '1738805',
        '1738807',
        '197363',
        '197364',
        '197365',
        '197366',
        '198045',
        '198046',
        '198047',
        '198427',
        '198428',
        '198429',
        '198430',
        '199283',
        '200371',
        '248642',
        '251200',
        '252478',
        '252479',
        '282401',
        '283406',
        '283407',
        '283485',
        '283672',
        '309313',
        '309314',
        '310384',
        '310385',
        '310386',
        '311264',
        '311265',
        '311725',
        '311726',
        '312036',
        '312242',
        '312347',
        '312938',
        '312940',
        '312941',
        '313447',
        '313496',
        '313498',
        '313499',
        '313580',
        '313581',
        '313582',
        '313583',
        '313584',
        '313585',
        '313586',
        '313989',
        '313990',
        '313995',
        '314111',
        '314277',
        '317136',
        '349010',
        '349332',
        '351249',
        '351250',
        '351285',
        '410503',
        '476809',
        '485514',
        '596926',
        '596930',
        '596934',
        '751139',
        '751563',
        '753451',
        '790264',
        '790288',
        '794947',
        '808744',
        '808748',
        '808751',
        '808753',
        '835564',
        '835568',
        '835572',
        '835577',
        '835589',
        '835591',
        '835593',
        '850087',
        '850091',
        '851748',
        '851750',
        '851752',
        '856364',
        '856369',
        '856373',
        '856377',
        '856706',
        '856720',
        '856762',
        '856769',
        '856773',
        '856783',
        '856792',
        '856797',
        '856825',
        '856834',
        '856840',
        '856845',
        '856853',
        '857297',
        '857301',
        '857305',
        '859186',
        '859190',
        '859193',
        '861064',
        '865206',
        '865210',
        '865214',
        '898697',
        '898704',
        '900156',
        '900164',
        '900865',
        '900890',
        '900983',
        '903873',
        '903879',
        '903884',
        '903887',
        '903891',
        '905168',
        '905172',
        '966787',
        '966793',
        '993503',
        '993518',
        '993536',
        '993541',
        '993550',
        '993557',
        '993567',
        '993681',
        '993687',
        '993691'
    }

class AmitriptylineHydrochloride(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent amitriptyline hydrochloride medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs; generic; human use only; prescribable; amitriptyline hydrochloride only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; amitriptyline hydrochloride in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1373'
    VALUE_SET_NAME = 'Amitriptyline Hydrochloride'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '856706',
        '856720',
        '856762',
        '856769',
        '856773',
        '856783',
        '856792',
        '856797',
        '856825',
        '856834',
        '856840',
        '856845',
        '856853'
    }

class Amobarbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Amobarbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Amobarbital only; Amobarbital in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1512'
    VALUE_SET_NAME = 'Amobarbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '308170'
    }

class Amoxapine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent amoxapine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs; generic; human use only; prescribable; amoxapine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; amoxapine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1273'
    VALUE_SET_NAME = 'Amoxapine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197363',
        '197364',
        '197365',
        '197366'
    }

class AndrogenDeprivationTherapyForUrologyCare(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent androgen deprivation therapy as identified for urology care.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication. This data element is to list androgen deprivation therapy for urology care for prostate cancer.

    **Inclusion Criteria:** Includes only relevant concepts associated with androgen deprivation therapy medications.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113762.1.4.1151.48'
    VALUE_SET_NAME = 'Androgen deprivation therapy for Urology Care'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1115257',
        '1115447',
        '1115454',
        '1115457',
        '1115462',
        '1115467',
        '1115472',
        '1946519',
        '1946521',
        '310592',
        '545835',
        '571914',
        '752884',
        '752889',
        '752894',
        '752899',
        '828749',
        '828751',
        '905053',
        '905062'
    }

class AntiInfectivesOther(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nitrofurantion (anti-infective medications).

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (component, form and strength); generic; human only; prescribable; nitrofurantion medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; nitrofurantion in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1481'
    VALUE_SET_NAME = 'Anti Infectives, other'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1648755',
        '1648759',
        '311988',
        '311989',
        '311991',
        '311994',
        '311995'
    }

class AntibioticMedicationsForPharyngitis(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent antibiotic medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active or Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; antibiotics only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable; antibiotics in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1001'
    VALUE_SET_NAME = 'Antibiotic Medications for Pharyngitis'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1013659',
        '1013662',
        '1013665',
        '1043022',
        '1043027',
        '1043030',
        '105171',
        '1088677',
        '1302650',
        '1302659',
        '1302664',
        '1302669',
        '1302674',
        '1373014',
        '141963',
        '142118',
        '1423080',
        '1648755',
        '1648759',
        '1649401',
        '1649405',
        '1649425',
        '1649429',
        '1649988',
        '1649990',
        '1650030',
        '1650142',
        '1650143',
        '1650444',
        '1650446',
        '1652673',
        '1652674',
        '1653433',
        '1656313',
        '1656318',
        '1659131',
        '1659137',
        '1659149',
        '1659278',
        '1659283',
        '1659287',
        '1659592',
        '1659598',
        '1662285',
        '1664981',
        '1664986',
        '1665005',
        '1665021',
        '1665046',
        '1665050',
        '1665052',
        '1665060',
        '1665088',
        '1665093',
        '1665097',
        '1665102',
        '1665107',
        '1665210',
        '1665212',
        '1665227',
        '1665229',
        '1665444',
        '1665449',
        '1665497',
        '1665507',
        '1665515',
        '1665517',
        '1665519',
        '1668238',
        '1668264',
        '1721458',
        '1721460',
        '1721473',
        '1721474',
        '1721475',
        '1721476',
        '1722916',
        '1722919',
        '1722921',
        '1723156',
        '1723160',
        '1728082',
        '1728087',
        '1737244',
        '1737578',
        '1737581',
        '1739890',
        '1743547',
        '1743549',
        '1747115',
        '1747121',
        '1791505',
        '1801138',
        '1807508',
        '1807510',
        '1807511',
        '1807513',
        '1807516',
        '1807518',
        '1870631',
        '1870633',
        '1870650',
        '1870676',
        '1870681',
        '1870685',
        '1870686',
        '197449',
        '197451',
        '197452',
        '197453',
        '197454',
        '197511',
        '197512',
        '197516',
        '197517',
        '197518',
        '197595',
        '197596',
        '197650',
        '197984',
        '197985',
        '198044',
        '198048',
        '198049',
        '198050',
        '198201',
        '198202',
        '198250',
        '198252',
        '198332',
        '198334',
        '198335',
        '199055',
        '199327',
        '199332',
        '199370',
        '1996246',
        '1998483',
        '199884',
        '199885',
        '2000127',
        '2000134',
        '200346',
        '204466',
        '204844',
        '205964',
        '207362',
        '207364',
        '207390',
        '207391',
        '239189',
        '239191',
        '239204',
        '239209',
        '240637',
        '240741',
        '240984',
        '242800',
        '242825',
        '248656',
        '259290',
        '283535',
        '284215',
        '308177',
        '308181',
        '308182',
        '308188',
        '308189',
        '308191',
        '308192',
        '308194',
        '308207',
        '308210',
        '308212',
        '308459',
        '308460',
        '309040',
        '309043',
        '309044',
        '309045',
        '309047',
        '309048',
        '309049',
        '309054',
        '309058',
        '309065',
        '309068',
        '309072',
        '309076',
        '309077',
        '309078',
        '309079',
        '309080',
        '309081',
        '309085',
        '309086',
        '309087',
        '309090',
        '309092',
        '309095',
        '309096',
        '309097',
        '309098',
        '309101',
        '309110',
        '309112',
        '309113',
        '309114',
        '309115',
        '309308',
        '309309',
        '309310',
        '309322',
        '309329',
        '309335',
        '309336',
        '309339',
        '310026',
        '310027',
        '310028',
        '310154',
        '310155',
        '310157',
        '311296',
        '311681',
        '311787',
        '311989',
        '311991',
        '311994',
        '311995',
        '312127',
        '312128',
        '312447',
        '313115',
        '313134',
        '313137',
        '313416',
        '313570',
        '313571',
        '313572',
        '313797',
        '313799',
        '313800',
        '313850',
        '313888',
        '313920',
        '313926',
        '313996',
        '314106',
        '314108',
        '315090',
        '317127',
        '348869',
        '348870',
        '351127',
        '351156',
        '359383',
        '359385',
        '388510',
        '403840',
        '403920',
        '403921',
        '406524',
        '409823',
        '419849',
        '434018',
        '476576',
        '477391',
        '562251',
        '562266',
        '562508',
        '562707',
        '577378',
        '597455',
        '597761',
        '597823',
        '598006',
        '598025',
        '617296',
        '617302',
        '617309',
        '617316',
        '617322',
        '617423',
        '617430',
        '617993',
        '617995',
        '629695',
        '629697',
        '629699',
        '636559',
        '637173',
        '637560',
        '645617',
        '686355',
        '686383',
        '686400',
        '686405',
        '686406',
        '686418',
        '700408',
        '728207',
        '731538',
        '731564',
        '731567',
        '731570',
        '745302',
        '745462',
        '745560',
        '749780',
        '749783',
        '757460',
        '757464',
        '757466',
        '789980',
        '799048',
        '802550',
        '834040',
        '834046',
        '834061',
        '834102',
        '835700',
        '836306',
        '847360',
        '858062',
        '858372',
        '863538',
        '901399'
    }

class AntidepressantMedication(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent antidepressant medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active or Medication, Dispensed.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable. Includes only relevant concepts associated with antidepressant medication. This is a grouping of RxNorm codes.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1213'
    VALUE_SET_NAME = 'Antidepressant Medication'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000048',
        '1000054',
        '1000058',
        '1000064',
        '1000070',
        '1000076',
        '1000097',
        '104837',
        '1086772',
        '1086778',
        '1086784',
        '1098649',
        '1098666',
        '1098670',
        '1098674',
        '1098678',
        '1099288',
        '1099292',
        '1099296',
        '1099300',
        '1099304',
        '1099316',
        '1190110',
        '1232585',
        '1298803',
        '1298857',
        '1298861',
        '1298870',
        '1430122',
        '1433217',
        '1433227',
        '1433233',
        '1433239',
        '1439808',
        '1439810',
        '1439812',
        '1439840',
        '1607617',
        '1738483',
        '1738495',
        '1738503',
        '1738511',
        '1738515',
        '1738519',
        '1738523',
        '1738527',
        '1738803',
        '1738805',
        '1738807',
        '1801289',
        '1874553',
        '1874559',
        '197363',
        '197364',
        '197365',
        '197366',
        '198045',
        '198046',
        '198047',
        '199283',
        '199820',
        '200371',
        '248642',
        '251200',
        '283406',
        '283407',
        '283485',
        '283672',
        '309313',
        '309314',
        '310384',
        '310385',
        '310386',
        '311725',
        '311726',
        '312036',
        '312242',
        '312347',
        '312938',
        '312940',
        '312941',
        '313447',
        '313496',
        '313497',
        '313498',
        '313499',
        '313580',
        '313581',
        '313582',
        '313583',
        '313584',
        '313585',
        '313586',
        '313989',
        '313990',
        '313995',
        '314111',
        '314277',
        '317136',
        '349332',
        '351249',
        '351250',
        '351285',
        '403969',
        '403970',
        '403971',
        '403972',
        '476809',
        '596926',
        '596930',
        '596934',
        '616402',
        '721787',
        '790264',
        '790288',
        '794947',
        '808744',
        '808748',
        '808751',
        '808753',
        '835564',
        '835568',
        '835572',
        '835577',
        '835589',
        '835591',
        '835593',
        '856364',
        '856369',
        '856373',
        '856377',
        '856706',
        '856720',
        '856762',
        '856769',
        '856773',
        '856783',
        '856792',
        '856797',
        '856825',
        '856834',
        '856840',
        '856845',
        '856853',
        '857291',
        '857296',
        '857297',
        '857301',
        '857305',
        '857315',
        '859186',
        '859190',
        '859193',
        '861064',
        '865206',
        '865210',
        '865214',
        '898697',
        '898704',
        '903873',
        '903879',
        '903884',
        '903887',
        '903891',
        '905168',
        '905172',
        '993503',
        '993518',
        '993536',
        '993541',
        '993550',
        '993557',
        '993567',
        '993681',
        '993687',
        '993691'
    }

class AromataseInhibitors(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent aromatase inhibitor medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active or Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; both steroidal and non-steroidal inhibitors; both non-selective and selective inhibitors; aromatase inhibitors only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable; aromatase inhibitors in combination with other medications; selective inhibitors vorozole, formestane, and fadrozole.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1265'
    VALUE_SET_NAME = 'Aromatase Inhibitors'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '199224',
        '200064',
        '310261'
    }

class Atropine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent atropine / diphenoxylate combination medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; atropine / diphenoxylate (combination medication).

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; atropine / diphenoxylate in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1274'
    VALUE_SET_NAME = 'Atropine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1046787',
        '1046815',
        '1046820',
        '1046997',
        '1048078',
        '1048124',
        '1048147',
        '1190536',
        '1190538',
        '1190540',
        '1190542',
        '1190546',
        '1190551',
        '1190552',
        '1190556',
        '1190568',
        '1190572',
        '1190692',
        '1190738',
        '1190748',
        '1190757',
        '1190764',
        '1190776',
        '1190783',
        '1190787',
        '1190793',
        '1190795',
        '1190798',
        '1190800',
        '1666781',
        '727415'
    }

class Benztropine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent benztropine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; benztropine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; benztropine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1361'
    VALUE_SET_NAME = 'Benztropine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '885209',
        '885213',
        '885219'
    }

class BetaBlockerTherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent beta blocker therapy.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; penbutolol sulfate, betaxolol hydrochloride, propranolol hydrochloride, atenolol/chlorthalidone, sotalol hydrochloride, metoprolol tartrate, nebivolol/valsartan, atenolol, bendroflumethiazide, nadolol, pindolol, timolol, oxprenolol, clopamide/pindolol, carvedilol, hydrochlorothiazide/pindolol, nebivolol, bisoprolol, bisoprolol/hydrochlorothiazide, hydrochlorothiazide/propranolol hydrochloride, propranolol hydrochloride, metoprolol, hydrochlorothiazide/metoprolol succinate, hydrochlorothiazide/metoprolol tartrate, labetalol, sotalol, acebutolol.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.526.3.1174'
    VALUE_SET_NAME = 'Beta Blocker Therapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1191185',
        '1297753',
        '1297757',
        '1495058',
        '152916',
        '1593725',
        '1606347',
        '1606349',
        '1798281',
        '1923422',
        '1923424',
        '1923426',
        '197379',
        '197380',
        '197381',
        '197382',
        '197383',
        '198000',
        '198001',
        '198006',
        '198007',
        '198008',
        '198104',
        '198105',
        '198284',
        '198285',
        '198286',
        '199277',
        '199494',
        '199495',
        '199717',
        '199786',
        '199787',
        '200031',
        '200032',
        '200033',
        '387013',
        '686924',
        '751612',
        '751618',
        '827073',
        '854901',
        '854905',
        '854908',
        '854916',
        '854919',
        '856422',
        '856429',
        '856448',
        '856457',
        '856460',
        '856481',
        '856519',
        '856535',
        '856556',
        '856569',
        '856578',
        '856713',
        '856724',
        '856733',
        '860510',
        '860516',
        '860522',
        '860532',
        '866412',
        '866419',
        '866427',
        '866436',
        '866452',
        '866461',
        '866472',
        '866479',
        '866482',
        '866491',
        '866511',
        '866514',
        '866924',
        '896758',
        '896762',
        '896766',
        '896983',
        '896987',
        '904589',
        '998685',
        '998689',
        '998693',
        '998695'
    }

class BetaBlockerTherapyForLvsd(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent beta blocker therapy for left ventricular systolic dysfunction (LVSD).

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; bisoprolol, carvedilol, or sustained release metoprolol succinate.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.526.3.1184'
    VALUE_SET_NAME = 'Beta Blocker Therapy for LVSD'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '200031',
        '200032',
        '200033',
        '686924',
        '854901',
        '854905',
        '854908',
        '854916',
        '854919',
        '860510',
        '860516',
        '860522',
        '860532',
        '866412',
        '866419',
        '866427',
        '866436',
        '866452',
        '866461',
        '866472'
    }

class BetaBlockerTherapyIngredient(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent beta blocker therapy ingredients.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Allergy/Intolerance.

    **Inclusion Criteria:** Includes only relevant concepts associated with prescribable ingredient only.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1493'
    VALUE_SET_NAME = 'Beta Blocker Therapy Ingredient'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '10600',
        '1202',
        '149',
        '1520',
        '19484',
        '20352',
        '2116',
        '6185',
        '6918',
        '7226',
        '8332',
        '8787'
    }

class Brompheniramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent brompheniramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs; generic; human use only; prescribable; brompheniramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; brompheniramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1427'
    VALUE_SET_NAME = 'Brompheniramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1014331',
        '1037164',
        '1053258',
        '1090463',
        '1094330',
        '1098497',
        '1098498',
        '1098906',
        '1111065',
        '1148155',
        '1192477',
        '1242002',
        '1244523',
        '1245722',
        '1251802',
        '1294015',
        '1300084',
        '1304105',
        '1304853',
        '1308438',
        '1356797',
        '1356800',
        '1356804',
        '1356807',
        '1356812',
        '1356815',
        '1356835',
        '1356838',
        '1356841',
        '1356848',
        '1356904',
        '1357010',
        '1357389',
        '1357395',
        '1357402',
        '1357422',
        '1357428',
        '1357883',
        '1363265',
        '1363502',
        '1363503',
        '1364916',
        '1367219',
        '1423702',
        '1430522',
        '1486964',
        '1541630',
        '1595631',
        '1663612',
        '1666116',
        '2049286',
        '2049407',
        '2101293',
        '2101296',
        '2167728',
        '2167730',
        '2167731',
        '2167732',
        '359281',
        '616346',
        '616351',
        '633164',
        '700851',
        '731032',
        '756268',
        '759494',
        '857556',
        '994289',
        '994402',
        '996998'
    }

class Butabarbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent butabarbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; butabarbital only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; butabarbital in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1402'
    VALUE_SET_NAME = 'Butabarbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1047805',
        '1251600',
        '1251610',
        '1251614',
        '1251625'
    }

class Butalbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Butalbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Butalbital only; Butalbital in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1514'
    VALUE_SET_NAME = 'Butalbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1249617',
        '1431286',
        '1724446',
        '197425',
        '197426',
        '197427',
        '197428',
        '1995136',
        '238134',
        '238135',
        '238153',
        '238154',
        '240093',
        '308322',
        '476152',
        '756245',
        '889520',
        '993943',
        '994237'
    }

class Carbinoxamine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent carbinoxamine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; carbinoxamine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; carbinoxamine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1306'
    VALUE_SET_NAME = 'Carbinoxamine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1010696',
        '1010946',
        '1010980',
        '1012681',
        '1012904',
        '1012956',
        '1012984',
        '1374770',
        '1424307',
        '1795581'
    }

class Carisoprodol(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent carisoprodol medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; carisoprodol only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; carisoprodol in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1369'
    VALUE_SET_NAME = 'Carisoprodol'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '105974',
        '197446',
        '197447',
        '730794',
        '994226'
    }

class Chlorpheniramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent chlorpheniramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; chlorpheniramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; chlorpheniramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1352'
    VALUE_SET_NAME = 'Chlorpheniramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1013619',
        '1038876',
        '1042688',
        '1042693',
        '1042829',
        '1046384',
        '1046781',
        '1046799',
        '1048124',
        '1052679',
        '1053618',
        '1053624',
        '1086443',
        '1086463',
        '1086475',
        '1086750',
        '1086991',
        '1087459',
        '1089968',
        '1090443',
        '1090699',
        '1091008',
        '1098496',
        '1101555',
        '1101855',
        '1111171',
        '1111440',
        '1112220',
        '1112489',
        '1112779',
        '1112864',
        '1112906',
        '1112908',
        '1113397',
        '1113417',
        '1113522',
        '1113998',
        '1114003',
        '1114361',
        '1114838',
        '1116173',
        '1117392',
        '1147795',
        '1190174',
        '1193292',
        '1193293',
        '1234941',
        '1236070',
        '1242240',
        '1242747',
        '1244951',
        '1245169',
        '1245291',
        '1245706',
        '1249040',
        '1250528',
        '1250904',
        '1250983',
        '1251185',
        '1251811',
        '1251928',
        '1291266',
        '1292342',
        '1293298',
        '1293331',
        '1293344',
        '1293468',
        '1293472',
        '1293491',
        '1294201',
        '1297369',
        '1297390',
        '1299646',
        '1299662',
        '1302760',
        '1303251',
        '1304074',
        '1307225',
        '1307244',
        '1308442',
        '1310503',
        '1313969',
        '1357553',
        '1357894',
        '1359114',
        '1359157',
        '1363212',
        '1363288',
        '1363306',
        '1363309',
        '1363651',
        '1363752',
        '1363780',
        '1366022',
        '1366508',
        '1366653',
        '1366819',
        '1366822',
        '1366825',
        '1366948',
        '1366953',
        '1367225',
        '1367227',
        '1368963',
        '1369910',
        '1370122',
        '1370125',
        '1370440',
        '1372265',
        '1372312',
        '1372644',
        '1421985',
        '1423710',
        '1423711',
        '1423834',
        '1424295',
        '1424872',
        '1425315',
        '1425331',
        '1429345',
        '1430400',
        '1432508',
        '1437775',
        '1489310',
        '1534666',
        '1535923',
        '1535979',
        '1536477',
        '1536840',
        '1536862',
        '1536931',
        '1536934',
        '1536993',
        '1537029',
        '1540507',
        '1593105',
        '1599133',
        '1652087',
        '1655571',
        '1659956',
        '1664543',
        '1741529',
        '1743369',
        '1744049',
        '1800670',
        '1801964',
        '1857273',
        '1876117',
        '1927026',
        '2001623',
        '2003130',
        '2003179',
        '2049411',
        '2049841',
        '2056893',
        '2119482',
        '2119625',
        '2121065',
        '2167740',
        '2167750',
        '2167752',
        '2167835',
        '2167842',
        '2178934',
        '2178941',
        '2181301',
        '2181307',
        '2181309',
        '2181310',
        '2181311',
        '2181312',
        '2181313',
        '2181315',
        '2181316',
        '2181317',
        '2181318',
        '2181319',
        '2182346',
        '2182349',
        '2183669',
        '2183672',
        '2183676',
        '2183684',
        '2183687',
        '2183697',
        '2183700',
        '2183701',
        '2183891',
        '2183896',
        '477045',
        '604664',
        '636568',
        '668752',
        '700949',
        '759494',
        '804145',
        '857510',
        '857512',
        '857734',
        '857839',
        '859027',
        '859137',
        '859146',
        '859156',
        '995041',
        '995062',
        '995065',
        '995068',
        '995071',
        '995075',
        '995079',
        '995082',
        '995086',
        '995093',
        '995108',
        '995116',
        '995120',
        '995123',
        '995128',
        '998254'
    }

class Chlorpropamide(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent chlorpropamide medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; chlorpropamide only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; chlorpropamide in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1303'
    VALUE_SET_NAME = 'Chlorpropamide'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197495',
        '197496'
    }

class Chlorzoxazone(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent chlorzoxazone medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; chlorzoxazone only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; chlorzoxazone in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1362'
    VALUE_SET_NAME = 'Chlorzoxazone'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1088934',
        '1088936',
        '197501',
        '197502'
    }

class Clemastine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent clemastine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; clemastine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; clemastine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1308'
    VALUE_SET_NAME = 'Clemastine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '857416',
        '857420',
        '857430',
        '857452',
        '857454',
        '857457',
        '857461'
    }

class Clomipramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent clomipramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; clomipramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; clomipramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1336'
    VALUE_SET_NAME = 'Clomipramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '857291',
        '857292',
        '857296',
        '857297',
        '857301',
        '857305',
        '857315',
        '857326'
    }

class ConjugatedEstrogens(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent conjugated estrogen medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; conjugated estrogen medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; conjugated estrogens in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1357'
    VALUE_SET_NAME = 'Conjugated Estrogens'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000353',
        '1000354',
        '1000395',
        '1000398',
        '1000486',
        '1000490',
        '1000496',
        '1441392',
        '197660',
        '197661',
        '197662',
        '197663',
        '310197',
        '403849',
        '432572'
    }

class ContraceptiveMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent contraceptive medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active or Medication, Order.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable. Includes only relevant concepts associated with contraceptive medications. This is a grouping of RxNorm codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1080'
    VALUE_SET_NAME = 'Contraceptive Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000126',
        '1000131',
        '1000153',
        '1000156',
        '1013629',
        '1037183',
        '1037184',
        '1050493',
        '105510',
        '1090992',
        '1095224',
        '1099638',
        '1251323',
        '1251334',
        '1251336',
        '1358762',
        '1358763',
        '1358776',
        '1359022',
        '1359023',
        '1359028',
        '1359117',
        '1359130',
        '1359131',
        '1359132',
        '1367436',
        '1373501',
        '1373502',
        '1373503',
        '1421459',
        '1426288',
        '198042',
        '198043',
        '238015',
        '238019',
        '240128',
        '240707',
        '242297',
        '248310',
        '249357',
        '259218',
        '310228',
        '310230',
        '310463',
        '311359',
        '312033',
        '312124',
        '314146',
        '315096',
        '348804',
        '348805',
        '389221',
        '392662',
        '402250',
        '406396',
        '433718',
        '483325',
        '578732',
        '654353',
        '687424',
        '722152',
        '729534',
        '748798',
        '748800',
        '748804',
        '748806',
        '748832',
        '748868',
        '748878',
        '748961',
        '749155',
        '749156',
        '749157',
        '749736',
        '749761',
        '749784',
        '749786',
        '749848',
        '749852',
        '749856',
        '749858',
        '749860',
        '749869',
        '749879',
        '750242',
        '751553',
        '751901',
        '753476',
        '759741',
        '759742',
        '759743',
        '763088',
        '810096',
        '823777',
        '978949'
    }

class CyclobenzaprineHydrochloride(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent cyclobenzaprine hydrochloride medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; cyclobenzaprine hydrochloride only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; cyclobenzaprine hydrochloride in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1372'
    VALUE_SET_NAME = 'Cyclobenzaprine Hydrochloride'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '828299',
        '828320',
        '828348',
        '828353',
        '828358',
        '999731'
    }

class Cyproheptadine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent cyproheptadine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; cyproheptadine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; cyproheptadine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1277'
    VALUE_SET_NAME = 'Cyproheptadine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '866021',
        '866144'
    }

class DementiaMedications(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dementia medications.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes semantic clinical drugs (includes component, form and strength); generic; prescribable. Includes dementia medications. This is a grouping of RXNORM codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1510'
    VALUE_SET_NAME = 'Dementia Medications'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1100184',
        '1308569',
        '1858970',
        '310436',
        '310437',
        '312835',
        '312836',
        '314214',
        '314215',
        '579148',
        '725021',
        '725023',
        '860695',
        '860707',
        '860715',
        '860901',
        '996561',
        '996571',
        '996572',
        '996594',
        '996603',
        '996609',
        '996615',
        '996624',
        '996740',
        '997220',
        '997223',
        '997226',
        '997229'
    }

class DesiccatedThyroid(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent desiccated thyroid medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; desiccated thyroid medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; desiccated thyroid in combination with other medications, synthetic thyroid hormones (e.g. levothyroxine, liothyronine, thyrolar, tirosint).
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1354'
    VALUE_SET_NAME = 'Desiccated Thyroid'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1041814',
        '1099948',
        '1537767',
        '1537803',
        '1537807',
        '1537811',
        '198277',
        '198278',
        '208545',
        '242927',
        '313385',
        '313386',
        '313387',
        '313389',
        '313391',
        '313393',
        '313396',
        '314267',
        '315234',
        '315235',
        '347151',
        '728581'
    }

class Desipramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent desipramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; desipramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; desipramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1278'
    VALUE_SET_NAME = 'Desipramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1099288',
        '1099292',
        '1099296',
        '1099300',
        '1099304',
        '1099316'
    }

class Dexbrompheniramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dexbrompheniramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; dexbrompheniramine.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; dexbrompheniramine in combination with other drugs.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1375'
    VALUE_SET_NAME = 'Dexbrompheniramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1190580',
        '1190600',
        '1251806',
        '1305588',
        '1369403',
        '1441376',
        '1491637',
        '1539185',
        '1545306',
        '1545309',
        '1551286',
        '1798453'
    }

class Dexchlorpheniramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dexbrompheniramine / dextromethorphan / pseudoephedrine combination medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; dexchlorpheniramine / dextromethorphan / pseudoephedrine (combination medication).

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; Dexchlorpheniramine / Dextromethorphan / Pseudoephedrine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1300'
    VALUE_SET_NAME = 'Dexchlorpheniramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1293239',
        '1298226',
        '1298433',
        '1305775',
        '1357940',
        '1369424',
        '1369971',
        '1369972',
        '1370680',
        '1440003',
        '1990881',
        '2168002',
        '2181304',
        '2183907',
        '2184088',
        '2184108',
        '2184127',
        '2184130'
    }

class Dicyclomine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dicyclomine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; dicyclomine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; dicyclomine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1279'
    VALUE_SET_NAME = 'Dicyclomine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '199725',
        '755900',
        '991061',
        '991065',
        '991082',
        '991086',
        '991151',
        '991616'
    }

class Dimenhydrinate(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dimenhydrinate medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; dimenhydrinate only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; dimenhydrinate in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1500'
    VALUE_SET_NAME = 'Dimenhydrinate'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1245184',
        '1294446',
        '198602',
        '198603',
        '245357',
        '245358',
        '309913',
        '309914',
        '429720',
        '755901'
    }

class Diphenhydramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent diphenhydramine / ibuprofen combination medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; diphenhydramine / ibuprofen (combination medication).

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; diphenhydramine / ibuprofen in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1293'
    VALUE_SET_NAME = 'Diphenhydramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1020477',
        '1046751',
        '1049630',
        '1049884',
        '1049900',
        '1049906',
        '1049909',
        '1050385',
        '1052462',
        '1052467',
        '1052928',
        '1085945',
        '1086720',
        '1087607',
        '1092189',
        '1092373',
        '1092398',
        '1093075',
        '1093083',
        '1093098',
        '1094131',
        '1098443',
        '1099872',
        '1117245',
        '1147619',
        '1190448',
        '1233575',
        '1236048',
        '1248354',
        '1250907',
        '1251783',
        '1291711',
        '1291867',
        '1291868',
        '1291961',
        '1291991',
        '1292323',
        '1293964',
        '1294322',
        '1294348',
        '1294365',
        '1294366',
        '1294370',
        '1294372',
        '1294376',
        '1294557',
        '1294567',
        '1294594',
        '1294602',
        '1297517',
        '1297947',
        '1298288',
        '1298348',
        '1310475',
        '1310483',
        '1312784',
        '1356113',
        '1375932',
        '1424551',
        '1424850',
        '1428880',
        '1535609',
        '1535702',
        '1537095',
        '1550957',
        '1593110',
        '1606291',
        '1653139',
        '1659175',
        '1659960',
        '1664631',
        '1664658',
        '1666116',
        '1721472',
        '1727571',
        '1730190',
        '1730192',
        '1731101',
        '1789740',
        '1799180',
        '1803669',
        '1804449',
        '1855193',
        '1926601',
        '1939343',
        '1941459',
        '1944254',
        '1947507',
        '1993219',
        '1993220',
        '1996098',
        '2002068',
        '2046528',
        '2047427',
        '2166129',
        '882504',
        '895664',
        '901814'
    }

class DiphenhydramineHydrochloride(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent diphenhydramine hydrochloride medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; diphenhydramine hydrochloride only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; diphenhydramine hydrochloride in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1371'
    VALUE_SET_NAME = 'Diphenhydramine Hydrochloride'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1020477',
        '1049289',
        '1049630',
        '1049633',
        '1049900',
        '1049904',
        '1049906',
        '1049909',
        '1085945',
        '1093098',
        '1248354',
        '1723740',
        '1723776',
        '882504'
    }

class Dipyridamole(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent dipyridamole medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; dipyridamole only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; dipyridamole in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1349'
    VALUE_SET_NAME = 'Dipyridamole'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197622',
        '199314',
        '309952',
        '309955',
        '392451'
    }

class Disopyramide(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent disopyramide medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; disopyramide only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; disopyramide in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1311'
    VALUE_SET_NAME = 'Disopyramide'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '104285',
        '199730',
        '199824',
        '309958',
        '309960',
        '636793',
        '636794'
    }

class Doxylamine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Doxylamine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Doxylamine only; Doxylamine in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1515'
    VALUE_SET_NAME = 'Doxylamine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1042684',
        '1043400',
        '1052647',
        '1089822',
        '1094350',
        '1094355',
        '1094549',
        '1101439',
        '1101446',
        '1101457',
        '1112865',
        '1115329',
        '1233546',
        '1234386',
        '1236395',
        '1237103',
        '1237110',
        '1242502',
        '1242561',
        '1242587',
        '1242618',
        '1244918',
        '1245233',
        '1297288',
        '1297404',
        '1311150',
        '1360638',
        '1366501',
        '1366502',
        '1371196',
        '1375948',
        '1426334',
        '1431245',
        '1441831',
        '1484901',
        '1487765',
        '1489002',
        '1489300',
        '1492380',
        '1534835',
        '1536503',
        '1536999',
        '1544175',
        '1546881',
        '1648203',
        '1657147',
        '1659805',
        '1730187',
        '1730191',
        '1730211',
        '1730212',
        '1730213',
        '1795585',
        '1798298',
        '1798548',
        '1801704',
        '1804384',
        '1805288',
        '1860085',
        '1927849',
        '1928005',
        '1999651',
        '2048713',
        '2048714',
        '2049454',
        '2056073',
        '2119242',
        '2172491',
        '2185293'
    }

class ErgoloidMesylates(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Ergoloid Mesylates medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Ergoloid Mesylates only; Ergoloid Mesylates in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1516'
    VALUE_SET_NAME = 'Ergoloid Mesylates'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '318179'
    }

class EsterifiedEstrogens(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent esterified estrogen medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; esterified estrogen medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; esterified estrogens in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1419'
    VALUE_SET_NAME = 'Esterified Estrogens'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000353',
        '197666',
        '197667',
        '197668',
        '197669'
    }

class Estradiol(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent estradiol medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; estradiol only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; estradiol in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1365'
    VALUE_SET_NAME = 'Estradiol'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000161',
        '1149632',
        '1251493',
        '1251499',
        '1359123',
        '1359124',
        '1359126',
        '1359127',
        '1483549',
        '1483550',
        '1483552',
        '1483553',
        '197657',
        '197658',
        '197659',
        '205333',
        '2108924',
        '238003',
        '238004',
        '241527',
        '241946',
        '242333',
        '242891',
        '242892',
        '248478',
        '249869',
        '250213',
        '250838',
        '348906',
        '402250',
        '403922',
        '403923',
        '476545',
        '483169',
        '577027',
        '577029',
        '728118',
        '749850',
        '978941',
        '978944',
        '978946',
        '978948',
        '978949'
    }

class Estropipate(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent estropipate medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; estropipate only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; estropipate in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1319'
    VALUE_SET_NAME = 'Estropipate'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '310212',
        '310213',
        '310215'
    }

class GlucocorticoidsOralOnly(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent glucocorticoid medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Active.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; cortisone, dexamethasone, hydrocortisone, prednisone, methyprednisone, triamcinolone, betamethasone, dexamethasone, fludrocortisone and triamcinolone. Includes only relevant concepts associated with only glucocorticoids taken orally, i.e., through an tablet, capsule, or oral solution.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable; glucorticoids in combination with other drugs. Excludes all glucocorticoids taken non-orally, i.e., as a nasal inhalant or injectable solution.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1266'
    VALUE_SET_NAME = 'Glucocorticoids (oral only)'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1005830',
        '1013114',
        '1085728',
        '1303125',
        '1303132',
        '1303135',
        '197577',
        '197579',
        '197580',
        '197581',
        '197582',
        '197583',
        '197783',
        '197787',
        '197969',
        '197971',
        '197973',
        '198142',
        '198144',
        '198145',
        '198146',
        '198148',
        '199343',
        '199771',
        '199967',
        '205301',
        '249066',
        '259966',
        '283077',
        '309684',
        '309686',
        '312614',
        '312615',
        '312617',
        '313979',
        '315187',
        '328161',
        '343033',
        '429199',
        '643123',
        '643127',
        '702306',
        '759481',
        '759697',
        '762675',
        '763179',
        '763181',
        '763183',
        '763185',
        '793099',
        '794979',
        '828248',
        '846192'
    }

class Glyburide(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent glyburide medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; glyburide only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; glyburide in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1368'
    VALUE_SET_NAME = 'Glyburide'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197737',
        '252960',
        '310534',
        '310536',
        '310537',
        '310539',
        '314000',
        '861743',
        '861748',
        '861753'
    }

class Guanfacine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent guanfacine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; guanfacine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; guanfacine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1341'
    VALUE_SET_NAME = 'Guanfacine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1092566',
        '197745',
        '197746',
        '862006',
        '862013',
        '862019',
        '862025'
    }

class HighIntensityStatinTherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent high intensity statin medications as defined by the 2013 American College of Cardiology (ACC) and the American Heart Association (AHA) guideline.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with high intensity statin therapy medications.

    **Exclusion Criteria:** Excludes any other intensity of statin therapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1572'
    VALUE_SET_NAME = 'High Intensity Statin Therapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '2167565',
        '2167569',
        '259255',
        '404011',
        '404013',
        '476351',
        '597984',
        '597990',
        '597993',
        '617311',
        '757705',
        '859419',
        '859751'
    }

class Hydroxyzine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent hydroxyzine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; hydroxyzine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; hydroxyzine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1374'
    VALUE_SET_NAME = 'Hydroxyzine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1794552',
        '1794554',
        '995218',
        '995232',
        '995241',
        '995258',
        '995270',
        '995274',
        '995278',
        '995281',
        '995285',
        '995428'
    }

class Hyoscyamine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent hyoscyamine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; hyoscyamine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; hyoscyamine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1501'
    VALUE_SET_NAME = 'Hyoscyamine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1037234',
        '1044608',
        '1046770',
        '1046787',
        '1046815',
        '1046820',
        '1046982',
        '1046985',
        '1046997',
        '1047786',
        '1047805',
        '1047881',
        '1047895',
        '1047905',
        '1047916',
        '1048078',
        '1048124',
        '1048147',
        '1048307',
        '1048336',
        '1048411',
        '1050325',
        '1087365',
        '1440869',
        '1598634',
        '1807886',
        '998726'
    }

class Imipramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent imipramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; imipramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; imipramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1359'
    VALUE_SET_NAME = 'Imipramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '835564',
        '835568',
        '835572',
        '835577',
        '835586',
        '835589',
        '835591',
        '835593'
    }

class Indomethacin(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent indomethacin medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; indomethacin only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; indomethacin in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1366'
    VALUE_SET_NAME = 'Indomethacin'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1490727',
        '1491529',
        '197817',
        '197818',
        '251255',
        '310991',
        '310992',
        '392073'
    }

class Isotretinoin(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent isotretinoin medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; isotretinoin only. This is a grouping of RxNorm codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1143'
    VALUE_SET_NAME = 'Isotretinoin'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1547561',
        '1547565',
        '197843',
        '197844',
        '197845',
        '403930'
    }

class Isoxsuprine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent isoxsuprine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; isoxsuprine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; isoxsuprine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1422'
    VALUE_SET_NAME = 'Isoxsuprine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1298799',
        '1298834'
    }

class KetorolacTromethamine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent ketorolac tromethamine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; ketorolac tromethamine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; ketorolac tromethamine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1364'
    VALUE_SET_NAME = 'Ketorolac Tromethamine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1665459',
        '1665461',
        '1665675',
        '1665679',
        '1665682',
        '1797855',
        '834022',
        '860092',
        '860096',
        '860113',
        '860114',
        '860115',
        '861846'
    }

class ListOfSingleRxnormCodeConceptsForHighRiskDrugsForTheElderly(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent medication concepts considered as high risk for the elderly.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; medications considered high risk for the elderly.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1272'
    VALUE_SET_NAME = 'List of Single RxNorm Code Concepts for High Risk Drugs for the Elderly'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1363513',
        '238133',
        '312289',
        '313406',
        '860771',
        '889614'
    }

class LowIntensityStatinTherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent low intensity statin medications as defined by the 2013 American College of Cardiology (ACC) and the American Heart Association (AHA) guideline.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with low intensity statin therapy medications.

    **Exclusion Criteria:** Excludes any other intensity of statin therapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1574'
    VALUE_SET_NAME = 'Low Intensity Statin Therapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1790679',
        '1944264',
        '197903',
        '197904',
        '2001254',
        '310404',
        '310405',
        '312962',
        '314231',
        '433849',
        '476345',
        '757702',
        '861643',
        '904458',
        '904467'
    }

class Meclizine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent meclizine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; meclizine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; meclizine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1506'
    VALUE_SET_NAME = 'Meclizine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1663815',
        '995624',
        '995632',
        '995666',
        '995682',
        '995686'
    }

class MedicationsForAboveNormalBmi(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent clinical medications prescribed for weight loss to patients with an above normal BMI measurement.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with oral drug forms prescribed for weight loss in patients with an above normal BMI measurement.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1561'
    VALUE_SET_NAME = 'Medications for Above Normal BMI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1112982',
        '1112987',
        '1249083',
        '1300706',
        '1302827',
        '1302839',
        '1302850',
        '1313059',
        '1808549',
        '314153',
        '692876',
        '803348',
        '803353',
        '826131',
        '826919',
        '900038',
        '968766',
        '978654',
        '978668'
    }

class MedicationsForBelowNormalBmi(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent clinical medications prescribed for weight gain to patients with a below normal BMI measurement.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with oral drug forms prescribed for weight gain in patients with a below normal BMI measurement.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.526.3.1562'
    VALUE_SET_NAME = 'Medications for Below Normal BMI'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197634',
        '197635',
        '197636',
        '577154',
        '860215',
        '860221',
        '860225',
        '860231'
    }

class Megestrol(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent megestrol medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs; generic; human use only; prescribable; megestrol only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; megestrol in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1342'
    VALUE_SET_NAME = 'Megestrol'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '577154',
        '860215',
        '860221',
        '860225',
        '860231'
    }

class Meperidine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent meperidine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; meperidine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; meperidine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1351'
    VALUE_SET_NAME = 'Meperidine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1655058',
        '1655060',
        '861455',
        '861467',
        '861479'
    }

class Meprobamate(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent meprobamate medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; meprobamate only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; meprobamate in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1284'
    VALUE_SET_NAME = 'Meprobamate'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197928',
        '197929',
        '197930'
    }

class Metaxalone(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent metaxalone medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; metaxalone only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; metaxalone in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1358'
    VALUE_SET_NAME = 'Metaxalone'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197935',
        '351254'
    }

class Methocarbamol(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent methocarbamol medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; methocarbamol only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; methocarbamol in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1370'
    VALUE_SET_NAME = 'Methocarbamol'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '197943',
        '197944',
        '197945'
    }

class Methyldopa(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent methyldopa medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; methyldopa only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; methyldopa in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1331'
    VALUE_SET_NAME = 'Methyldopa'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '104357',
        '197955',
        '197956',
        '197958',
        '197959',
        '197960',
        '197961',
        '197962',
        '197963'
    }

class ModerateIntensityStatinTherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent moderate intensity statin medications as defined by the 2013 American College of Cardiology (ACC) and the American Heart Association (AHA) guideline.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category or attribute related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with moderate intensity statin therapy medications.

    **Exclusion Criteria:** Excludes any other intensity of statin therapy.
    """

    OID = '2.16.840.1.113883.3.526.3.1575'
    VALUE_SET_NAME = 'Moderate Intensity Statin Therapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1790679',
        '1944264',
        '197905',
        '198211',
        '2001262',
        '2001266',
        '200345',
        '2167557',
        '2167573',
        '310405',
        '312961',
        '359731',
        '359732',
        '360507',
        '476349',
        '476350',
        '597967',
        '597971',
        '597974',
        '597977',
        '597980',
        '597987',
        '617310',
        '617312',
        '757703',
        '757704',
        '859424',
        '859747',
        '861648',
        '861652',
        '904475',
        '904481'
    }

class Nifedipine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nifedipine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; nifedipine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; nifedipine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1353'
    VALUE_SET_NAME = 'Nifedipine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '198032',
        '198033',
        '199329',
        '199782',
        '314132',
        '391901',
        '391980'
    }

class NonbenzodiazepineHypnotics(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nonbenzodiazepine hypnotic medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; nonbenzodiazepine hypnotic medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; benzodiazepine derivative medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1480'
    VALUE_SET_NAME = 'Nonbenzodiazepine hypnotics'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1232194',
        '1232202',
        '313761',
        '313762',
        '485440',
        '485442',
        '485465',
        '828692',
        '836641',
        '836647',
        '854873',
        '854876',
        '854880',
        '854885',
        '854886',
        '854894'
    }

class Nortriptyline(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent nortriptyline medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; nortriptyline only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; nortriptyline in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1507'
    VALUE_SET_NAME = 'Nortriptyline'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '198045',
        '198046',
        '198047',
        '199283',
        '199406',
        '312036',
        '317136',
        '865143',
        '865146'
    }

class OpiateAntagonists(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts to represent treatment of substance abuse with an opioid antagonist medication.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Encounter, Performed.

    **Inclusion Criteria:** Includes only relevant concepts associated treatment of substance abuse with an opiate antagonist medication. This is a grouping of ICD10PCS codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113883.3.464.1003.198.12.1132'
    VALUE_SET_NAME = 'Opiate Antagonists'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1010600',
        '1010604',
        '1307056',
        '1307061',
        '1431076',
        '1431102',
        '1483744',
        '1483774',
        '1483780',
        '1542390',
        '1544851',
        '1544854',
        '1597568',
        '1597573',
        '1655032',
        '1666338',
        '1797650',
        '1864412',
        '1996184',
        '1996192',
        '2058257',
        '238129',
        '246474',
        '250426',
        '351264',
        '351265',
        '351266',
        '351267',
        '637213'
    }

class Orphenadrine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent aspirin / caffeine / orphenadrine combination medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; aspirin / caffeine / orphenadrine (combination medication).

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; aspirin / caffeine / orphenadrine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1302'
    VALUE_SET_NAME = 'Orphenadrine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '994521',
        '994528',
        '994535',
        '994810',
        '994811',
        '994824',
        '994837',
        '994841',
        '994847'
    }

class Paroxetine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent paroxetine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; paroxetine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; paroxetine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1508'
    VALUE_SET_NAME = 'Paroxetine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1430122',
        '1738483',
        '1738495',
        '1738503',
        '1738511',
        '1738515',
        '1738519',
        '1738523',
        '1738527',
        '1738803',
        '1738805',
        '1738807',
        '312242'
    }

class Pentobarbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Pentobarbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Pentobarbital only; Pentobarbital in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1518'
    VALUE_SET_NAME = 'Pentobarbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '238090'
    }

class PharmacologicTherapyForHypertension(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent clinical medications prescribed for patients diagnosed with hypertension.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; oral and injectable drug forms that are prescribed for treatment of hypertension.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.526.1577'
    VALUE_SET_NAME = 'Pharmacologic Therapy for Hypertension'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1000001',
        '1011710',
        '1011713',
        '1011736',
        '1011739',
        '1011750',
        '1011753',
        '1013930',
        '1013937',
        '104222',
        '1091646',
        '1091652',
        '1092566',
        '1191185',
        '1233709',
        '1234256',
        '1235144',
        '1235151',
        '1297753',
        '1297757',
        '1299859',
        '1299871',
        '1299890',
        '1299896',
        '1299897',
        '1423767',
        '1435624',
        '1495058',
        '152916',
        '153822',
        '153823',
        '1593725',
        '1606347',
        '1606349',
        '1656340',
        '1656349',
        '1656354',
        '1665057',
        '1665061',
        '1719286',
        '1719290',
        '1719291',
        '1729200',
        '1729205',
        '1736541',
        '1736546',
        '1790239',
        '1790245',
        '1790247',
        '1791229',
        '1791232',
        '1791233',
        '1791240',
        '1798281',
        '1806884',
        '1923422',
        '1923424',
        '1923426',
        '197361',
        '197379',
        '197380',
        '197381',
        '197382',
        '197383',
        '197417',
        '197418',
        '197419',
        '197436',
        '197437',
        '197438',
        '197439',
        '197475',
        '197476',
        '197499',
        '197500',
        '197625',
        '197626',
        '197627',
        '197628',
        '197730',
        '197731',
        '197732',
        '197745',
        '197746',
        '197770',
        '197815',
        '197816',
        '197848',
        '197849',
        '197884',
        '197885',
        '197886',
        '197887',
        '197951',
        '197956',
        '197958',
        '197960',
        '197963',
        '197977',
        '197978',
        '197979',
        '197986',
        '197987',
        '198000',
        '198001',
        '198006',
        '198007',
        '198008',
        '198032',
        '198033',
        '198034',
        '198035',
        '198036',
        '198037',
        '198104',
        '198105',
        '198110',
        '198111',
        '198112',
        '198141',
        '198188',
        '198189',
        '198198',
        '198222',
        '198223',
        '198224',
        '198225',
        '198284',
        '198285',
        '198286',
        '198312',
        '198313',
        '198314',
        '198316',
        '198369',
        '198370',
        '198371',
        '198372',
        '199277',
        '199329',
        '199351',
        '199352',
        '199353',
        '199610',
        '199622',
        '199717',
        '199757',
        '199776',
        '199783',
        '199797',
        '199798',
        '199799',
        '199816',
        '199817',
        '199903',
        '1999031',
        '1999033',
        '1999035',
        '1999037',
        '200031',
        '200032',
        '200033',
        '200094',
        '200095',
        '200096',
        '200284',
        '200285',
        '205304',
        '205305',
        '205326',
        '251856',
        '251857',
        '260376',
        '261962',
        '282486',
        '282755',
        '283316',
        '283317',
        '308135',
        '308136',
        '308614',
        '308962',
        '308963',
        '308964',
        '309198',
        '310140',
        '310429',
        '310792',
        '310793',
        '310796',
        '310797',
        '310798',
        '310809',
        '310812',
        '310818',
        '311353',
        '311354',
        '311671',
        '311984',
        '311985',
        '312593',
        '312594',
        '312748',
        '312749',
        '312750',
        '313096',
        '313215',
        '313217',
        '313219',
        '313988',
        '314076',
        '314077',
        '314132',
        '314203',
        '317173',
        '349199',
        '349200',
        '349201',
        '349353',
        '349373',
        '349401',
        '349405',
        '349483',
        '351292',
        '351293',
        '360344',
        '387013',
        '401965',
        '401968',
        '402695',
        '402696',
        '402698',
        '403853',
        '403854',
        '403855',
        '404011',
        '404013',
        '411434',
        '429503',
        '477130',
        '484152',
        '485471',
        '562518',
        '562520',
        '577776',
        '578325',
        '578330',
        '597967',
        '597971',
        '597974',
        '597977',
        '597980',
        '597984',
        '597987',
        '597990',
        '597993',
        '636042',
        '636045',
        '636360',
        '636361',
        '639537',
        '686924',
        '722126',
        '722131',
        '722134',
        '722137',
        '727574',
        '727575',
        '730861',
        '730866',
        '730869',
        '730872',
        '751612',
        '751618',
        '763519',
        '763574',
        '763589',
        '790489',
        '802749',
        '827073',
        '830795',
        '830801',
        '830837',
        '830845',
        '830861',
        '830865',
        '830869',
        '830872',
        '830874',
        '830877',
        '830879',
        '830882',
        '830897',
        '830900',
        '831054',
        '831102',
        '831103',
        '831359',
        '833217',
        '845488',
        '848131',
        '848135',
        '848140',
        '848145',
        '848151',
        '854901',
        '854905',
        '854908',
        '854916',
        '854919',
        '854925',
        '854984',
        '854988',
        '856422',
        '856429',
        '856443',
        '856448',
        '856457',
        '856460',
        '856481',
        '856519',
        '856535',
        '856556',
        '856569',
        '856578',
        '856713',
        '856724',
        '856733',
        '857166',
        '857169',
        '857174',
        '857183',
        '857187',
        '858580',
        '858587',
        '858599',
        '858603',
        '858607',
        '858613',
        '858616',
        '858804',
        '858810',
        '858813',
        '858817',
        '858824',
        '858828',
        '858921',
        '860510',
        '860516',
        '860522',
        '860532',
        '861402',
        '862006',
        '862013',
        '862019',
        '862025',
        '866412',
        '866419',
        '866427',
        '866436',
        '866452',
        '866461',
        '866472',
        '866479',
        '866482',
        '866491',
        '866508',
        '866511',
        '866514',
        '866924',
        '876514',
        '876519',
        '876524',
        '876529',
        '884173',
        '884185',
        '884189',
        '884192',
        '884198',
        '884203',
        '884221',
        '884225',
        '892791',
        '896758',
        '896762',
        '896766',
        '896771',
        '896983',
        '896987',
        '897584',
        '897590',
        '897596',
        '897612',
        '897618',
        '897624',
        '897630',
        '897640',
        '897649',
        '897659',
        '897666',
        '897683',
        '897722',
        '897781',
        '897783',
        '897844',
        '897853',
        '898316',
        '898342',
        '898346',
        '898350',
        '898353',
        '898356',
        '898359',
        '898362',
        '898367',
        '898372',
        '898378',
        '898687',
        '898690',
        '898719',
        '898723',
        '901438',
        '904589',
        '904630',
        '905199',
        '905222',
        '905225',
        '905377',
        '905395',
        '966571',
        '977880',
        '977883',
        '977959',
        '979432',
        '979464',
        '979468',
        '979471',
        '979480',
        '979485',
        '979492',
        '998685',
        '998689',
        '998693',
        '998695',
        '999967',
        '999986',
        '999991',
        '999996'
    }

class Phenobarbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent phenobarbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; phenobarbital only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; Phenobarbital in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1348'
    VALUE_SET_NAME = 'Phenobarbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1046787',
        '1046815',
        '1046997',
        '1048147',
        '1091265',
        '1294394',
        '198083',
        '198084',
        '198085',
        '198086',
        '198089',
        '198368',
        '199164',
        '199167',
        '199168',
        '245385',
        '251325',
        '282462',
        '282463',
        '308589',
        '312357',
        '312362',
        '312363',
        '312368',
        '312370',
        '702519',
        '756143',
        '756144',
        '756260',
        '756331'
    }

class PromethazineHydrochloride(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent promethazine hydrochloride medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; promethazine hydrochloride only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; promethazine hydrochloride in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1367'
    VALUE_SET_NAME = 'Promethazine Hydrochloride'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1248057',
        '756160',
        '861578',
        '991486',
        '991528',
        '992432',
        '992438',
        '992447',
        '992460',
        '992471',
        '992475',
        '992858',
        '992898',
        '992900',
        '992904',
        '992908',
        '996757'
    }

class Propantheline(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Propantheline medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Propantheline only; Propantheline in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1519'
    VALUE_SET_NAME = 'Propantheline'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '198165',
        '312673'
    }

class Protriptyline(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent protriptyline medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; protriptyline only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; protriptyline in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1509'
    VALUE_SET_NAME = 'Protriptyline'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '905168',
        '905172'
    }

class Scopolamine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Scopolamine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; Scopolamine only; Scopolamine in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1520'
    VALUE_SET_NAME = 'Scopolamine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1046787',
        '1046815',
        '1046997',
        '1048078',
        '1048124',
        '1048147',
        '106507',
        '198207',
        '199442',
        '200059',
        '226552',
        '245350',
        '250536',
        '250537',
        '412723',
        '429720'
    }

class Secobarbital(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent Secobarbital medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; secobarbital only; secobarbital in combination with other medications.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1521'
    VALUE_SET_NAME = 'Secobarbital'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '308167',
        '308171',
        '312914',
        '315201'
    }

class StatinAllergen(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent an allergy to statin medications.

    **Data Element Scope:** This value set may use Quality Data Model (QDM) category related to Allergy/Intolerance.

    **Inclusion Criteria:** Includes only relevant concepts associated with statins and statin allergens. This is a grouping value set of RXNORM and SNOMED codes.

    **Exclusion Criteria:** No exclusions.
    """

    OID = '2.16.840.1.113762.1.4.1110.42'
    VALUE_SET_NAME = 'Statin Allergen'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '301542',
        '36567',
        '41127',
        '42463',
        '6472',
        '83367',
        '861634'
    }

    SNOMEDCT = {
        '372912004'
    }

class TobaccoUseCessationPharmacotherapy(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent medications that may be used to assist patients in decreasing or quitting tobacco use.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) category related to Medication.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; prescribable; bupropion hydrochloride, nicotine products (e.g., chewing gum, nasal spray, etc.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredients only; non-prescribable.
    """

    OID = '2.16.840.1.113883.3.526.3.1190'
    VALUE_SET_NAME = 'Tobacco Use Cessation Pharmacotherapy'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1232585',
        '151226',
        '1551468',
        '1797886',
        '1801289',
        '198029',
        '198030',
        '198031',
        '198045',
        '198046',
        '198047',
        '199283',
        '199888',
        '199889',
        '199890',
        '205315',
        '205316',
        '250983',
        '311975',
        '312036',
        '314119',
        '317136',
        '359817',
        '359818',
        '636671',
        '636676',
        '749289',
        '749788',
        '892244',
        '993503',
        '993518',
        '993536',
        '993541',
        '993550',
        '993557',
        '993567',
        '993681',
        '993687',
        '993691',
        '998671',
        '998675',
        '998679'
    }

class Trihexyphenidyl(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent trihexyphenidyl medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; trihexyphenidyl only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; trihexyphenidyl in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1334'
    VALUE_SET_NAME = 'Trihexyphenidyl'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '905269',
        '905273',
        '905283',
        '905292'
    }

class Trimipramine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent trimipramine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; trimipramine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; trimipramine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1285'
    VALUE_SET_NAME = 'Trimipramine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '199820',
        '245372',
        '245373',
        '245374',
        '250033',
        '313496',
        '313497',
        '313498',
        '313499'
    }

class Triprolidine(ValueSet):
    """
    **Clinical Focus:** This value set contains concepts that represent triprolidine medications.

    **Data Element Scope:** This value set may use the Quality Data Model (QDM) datatype related to Medication, Ordered.

    **Inclusion Criteria:** Includes only relevant concepts associated with semantic clinical drugs (concepts associated with component, form and strength); generic; human use only; prescribable; triprolidine only.

    **Exclusion Criteria:** Excludes branded drugs; components or ingredient only; non-prescribable; triprolidine in combination with other medications.
    """

    OID = '2.16.840.1.113883.3.464.1003.196.12.1408'
    VALUE_SET_NAME = 'Triprolidine'
    EXPANSION_VERSION = 'eCQM Update 2020-05-07'

    RXNORM = {
        '1094434',
        '1099308',
        '1099446',
        '1099653',
        '1099668',
        '1099711',
        '1428927',
        '1490671',
        '1491649',
        '1492052',
        '1661319',
        '1789508',
        '1926926',
        '1939354',
        '2173662',
        '2173667',
        '996640'
    }
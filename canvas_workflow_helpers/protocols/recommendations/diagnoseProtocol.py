from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import DiagnoseRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2021 import DiagnosisOfHypertension



from canvas_workflow_kit.timeframe import Timeframe

"""
A protocol that follows the following logic: If a patient has vitals reading of high blood pressure, recommend
a diagnosis of hypertension.
"""


class Hypertension(ValueSet):
    """
    A ValueSet class that includes the coding for the condition that will populate the Diagnose command. If a title is
    not added to the recommendation, the value set name will populate the diagnose command.
    """
    VALUE_SET_NAME = 'Essential (Primary) Hypertension'
    ICD10CM = {'H35031', 'I10'}




class DiagnoseProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload diagnoseProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and vital sign (it will re-run if a new
        vitals panel has been entered).

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Hypertension Diagnosis'

        description = 'Diagnose a patient with hypertension if their vitals contain elevated levels of blood pressure.'

        version = '2022-08-08v0'

        information = 'https://www.cdc.gov/bloodpressure/facts.htm'

        identifiers = ['ACM15']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.VITAL_SIGN
        ]

        references = [
            'https://www.cdc.gov/bloodpressure/facts.htm'
        ]

    def in_denominator(self):
        """
        If the patient has high blood pressure on record, this function will return true.
        """
        HBP_records = [] #a list to store any records for high blood pressure
        for record in self.patient.vital_signs: # for each record in the vital signs list
            if record['loincNum'] == "8480-6": #if the record is a recording of the systole bp
                if (record['value'] != "") and (record['value'].isnumeric()):
                #This check is required because when vital signs are recorded in Canvas, the entire list of vitals
                #are stored, and teh one's that are not filled out are just stored as empty.
                    if int(record['value']) > 130: #if the systole bp is higher than recommended
                        HBP_records.append(record)
            elif record['loincNum'] ==  "8462-4": #diastole
                if (record['value'] != "") and (record['value'].isnumeric()):
                    if int(record['value']) > 80: #if the diastole is higher than recommended
                        HBP_records.append(record)
        return HBP_records != []


    def in_numerator(self):
        """
        Determines whether a patient has satisfied the protocol. In this case, it checks for an existing diagnosis
        of hypertension, it will return True.
        """

        hypertension_conditions = self.patient.conditions.find(DiagnosisOfHypertension).filter(
            clinicalStatus='active')

        return bool(hypertension_conditions)


    def compute_results(self):
        """
        A diagnose recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are diagnosing a patient, it has been
        set to 'diagnose'

        - patient is always going to be set to self.patient

        - condition is a class that contains codings that map to specific diagnoses. A valid coding will result in the
        Diagnose command being populated with this condition.

        - title is used to display next to the button. It is also the text that will populate the diagnose command, and will
        be displayed as the name of the diagnosis on the patient's chart. It is strongly recommended that the title is set
        to the name of the diagnosis.

        - narrative displays under the title of the protocol on the patient's protocols page
        (result.add_narrative(diagnose_recommendation.narrative)). Without this, it will not display on the UI.

        """
        diagnose_recommendation = DiagnoseRecommendation(
            key='RECOMMEND_HYPERTENSION_DIAGNOSIS',
            rank=1,
            button='Diagnose',
            patient=self.patient,
            condition=Hypertension,
            title='Essential Hypertension',
            narrative="This is the narrative!"
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been diagnosed with hypertension.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    diagnose_recommendation
                )
                result.add_narrative(
                    diagnose_recommendation.narrative
                )


        return result

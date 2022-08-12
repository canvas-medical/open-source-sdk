from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import InstructionRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe

"""
Below is an importation of a valueset that contains a list of codes that all represent unique instruction on
diet and nutrition. This valueset will be used to search to determine if a patient has already received instruction
on this within the last year.
"""
from canvas_workflow_kit.value_set.v2022.intervention import CounselingForNutrition #Imports an entire ValueSet.





"""
Instruct patients who have a record of high blood pressure on how to eat healthy.

Protocol reminds user to instruct patients on a healthy diet once every 5 years
if they have ever had a record of high blood pressure (regardless of when high blood
pressure was recorded).
"""


"""
This is a ValueSet class that is only importing a single code. This later will be used as a recommendation for what to
autofill the instruct command with.
"""
class LowCholesterolInstruction(ValueSet):
    VALUE_SET_NAME = 'How to Eat to Lower Cholesterol'
    SNOMEDCT = {'183062005'}


class InstructionProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload imagingProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        vital sign (so it will re-run if a patient has a new or changed vital signs report) and instruction (it will re-run if a new
        instruction has been recorded)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Instruct patient on healthy diet recommendations'

        description = 'Review the building blocks of a healthy and nutrient-dense diet.'

        version = '2022-07-07v3'

        information = 'https://www.cdc.gov/healthyweight/healthy_eating/index.html'

        identifiers = ['ACM03']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.VITAL_SIGN,
            CHANGE_TYPE.INSTRUCTION,
        ]

        references = [
            'https://www.cdc.gov/healthyweight/healthy_eating/index.html'
        ]

    def in_denominator(self):
        """
        If the patient has high blood pressure on record, it will return true
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
        #return true if there exists a record where BP is above 130 systolic or 80 diastolic.

    def in_numerator(self):
        """
        If the patient has already received instruction on healthy eating within the last 5 years,
        it will return false
        """
        last_instructing_timeframe = Timeframe(self.now.shift(years=-5), self.now)
        instruction_completed = self.patient.instructions.find(
            CounselingForNutrition
        ).within(last_instructing_timeframe)
        return bool(instruction_completed)
        #returns True if the patient has already been instructed on how to maintain a healthy diet.

    def compute_results(self):
        """
        An instruction recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are ordering an image, it has been
        set to 'order'

        - patient is always going to be set to self.patient

        - instruction is a class that contains codings that map to specific instructions. The valueset must be imported. A valid
        coding will result in the instruct command being autofilled with this type. If multiple codes are entered, ........TODO

        - title is used to display next to the button. It is also used if there is not a matching instruction
        for the given coding (from the 'imaging' attribute) to generate a display title within the instruction command.
        If the title starts with 'order a', 'refer for a' or 'perform a', everything after those phrases is kept and saved as
        the instruction's title. If none of these keywords are at the beginning of the title, the instruction command will
        simply populate with the entire string inputtef as title.

        - narrative displays under the title of the protocol on the patient's protocols page (via
        result.add_narrative(instruction_recommendation.narrative)). Without this, it will not display on the UI.

        """
        instruction_recommendation = InstructionRecommendation(
            key='RECOMMEND_DISCUSS_DIET',
            rank=1,
            button='Instruct',
            patient=self.patient,
            instruction=LowCholesterolInstruction,
            title='Discuss and Instruct on Dietary Recommendations',
            narrative="This is the narrative"
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been instructed on dietary recommendations.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    instruction_recommendation
                )
                result.add_narrative(instruction_recommendation.narrative)


        return result

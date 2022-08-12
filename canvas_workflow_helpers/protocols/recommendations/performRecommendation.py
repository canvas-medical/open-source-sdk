from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import PerformRecommendation
from canvas_workflow_kit.value_set.v2021.diagnosis import RetinalDetachmentWithRetinalDefect
from canvas_workflow_kit.value_set.v2021 import RetinalOrDilatedEyeExam
from canvas_workflow_kit.value_set import ValueSet



from canvas_workflow_kit.timeframe import Timeframe



"""
This protocol recommends a retinal eye exam for all patients diagnosed with any retinal detachment or retinal defect.
It will be satisfied if a retinal exam is completed.
"""


class EyeExam(ValueSet):
    VALUE_SET_NAME = 'Remote Imaging Retinal Exam'
    CPT = {'92229' }



class PerformProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload PerformgProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and encounter (it will re-run after any changes
        are made to an encounter)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Retinal Detachment Eye Exam'

        description = 'Perform a remote imaging exam on the retina post-retinal detachment'

        version = '2022-07-18v0'

        information = 'https://www.mayoclinic.org/diseases-conditions/retinal-detachment/symptoms-causes/syc-20351344'

        identifiers = ['ACM06']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.ENCOUNTER,
            CHANGE_TYPE.CONDITION
        ]

        references = [
            'https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/retinal-detachment#:~:text=Your%20doctor%20will%20give%20you,be%20uncomfortable%20for%20some%20people.'
        ]

    def in_denominator(self):
        """
        This fucntion determines if a patient qualifies for this protocol. Specifically, this function determines if the
        patient has an active condition of retinal detachment.
        """
        # example:
        retinal_conditions = self.patient.conditions.find(RetinalDetachmentWithRetinalDefect).filter(
            clinicalStatus='active')

        return retinal_conditions.records != []
        #returns true if the patient has an active condition of retinal detachment/retinal defects


    def in_numerator(self):
        """
        This function determines if a patient has satisfied this protocol. Specifically, it checks if there has been an
        eye exam within the period since the diagnosis to the current date and time. Any eye exams that happened previous
        to the injury or diagnosis will not satisfy the protocol.
        """
        diagnosis_date = self.patient.conditions.find(RetinalDetachmentWithRetinalDefect)[0].get("created")
        exam_timeframe = Timeframe(diagnosis_date, self.now)
        exam_completed = self.patient.procedures.find(
            EyeExam
        ).within(exam_timeframe)
        return bool(exam_completed)
        #returns true if the patient has already recieved an eye exam post-diagnosis.



    def compute_results(self):
        """
        A perform recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending a procedure, it has been
        set to 'perform'

        - patient is always going to be set to self.patient

        - procedure is a class that contains codings that map to specific procedures. The valueset must be imported. A valid
        coding will result in the perform command being autofilled with this procedure. In order for the command to autofill,
        these codes must be within the fee schedule page on the admin settings. If multiple codes are entered (and are in the fee
        schedule), the display will default to the item in the list that was last entered into your practice's database.

        - condition is a valueset that contains the condition code for the diagnosis tied to this lab report. It is only used to
        generate a narrative if a title is not included. The name of the valueset is utilized in the narrative that is autogenerated
        when title is absent. This Valueset can contain multiple codes since the only thing pulled from it is the name.

        - title is used to display next to the button. It is also used to title the procedure if it is a valid coding within the fee scheduler.
        If the title starts with 'order a', 'refer for a' or 'perform a', everything after those phrases is kept and saved as
        the procedure's title. After this text, the coding associated with the procedure is added in parentheses.
        (Eg. Retinal Examination (CPT: 92229))
        ** Note: the fee schedule only accepts CPT codes.

        - narrative displays under the title of the protocol on the patient's protocols page via:
        (result.add_narrative(perform_recommendation.narrative)). Without this, it will not display on the UI.

        """

        perform_recommendation = PerformRecommendation(
            key='RECOMMEND_PERFORM_EYE_EXAM',
            rank=1,
            button='Perform',
            patient=self.patient,
            procedure=EyeExam,
            condition=RetinalDetachmentWithRetinalDefect,
            title='Perform retinal examination'
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been given an eye exam.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    perform_recommendation
                )


        return result

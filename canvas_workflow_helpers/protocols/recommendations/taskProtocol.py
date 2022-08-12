from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import TaskRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe


"""
A protocol to recommend that a medical reconciliation is completed for patients.
"""

class TaskProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload taskProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on
        condition (so it will re-run if a patient has a new diagnosis) and task (it will re-run if a new task is created)

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Routine Medication Reconsiliation'

        description = 'Ensure medications are up to date'

        version = '2022-07-21v0'

        information = 'https://www.ihi.org/Topics/ADEsMedicationReconciliation/Pages/default.aspx'

        identifiers = ['ACM11']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.PATIENT,
            CHANGE_TYPE.TASK
        ]

        references = [
            'https://psnet.ahrq.gov/primer/medication-reconciliation'
        ]

    def in_denominator(self):
        """
        Returns true for patients who qualify for this protocol. All patients qualify for this protocol,
        so this function will always return true.
        """

        return True # all patients qualify for this protocol

    def in_numerator(self):
        """
        Determines if a patient has satisfied the protocol. In this case, if there has ever been a task created
        for medicine reconsiliation, it will return true.
        """

        task_completed = self.patient.tasks.filter(
            title='Medication Reconciliation Task'
        )
        return bool(task_completed)


    def compute_results(self):
        """
        A task recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are creating a task, it has been
        set to 'task'

        - patient is always going to be set to self.patient

        - title is used to display next to the button. It also populates the task command as the title of the task.

        - narrative displays under the title of the protocol on the patient's protocols page via
        (result.add_narrative(task_recommendation.narrative)). Without this, it will not display on the UI.

        - context is a dictionary that optionally may include a 'labels' key that maps to a list of strings. If any labels other
        than 'Urgent', 'Routine' or 'Emergent' are entered, they will not be displayed. Context may also include 'due_date' which
        maps to a date stirng, formatted as YYYY-MM-DD.

        """
        task_recommendation = TaskRecommendation(
            patient=self.patient,
            key='TASK_MEDICATION_RECONCILIATION',
            rank=1,
            button='Task',
            title='Medication Reconciliation Task',
            context={
            'labels':['Urgent'],
            'due_date':'2022-07-31'
            },
            narrative="Patient medications should be reviewed for safety measures."
        )
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'A task has already been created for {self.patient.first_name}.'
                )
            else:
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    task_recommendation
                )


        return result

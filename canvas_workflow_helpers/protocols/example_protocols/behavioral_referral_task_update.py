import requests
from canvas_workflow_kit.protocol import ClinicalQualityMeasure, ProtocolResult
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.fhir import FumageHelper


class BehvaioralReferralTaskUpdate(ClinicalQualityMeasure):

    class Meta:
        title = "Behavioral Referral Task Update"
        version = "2023-v01"
        description = "This protocol updates the label and team for a task created from a behavioral health referral. "
        information = "https://link_to_protocol_information"
        types = ["Task"]
        compute_on_change_types = [CHANGE_TYPE.TASK]
        authors = ["Canvas Example Medical Association (CEMA)"]
        notification_only = True

    token = None
    task_id = None

    # TODO: These are hard coded variables that can be updated based on your needs

    # The group ID you can retreive from a FHIR Group Search call
    behavioral_group_fhir_id = "Group/e3fabb40-1ccc-4bb4-9e64-e813f27bf2e2"

    # This is the name of the Team/Group you want to use when re-assigning a task
    behavioral_group_name = "Behavioral Health Coordinators"

    # This is the label you want to add to the task we are updating
    internal_referral_label = "Internal Referral"

    # This is the exact title of the Task we are trying to find and update
    referral_task_title = "Refer patient to Psychiatry (TBD)"

    ##################### HELPER FUNCTIONS ##################################

    def get_fhir_api_token(self):
        """Given the Client ID and Client Secret for authentication to FHIR,
        return a bearer token"""

        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET

        token_response = requests.request(
            "POST",
            f"https://{self.settings.INSTANCE_NAME}.canvasmedical.com/auth/token/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}",
        )

        if token_response.status_code != 200:
            raise Exception('Unable to get a valid FHIR bearer token')

        return token_response.json().get("access_token")

    def get_fhir_task(self):
        """Given a Task ID, request a FHIR Task Resource"""

        response = self.fhir.search("Task", {"identifier": self.task_id})

        if response.status_code != 200:
            raise Exception(f'Failed to get FHIR Task {self.task_id} {response.text} {response.headers}')

        resources = response.json().get("entry", [])
        if len(resources) == 0:
            return None

        return resources[0].get("resource")

    def update_fhir_task(self, task):
        """Given a Task ID and Task Resource perform a FHIR Task Update"""

        response = fhir.update("Task", self.task_id, task)

        if response.status_code != 200:
            raise Exception(f"Failed to mark Task as completed with {response.status_code} and payload {payload} {response.text} {response.headers}")

    def edit_task(self, task):
        """Given a Task update the payload to supply a Group extension and label"""

        # Add an extension for Group assignee in the task payload
        new_extension = {
            "url": "http://schemas.canvasmedical.com/fhir/extensions/task-group",
            "valueReference": {
                "reference": self.behavioral_group_fhir_id,
                "display": self.behavioral_group_name,
            },
        }
        extension = [*task.get("extension", []), new_extension]

        # add label to the task payload
        new_input = {
            "type": {"text": "label"},
            "valueString": self.internal_referral_label,
        }
        input = [*task.get("input", []), new_input]

        new_task = task | {"extension": extension, "input": input}
        return {k: v for k, v in new_task.items() if k != "note"}

    def is_a_referral_task(self):
        """Returns true if the task has the title we are targetting """

        return (
            len(
                self.patient.tasks.filter(
                    externallyExposableId=self.task_id, title=self.referral_task_title
                )
            )
            == 1
        )

    ##################### END HELPER FUNCTIONS ##################################

    def compute_results(self):
        """ This is the main function that will check if the task that triggered this protocol
        is the one that we are hoping to update. If it is, we fetch the task payload from FHIR
        and update the assignee and label
        """

        self.fhir = FumageHelper(self.settings)
        fhir.get_fhir_api_token()

        result = ProtocolResult()

        field_changes = self.field_changes or {}
        self.task_id = str(field_changes.get("external_id", ""))
        created = field_changes.get("created") == True
        if not created or not self.task_id or not self.is_a_referral_task():
            return result

        if not (task := self.get_fhir_task()):
            return result

        self.update_fhir_task(self.edit_task(task))

        return result

import requests
from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import ClinicalQualityMeasure, ProtocolResult
from canvas_workflow_kit.constants import CHANGE_TYPE


class BehvaioralReferralTaskUpdate(ClinicalQualityMeasure):
    """
    This protocol updates the label and team for a task created from a behvaioral health referral.
    """

    class Meta:
        title = "Behvaioral Referral Task Update"

        version = "2023-v01"

        description = "This protocol updates the label and team for a task created from a behvaioral health referral. "

        information = "https://link_to_protocol_information"

        identifiers = ["BehvaioralReferralTaskUpdate"]

        types = ["CQM"]

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [CHANGE_TYPE.TASK]

        authors = ["Canvas Example Medical Association (CEMA)"]

        notification_only = True

        token = None
        task_id = None

        behavioral_group_fhir_id = "Group/a588ba00-cc4f-4651-829b-4abf17803f89"
        behavioral_group_name = "Behavioral Health Coordinators"
        internal_referral_label = "Internal Referral"
        referral_task_title = "Refer patient to Psychiatry (TBD)"

    def get_fhir_api_token(self):
        """Given the Client ID and Client Secret for authentication to FHIR,
        return a bearer token"""

        if not self.token:
            return None

        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET

        token_response = requests.request(
            "POST",
            f"https://{self.settings.INSTANCE_NAME}.canvasmedical.com/auth/token/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}",
        )

        return token_response.json().get("access_token")

    def get_fhir_task(self):
        """Given a Task ID, request a FHIR Task Resource"""
        if not self.token or not self.task_id:
            return None

        bundle = requests.get(
            (
                f"https://fhir-{self.settings.INSTANCE_NAME}.canvasmedical.com/"
                f"Task?identifier={self.task_id}"
            ),
            headers={
                "Authorization": f"Bearer {self.token}",
                "accept": "application/json",
            },
        ).json()

        resources = bundle.get("entry", [])
        if len(resources) == 0:
            return None

        return resources[0].get("resource")

    def update_fhir_task(self, task):
        """Given a Task ID and Task Resource perform a FHIR Task Update"""
        if not self.token or not self.task_id:
            return None

        return requests.put(
            (
                f"https://fhir-{self.settings.INSTANCE_NAME}.canvasmedical.com/"
                f"Task/{self.task_id}"
            ),
            json=task,
            headers={
                "Authorization": f"Bearer {self.token}",
                "accept": "application/json",
                "content-type": "application/json",
            },
        )

    def edit_task(self, task):
        # update behavioral team to owner
        new_extension = {
            "url": "http://schemas.canvasmedical.com/fhir/extensions/task-group",
            "valueReference": {
                "reference": self.behavioral_group_fhir_id,
                "display": self.behavioral_group_name,
            },
        }
        extension = [*task.get("extension", []), new_extension]

        # add label
        new_input = {
            "type": {"text": "label"},
            "valueString": self.internal_referral_label,
        }
        input = [*task.get("input", []), new_input]

        new_task = task | {"extension": extension, "input": input}
        # remove owner
        return {k: v for k, v in new_task.items() if k != "owner"}

    def is_a_referral_task(self, task_id):
        return (
            len(
                self.patient.tasks.filter(
                    externallyExposableId=task_id, title=self.referral_task_title
                )
            )
            == 1
        )

    def compute_results(self):
        if not (token := self.get_fhir_api_token()):
            return result
        self.token = token

        result = ProtocolResult()

        field_changes = self.field_changes or {}
        task_id = field_changes.get("external_id")
        created = field_changes.get("created") == True
        if not created or not task_id or not self.is_a_referral_task(task_id):
            return result

        self.task_id = str(task_id)
        if not (task := self.get_fhir_task()):
            return result

        self.update_fhir_task(self.edit_task(task))

        return result

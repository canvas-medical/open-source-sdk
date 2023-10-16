from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_NOT_APPLICABLE
)
from canvas_workflow_kit.constants import CHANGE_TYPE
import requests
import json
from canvas_workflow_kit.utils import send_notification
from canvas_workflow_kit.fhir import FumageHelper

class TestFhir(ClinicalQualityMeasure):
    class Meta:
        title = 'Test FHIR'
        version = 'v1.0.0'
        description = 'Example of how to make a FHIR Endpoint call to Canvas'
        compute_on_change_types = [CHANGE_TYPE.PATIENT]
        notification_only = True


    # REPLACE this url with your server url which should receive these notifications
    notification_url = 'https://webhook.site/5ec63074-3419-4367-8227-b6facb96dd12'
    notification_headers = {'Content-Type': 'application/json'}

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        fhir = FumageHelper(self.settings)
        fhir.get_fhir_api_token()

        response = fhir.read("Patient", self.patient.patient['key'])
        if response.status_code != 200:
            raise Exception(f"Failed to find patient {self.patient.patient['key']} {response.text}")

        send_notification(self.notification_url, json.dumps(response.json()),
                          self.notification_headers)
        return result

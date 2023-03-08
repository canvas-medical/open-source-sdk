from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_NOT_APPLICABLE
)
from canvas_workflow_kit.constants import CHANGE_TYPE
import requests
import json
from canvas_workflow_kit.utils import send_notification

class TestFhir(ClinicalQualityMeasure):
    class Meta:

        title = 'Test FHIR'

        version = 'v1.0.0'

        description = 'Example of how to make a FHIR Endpoint call to Canvas'

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        compute_on_change_types = [
            CHANGE_TYPE.PATIENT
        ]

        funding_source = ''

        notification_only = True


    # REPLACE this url with your server url which should receive these notifications
    notification_url = 'https://webhook.site/5ec63074-3419-4367-8227-b6facb96dd12'
    notification_headers = {'Content-Type': 'application/json'}
    
    # change this to your canvas instance name
    instance_name = 'training'


    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        # These are stored in the Protocol Settings Model on the Canvas Settings Page
        grant_type = "client_credentials"
        client_id = self.settings.CLIENT_ID
        client_secret = self.settings.CLIENT_SECRET

        token_response = requests.request(
            "POST",
            f'https://{self.instance_name}.canvasmedical.com/auth/token/',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
        )

        token = token_response.json().get('access_token')

        response = requests.get(
            f"https://fhir-{self.instance_name}.canvasmedical.com/Patient/{self.patient.patient['key']}",
            headers={
                'Authorization': f'Bearer {token}',
                'accept': 'application/json'
            }
        )

        send_notification(self.notification_url, json.dumps(response.json()),
                          self.notification_headers)
        return result

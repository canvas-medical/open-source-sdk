import arrow
import requests
import json
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.value_set.value_set import ValueSet
from canvas_workflow_kit.fhir import FumageHelper


class Obesity(ValueSet):
    VALUE_SET_NAME = "Obesity, unspecified"
    ICD10CM = {'E669'}


class ReviewClaimTask(ClinicalQualityMeasure):

    class Meta:
        title = "Task to Review Claim"
        version = "2023-v01"
        description = "Task Creation based on diagnosis of obesity, use of cpt code 99402 and specific coverage"
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.BILLING_LINE_ITEM]
        notification_only = True

    # CHANGE FOR GIVEN INSTNACE
    CANVAS_BOT_KEY = '5eede137ecfe4124b8b773040e33be14'
    ASSIGNING_GROUP_ID = 'ddb6ae91-826c-431c-808b-b7a1f14b2bbb'


    def get_fhir_coverages(self):
        """Given a Patient, request a FHIR Coverage Resources"""

        response = self.fhir.search("Coverage", {"patient": f"Patient/{self.patient.patient_key}"})

        if response.status_code != 200:
            raise Exception(f'Failed to get FHIR Coverages for patient {response.text} {response.headers}')

        resources = response.json().get("entry", [])
        if len(resources) == 0:
            return None

        return resources

    def has_group_number_in_coverage(self, group_number, transactor_name, transactor_type):
        if any([
            c['transactorName'] == transactor_name and
            c['transactorType'] == transactor_type and
            c['isActive']
            for c in self.patient.coverages]):

            # search FHIR to get the group ID

            self.fhir = FumageHelper(self.settings)

            group_number_found = False
            for coverage in self.get_fhir_coverages():
                coverage = coverage['resource']
                if (
                    coverage['status'] == "active" and
                    coverage['payor'][0]['display'] == transactor_name
                ):
                    # skip over expired ones
                    if (coverage['period'].get("end") and
                        arrow.get(coverage['period']['end']).date() < arrow.now().date()):
                        continue

                    # confirm the group number
                    group_number_found = any([_class['type']['coding'][0]['code'] == 'group'
                        and _class['value'] == group_number
                        for _class in coverage['class']])

            return group_number_found

    def create_fhir_task(self):
        payload = json.dumps({
            "resourceType": "Task",
            "extension": [
                {
                  "url": "http://schemas.canvasmedical.com/fhir/extensions/task-group",
                  "valueReference": {
                    "reference": f"Group/{self.ASSIGNING_GROUP_ID}"
                  }
                }
            ],
            "status": "requested",
            "description": "Adjust diagnosis to Pre-Diabetes or Hypertension if present in patient problem list",
            "for": {
                "reference": f"Patient/{self.patient.patient_key}"
            },
            "requester": {
                "reference": f"Practitioner/{self.CANVAS_BOT_KEY}"
            },
            "input": [
                {
                  "type": {
                    "text": "label"
                  },
                  "valueString": "Urgent"
                }
            ],
            "restriction": {
                "period": {
                  "end": f'{arrow.now().shift(days=1).format("YYYY-MM-DD")}T00:00:00+00:00'
                }
            }
        })
        response = self.fhir.create("Task", payload)

        if response.status_code != 201:
            raise Exception(f"Failed to create FHIR Task status {response.status_code} and payload {payload} {response.text} {response.headers}")


    def has_diagnosis_with_cpt_code(self, condition, cpt_code):

        if self.field_changes['model_name'] == 'condition' and self.field_changes['created']:
            # check if the condition being added is Obesity
            conditions = self.patient.conditions.find(Obesity).filter(id=self.field_changes['canvas_id'])

            for condition in conditions:
                note_timestamp = condition['noteTimestamp']

                # see if billing line item exists on that note
                for item in self.patient.billing_line_items.filter(cpt=cpt_code):
                    if arrow.get(item['datetimeOfService']) == arrow.get(note_timestamp):
                        return True

        if self.field_changes['model_name'] == 'billinglineitem' and self.field_changes['created']:
            #check if the billing line being added is the one we care about
            items = self.patient.billing_line_items.filter(id=self.field_changes['canvas_id'], cpt=cpt_code)
            for item in items:
                note_timestamp = item['datetimeOfService']

                if len(self.patient.conditions.find(Obesity).filter(noteTimestamp=note_timestamp)):
                    return True

    def compute_results(self):
        result = ProtocolResult()

        if self.has_group_number_in_coverage(
            group_number='123456789',
            transactor_name="AL BCBS",
            transactor_type="commercial"):

                if self.has_diagnosis_with_cpt_code(condition=Obesity, cpt_code='99402'):
                    result.status = STATUS_DUE
                    self.create_fhir_task()
                else:
                    result.status = STATUS_SATISFIED
        else:
            result.add_narrative("No AL BCBS coverage found with group number 123456789")

        return result

import arrow
import requests
from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.fhir import FumageHelper


class CPTCoverageBannerAlert(ClinicalQualityMeasure):

    class Meta:
        title = "CPT Coverage Banner Alert"
        version = "2023-v01"
        description = "Banner alert that displays cpt code recommendation based on coverage"
        types = []
        compute_on_change_types = [CHANGE_TYPE.COVERAGE]
        notification_only = True

    def get_fhir_coverages(self):
        """Given a Patient, request a FHIR Coverage Resources"""

        response = self.fhir.search("Coverage": {"patient": f"Patient/{self.patient.patient_key}"})

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

            # First get a FHIR API Token
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

    def compute_results(self):
        result = ProtocolResult()
        if self.has_group_number_in_coverage(
            group_number='123456789',
            transactor_name="United Health Care",
            transactor_type="commercial"):

            result.due_in = -1
            result.status = STATUS_DUE
            result.recommendations.append(
                BannerAlertIntervention(
                    narrative="UHC doesn't cover 99402 for patient's telehealth visits. Please use code G0447 instead",
                    placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value],
                    intent=AlertIntent.ALERT_INTENT_WARNING.value,
                )
            )
        return result

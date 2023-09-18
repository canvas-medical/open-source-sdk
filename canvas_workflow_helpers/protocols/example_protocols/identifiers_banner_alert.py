from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
)
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention


class ExternalIdentifierBanner(ClinicalQualityMeasure):
    class Meta:
        title = 'External Identifier Banner'
        description = 'Display any external identifiers in a banner'
        version = '2022-05-10v8'
        types = ['Banner']
        compute_on_change_types = [CHANGE_TYPE.PATIENT]

    def compute_results(self):
        result = ProtocolResult()

        external_identifiers = self.patient.patient["externalIdentifiers"]
        if len(external_identifiers):
            result.status = STATUS_DUE
            result.due_in = -1
            for external_identifier in external_identifiers:
                result.recommendations.append(
                    BannerAlertIntervention(
                        narrative=(f"{external_identifier['system']}: {external_identifier['value']}"),
                        placement=['profile', 'chart'],
                        intent='info')
                    )
        return result

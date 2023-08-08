# type: ignore
from typing import Dict, Optional

from cached_property import cached_property

from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult
)

class EMOProgramStage1(ClinicalQualityMeasure):

    class Meta:
        title = '[EMO] 1. Pending Review'
        version = '1.0.0'
        description = (
            'Protocol that displays the EMO (Expert Medical Option) program phase 1 for a patient '
            'based on their identifiers')
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.PATIENT]
        notification_only = True

    def find_emo_program_status(self, stage: str) -> bool:
        for identifier in self.patient.patient['externalIdentifiers']:
            if identifier["value"] == stage:
                return True
        return False

    def compute_results(self) -> ProtocolResult:

        result = ProtocolResult()

        if self.find_emo_program_status("EMOstage1"):
            result.status = STATUS_DUE

        return result


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

class ProgramStage3(ClinicalQualityMeasure):

    class Meta:
        title = 'Stage 3. Review Complete'
        version = '1.0.0'
        description = (
            'Protocol that displays the program phase 3 for a patient '
            'based on their identifiers')
        types = ['']
        compute_on_change_types = [CHANGE_TYPE.PATIENT]
        notification_only = True

    def find_program_status(self, stage: str) -> bool:
        for identifier in self.patient.patient['externalIdentifiers']:
            if identifier["value"] == stage:
                return True
        return False

    def compute_results(self) -> ProtocolResult:

        result = ProtocolResult()

        if self.find_program_status("stage3"):
            result.status = STATUS_DUE

        return result


import arrow
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import PrescribeRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.value_set.v2020 import Diabetes
from canvas_workflow_kit.internal.integration_messages import (
    create_task_payload,
)


class Citalopram(ValueSet):
    FDB = {'176094'}

class Depression(ValueSet):
    VALUE_SET_NAME = "Postpartum depression"
    ICD10CM = {'F530'}

EncounterForDepressionCondition = {
    "code": "F530",
    "system": "ICD-10",
    "display": "Postpartum depression",
}

class PostpartumDepressionPrescribeRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Postpartum Depression: Prescribe Recommendations'
        version = '2023-v1'
        description = 'Recommend Prescription for postpartum depression'
        types = []
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.MEDICATION, CHANGE_TYPE.INTERVIEW]
        notification_only = True # add this so your protocol doesn't try to recompute on upload

    condition_date = None
    prescribed_recommended_meds = False
    prescibed_other_meds = False
    CARE_COORDINATION_GROUP_ID = "4dfcb0f8-3594-4195-8870-32464756ae47"
    CANVAS_BOT_KEY = "5eede137ecfe4124b8b773040e33be14"

    def in_denominator(self):
        """ Find patient with an active diagnosis for depression"""
        conditions = self.patient.conditions.find(Depression).filter(clinicalStatus='active')

        if len(conditions):
            most_recent = max(conditions, key=lambda x: x['created'])
            self.condition_date = arrow.get(most_recent['created'])

            # create a task on the creation of the diagnosis
            if most_recent['id'] == self.field_changes['canvas_id'] and self.field_changes['created']:
                task_payload = create_task_payload(
                    patient_key=self.patient.patient['key'],
                    created_by_key=self.CANVAS_BOT_KEY,
                    status='OPEN',
                    title=f"Contact patient to schedule follow up appointment",
                    team_identifier=self.CARE_COORDINATION_GROUP_ID,
                    due=arrow.now().isoformat(),
                    created=arrow.now().shift(days=1).isoformat(),
                    tag=None,
                    labels=['Routine'],
                )
                self.set_updates([task_payload])

            return True

        return False

    def in_numerator(self):
        """Find Patients that already are on Citalopram"""
        return len(self.patient.prescriptions.find(Citalopram).filter(status='active'))


    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        if self.in_denominator():
            if self.in_numerator():
                result.status = STATUS_SATISFIED
                result.add_narrative("Patient with postpartum depression is already on Citalopram")

            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative(f'{self.patient.first_name} has been diagnosed with Postpartum Depression, consider prescribing the following:')

                prescribe_recommendation = PrescribeRecommendation(
                        key='RECOMMEND_CITALOPRAM_PRESCRIPTION',
                        rank=2,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=Citalopram,
                        title='Prescribe Citalopram',
                        context={
                            'conditions': [[EncounterForDepressionCondition]],
                            'sig_original_input': 'Take once a day with or without food',
                            'duration_in_days': 30,
                            'dispense_quantity': 30,
                            'dosage_form': 'tablet',
                            'count_of_refills_allowed': 1,
                            'generic_substitutions_allowed': True,
                    }
                )
                result.add_recommendation(prescribe_recommendation)
        else:
            result.add_narrative("Patient does not have an active postpartum depression condition")

        return result

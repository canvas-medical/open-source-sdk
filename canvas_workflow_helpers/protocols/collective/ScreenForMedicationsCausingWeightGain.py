
from canvas_workflow_kit.protocol import (
    CHANGE_TYPE,
    STATUS_DUE,
    STATUS_NOT_APPLICABLE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.value_set import ValueSet


class WeightLossProgramStatusQuestionnaire(ValueSet):
    """Questionnaire for Weight Loss Program Status"""

    VALUE_SET_NAME = 'Weight Loss Program Status Questionnaire'
    INTERNAL = {'i2'}


class Thiazolidinediones(ValueSet):
    VALUE_SET_NAME = 'Thiazolidinediones'
    RXNORM = {
        '1368403',  # 	alogliptin 12.5 MG / pioglitazone 15 MG
        '1368409',  # 	alogliptin 12.5 MG / pioglitazone 15 MG
        '1368410',  # 	alogliptin 12.5 MG / pioglitazone 30 MG
        '1368416',  # 	alogliptin 12.5 MG / pioglitazone 30 MG
        '1368417',  # 	alogliptin 12.5 MG / pioglitazone 45 MG
        '1368423',  # 	alogliptin 12.5 MG / pioglitazone 45 MG
        '1368424',  # 	alogliptin 25 MG / pioglitazone 15 MG
        '1368430',  # 	alogliptin 25 MG / pioglitazone 15 MG
        '1368431',  # 	alogliptin 25 MG / pioglitazone 30 MG
        '1368437',  # 	alogliptin 25 MG / pioglitazone 30 MG
        '1368438',  # 	alogliptin 25 MG / pioglitazone 45 MG
        '1368444',  # 	alogliptin 25 MG / pioglitazone 45 MG
        '261266',  # 	pioglitazone 15 MG
        '261267',  # 	pioglitazone 30 MG
        '261268',  # 	pioglitazone 45 MG
        '312440',  # 	pioglitazone 30 MG
        '312441',  # 	pioglitazone 45 MG
        '317573',  # 	pioglitazone 15 MG
        '647237',  # 	glimepiride 2 MG / pioglitazone 30 MG
        '647239',  # 	glimepiride 4 MG / pioglitazone 30 MG
        '731457',  # 	glimepiride 4 MG / pioglitazone 30 MG
        '731463',  # 	glimepiride 2 MG / pioglitazone 30 MG
        '861783',  # 	metformin hydrochloride 500 MG / pioglitazone 15 MG
        '861785',  # 	metformin hydrochloride 500 MG / pioglitazone 15 MG
        '861822',  # 	metformin hydrochloride 850 MG / pioglitazone 15 MG
        '861824',  # 	metformin hydrochloride 850 MG / pioglitazone 15 MG
        '899989',  # 	24 HR metformin hydrochloride 1000 MG / pioglitazone
        '899993',  # 	24 HR metformin hydrochloride 1000 MG / pioglitazone
        '261241',  # 	rosiglitazone 2 MG
        '261242',  # 	rosiglitazone 4 MG
        '312859',  # 	rosiglitazone 2 MG
        '312860',  # 	rosiglitazone 4 MG
        '861760',  # 	metformin hydrochloride 1000 MG / rosiglitazone 2 MG
        '861762',  # 	metformin hydrochloride 1000 MG / rosiglitazone 2 MG
        '861763',  # 	metformin hydrochloride 1000 MG / rosiglitazone 4 MG
        '861806',  # 	metformin hydrochloride 500 MG / rosiglitazone 2 MG
        '861808',  # 	metformin hydrochloride 500 MG / rosiglitazone 2 MG
        '861816',  # 	metformin hydrochloride 500 MG / rosiglitazone 4 MG
    }


class Sulfonylureas(ValueSet):
    VALUE_SET_NAME = 'Sulfonylureas'
    RXNORM = {
        '861747',  # 	glyburide 1.25 MG / metformin hydrochloride 250 MG
        '197737',  # 	glyburide 1.25 MG
        '314000',  # 	glyburide 1.5 MG
        '881407',  # 	glyburide 1.5 MG
        '861748',  # 	glyburide 2.5 MG / metformin hydrochloride 500 MG
        '310534',  # 	glyburide 2.5 MG
        '310536',  # 	glyburide 3 MG
        '881409',  # 	glyburide 3 MG
        '861753',  # 	glyburide 5 MG / metformin hydrochloride 500 MG
        '310537',  # 	glyburide 5 MG
        '310539',  # 	glyburide 6 MG
        '881411',  # 	glyburide 6 MG
        '199245',  # 	glimepiride 1 MG
        '153843',  # 	glimepiride 1 MG
        '647237',  # 	glimepiride 2 MG / pioglitazone 30 MG
        '731463',  # 	glimepiride 2 MG / pioglitazone 30 MG
        '199246',  # 	glimepiride 2 MG
        '153591',  # 	glimepiride 2 MG
        '153842',  # 	glimepiride 3 MG
        '647239',  # 	glimepiride 4 MG / pioglitazone 30 MG
        '731457',  # 	glimepiride 4 MG / pioglitazone 30 MG
        '199247',  # 	glimepiride 4 MG
        '153845',  # 	glimepiride 4 MG
        '1361493',  # 	glimepiride 6 MG
        '1361495',  # 	glimepiride 8 MG
        '197495',  # 	chlorpropamide 100 MG
        '197496',  # 	chlorpropamide 250 MG
        '315107',  # 	24 HR glipizide 10 MG Extended Release
        '865568',  # 	24 HR glipizide 10 MG Extended Release
        '310489',  # 	24 HR glipizide 2.5 MG Extended Release
        '865571',  # 	24 HR glipizide 2.5 MG Extended Release
        '314006',  # 	24 HR glipizide 5 MG Extended Release
        '865573',  # 	24 HR glipizide 5 MG Extended Release
        '310488',  # 	glipizide 10 MG
        '205830',  # 	glipizide 10 MG
        '861731',  # 	glipizide 2.5 MG / metformin hydrochloride 250 MG
        '861733',  # 	glipizide 2.5 MG / metformin hydrochloride 250 MG
        '861736',  # 	glipizide 2.5 MG / metformin hydrochloride 500 MG
        '861740',  # 	glipizide 5 MG / metformin hydrochloride 500 MG
        '310490',  # 	glipizide 5 MG
        '205828',  # 	glipizide 5 MG
        '198292',  # 	tolazamide 250 MG
        '198293',  # 	tolazamide 500 MG
    }


class WeightGainMedicationReview(ClinicalQualityMeasure):
    class Meta:
        title = 'Check for sulfonylureas or thiazolidinediones'
        description = (
            'This protocol recommends reviewing the medications '
            'of patients who are on thiazolidinediones or sulfonylureas, '
            'as these can cause weight gain. Consideration should '
            'be given to switching to alternative medications.'
        )
        version = '1.0.6'
        information = 'https://canvasmedical.com/gallery'
        identifiers = []
        types = []
        compute_on_change_types = [
            CHANGE_TYPE.MEDICATION,
            CHANGE_TYPE.INTERVIEW,
        ]
        references = []

    def on_thiazolidinediones(self) -> bool:
        return bool(
            self.patient.medications.find(Thiazolidinediones).filter(
                status='active'
            )
        )

    def on_sulfonylureas(self) -> bool:
        return bool(
            self.patient.medications.find(Sulfonylureas).filter(status='active')
        )

    def in_treatment(self) -> bool:
        """
        Return the most recent status if any based on the
        questionnaire "Program status".

        Possible values:
            "a211": "Intake",
            "a212": "Condition screening",
            "a213": "Treatment",
            "a214": "Disqualified",
        """

        status_interviews = self.patient.interviews.find(
            WeightLossProgramStatusQuestionnaire
        ).filter(status='AC')

        if not status_interviews:
            return False

        most_recent = max(status_interviews, key=lambda x: x['created'])
        return most_recent['responses'][0]['code'] == 'a213'

    def in_denominator(self) -> bool:
        return self.in_treatment() and (
            self.on_thiazolidinediones() or self.on_sulfonylureas()
        )

    def in_numerator(self) -> bool:
        """No one is excluded."""
        False

    def remainder_tasks(self, result: ProtocolResult):
        result.add_narrative(
            (
                f'{self.patient.first_name}\'s med list contains a '
                'thiazolidinedione or sulfonylurea, '
                'which can cause weight gain. '
                'Consider switching to alternatives.'
            )
        )
        result.status = STATUS_DUE

    def numerator_tasks(self, result: ProtocolResult):
        result.add_narrative(
            'Medications have been reviewed and alternatives considered.'
        )
        result.status = STATUS_SATISFIED

    def excluded_tasks(self, result: ProtocolResult):
        result.add_narrative('Protocol not applicable.')
        result.status = STATUS_NOT_APPLICABLE

    def compute_results(self) -> ProtocolResult:
        result = ProtocolResult()
        if self.in_denominator():
            if self.in_numerator():
                self.numerator_tasks(result)
            else:
                self.remainder_tasks(result)
        else:
            self.excluded_tasks(result)
        return result

import arrow
import json
from canvas_workflow_kit.constants import CHANGE_TYPE, AlertPlacement, AlertIntent
from canvas_workflow_kit.intervention import BannerAlertIntervention
from canvas_workflow_kit.protocol import (STATUS_NOT_APPLICABLE, STATUS_DUE, STATUS_SATISFIED, ClinicalQualityMeasure, ProtocolResult)
from canvas_workflow_kit.recommendation import InterviewRecommendation, PrescribeRecommendation, DiagnoseRecommendation
from canvas_workflow_kit.timeframe import Timeframe
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.fhir import FumageHelper
from canvas_workflow_kit.utils import send_notification

class Sumatriptan(ValueSet):
    FDB = {'177730'}
    VALUE_SET_NAME = 'Sumitriptan 100mg'
    FIELDS = {
        'sig_original_input': 'Take as needed to relieve migraine symptoms. If needed, another dose may be taken 2 hours after the first dose',
        'duration_in_days': 30,
        'dispense_quantity': 30,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Rizatriptan(ValueSet):
    FDB = {'185452'}
    VALUE_SET_NAME = 'Rizatriptan 10mg'
    FIELDS = {
        'sig_original_input': 'Take as needed to relieve migraine symptoms. If needed, another dose may be taken 2 hours after the first dose. Do not exceed 30mg in 24 hrs',
        'duration_in_days': 30,
        'dispense_quantity': 30,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Zolmitriptan(ValueSet):
    FDB = {'207488'}
    VALUE_SET_NAME = 'Zolmitriptan 5mg'
    FIELDS = {
        'sig_original_input': 'Take half a tablet to relieve migraine symptoms. Another dose may be taken 2 hours after the first dose. Do not exceed 10mg in 24 hrs',
        'duration_in_days': 30,
        'dispense_quantity': 30,
        'dosage_form': 'Tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Topiramate(ValueSet):
    FDB = {'197564'}
    VALUE_SET_NAME = 'Topiramate 25mg '
    FIELDS = {
        'sig_original_input': 'Take once per day',
        'duration_in_days': 30,
        'dispense_quantity': 30,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Propranolol(ValueSet):
    FDB = {'221898'}
    VALUE_SET_NAME = 'Propranolol 40mg'
    FIELDS = {
        'sig_original_input': 'Take twice daily',
        'duration_in_days': 30,
        'dispense_quantity': 30,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Ondansetron(ValueSet):
    FDB = {'183591'}
    VALUE_SET_NAME = 'Ondansetron 4mg'
    FIELDS = {
        'sig_original_input': 'Take orally at first sign of nausea, then again 4 and 8 hours after initial dose',
        'duration_in_days': 30,
        'dispense_quantity': 120,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class OndansetronODT(ValueSet):
    FDB = {'285288'}
    VALUE_SET_NAME = 'Ondansetron ODT 4mg'
    FIELDS = {
        'sig_original_input': 'Take orally at first sign of nausea, then again 4 and 8 hours after initial dose',
        'duration_in_days': 30,
        'dispense_quantity': 120,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }
class Metoclopramide(ValueSet):
    FDB = {'295749'}
    VALUE_SET_NAME = 'Metoclopramide 10mg'
    FIELDS = {
        'sig_original_input': 'Take 30 minutes before each meal and at bedtime',
        'duration_in_days': 30,
        'dispense_quantity': 120,
        'dosage_form': 'tablet',
        'count_of_refills_allowed': 1,
        'generic_substitutions_allowed': True,
    }

PRESCRIPTION_MEDS = [Sumatriptan, Rizatriptan, Zolmitriptan, Topiramate, Propranolol, Ondansetron, OndansetronODT, Metoclopramide]

class MigraineCondition(ValueSet):
    VALUE_SET_NAME = "Migraine, unspecified, not intractable, without status migrainosus"
    ICD10CM = {'G43909'}

class PrescriptionRecommendationQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Prescription Recommendations'
    INTERNAL = {'medrec123'}

class PatientEducationQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Patient Education'
    INTERNAL = {'medication_education'}
    FHIR_ID = '2cd73b10-4343-4689-875f-c033349e6dd5'

class MedicationAcceptanceQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Medication Acceptance'
    INTERNAL = {'medcon123'}
    FHIR_ID = '12f68f8a-ed40-4482-a010-8207df8a5e5c'

class MigraineIntakeQuestionnaire(ValueSet):
    VALUE_SET_NAME = 'Migraine Intake'
    INTERNAL = {'migint-123'}
    FHIR_ID = '9e984119-558e-415e-a19a-44205dcdaa1b'

PROVIDER_ROLE = {
    "system": "http://snomed.info/sct",
    "code": "010101",
    "display": "Cove Provider"
}

class MigraineWorkflowRecommendations(ClinicalQualityMeasure):
    class Meta:
        title = 'Cove Recommendations'
        version = '2023-v1'
        description = 'This protocol will go through the different stages of the Cove Business Line Workflow'
        types = [""]
        compute_on_change_types = [CHANGE_TYPE.CONDITION, CHANGE_TYPE.PRESCRIPTION, CHANGE_TYPE.INTERVIEW, CHANGE_TYPE.MEDICATION]
        notification_only = False # add this so your protocol doesn't try to recompute on upload

    def chosen_meds_prescibed(self):
        for drug in self.chosen_meds:
            records = self.patient.prescriptions.find(drug).filter(status='active').records
            if not records:
                return False
            else:
                medication = self.patient.medications.filter(id=records[0]['medicationId']).records[0]
                self.drug_dates.append(f"{drug.VALUE_SET_NAME} on {medication['periods'][0]['from']}")

        return len(self.chosen_meds)

    def patient_approval_submitted(self):
        interviews = self.patient.interviews.find(MedicationAcceptanceQuestionnaire)

        self.patient_approval = None
        approval_id = None
        answers = []
        if len(interviews):

            date = arrow.get(interviews.last()['noteTimestamp'])

            # find the record in FHIR
            response = self.fhir.search("QuestionnaireResponse", {
                "patient": f"Patient/{self.patient.patient_key}",
                "questionnaire": f"Questionnaire/{MedicationAcceptanceQuestionnaire.FHIR_ID}",
                "authored": f"eq{date.format('YYYY-MM-DD')}"
            })

            if response.status_code != 200:
                raise Exception(f"FHIR Questionnaire Responses could not be fetched: {response.text} and fumage_correlation_id: {response.headers['fumage-correlation-id']}")

            for entry in response.json().get('entry', []):
                if arrow.get(entry['resource']['authored']) == date:
                    approval_id = entry['resource']['id']
                    for item in entry['resource']['item']:
                        if 'answer' in item:
                            coding_display = item['answer'][0]['valueCoding']['display'] if 'valueCoding' in item['answer'][0] else item['answer'][0]['valueString']
                            code = item['answer'][0]['valueCoding']['code'] if 'valueCoding' in item['answer'][0] else None
                            answers.append(f"Q: {item['text']} \n A: {coding_display}")
                            if code == 'medcon125': # yes
                                self.patient_approval = True 
                            elif code == 'medcon126': # no
                                self.patient_approval = False

        return self.patient_approval, approval_id, answers

    def patient_education_submitted(self):
        interview = self.patient.interviews.find(PatientEducationQuestionnaire).last()

        if interview: 
            for response in interview['responses']:
                for drug in PRESCRIPTION_MEDS:
                    print(drug.FDB, response['code'], drug.FDB == response['code'])
                    if response['code'] in drug.FDB:
                        self.chosen_meds.append(drug)

        return len(self.chosen_meds)

    def build_prescription_recs(self, result, ls):
        for drug in ls:
            if not self.patient.prescriptions.find(drug).filter(status='active').records:
                prescribe_recommendation = PrescribeRecommendation(
                        key=f'RECOMMEND_{drug.VALUE_SET_NAME}_PRESCRIPTION',
                        rank=1,
                        button='Prescribe',
                        patient=self.patient,
                        prescription=drug,
                        title=f'Prescribe {drug.VALUE_SET_NAME}',
                        context={
                            'conditions': [self.conditions],
                            **drug.FIELDS
                    }
                )
                result.add_recommendation(prescribe_recommendation)
        return result

    def build_interview_rec(self, result, questionnaire):
        interview_recommendation = InterviewRecommendation(
            key=f'RECOMMEND_{questionnaire.VALUE_SET_NAME}_QUES',
            rank=1,
            button='Interview',
            patient=self.patient,
            questionnaires=[questionnaire],
            title=f'Please fill out {questionnaire.VALUE_SET_NAME} questionnaire'
        )
        result.add_recommendation(interview_recommendation)
        return result

    def prescribed_rec_interview_submitted(self, interview):
        for response in interview['responses']:
            for drug in PRESCRIPTION_MEDS:
                print(drug.FDB, response['code'], drug.FDB == response['code'])
                if response['code'] in drug.FDB:
                    self.prescribed_rec.append(drug)

        return len(self.prescribed_rec)


    def has_diagnosis(self):
        for condition in self.patient.conditions.filter(clinicalStatus="active"):
            for coding in condition.get('coding', []):
                if coding['code'].startswith("G43"):
                    self.conditions.append(coding)
                    break

        return len(self.conditions)

    def add_banner_alert(self, result, narrative): 
        result.recommendations.append(
            BannerAlertIntervention(
                narrative=narrative,
                placement=[AlertPlacement.ALERT_PLACEMENT_CHART.value, AlertPlacement.ALERT_PLACEMENT_PROFILE.value],
                intent=AlertIntent.ALERT_INTENT_INFO.value,
            )
        )
        return result
    
    def patient_education_interview_id(self):
        """ Patient has submitted the Migraine Intake Questionnaire """
        interviews = self.patient.interviews.find(PatientEducationQuestionnaire)
        if len(interviews):

            date = arrow.get(interviews.last()['noteTimestamp'])

            # find the record in FHIR
            response = self.fhir.search("QuestionnaireResponse", {
                "patient": f"Patient/{self.patient.patient_key}",
                "questionnaire": f"Questionnaire/{PatientEducationQuestionnaire.FHIR_ID}",
                "authored": f"eq{date.format('YYYY-MM-DD')}"
            })

            if response.status_code != 200:
                raise Exception(f"FHIR Questionnaire Responses could not be fetched: {response.text} and fumage_correlation_id: {response.headers['fumage-correlation-id']}")

            for entry in response.json().get('entry', []):
                if arrow.get(entry['resource']['authored']) == date:
                    return entry['resource']['id']

        return None

    def intake_submitted(self):
        """ Patient has submitted the Migraine Intake Questionnaire """
        interviews = self.patient.interviews.find(MigraineIntakeQuestionnaire)
        if len(interviews):

            date = arrow.get(interviews.last()['noteTimestamp'])

            # find the record in FHIR
            response = self.fhir.search("QuestionnaireResponse", {
                "patient": f"Patient/{self.patient.patient_key}",
                "questionnaire": f"Questionnaire/{MigraineIntakeQuestionnaire.FHIR_ID}",
                "authored": f"eq{date.format('YYYY-MM-DD')}"
            })

            if response.status_code != 200:
                raise Exception(f"FHIR Questionnaire Responses could not be fetched: {response.text} and fumage_correlation_id: {response.headers['fumage-correlation-id']}")

            for entry in response.json().get('entry', []):
                if arrow.get(entry['resource']['authored']) == date:
                    self.intake_interview = entry['resource']
                    return True

        return False

    def update_care_team(self, staff, role):
        read_response = self.fhir.read("CareTeam", self.patient.patient_key)

        if read_response.status_code != 200:
            raise Exception(f"FHIR Care Team could not be fetched: {read_response.text} and fumage_correlation_id: {read_response.headers['fumage-correlation-id']}")

        payload = read_response.json()

        # Create new participant payload 
        # remove any items where the role or member could be duplicated
        new_participants = []
        for obj in payload.get('participant', []):
            role_match = obj['role'][0]['coding'][0] == role
            member_match = obj['member']['reference'] == staff['reference']

            if not role_match and not member_match:
                new_participants.append(obj)
                continue

        new_participants.append({
            "role": [{"coding": [role]}],
            "member": staff
        })
        payload['participant'] = new_participants

        update_response = self.fhir.update("CareTeam", self.patient.patient_key, payload)

        if update_response.status_code != 200:
            raise Exception(f"FHIR Care Team could not be updated: {update_response.text} with {payload} and fumage_correlation_id: {update_response.headers['fumage-correlation-id']}")

    def create_fhir_task(self, title, staff, label, note_text, due):
        payload = {
            "resourceType": "Task",
            "status": "requested",
            "intent": "unknown",
            "description": title,
            "for": {
                "reference": f"Patient/{self.patient.patient_key}"
            },
            "authoredOn": self.now,
            "requester": {
                "reference": f"Practitioner/{self.settings['CANVAS_BOT']}"
            },
            "owner": staff,
            "note": [
                {
                    "authorReference": {
                        "reference": f"Practitioner/{self.settings['CANVAS_BOT']}"
                    },
                    "time": self.now,
                    "text": note_text
                }
            ],
            "input": [
              {
                "type": {
                    "text": "label"
                },
                "valueString": label
              }
            ],
            "restriction": {
                "period": {
                    "end": due
                }
            }
        }
        response = self.fhir.create("Task", payload)

        if response.status_code != 201:
            raise Exception(f"FHIR Task Create failed: {response.text} with {payload}")

    def questionnaire_matches(self, questionnaire, value_set):
        if not questionnaire:
            return False

        return questionnaire['questionnaires'][0]['code'] in value_set.INTERNAL

    def check_if_last_prescription_committed(self, result):
        # lets check the record triggering this was the final drug needed
        if self.field_changes.get('model_name') == 'prescription' and self.field_changes.get('created'):
            read_response = self.fhir.read("MedicationRequest", self.field_changes['external_id'])

            if read_response.status_code != 200:
                raise Exception(f"Failed to fetch FHIR MedicationRequest/{self.field_changes['external_id']} with {read_response.text} and fumage_correlation_id {read_response.headers['fumage-correlation-id']}")

            record = read_response.json()

            if record['status'] == 'active' and record['intent'] == 'order':
                coding = [c['code'] for c in record['medicationCodeableConcept']['coding'] if c['system'] == 'http://www.fdbhealth.com/']
                
                if coding and coding[0] in [list(drug.FDB)[0] for drug in self.chosen_meds]:
                    # create Task
                    if not self.patient.tasks.filter(status='OPEN', title='New treatment follow up in one month').records:
                        self.create_fhir_task(
                            title='New treatment follow up in one month', 
                            staff=self.care_team_staff_member, 
                            label='Cove', 
                            note_text=f"{self.patient.first_name} was started on these medications: <br>" + '\n'.join(self.drug_dates), 
                            due=self.now)

                    send_notification(
                        "https://webhook.site/8f236112-e28c-41df-9c76-0888de0535a1", 
                        json.dumps({
                            'patient_identifier': ",".join(self.identifiers) if self.identifiers else self.patient.patient_key,
                            'chosen medications': [drug.VALUE_SET_NAME for drug in self.chosen_meds],
                            'narrative': 'Prescriptions sent to pharmacy.  Please reach out if you have additional quesitons'
                        }), 
                        {'Content-Type': 'application/json'})
                    result.add_narrative("Notification sent")
        return result

    def compute_results(self):
        result = ProtocolResult()
        result.status = STATUS_NOT_APPLICABLE

        self.fhir = FumageHelper(self.settings)
        self.now = arrow.now().isoformat()

        self.intake_interview = None
        self.conditions = []
        self.prescribed_rec = []
        self.chosen_meds = []
        self.patient_approval = None
        self.drug_dates = []

        has_diagnosis = self.has_diagnosis()
        patient_education_submitted = self.patient_education_submitted()
        patient_approval_submitted, approval_id, approval_answers = self.patient_approval_submitted()
        self.identifiers = [i['value'] for i in self.patient.patient['externalIdentifiers'] if i['system'] == "ThirtyMadison"]
        care_team_member = [c['staff']['key'] for c in self.patient.patient['careTeamMemberships'] if c['role']['code'] == PROVIDER_ROLE['code']]
        self.care_team_staff_member = ({
            "reference": f"Practitioner/{care_team_member[0]}",
            "type": "Practitioner"
        } if care_team_member else None)

        questionnaires = sorted(
            self.patient.interviews.find(PrescriptionRecommendationQuestionnaire | PatientEducationQuestionnaire | MedicationAcceptanceQuestionnaire | MigraineIntakeQuestionnaire),
            key=lambda i: i['created']
        )
        last_filled_questionnaire = questionnaires[-1] if questionnaires else None

        if has_diagnosis and self.chosen_meds_prescibed():
            result.due_in = -1
            result.status = STATUS_DUE
            result = self.add_banner_alert(result, "Cove: Patient Treatment Active")

            result = self.check_if_last_prescription_committed(result)

        elif has_diagnosis and self.questionnaire_matches(last_filled_questionnaire, MedicationAcceptanceQuestionnaire) and patient_approval_submitted is not None:
            result.due_in = -1
            result.status = STATUS_DUE
            result = self.add_banner_alert(result, "Cove: Patient Active")

            if self.patient_approval:
                result = self.build_prescription_recs(result, self.chosen_meds)
                result.add_narrative(f'{self.patient.first_name} has approved the recommended prescriptions. Please send the prescriptions to the pharmacy')
            else:
                result.add_narrative(f'{self.patient.first_name} did not approve the recommended prescriptions. Please review other prescription options')
                result = self.build_interview_rec(result, PrescriptionRecommendationQuestionnaire)

            if (self.field_changes.get('model_name') == 'interview' and 
                self.field_changes.get('created') and
                self.field_changes.get('external_id') == approval_id and
                not self.patient.tasks.filter(status='OPEN', title='Patient Medication Response Received').records):
                
                self.create_fhir_task(
                    title='Patient Medication Response Received', 
                    staff=self.care_team_staff_member, 
                    label='Cove', 
                    note_text="\n\n".join(approval_answers), 
                    due=self.now)

        elif has_diagnosis and self.questionnaire_matches(last_filled_questionnaire, PatientEducationQuestionnaire) and patient_education_submitted:
            result.due_in = -1
            result.status = STATUS_DUE
            result = self.add_banner_alert(result, "Cove: Patient Active")

            if (self.field_changes.get('model_name') == 'interview' and 
                self.field_changes.get('created') and
                self.field_changes.get('external_id') == self.patient_education_interview_id()):
                
                send_notification(
                    "https://webhook.site/8f236112-e28c-41df-9c76-0888de0535a1", 
                    json.dumps({
                        'patient_identifier': ",".join(self.identifiers) if self.identifiers else self.patient.patient_key,
                        'chosen medications': [drug.VALUE_SET_NAME for drug in self.chosen_meds],
                        'narrative': 'Please select the following treatments that you would like to share information with the patient via the Cove app'
                    }), 
                    {'Content-Type': 'application/json'})
                result.add_narrative("Notification sent")

        elif has_diagnosis and self.questionnaire_matches(last_filled_questionnaire, PrescriptionRecommendationQuestionnaire) and self.prescribed_rec_interview_submitted(last_filled_questionnaire):
            result.due_in = -1
            result.status = STATUS_DUE
            result.add_narrative("Insert the prescriptions previously selected to verify allergy and drug interactions. "
                "Complete the Patient Education questionnaire to send information to patient via Cove app for patient approval prior to sending prescription.")

            result = self.add_banner_alert(result, "Cove: Patient Active")
            result = self.build_prescription_recs(result, self.prescribed_rec)
            result = self.build_interview_rec(result, PatientEducationQuestionnaire)

        elif has_diagnosis:
            result.due_in = -1
            result.status = STATUS_DUE
            
            result = self.add_banner_alert(result, "Cove: Patient Active")
            result = self.build_interview_rec(result, PrescriptionRecommendationQuestionnaire)

            condition_names = " and ".join([f"\'{c['display']}\'" for c in self.conditions])
            result.add_narrative(f'{self.patient.first_name} has a diagnosis of {condition_names}. Please review prescription options')
        
        elif self.questionnaire_matches(last_filled_questionnaire, MigraineIntakeQuestionnaire) and self.intake_submitted():
            # Cove Intake completed
            result.due_in = -1
            result.status = STATUS_DUE
            
            result = self.add_banner_alert(result, "Cove: Intake Complete")
            self.update_care_team(self.intake_interview['author'], PROVIDER_ROLE)

            answers = []
            diagnose_rec_needed = False
            for item in self.intake_interview['item']:
                coding = item['answer'][0]['valueCoding']
                answers.append(f"Q: {item['text']} \n A: {coding['display']}")
                if coding['code'] == 'migint-133':
                    diagnose_rec_needed = True

            if (self.field_changes.get('model_name') == 'interview' and 
                self.field_changes.get('created') and
                self.field_changes.get('external_id') == self.intake_interview['id'] and
                not self.patient.tasks.filter(status='OPEN', title='Review New Intake').records):
                
                self.create_fhir_task(
                    title='Review New Intake', 
                    staff=self.intake_interview['author'], 
                    label='Cove', 
                    note_text="\n\n".join(answers), 
                    due=self.now)

            # look at question 1 answer for diagnose recs
            if diagnose_rec_needed:
                diagnose_recommendation = DiagnoseRecommendation(
                    key='RECOMMEND_MIGRAINE_DIAGNOSIS',
                    rank=1,
                    button='Diagnose',
                    patient=self.patient,
                    condition=MigraineCondition,
                    title=MigraineCondition.VALUE_SET_NAME,
                )
                result.add_recommendation(diagnose_recommendation)
                result.add_narrative(f"{self.patient.first_name} has been diagnosed in the past by another provider. "
                    "Patient meets Cove requirements for current migraine diagnosis.")
        else:
            result.add_narrative("Cove Intake has not been completed")


        return result

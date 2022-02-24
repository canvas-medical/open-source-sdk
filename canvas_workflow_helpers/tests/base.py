import json
import os

from unittest import TestCase

from pathlib import Path

from canvas_workflow_kit.patient import Patient
from canvas_workflow_kit.protocol import ProtocolResult
from canvas_workflow_kit.utils import load_local_patient


class WorkflowHelpersBaseTest(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            currentDir = Path(__file__).parent.resolve()
            self.mocks_path = f'{currentDir}/mock_data/'
        except:
            self.mocks_path = '.'

    def load_patient(self, patient_key) -> Patient:
        patient_path = Path(f'{self.mocks_path}/{patient_key}/')

        assert patient_path.is_dir(
        ), f'no patient directory exists from {patient_path}'

        patient = load_local_patient(patient_path)
        patient.patient['key'] = patient_key
        return patient

    def load_patient_data(self, patient_key, field):
        """
        Load data from mock data JSON files dumped by the dump_patient command.
        """
        filename = f'{self.mocks_path}/{patient_key}/{field}.json'

        if not os.path.exists(filename):
            if field == 'patient':
                raise Exception(
                    f'Missing mock patient data for {patient_key}!')

            return []

        with open(filename, 'r') as fh:
            return json.load(fh)

    def assertIsNotApplicable(self, result: ProtocolResult):
        self.assertEqual('not_applicable', result.status)
        self.assertEqual('', result.narrative)
        self.assertEqual([], result.recommendations)
        self.assertIsNone(result.due_in)

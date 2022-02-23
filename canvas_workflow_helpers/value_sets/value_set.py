from collections import defaultdict
from typing import Dict


class SuperValueSet(object):
    """
    SuperValueSet allows multiple value-sets to be logically combined
    with |.  So if you need to check if someone has condition A or
    condition B you can:

       patient.has_condition(ConditionA | ConditionB)

    More than two works:

       patient.has_condition(ConditionA | ConditionB | ConditionC)

    """

    def __init__(self, value_sets):
        self.value_sets = value_sets

    @property
    def values(self):
        values: Dict[str, set] = defaultdict(set)

        for value_set in self.value_sets:
            sub_values = value_set.values

            for key in sub_values:
                values[key] |= sub_values[key]

        return values

    @property
    def name(self):
        return ' or '.join([cls.name for cls in self.value_sets])

    def __or__(value_set, other_value_set):
        return SuperValueSet([value_set, other_value_set])


class ValueSystems(type):

    @property
    def values(cls):
        return {
            system.lower(): getattr(cls, system)
            for system in cls.value_systems if hasattr(cls, system)
        }

    @property
    def name(cls):
        return cls.VALUE_SET_NAME

    def __or__(value_set, other_value_set):
        return SuperValueSet([value_set, other_value_set])


class ValueSet(object, metaclass=ValueSystems):

    value_systems = [
        'CANVAS',
        'CPT',
        'CVX',
        'HCPCS',
        'ICD10CM',
        'ICD10PCS',
        'ICD9CM',
        'LOINC',
        'RXNORM',
        'SNOMEDCT',
        'FDB',
        'INTERNAL',
    ]

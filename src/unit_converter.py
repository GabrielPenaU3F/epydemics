from abc import ABC, abstractmethod

import numpy as np

import src.utils.unit_conversion_utils as uc


class UnitConverter(ABC):

    instance = None
    supported_units = {}

    def __init__(self):
        self.config_supported_units()

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def config_supported_units(self):
        pass


class DaysConverter(UnitConverter):

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = DaysConverter()
        return cls.instance

    def config_supported_units(self):
        self.supported_units = {
            'sec': uc.days_to_seconds,
            'min': uc.days_to_minutes
        }

    def convert_days_to(self, unit_id, days):
        return self.supported_units.get(unit_id)(np.array(days))

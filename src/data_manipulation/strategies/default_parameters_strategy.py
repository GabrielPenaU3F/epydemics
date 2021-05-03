from abc import ABC, abstractmethod


class DefaultParametersStrategy(ABC):

    default_dataset = None

    def get_default_dataset(self):
        return self.default_dataset


class OWIDDefaultParametersStrategy(DefaultParametersStrategy):

    def __init__(self):
        self.default_dataset = 'total_cases'



class MapacheArgDefaultParametersStrategy(DefaultParametersStrategy):

    def __init__(self):
        self.default_dataset = 'provincia_residencia'

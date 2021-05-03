from abc import ABC, abstractmethod


class ColumnChoosingStrategy(ABC):

    default_dataset = None
    location_column_name = None
    date_column_name = None

    def get_default_dataset(self):
        return self.default_dataset

    def get_location_column_name(self):
        return self.location_column_name

    def get_date_column_name(self):
        return self.date_column_name


class OWIDColumnChoosingStrategy(ColumnChoosingStrategy):

    def __init__(self):
        self.default_dataset = 'total_cases'
        self.location_column_name = 'location'
        self.date_column_name = 'date'


class MapacheArgColumnChoosingStrategy(ColumnChoosingStrategy):

    def __init__(self):
        self.default_dataset = 'numero_de_caso'
        self.location_column_name = 'provincia_residencia'
        self.date_column_name = 'fecha_apertura'

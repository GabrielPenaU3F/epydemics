from src.data_manipulation.strategies.data_filter_strategy import *
from src.data_manipulation.strategies.column_choosing_strategy import *


class DataSource(ABC):

    source_url = None
    supported_datasets = None
    data_filter_strategy = None
    column_choosing_strategy = None

    def get_url(self):
        return self.source_url

    def get_supported_datasets(self):
        return self.supported_datasets

    def get_filter_strategy(self):
        return self.data_filter_strategy

    def get_column_choosing_strategy(self):
        return self.column_choosing_strategy


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.supported_datasets = ['total_cases', 'total_deaths']
        self.data_filter_strategy = OWIDFilterStrategy()
        self.column_choosing_strategy = OWIDColumnChoosingStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://github.com/SistemasMapache/Covid19arData/raw/master/datosAbiertosOficiales/covid19casos.csv'
        self.supported_datasets = ['numero_de_caso']
        self.data_filter_strategy = MapacheArgFilterStrategy()
        self.column_choosing_strategy = MapacheArgColumnChoosingStrategy()

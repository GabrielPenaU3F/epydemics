from src.data_manipulation.strategies.data_filter_strategy import *
from src.data_manipulation.strategies.default_parameters_strategy import *


class DataSource(ABC):

    source_url = ''
    data_filter_strategy = None
    default_parameters_strategy = None

    def get_url(self):
        return self.source_url

    def get_filter_strategy(self):
        return self.data_filter_strategy

    def get_default_parameters_strategy(self):
        return self.default_parameters_strategy


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.data_filter_strategy = OWIDFilterStrategy()
        self.default_parameters_strategy = OWIDDefaultParametersStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://github.com/SistemasMapache/Covid19arData/raw/master/datosAbiertosOficiales/covid19casos.csv'
        self.data_filter_strategy = MapacheArgFilterStrategy()
        self.default_parameters_strategy = MapacheArgDefaultParametersStrategy()

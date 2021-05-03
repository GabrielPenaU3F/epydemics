from abc import ABC

from src.data_manipulation.data_filter_strategy import *


class DataSource(ABC):

    source_url = ''
    data_filter_strategy = None

    def get_url(self):
        return self.source_url

    def get_filter_strategy(self):
        return self.data_filter_strategy


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.data_filter_strategy = OWIDFilterStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://github.com/SistemasMapache/Covid19arData/raw/master/datosAbiertosOficiales/covid19casos.csv'
        self.data_filter_strategy = MapacheArgFilterStrategy()

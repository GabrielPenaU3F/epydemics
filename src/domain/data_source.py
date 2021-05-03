from src.data_manipulation.strategies.data_filter_strategy import *
from src.data_manipulation.strategies.column_choosing_strategy import *


class DataSource(ABC):

    source_url = None
    supported_datasets = None
    default_dataset = None
    location_column_name = None
    date_column_name = None
    data_filter_strategy = None

    @abstractmethod
    def __init__(self):
        pass

    def get_url(self):
        return self.source_url

    def get_supported_datasets(self):
        return self.supported_datasets

    def get_default_dataset(self):
        return self.default_dataset

    def get_location_column_name(self):
        return self.location_column_name

    def get_date_column_name(self):
        return self.date_column_name

    def get_filter_strategy(self):
        return self.data_filter_strategy


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.supported_datasets = ['total_cases', 'total_deaths']
        self.default_dataset = 'total_cases'
        self.location_column_name = 'location'
        self.date_column_name = 'date'
        self.data_filter_strategy = OWIDFilterStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://github.com/SistemasMapache/Covid19arData/raw/master/datosAbiertosOficiales/covid19casos.csv'
        self.supported_datasets = ['numero_de_caso']
        self.default_dataset = 'numero_de_caso'
        self.location_column_name = 'provincia_residencia'
        self.date_column_name = 'fecha_apertura'
        self.data_filter_strategy = MapacheArgFilterStrategy()

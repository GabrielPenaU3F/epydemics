from src.data_manipulation.strategies.data_filter_strategy import *
from src.data_manipulation.strategies.column_choosing_strategy import *


class DataSource(ABC):

    source_url = None
    dataset_titles = None
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
        return self.dataset_titles.keys()

    def get_default_dataset(self):
        return self.default_dataset

    def get_location_column_name(self):
        return self.location_column_name

    def get_date_column_name(self):
        return self.date_column_name

    def get_filter_strategy(self):
        return self.data_filter_strategy

    def get_dataset_title(self, dataset_id):
        return self.dataset_titles.get(dataset_id)


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.dataset_titles = {'total_cases': 'Total cases',
                              'total_deaths': 'Total deaths'}
        self.default_dataset = 'total_cases'
        self.location_column_name = 'location'
        self.date_column_name = 'date'
        self.data_filter_strategy = OWIDFilterStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
        self.dataset_titles = {'nue_casosconf_diff': 'Total cases'}
        self.default_dataset = 'nue_casosconf_diff'
        self.location_column_name = 'osm_admin_level_4'
        self.date_column_name = 'fecha'
        self.data_filter_strategy = MapacheArgFilterStrategy()

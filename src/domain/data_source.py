from src.data_manipulation.strategies.data_management_strategy import *
from src.data_manipulation.strategies.column_choosing_strategy import *


class DataSource(ABC):

    source_url = None
    dataset_titles = None
    dataset_plot_ylabels = None
    default_dataset = None
    location_column_name = None
    date_column_name = None
    data_management_strategy = None

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

    def get_data_management_strategy(self):
        return self.data_management_strategy

    def get_dataset_title(self, dataset_id):
        return self.dataset_titles.get(dataset_id)

    def get_fit_plot_ylabel(self, dataset_id):
        return self.dataset_plot_ylabels.get(dataset_id)


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.dataset_titles = {'total_cases': 'Total cases',
                              'total_deaths': 'Total deaths'}
        self.dataset_plot_ylabels = {'total_cases': 'Cumulative cases',
                                     'total_deaths': 'Cumulative deaths'}
        self.default_dataset = 'total_cases'
        self.location_column_name = 'location'
        self.date_column_name = 'date'
        self.data_management_strategy = OWIDManagementStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
        self.dataset_titles = {'nue_casosconf_diff': 'Total cases'}
        self.dataset_plot_ylabels = {'nue_casosconf_diff': 'Cumulative cases'}
        self.default_dataset = 'nue_casosconf_diff'
        self.location_column_name = 'osm_admin_level_4'
        self.date_column_name = 'fecha'
        self.data_management_strategy = MapacheArgManagementStrategy()

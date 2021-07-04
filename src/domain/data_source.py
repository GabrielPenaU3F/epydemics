from abc import ABC, abstractmethod
from src.data_manipulation.strategies.data_management_strategy import OWIDManagementStrategy, \
    MapacheArgManagementStrategy, CustomManagementStrategy


class DataSource(ABC):

    source_url = None
    dataset_titles = None
    dataset_datacurve_titles = None
    dataset_plot_ylabels = None
    dataset_datacurve_ylabels = None
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

    def get_dataset_datacurve_title(self, dataset_id, data_format):
        key = data_format + '_' + dataset_id
        return self.dataset_datacurve_titles.get(key)

    def get_dataset_datacurve_ylabel(self, dataset_id, data_format):
        key = data_format + '_' + dataset_id
        return self.dataset_datacurve_ylabels.get(key)


class OWIDDataSource(DataSource):

    def __init__(self):
        self.source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        self.dataset_titles = {'total_cases': 'Total cases',
                              'total_deaths': 'Total deaths'}
        self.dataset_plot_ylabels = {'total_cases': 'Cumulative cases',
                                     'total_deaths': 'Cumulative deaths'}
        self.dataset_datacurve_titles = {'cumulative_total_cases': 'Cumulative cases',
                                         'cumulative_total_deaths': 'Cumulative deaths',
                                         'daily_total_cases': 'Incidence data',
                                         'daily_total_deaths': 'Daily deaths'}
        self.dataset_datacurve_ylabels = {'cumulative_total_cases': 'Cumulative cases',
                                         'cumulative_total_deaths': 'Cumulative deaths',
                                         'daily_total_cases': 'Incidence',
                                         'daily_total_deaths': 'Deaths'}
        self.default_dataset = 'total_cases'
        self.location_column_name = 'location'
        self.date_column_name = 'date'
        self.data_management_strategy = OWIDManagementStrategy()


class MapacheArgDataSource(DataSource):

    def __init__(self):
        self.source_url = \
            'https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0'
        self.dataset_titles = {'nue_casosconf_diff': 'Total cases',
                               'nue_fallecidos_diff': 'Total deaths'}

        self.dataset_plot_ylabels = {'nue_casosconf_diff': 'Cumulative cases',
                                     'nue_fallecidos_diff': 'Cumulative deaths'}
        self.dataset_datacurve_titles = {'cumulative_nue_casosconf_diff': 'Cumulative cases',
                                         'cumulative_nue_fallecidos_diff': 'Cumulative deaths',
                                         'daily_nue_casosconf_diff': 'Incidence data',
                                         'daily_nue_fallecidos_diff': 'Daily deaths'}
        self.dataset_datacurve_ylabels = {'cumulative_nue_casosconf_diff': 'Cumulative cases',
                                         'cumulative_nue_fallecidos_diff': 'Cumulative deaths',
                                         'daily_nue_casosconf_diff': 'Incidence',
                                         'daily_nue_fallecidos_diff': 'Deaths'}
        self.default_dataset = 'nue_casosconf_diff'
        self.location_column_name = 'osm_admin_level_4'
        self.date_column_name = 'fecha'
        self.data_management_strategy = MapacheArgManagementStrategy()


class CustomDataSource(DataSource):

    def __init__(self):
        self.source_url = None
        self.dataset_titles = {'custom_data': 'Total cases'}
        self.dataset_datacurve_titles = {'cumulative_custom_data': 'Cumulative cases',
                                         'daily_custom_data': 'Incidence data'}
        self.dataset_datacurve_ylabels = {'cumulative_custom_data': 'Cumulative cases',
                                          'daily_custom_data': 'Incidence'}
        self.dataset_plot_ylabels = {'custom_data': 'Cumulative cases'}
        self.default_dataset = 'custom_data'
        self.location_column_name = 'custom_location'
        self.date_column_name = 'custom_date'
        self.data_management_strategy = CustomManagementStrategy()

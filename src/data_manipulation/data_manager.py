import numpy as np
import pandas

from src.data_manipulation.argument_manager import ArgumentManager
from src.data_io.data_writer import DataWriter
from src.utils.path_utils import get_project_root
from src.domain.full_dataset import FullDataset
from src.repository.source_repository import SourceRepository

pandas.options.mode.chained_assignment = None  # default='warn'


class DataManager:

    data = None
    current_data_source = None
    default_path = str(get_project_root() + '\\resources\\data\\')

    @classmethod
    def update_data(cls, source=None, filename=''):
        print('Updating data...')
        if source is not None:
            ArgumentManager.validate_source(source)
            filename = cls.choose_filename(filename, source)
            cls.setup(source, cls.default_path, filename)
        else:
            sources = SourceRepository.list_sources()
            for source in sources:
                filename = cls.choose_filename(filename, source)
                cls.setup(source, cls.default_path, filename)
        print('Ready')
        return True

    @classmethod
    def setup(cls, source_id, path, filename):
        cls.current_data_source = SourceRepository.retrieve_data_source(source_id)
        cls.data = FullDataset(source_id, pandas.read_csv(cls.current_data_source.get_url()))
        full_path = path + filename
        DataWriter.write_to_csv(cls.data.get_raw_data(), full_path)

    @classmethod
    def load_dataset(cls, source='owid', filename=''):
        filename = cls.choose_filename(filename, source)
        rel_path = cls.default_path + filename
        cls.current_data_source = SourceRepository.retrieve_data_source(source)
        cls.data = FullDataset(source, pandas.read_csv(rel_path))

    @classmethod
    def get_location_list(cls):
        filter_strategy = cls.current_data_source.get_data_management_strategy()
        return filter_strategy.get_location_list(cls.data.get_raw_data())

    @classmethod
    def get_fittable_location_data(cls, location_id, dataset='', start=1, end=None):
        data = cls.get_location_data(location_id, dataset, start, end)
        ready_data = cls.process_data_for_fitting(data, location_id, dataset, start)
        return ready_data

    @classmethod
    def get_location_data(cls, location_id, dataset, start, end):
        source = cls.current_data_source
        dataset = cls.choose_dataset(dataset)
        data = cls.data.get_raw_data().copy()
        dm_strategy = source.get_data_management_strategy()
        location_column_name = source.get_location_column_name()
        ArgumentManager.validate_location(data, location_column_name, location_id)
        location_data = data[data[location_column_name] == location_id]
        ArgumentManager.validate_dataset_arguments(source, location_data, dataset, start, end)
        date_column_name = source.get_date_column_name()
        requested_columns_df = location_data[[date_column_name, dataset]]
        nonnan_data = requested_columns_df.dropna().reset_index(drop=True)
        requested_rows = dm_strategy.filter_rows(nonnan_data, dataset, start, end)
        ready_dataset = requested_rows.set_index(np.arange(1, len(requested_rows) + 1), drop=True)
        return ready_dataset.astype({dataset: 'int32'})

    @classmethod
    def process_data_for_fitting(cls, data, location, dataset, start):
        dataset = cls.choose_dataset(dataset)
        data.loc[:, dataset] -= cls.calculate_accumulated_events_prior_to_start(location, dataset, start)
        return data

    @classmethod
    def list_supported_sources(cls):
        print('The currently supported data sources are: ')
        print(SourceRepository.list_sources())

    @classmethod
    def choose_filename(cls, filename, source):
        if filename == '':
            filename = str(source) + '_dataset.csv'
        return filename

    @classmethod
    def choose_dataset(cls, dataset):
        if dataset == '':
            dataset = cls.current_data_source.get_default_dataset()
        return dataset

    @classmethod
    def get_data_source(cls):
        return cls.current_data_source

    @classmethod
    def get_single_datum(cls, location, dataset, s):
        dataset = cls.choose_dataset(dataset)
        location_data = cls.get_fittable_location_data(location, dataset)
        return location_data[[dataset]].iloc[s - 1][0]

    @classmethod
    def get_raw_cumulative_data(cls, location_id, dataset='', start=1, end=None):
        dataset = cls.choose_dataset(dataset)
        return cls.get_location_data(location_id, dataset, start, end)[dataset].values

    @classmethod
    def get_raw_incidence_data(cls, location_id, dataset='', start=1, end=None):
        dataset = cls.choose_dataset(dataset)
        accumulated_events_prior_to_start = cls.calculate_accumulated_events_prior_to_start(location_id, dataset, start)
        cumulative_data = np.concatenate(
            ([accumulated_events_prior_to_start], cls.get_raw_cumulative_data(location_id, dataset, start, end))
        )
        return np.diff(cumulative_data)

    @classmethod
    def calculate_accumulated_events_prior_to_start(cls, location, dataset, start):
        accumulated_events_prior_to_start = 0
        if start > 1:
            accumulated_events_prior_to_start = cls.get_single_datum(location, dataset, start - 1)
        return accumulated_events_prior_to_start

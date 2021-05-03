import numpy as np
import pandas

from src.argument_verifier import ArgumentVerifier
from src.data_io.data_writer import DataWriter
from src.data_io.path_utils import get_project_root
from src.domain.full_dataset import FullDataset
from src.repository.source_repository import SourceRepository

pandas.options.mode.chained_assignment = None  # default='warn'


class DataManager:

    data = None
    current_data_source = None
    default_path = str(get_project_root() + '\\resources\\data\\')

    @classmethod
    def update_data(cls, source='owid', filename=''):
        filename = cls.choose_filename(filename, source)
        print('Updating data...')
        cls.setup(source, cls.default_path, filename)
        print('Ready')

    @classmethod
    def setup(cls, source_id, path, filename):
        cls.current_data_source = SourceRepository.retrieve_data_source(source_id)
        cls.data = FullDataset(source_id, pandas.read_csv(cls.current_data_source.get_url()))
        full_path = path + filename
        DataWriter.write_to_csv(cls.data.get_raw_data(), full_path)

    @classmethod
    def load_dataset(cls, source_id='owid', filename=''):
        filename = cls.choose_filename(filename, source_id)
        rel_path = cls.default_path + filename
        cls.current_data_source = SourceRepository.retrieve_data_source(source_id)
        cls.data = FullDataset(source_id, pandas.read_csv(rel_path))

    @classmethod
    def get_location_list(cls):
        filter_strategy = cls.current_data_source.get_filter_strategy()
        return filter_strategy.get_location_list(cls.data.get_raw_data())

    @classmethod
    def get_location_data(cls, location_id, dataset='', start=1, end=-1):
        dataset = cls.choose_dataset(dataset)
        data = cls.data.get_raw_data().copy()
        location_column_name = cls.current_data_source.get_location_column_name()
        ArgumentVerifier.validate_location(data, location_column_name, location_id)
        location_data = data[data[location_column_name] == location_id]
        ArgumentVerifier.validate_dataset_arguments(cls.current_data_source, location_data, dataset, start, end)
        date_column_name = cls.current_data_source.get_date_column_name()
        requested_columns_df = location_data[[date_column_name, dataset]]
        return cls.prepare_dataset(requested_columns_df, dataset, start, end)

    @classmethod
    def prepare_dataset(cls, data, dataset_column, start, end):
        nonnan_dataset = data.dropna().reset_index(drop=True)
        requested_subset = cls.slice_data_by_index(nonnan_dataset, start, end)
        accumulated_events_previous_to_start = 0
        if start > 1:
            accumulated_events_previous_to_start = nonnan_dataset[dataset_column].iloc[start-2]
        requested_subset.loc[:, dataset_column] -= accumulated_events_previous_to_start
        correctly_indexed_dataset = requested_subset.set_index(np.arange(1, len(requested_subset) + 1), drop=True)
        return correctly_indexed_dataset.astype({dataset_column: 'int32'})

    @classmethod
    def slice_data_by_index(cls, data, start, end):
        sliced_data = data.iloc[start-1:end, :]
        correct_index = np.arange(1, len(sliced_data) + 1)
        sliced_data.set_index(correct_index, inplace=True, drop=True)
        return sliced_data

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
import numpy as np
import pandas

from src.data_io.data_writer import DataWriter
from src.data_io.path_utils import get_project_root


class DataManager:

    data_source = None
    data = None
    default_path = str(get_project_root() + '\\resources\\data\\')
    default_filename = 'full_dataset.csv'

    @classmethod
    def setup(cls, data_source_url, path=default_path, filename=default_filename):
        cls.data_source = data_source_url
        cls.data = pandas.read_csv(cls.data_source)
        full_path = path + filename
        DataWriter.write_to_csv(cls.data, full_path)

    @classmethod
    def load_dataset(cls, rel_path=default_path + default_filename):
        cls.data = pandas.read_csv(rel_path)

    @classmethod
    def get_country_list(cls):
        return cls.data['location'].unique()

    @classmethod
    def get_country_data(cls, country_id, dataset='total_cases'):
        country_data = cls.data[cls.data['location'] == country_id]
        requested_dataset = country_data[['date', dataset]]
        return cls.prepare_dataset(requested_dataset, dataset)

    @classmethod
    def prepare_dataset(cls, data, dataset_column):
        nonnan_dataset = data.dropna()
        correctly_indexed_dataset = nonnan_dataset.reset_index(drop=True)
        return correctly_indexed_dataset.astype({dataset_column: 'int32'})

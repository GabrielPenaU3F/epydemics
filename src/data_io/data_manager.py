import pandas

from src.data_io.data_writer import DataWriter


class DataManager:

    data_source = None
    data = None
    default_path = '../../resources/data/'
    default_filename = 'full_dataset.csv'

    @classmethod
    def setup(cls, data_source_url, path=default_path, filename=default_filename):
        cls.data_source = data_source_url
        cls.data = pandas.read_csv(cls.data_source)
        full_path = path + filename
        DataWriter.write_to_csv(cls.data, full_path)

    @classmethod
    def get_country_list(cls):
        return cls.data['location'].unique()

    @classmethod
    def load_dataset(cls, rel_path):
        cls.data = pandas.read_csv(rel_path)

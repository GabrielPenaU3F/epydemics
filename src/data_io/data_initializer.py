from src.data_io.data_manager import DataManager

# Default data URL

default_source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


def setup_data(data_source_url):
    DataManager.setup(data_source_url)


def update_data():
    print('Updating data...')
    setup_data(default_source_url)
    print('Ready')

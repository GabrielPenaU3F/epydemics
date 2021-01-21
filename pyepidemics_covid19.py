from src.data_io.data_manager import DataManager

# Initializations

# Default data URL

default_source_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


def config_data_source(data_source_url):
    DataManager.setup(data_source_url)


def initialize():
    print('Updating data...')
    config_data_source(default_source_url)
    print('Ready')


if __name__ == '__main__':
    initialize()




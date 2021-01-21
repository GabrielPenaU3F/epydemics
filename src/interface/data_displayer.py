import pandas

from src.data_io.data_manager import DataManager


def configure_dataframe_prints():
    pandas.set_option("display.max_rows", None, "display.max_columns", None)


def show_available_countries():
    configure_dataframe_prints()
    countries = DataManager.get_country_list()
    print(countries)


def show_data_from_country(country_id):
    configure_dataframe_prints()
    country_data = DataManager.get_country_data(country_id)
    print(country_data)

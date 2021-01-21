from src.data_io.data_manager import DataManager


def show_available_countries():
    countries = DataManager.get_country_list()
    print(countries)

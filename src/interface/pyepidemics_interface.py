from src.data_io.console_manager import ConsoleManager
from src.data_io.data_manager import DataManager
from src.fitters.fitter import Fitter

console = ConsoleManager.get_instance()


def show_available_countries():
    countries = DataManager.get_country_list()
    console.print_data_frame(countries)


def show_data_from_country(country_id):
    country_data = DataManager.get_country_data(country_id)
    console.print_data_frame(country_data)


def fit_contagion_model(country_name, dataset='total_cases', output=True, plot=True):
    fit = Fitter.fit(country_name, dataset)

    if output is True:
        console.show_fit_results(fit)
        
    if plot is True:
        pass

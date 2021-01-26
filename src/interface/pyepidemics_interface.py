from src.data_io.console_manager import ConsoleManager
from src.data_io.data_manager import DataManager
from src.data_io.plot_manager import PlotManager
from src.fitters.fitter import Fitter

console = ConsoleManager.get_instance()
plotter = PlotManager.get_instance()


def show_available_countries():
    countries = DataManager.get_country_list()
    console.print_data_frame(countries)


def show_data_from_country(country_id, dataset='total_cases'):
    country_data = DataManager.get_country_data(country_id, dataset, start=0, end=-1)
    console.print_data_from_country(country_data, country_id, dataset)


def fit_contagion_model(country_name, dataset='total_cases', start=1, end=-1, output=True, plot=True):
    fit = Fitter.fit(country_name, dataset, start, end)

    if output is True:
        console.show_fit_results(fit)
        
    if plot is True:
        plotter.plot_fit_results(fit)

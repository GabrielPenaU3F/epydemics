from src.data_io.console_manager import ConsoleManager
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager
from src.fitters.fitter import Fitter

console = ConsoleManager.get_instance()
plotter = PlotManager.get_instance()


def show_available_locations():
    locations = DataManager.get_location_list()
    console.print_locations(locations)


def show_data_from_location(location_id, dataset=''):
    location_data = DataManager.get_location_data(location_id, dataset)
    source = DataManager.get_data_source()
    console.print_data_from_location(source, location_id, dataset, location_data)


def fit_contagion_model(location_id, dataset='', start=1, end=-1, x0=(0.1, 1), output=True, plot=True):
    fit = Fitter.fit(location_id, dataset, start, end, x0)

    if output is True:
        console.show_fit_results(fit)
        
    if plot is True:
        plotter.plot_fit_results(fit)


def analyze_model_parameters_over_time(location, dataset='', start=1, end=-1, start_from=30,
                                       fit_x0=(0.1, 1)):
    parameter_tuples = Fitter.perform_range_fits(location, dataset, start, end, start_from, fit_x0)
    plotter.plot_parameters_over_time(parameter_tuples, start_from)


def calculate_mtbi(location, dataset='', start=1, end=-1, start_from=30, fit_x0=(0.1, 1), plot_unit='day'):
    mtbis = Fitter.calculate_mtbis(location, dataset, start, end, start_from, fit_x0)
    plotter.plot_mtbis(mtbis, start_from, plot_unit)

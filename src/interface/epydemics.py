import numpy as np

from src.data_manipulation.argument_manager import ArgumentManager
from src.data_io.console_manager import ConsoleManager
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager
from src.domain.fitter import Fitter

console = ConsoleManager.get_instance()
plotter = PlotManager.get_instance()


def show_available_locations():
    locations = DataManager.get_location_list()
    console.print_locations(locations)


def show_data_from_location(location_id, dataset=''):
    location_data = DataManager.get_fittable_location_data(location_id, dataset)
    source = DataManager.get_data_source()
    console.print_data_from_location(source, location_id, dataset, location_data)


def fit_model(location_id, dataset='', model='contagion', start=1, end=None, x0=(0.1, 1), output=True):
    fit = Fitter.fit(location_id, dataset, model,  start, end, x0)

    if output is True:
        console.show_fit_results(fit)
        plotter.plot_fit_results(fit)

    return fit


def analyze_model_parameters_over_time(location, dataset='', start=1, end=None, start_from=30,
                                       fit_x0=(0.1, 1), output=True):
    parameter_tuples = Fitter.fit_parameters_over_time(location, dataset, start, end, start_from, fit_x0)
    if output is True:
        plotter.plot_parameters_over_time(parameter_tuples, location, start_from)
    return parameter_tuples


def calculate_mtbi(location, dataset='', start=1, end=None, start_from=30,
                   fit_x0=(0.1, 1), unit='day', formula='exact_conditional', output=True):
    mtbis = Fitter.calculate_mtbis(location, dataset, start, end, start_from, fit_x0, formula)
    if output is True:
        console.show_minimum_status(mtbis, start_from, unit)
        plotter.plot_mtbis(mtbis, location, start_from, unit)
    return mtbis


def calculate_mtbi_inverse(location, dataset='', start=1, end=None, start_from=30, fit_x0=(0.1, 1),
                           formula='exact_conditional', output=True, real_data=True):
    mtbis = Fitter.calculate_mtbis(location, dataset, start, end, start_from, fit_x0, formula)
    if output is True:
        plotter.plot_mtbi_inverses(mtbis, location, dataset, start + start_from, real_data)
    inverses = np.power(mtbis, -1)
    return inverses


def show_incidence_spectrum(location, dataset='', start=1, end=None, output=True):
    spectrum = DataManager.get_raw_data_spectrum(location, dataset, start, end)
    if output is True:
        spectrum_mod = np.abs(spectrum)
        plotter.plot_incidence_spectrum(spectrum_mod, location)
    return spectrum

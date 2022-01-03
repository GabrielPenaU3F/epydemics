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


def fit_model(location, dataset='', model='contagion', start=1, end=None, x0=(0.1, 1), output=True):
    fit = Fitter.fit_model(location, dataset, model, start, end, x0)

    if output is True:
        console.show_fit_results(fit, location, dataset)
        plotter.plot_fit_results(fit, location, dataset)

    return fit


def analyze_model_parameters_over_time(location, dataset='', start=1, end=None, start_from=30,
                                       fit_x0=(0.1, 1), output=True, fit_output='params'):
    parameter_tuples = Fitter.fit_parameters_over_time(location, dataset, start, end, start_from, fit_x0, fit_output)
    if output is True:
        plotter.plot_parameters_over_time(parameter_tuples, location, start_from)
    return parameter_tuples


def calculate_mtbi(location, dataset='', start=1, end=None, start_from=30,
                   fit_x0=(0.1, 1), unit='day', formula='approx_conditional', output=True):
    mtbis = Fitter.calculate_mtbis(location, dataset, start, end, start_from, unit, fit_x0, formula)
    if output is True:
        console.show_minimum_status(mtbis, start_from, unit)
        plotter.plot_mtbis(mtbis, location, start_from, unit)
    return mtbis


def calculate_mtbi_inverse(location, dataset='', start=1, end=None, start_from=30, mtbi_unit='sec', fit_x0=(0.1, 1),
                           formula='exact_conditional', output=True, real_data=True):
    mtbis = Fitter.calculate_mtbis(location, dataset, start, end, start_from, mtbi_unit, fit_x0, formula)
    if output is True:
        plotter.plot_mtbi_inverses(mtbis, location, dataset, start + start_from, real_data)
    inverses = np.power(mtbis, -1)
    return inverses


def show_cumulative_data_curve(location, dataset='', start=1, end=None):
    raw_data = DataManager.get_raw_cumulative_data(location, dataset, start, end)
    plotter.plot_cumulative_data(raw_data, location, dataset)


def show_daily_data_curve(location, dataset='', start=1, end=None):
    raw_data = DataManager.get_raw_daily_data(location, dataset, start, end)
    plotter.plot_daily_data(raw_data, location, dataset)


def show_daily_data_spectrum(location, dataset='', start=1, end=None, output=True, xscale='rad'):
    spectrum = DataManager.get_raw_data_spectrum(location, dataset, start, end)
    if output is True:
        spectrum_mod = np.abs(spectrum)
        plotter.plot_daily_data_spectrum(spectrum_mod, location, xscale)
    return spectrum


def show_fit_residuals(location, dataset='', model='contagion', start=1, end=None,
                       fit_x0=(0.1, 1), output=True, type='true'):
    residuals = Fitter.compute_fit_residuals(location, dataset, model, start, end, fit_x0, type)
    if output is True:
        plotter.plot_fit_residuals(residuals, location, dataset)
    return residuals


def analyze_last_residual_over_time(location, dataset='', start=1, end=None, start_from=30,
                                    fit_x0=(0.1, 1), output=True, type='true'):
    residuals = Fitter.compute_last_residuals_over_time(location, dataset, start, end, start_from, fit_x0, type)
    if output is True:
        plotter.plot_last_residual_over_time(residuals, location, start_from)
    return residuals

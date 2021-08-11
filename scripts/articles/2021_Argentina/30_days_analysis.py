import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.models.model import ContagionModel
from src.domain.unit_converter import DaysConverter


def filter(y, L, n):
    ma_kernel = np.ones(L) / L
    for i in range(n):
        y = np.convolve(y, ma_kernel, mode='same')
    return y


def calculate_accumulated_events_prior_to_start(cumulative_data, start):
    accumulated_events_prior_to_start = 0
    if start > 1:
        accumulated_events_prior_to_start = cumulative_data[start - 1]
    return accumulated_events_prior_to_start


def perform_fits_with_window(daily_data, window_len, start_from, filtering=True):
    y = daily_data.copy()
    if filtering:
       y = filter(y, 7, 7)
    cumulative_data = np.cumsum(y)

    end = len(cumulative_data) + 1
    model = ContagionModel()
    output_list = []
    for i in range(start_from, end):

        fittable_data = cumulative_data - calculate_accumulated_events_prior_to_start(cumulative_data, i - window_len)
        fittable_data = fittable_data[i - window_len: i]
        x = np.arange(1, len(fittable_data) + 1)

        params = model.fit(x, fittable_data, (1, 0.5))
        explained = model.mean_value_function(x, *params)
        rsq = r2_score(fittable_data, explained)
        output_list.append(Fit(x, cumulative_data, explained, params, rsq))

    return output_list


def calculate_mtbis_with_window(daily_data, window_len, start_from, filtering):

    y = daily_data.copy()
    if filtering:
       y = filter(y, 7, 7)
    cumulative_data = np.cumsum(y)

    end = len(cumulative_data) + 1
    model = ContagionModel()
    mtbis = []
    for i in range(start_from, end):

        fittable_data = cumulative_data - calculate_accumulated_events_prior_to_start(cumulative_data, i - window_len)
        fittable_data = fittable_data[i - window_len: i]
        x = np.arange(1, len(fittable_data) + 1)

        params = model.fit(x, fittable_data, (1, 0.5))
        rho = params[0]
        gamma_per_rho = params[1]
        s = i
        mtbi = (1 + rho * s) / (rho * ((1 + rho * s) ** gamma_per_rho - 1))
        mtbis.append(mtbi)

    return mtbis


def plot_gamma_per_rho(x, gamma_per_rhos):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, gamma_per_rhos, linewidth=1, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=20, labelpad=15)
    axes.legend(loc='upper right', prop={'size': 20})
    plt.show()


def plot_rho(x, rhos):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, rhos, linewidth=1, color='#db6400', linestyle='-', label='\u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('\u03C1 (1/day)', fontsize=20, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 20})
    plt.show()


def plot_parameters_over_time(parameter_tuples, start_from):
    x_right_lim = start_from + len(parameter_tuples)
    x = np.arange(start_from, x_right_lim)
    rhos = [tup[0] for tup in parameter_tuples]
    gamma_per_rhos = [tup[1] for tup in parameter_tuples]
    plot_rho(x, rhos)
    plot_gamma_per_rho(x, gamma_per_rhos)


def plot_mtbis(mtbis, start_from, unit):
    converter = DaysConverter.get_instance()
    converted_mtbis = converter.convert_days_to(unit, mtbis)

    x_right_lim = start_from + len(mtbis)
    x = np.arange(start_from, x_right_lim)

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, converted_mtbis, linewidth=1, color='#0008AC', linestyle='-', label='MTBI')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('MTBI (' + str(unit) + ')', fontsize=20, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 20})
    plt.show()


DataManager.load_dataset('owid')
location = 'Argentina'
window_len = 30
start_from = 30

# Mínimums: [281 351 426]
# Maximums: [229 315 412 449]

# Cases dataset, first wave, initial stage
dataset = 'total_cases'
start = 1
end = 229

# Cases dataset, first wave, mitigation stage
# dataset = 'total_cases'
# start = 229
# end = 281

# Minimums: [295 376]
# Maximums: [207 321 458]

# Deaths dataset, first wave, initial stage
# dataset = 'total_deaths'
# start = 1
# end = 207

# Deaths dataset, first wave, mitigation stage
# dataset = 'total_deaths'
# start = 207
# end = 295


daily_data = DataManager.get_raw_daily_data(location, dataset, start, end)

fits = perform_fits_with_window(daily_data, window_len, start_from, filtering=False)
param_tuples = [fit.get_params() for fit in fits]
plot_parameters_over_time(param_tuples, start_from)

mtbis = calculate_mtbis_with_window(daily_data, window_len, start_from, filtering=False)
plot_mtbis(mtbis, start_from, 'sec')

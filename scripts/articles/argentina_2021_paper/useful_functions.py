import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg
from sklearn.metrics import r2_score

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.domain.fit import Fit
from src.domain.models.model import ContagionModel
from src.domain.unit_converter import DaysConverter
from src.interface import epydemics as ep


def apply_ma_filter(data, n, L):
    ma_kernel = np.ones(L) / L
    y = data.copy()
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
       y = apply_ma_filter(y, 7, 7)
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
       y = apply_ma_filter(y, 7, 7)
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


def plot_gamma_per_rho(x, gamma_per_rhos, filename, legend_loc):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, gamma_per_rhos, linewidth=2, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=32, labelpad=15)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.legend(loc=legend_loc, prop={'size': 32})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_rho(x, rhos, filename, legend_loc):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, rhos, linewidth=2, color='#db6400', linestyle='-', label='\u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('\u03C1 (1/day)', fontsize=32, labelpad=15)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.legend(loc=legend_loc, prop={'size': 32})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_parameters_over_time(parameter_tuples, x_start, rho_filename=None, gpr_filename=None,
                              rho_legend='upper left', gpr_legend='upper right'):
    x_right_lim = x_start + len(parameter_tuples)
    x = np.arange(x_start, x_right_lim)
    rhos = [tup[0] for tup in parameter_tuples]
    gamma_per_rhos = [tup[1] for tup in parameter_tuples]
    plot_rho(x, rhos, rho_filename, rho_legend)
    plot_gamma_per_rho(x, gamma_per_rhos, gpr_filename, gpr_legend)


def plot_mtbis(mtbis, unit, x_start, filename=None, legend_loc='upper left', dataset='total_cases'):
    converter = DaysConverter.get_instance()
    converted_mtbis = converter.convert_days_to(unit, mtbis)

    x_right_lim = x_start + len(mtbis)
    x = np.arange(x_start, x_right_lim)

    if dataset=='total_cases' or dataset=='nue_casosconf_diff':
        mtbe_title = 'MTBI'
    elif dataset=='total_deaths' or dataset=='nue_fallecidos_diff':
        mtbe_title = 'MTBD'

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, converted_mtbis, linewidth=2, color='#0008AC', linestyle='-', label=mtbe_title)
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel(mtbe_title + ' (' + str(unit) + ')', fontsize=32, labelpad=15)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.legend(loc=legend_loc, prop={'size': 32})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_mtbi_inverses(inverses, data, x_start, mtbi_filename, mtbi_legend):

    x_right_lim = x_start + len(inverses)
    x = np.arange(x_start, x_right_lim)

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, inverses, linewidth=2, color='#0008AC', linestyle='-', label='1/MTBI')
    axes.plot(x, data, linewidth=2, color='#C70F0B', linestyle='-', label='Daily data')

    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    axes.legend(loc=mtbi_legend, prop={'size': 32})
    fig.tight_layout()
    plt.show()

    if mtbi_filename is not None:
        fig.savefig(mtbi_filename)


def plot_indicators(location, dataset, start, end, start_from,
                    rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend):

    fit_tuples = ep.analyze_model_parameters_over_time(location, dataset=dataset, start=start, end=end,
                                                       start_from=start_from, output=False, fit_output='full')
    rsqs = []
    param_tuples = []
    for i in range(len(fit_tuples)):
        rsqs.append(fit_tuples[i].get_rsq())
        param_tuples.append(fit_tuples[i].get_params())

    plot_parameters_over_time(param_tuples, start + start_from - 1, rho_filename, gpr_filename, rho_legend, gpr_legend)

    mtbes = ep.calculate_mtbi(location, dataset=dataset, start=start, end=end,
                              start_from=start_from, output=False, formula='approx_conditional')
    plot_mtbis(mtbes, 'sec', start + start_from - 1, mtbi_filename, mtbi_legend, dataset)

    print('Minimum RSQ: ' + str(np.min(rsqs)))
    print('Maximum RSQ: ' + str(np.max(rsqs)))
    print('Mean RSQ: ' + str(np.mean(rsqs)))


def plot_indicators_with_window(location, dataset, start, end, start_from, window_len,
                                rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend):

    daily_data = DataManager.get_raw_daily_data(location, dataset, start, end)
    fits = perform_fits_with_window(daily_data, window_len, start_from, filtering=False)

    param_tuples = [fit.get_params() for fit in fits]
    rsqs = [fit.get_rsq() for fit in fits]

    plot_parameters_over_time(param_tuples, start + start_from - 1, rho_filename, gpr_filename, rho_legend, gpr_legend)

    mtbes = calculate_mtbis_with_window(daily_data, window_len, start_from, filtering=False)

    plot_mtbis(mtbes, 'sec', start + start_from - 1, mtbi_filename, mtbi_legend, dataset)

    print('Minimum RSQ: ' + str(np.min(rsqs)))
    print('Maximum RSQ: ' + str(np.max(rsqs)))
    print('Mean RSQ: ' + str(np.mean(rsqs)))


def plot_mtbi_inverse_vs_data(location, dataset, start, end, start_from, mtbi_filename, mtbi_legend):
    daily_data = DataManager.get_raw_daily_data(location, dataset, start + start_from - 1, end)
    mtbes = ep.calculate_mtbi(location, dataset=dataset, start=start, end=end,
                              start_from=start_from, output=False, formula='approx_conditional')
    inverses = np.power(mtbes, -1)
    plot_mtbi_inverses(inverses, daily_data, start + start_from - 1, mtbi_filename, mtbi_legend)


def plot_maxs_and_mins(y, filtering=False, n=7, L=7, filename=None):

    if filtering is True:
        y = apply_ma_filter(y, n, L)

    mins, _ = sg.find_peaks(-y)
    maxs, _ = sg.find_peaks(y)
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(y, color='#6F17A6', linewidth=2)
    axes.scatter(mins, y[mins], marker='x', s=128, color='#193894', linewidths=3, label='Minimums')
    axes.scatter(maxs, y[maxs], marker='o', s=32, color='#B90F0F', linewidths=2,  label='Maximums')
    pm = PlotManager()
    pm.config_axis_plain_style(axes)
    pm.config_plot_background(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 32})

    print('Maximums: ' + str(maxs))
    print('Minimums: ' + str(mins))

    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def config_spectrum_plot(axes, xscale):
    pm = PlotManager()
    pm.config_axis_plain_style(axes)
    pm.config_plot_background(axes)
    xticks = None
    xticklabels = None
    if xscale == 'rad':
        xticks = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
        xticklabels = ['0', r'$\pi$/4', r'$\pi$/2', r'3$\pi$/4', r'$\pi$']
        axes.set_xlabel('\u03C9 (rad/day)', fontsize=32, labelpad=15)
    elif xscale == 'freq':
        xticks = [0, 1/7, 2/7, 1/2]
        xticklabels = ['0', '1/7', '2/7', '1/2']
        axes.set_xlabel('Frequency (1/day)', fontsize=32, labelpad=15)
    axes.set_xticks(xticks)
    axes.set_xticklabels(xticklabels, fontsize=14)
    axes.tick_params(axis='y', which='major', labelsize=24)
    axes.legend(loc='upper right', prop={'size': 32})


def plot_spectrum(spectrum_mod, xscale, filename=None):

    fig, axes = plt.subplots(figsize=(12, 8))

    spectrum_mod = spectrum_mod[:int(len(spectrum_mod) / 2)]
    if xscale == 'rad':
        w = np.linspace(0, np.pi, len(spectrum_mod), endpoint=None)
    elif xscale == 'freq':
        w = np.linspace(0, 1 / 2, len(spectrum_mod), endpoint=None)

    axes.plot(w, spectrum_mod, linewidth=2, color='#6F17A6', linestyle='-', label='Spectrum absolute value')

    config_spectrum_plot(axes, xscale)
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_daily_data(raw_data, label, filename=None):
    pm = PlotManager()
    x = np.arange(1, len(raw_data) + 1)
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, raw_data, linewidth=2, color='#6F17A6', linestyle='-', label=label)
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 32})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)

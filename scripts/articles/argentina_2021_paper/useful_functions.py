import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg
from scipy import stats as st
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


def calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering):

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

    mtbis = DaysConverter.get_instance().convert_days_to(mtbi_unit, mtbis)
    return mtbis


def config_regular_plot_structure(axes, legend_loc=None):
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)

    if legend_loc is not None:
        axes.legend(loc=legend_loc, prop={'size': 32})


def config_scatterplot_mtbi_vs_mobility(axes):
    config_regular_plot_structure(axes)
    axes.set_xlabel('Mobility percent', fontsize=32, labelpad=15)
    axes.set_ylabel('MTBI', fontsize=32, labelpad=15)


def config_spectrum_plot(axes, xscale):
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
    config_regular_plot_structure(axes, legend_loc='upper right')


def plot_gamma_per_rho(x, gamma_per_rhos, filename, legend_loc):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, gamma_per_rhos, linewidth=2, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=32, labelpad=15)
    config_regular_plot_structure(axes, legend_loc)
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_rho(x, rhos, filename, legend_loc):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, rhos, linewidth=2, color='#db6400', linestyle='-', label='\u03C1')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('\u03C1 (1/day)', fontsize=32, labelpad=15)
    config_regular_plot_structure(axes, legend_loc)
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

    x_right_lim = x_start + len(mtbis)
    x = np.arange(x_start, x_right_lim)

    if dataset=='total_cases' or dataset=='nue_casosconf_diff':
        mtbe_title = 'MTBI'
    elif dataset=='total_deaths' or dataset=='nue_fallecidos_diff':
        mtbe_title = 'MTBD'

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, mtbis, linewidth=2, color='#0008AC', linestyle='-', label=mtbe_title)
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel(mtbe_title + ' (' + str(unit) + ')', fontsize=32, labelpad=15)
    config_regular_plot_structure(axes, legend_loc)
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
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    config_regular_plot_structure(axes, mtbi_legend)
    fig.tight_layout()
    plt.show()

    if mtbi_filename is not None:
        fig.savefig(mtbi_filename)


def plot_indicators(location, dataset, start, end, start_from, mtbi_unit,
                    rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend):

    fit_tuples = ep.analyze_model_parameters_over_time(location, dataset=dataset, start=start, end=end,
                                                       start_from=start_from, output=False, fit_output='full')
    rsqs = []
    param_tuples = []
    for i in range(len(fit_tuples)):
        rsqs.append(fit_tuples[i].get_rsq())
        param_tuples.append(fit_tuples[i].get_params())

    plot_parameters_over_time(param_tuples, start + start_from - 1, rho_filename, gpr_filename, rho_legend, gpr_legend)

    mtbes = ep.calculate_mtbi(location, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                              start_from=start_from, output=False, formula='approx_conditional')
    plot_mtbis(mtbes, mtbi_unit, start + start_from - 1, mtbi_filename, mtbi_legend, dataset)

    print('Minimum RSQ: ' + str(np.min(rsqs)))
    print('Maximum RSQ: ' + str(np.max(rsqs)))
    print('Mean RSQ: ' + str(np.mean(rsqs)))


def plot_indicators_with_window(location, dataset, start, end, start_from, window_len, mtbi_unit,
                                rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend):

    daily_data = DataManager.get_raw_daily_data(location, dataset, start, end)
    fits = perform_fits_with_window(daily_data, window_len, start_from, filtering=False)

    param_tuples = [fit.get_params() for fit in fits]
    rsqs = [fit.get_rsq() for fit in fits]

    plot_parameters_over_time(param_tuples, start + start_from - 1, rho_filename, gpr_filename, rho_legend, gpr_legend)

    mtbes = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)

    plot_mtbis(mtbes, mtbi_unit, start + start_from - 1, mtbi_filename, mtbi_legend, dataset)

    print('Minimum RSQ: ' + str(np.min(rsqs)))
    print('Maximum RSQ: ' + str(np.max(rsqs)))
    print('Mean RSQ: ' + str(np.mean(rsqs)))


def plot_mtbi_inverse_vs_data(location, dataset, start, end, start_from, mtbi_unit, mtbi_filename, mtbi_legend):
    daily_data = DataManager.get_raw_daily_data(location, dataset, start + start_from - 1, end)
    mtbes = ep.calculate_mtbi(location, dataset=dataset, start=start, end=end,
                              start_from=start_from, unit=mtbi_unit, output=False, formula='approx_conditional')
    inverses = np.power(mtbes, -1)
    plot_mtbi_inverses(inverses, daily_data, start + start_from - 1, mtbi_filename, mtbi_legend)


def plot_maxs_and_mins(y, filtering=False, n=7, L=7, filename=None):

    if filtering is True:
        y = apply_ma_filter(y, n, L)

    mins, _ = sg.find_peaks(-y)
    maxs, _ = sg.find_peaks(y)
    fig, axes = plt.subplots(figsize=(12, 8))
    config_regular_plot_structure(axes, legend_loc='upper left')
    axes.plot(y, color='#6F17A6', linewidth=2)
    axes.scatter(mins, y[mins], marker='x', s=128, color='#193894', linewidths=3, label='Minimums')
    axes.scatter(maxs, y[maxs], marker='o', s=32, color='#B90F0F', linewidths=2,  label='Maximums')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)

    print('Maximums: ' + str(maxs))
    print('Minimums: ' + str(mins))

    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


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
    x = np.arange(1, len(raw_data) + 1)
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, raw_data, linewidth=2, color='#6F17A6', linestyle='-', label=label)
    config_regular_plot_structure(axes, legend_loc='upper left')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


def plot_residual_variances(t_axis, vars):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(t_axis, vars, linewidth=2, color='#000275', label='Variance of the residuals')
    config_regular_plot_structure(axes, legend_loc='upper right')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Variance', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()


def plot_pvalues(t_axis, pvalues, alpha):
    fig, axes = plt.subplots(figsize=(12, 8))
    significance_line = np.full_like(t_axis, alpha, dtype=np.double)
    axes.plot(t_axis, pvalues, linewidth=2, color='#089107', label='P-value')
    axes.plot(t_axis, significance_line, color='#CA2A00', linestyle='--', linewidth=3,
              label=(str(alpha) + ' significance level'))
    config_regular_plot_structure(axes, legend_loc='upper left')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Probability', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()


def plot_confidence_intervals(t_axis, confidence_intervals, alpha):
    lim_infs = [interval[0] for interval in confidence_intervals]
    lim_sups = [interval[1] for interval in confidence_intervals]
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.fill_between(x=t_axis, y1=lim_infs, y2=lim_sups, alpha=0.5, color='#155CCF',
                      label=(str(alpha) + ' confidence interval'))
    config_regular_plot_structure(axes, legend_loc='upper right')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Residuals range', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()


def plot_prediction_errors(t_axis, prediction_errors):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(t_axis, prediction_errors, linewidth=2, color='#650782', label='1-day prediction errors')
    config_regular_plot_structure(axes, legend_loc='upper right')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Error magnitude', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()



def show_mtbi_vs_mobility_scatterplot(mtbis, mobility, x_start, legend_loc='lower left'):

    x_right_lim = x_start + len(mtbis)
    x = np.arange(x_start, x_right_lim)

    fig, axes = plt.subplots(figsize=(12, 8))

    axes.scatter(mobility, mtbis)

    config_scatterplot_mtbi_vs_mobility(axes)
    fig.tight_layout()
    plt.show()


def show_correlation_coefficients(var_1, var_2):

    r_pearson, pv_pearson = st.pearsonr(var_1, var_2)
    r_spearman, pv_spearman = st.spearmanr(var_1, var_2)
    t_kendall, pv_kendall = st.kendalltau(var_1, var_2)
    decimals = 4

    print('Pearson: r = ' + str(round(r_pearson, decimals)) + '    p-value: ' + '{:0.2e}'.format(pv_pearson))
    print('Spearman: \u03C1 = ' + str(round(r_spearman, decimals)) + '    p-value: ' + '{:0.2e}'.format(pv_spearman))
    print('Kendall: \u03C4 = ' + str(round(t_kendall, decimals)) + '    p-value: ' + '{:0.2e}'.format(pv_kendall))


def show_regression_coefficients(coefs):
    fig, axes = plt.subplots(figsize=(12, 8))
    coefs = np.array(coefs)
    labels = [r'$a_{' + str(i) + '}$' for i in range(1, len(coefs) + 1)]
    config_coeffs_barplot_structure(axes)
    axes.bar(labels, coefs, bottom=0, color='#000285', width=0.3)
    axes.axhline(0, linewidth=1.5, color='black')
    axes.set_title('Regression coefficients', fontsize=32, pad=18)
    axes.set_xlabel('Coefficient', fontsize=32, labelpad=15)
    fig.tight_layout()
    plt.show()


def config_coeffs_barplot_structure(axes):
    axes.patch.set_facecolor("#ffffff")
    axes.patch.set_edgecolor('black')
    axes.patch.set_linewidth('1')
    axes.set_facecolor("#ffffff")
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.axhline(0, linewidth=1.5, color='black')

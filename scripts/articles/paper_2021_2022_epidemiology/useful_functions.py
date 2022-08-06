import numpy as np
import datetime as dt
import matplotlib.dates as mdates

from matplotlib import pyplot as plt, rc

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter, perform_fits_with_window, \
    calculate_mtbis_with_window
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep

rc('font', **{'family': 'serif', 'serif': ['Arial']})
plt.rcParams['pdf.fonttype'] = 42


def plot_daily_data_and_filtered_curve(dataframe, ylabel, filename=None, n=7, L=7, legend_loc=None):
    data = dataframe['daily_data'].values
    filtered_data = apply_ma_filter(data, n, L)
    dates = dataframe['date'].values
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    fig, axes = plt.subplots(figsize=(12, 8))
    config_date_plot_structure(axes, tick_interval=60)
    axes.plot(x, data, linewidth=1, color='#6F17A6', linestyle='-', alpha=0.7, label='Reported data')
    axes.plot(x, filtered_data, linewidth=2, color='#CC2B04', linestyle='-', label='Filtered data')
    axes.set_xlabel('Date', fontsize=32, labelpad=15)
    axes.set_ylabel(ylabel, fontsize=32, labelpad=15)
    if legend_loc is not None:
        axes.legend(loc=legend_loc, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename, dpi=600)


def plot_spectrum(spectrum_mod, xscale, filename=None, legend_loc=None):

    fig, axes = plt.subplots(figsize=(12, 8))
    spectrum_mod = spectrum_mod[:int(len(spectrum_mod) / 2)]
    w = None
    if xscale == 'rad':
        w = np.linspace(0, np.pi, len(spectrum_mod), endpoint=None)
    elif xscale == 'freq':
        w = np.linspace(0, 1 / 2, len(spectrum_mod), endpoint=None)

    config_spectrum_plot(axes, xscale)
    axes.plot(w, spectrum_mod, linewidth=2, color='#6F17A6', linestyle='-', label='Spectrum absolute value')
    if legend_loc is not None:
        axes.legend(loc=legend_loc, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename, dpi=600)


def plot_daily_cases_vs_deaths(dates, cases, mins_cases, maxs_cases,
                               deaths, mins_deaths, maxs_deaths,
                               cases_legend_loc, deaths_legend_loc,
                               filename=None):

    fig, axes_left = plt.subplots(figsize=(12, 8))
    axes_right = axes_left.twinx()
    config_dual_plot_structure(axes_left, axes_right)
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    x_mins_cases = [x[i] for i in mins_cases]
    x_maxs_cases = [x[i] for i in maxs_cases]
    x_mins_deaths = [x[i] for i in mins_deaths]
    x_maxs_deaths = [x[i] for i in maxs_deaths]

    # Cases plot
    axes_left.plot(x, cases, color='#193894', linewidth=2, label='Daily cases')
    axes_left.plot(x_mins_cases, cases[mins_cases], "x", color='#193894', markersize=7)
    axes_left.plot(x_maxs_cases, cases[maxs_cases], "o", color='#193894', markersize=7)
    axes_left.set_xlabel('Date', fontsize=32, labelpad=15)
    axes_left.set_ylabel('Number of cases', fontsize=32, labelpad=15)

    # Deaths plot
    axes_right.plot(x, deaths, color='#B90F0F', linewidth=2, label='Daily deaths')
    axes_right.plot(x_mins_deaths, deaths[mins_deaths], "x", color='#B90F0F', markersize=7)
    axes_right.plot(x_maxs_deaths, deaths[maxs_deaths], "o", color='#B90F0F', markersize=7)
    axes_right.set_ylabel('Number of deaths', fontsize=32, labelpad=15)

    axes_left.legend(loc=cases_legend_loc, prop={'size': 24})
    axes_right.legend(loc=deaths_legend_loc, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename, dpi=600)


def plot_indicators_with_and_without_window(country, dataset, start, end, start_from,
                                            mtbe_unit, window_len, tick_interval,
                                            rho_filename, rho_legend, gpr_filename, gpr_legend,
                                            mtbe_filename, mtbe_legend):
    dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
    dates = dataframe['date']
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates[start_from - 1:]]
    daily_data = dataframe['daily_data']
    rhos_nowindow, gprs_nowindow = get_fits_without_window(country, dataset, end, start, start_from)
    rhos_window, gprs_window = get_fits_with_window(daily_data, start_from, window_len)
    mtbes_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbe_unit,
                                       start_from=start_from, output=False, formula='approx_conditional')
    mtbes_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbe_unit, filtering=False)

    plot_rhos(x, rhos_nowindow, rhos_window, rho_legend, rho_filename, tick_interval)
    plot_gprs(x, gprs_nowindow, gprs_window, gpr_legend, gpr_filename, tick_interval)
    plot_mtbes(x, mtbes_nowindow, mtbes_window, mtbe_legend, mtbe_filename, tick_interval, mtbe_unit, dataset)


def plot_rhos(x, rhos_nowindow, rhos_window, rho_legend, rho_filename, tick_interval):
    fig, axes_left = plt.subplots(figsize=(12, 8))
    axes_right = axes_left.twinx()
    config_dual_plot_structure(axes_left, axes_right, tick_interval=tick_interval)

    # No window
    line1 = axes_left.plot(x, rhos_nowindow, color='#1D8024', linewidth=2, label='Full stage history')
    axes_left.set_xlabel('Date', fontsize=32, labelpad=15)
    axes_left.set_ylabel('\u03C1 (1/day)', fontsize=32, labelpad=15)

    # Window
    line2 = axes_right.plot(x, rhos_window, color='#B80000', linewidth=2, label='Time window')
    axes_right.set_ylabel('\u03C1 (1/day)', fontsize=32, labelpad=15)

    axes_left.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useMathText=True)
    axes_left.yaxis.get_offset_text().set_fontsize(24)
    axes_right.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useMathText=True)
    axes_right.yaxis.get_offset_text().set_fontsize(24)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    axes_left.legend(lines, labels, loc=rho_legend, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if rho_filename is not None:
        fig.savefig(rho_filename, dpi=600)


def plot_gprs(x, gprs_nowindow, gprs_window, gpr_legend, gpr_filename, tick_interval):
    fig, axes = plt.subplots(figsize=(12, 8))
    config_date_plot_structure(axes, tick_interval=tick_interval)

    # No window
    axes.plot(x, gprs_nowindow, color='#1D8024', linewidth=2, label='Full stage history')
    axes.set_xlabel('Date', fontsize=32, labelpad=15)
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=32, labelpad=15)

    # Window
    axes.plot(x, gprs_window, color='#B80000', linewidth=2, label='Time window')
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=32, labelpad=15)

    axes.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useMathText=True)
    axes.yaxis.get_offset_text().set_fontsize(24)

    axes.legend(loc=gpr_legend, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if gpr_filename is not None:
        fig.savefig(gpr_filename, dpi=600)


def plot_mtbes(x, mtbes_nowindow, mtbes_window, mtbe_legend, mtbe_filename, tick_interval, unit, dataset='total_cases'):
    fig, axes = plt.subplots(figsize=(12, 8))
    config_date_plot_structure(axes, tick_interval=tick_interval)

    ylabel = 'MTBI (' + str(unit) + ')'
    if dataset == 'total_deaths':
        'MTBD (' + str(unit) + ')'

    # No window
    axes.plot(x, mtbes_nowindow, color='#1D8024', linewidth=2, label='Full stage history')
    axes.set_xlabel('Date', fontsize=32, labelpad=15)
    axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

    # Window
    axes.plot(x, mtbes_window, color='#B80000', linewidth=2, label='Time window')
    axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

    axes.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useMathText=True)
    axes.yaxis.get_offset_text().set_fontsize(24)

    axes.legend(loc=mtbe_legend, prop={'size': 24})
    fig.tight_layout()
    plt.show()

    if mtbe_filename is not None:
        fig.savefig(mtbe_filename, dpi=600)


def get_fits_with_window(daily_data, start_from, window_len):
    fits = perform_fits_with_window(daily_data, window_len, start_from, filtering=False)
    rsqs = []
    rhos = []
    gprs = []
    for i in range(len(fits)):
        rsqs.append(fits[i].get_rsq())
        rhos.append(fits[i].get_params()[0])
        gprs.append(fits[i].get_params()[1])
    print('Minimum RSQ: ' + str(np.min(rsqs)))
    return np.array(rhos), np.array(gprs)


def get_fits_without_window(country, dataset, end, start, start_from):
    fits = ep.analyze_model_parameters_over_time(country, dataset=dataset, start=start, end=end,
                                                 start_from=start_from, output=False, fit_output='full')
    rsqs = []
    rhos = []
    gprs = []
    for i in range(len(fits)):
        rsqs.append(fits[i].get_rsq())
        rhos.append(fits[i].get_params()[0])
        gprs.append(fits[i].get_params()[1])
    print('Minimum RSQ: ' + str(np.min(rsqs)))
    return rhos, gprs


def config_date_plot_structure(axes, tick_interval=60):
    config_plot_background(axes)
    config_axis_plain_style(axes)
    axes.tick_params(axis='y', which='major', labelsize=24)
    axes.tick_params(axis='x', which='major', labelsize=20)

    axes.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    axes.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
    plt.gcf().autofmt_xdate(rotation=45)


def config_axis_plain_style(axes):
    axes.ticklabel_format(axis='y', style='plain')


def config_plot_background(axes):
    axes.patch.set_facecolor("#ffffff")
    axes.patch.set_edgecolor('black')
    axes.patch.set_linewidth('1')
    axes.set_facecolor("#ffffff")
    axes.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)


def config_spectrum_plot(axes, xscale):
    config_plot_background(axes)
    config_axis_plain_style(axes)
    xticks = None
    xticklabels = None
    if xscale == 'rad':
        xticks = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
        xticklabels = ['0', r'$\pi$/4', r'$\pi$/2', r'3$\pi$/4', r'$\pi$']
        axes.set_xlabel('\u03C9 (rad/day)', fontsize=32, labelpad=15)
    elif xscale == 'freq':
        xticks = [0, 1/7, 2/7, 3/7, 1/2]
        xticklabels = ['0', '1/7', '2/7', '3/7', '1/2']
        axes.set_xlabel('Frequency (1/day)', fontsize=32, labelpad=15)
    axes.set_xticks(xticks)
    axes.set_xticklabels(xticklabels, fontsize=24)
    axes.tick_params(axis='y', which='major', labelsize=24)


def config_dual_plot_structure(axes_left, axes_right, tick_interval=60):
    config_date_plot_structure(axes_left, tick_interval)
    config_date_plot_structure(axes_right, tick_interval)

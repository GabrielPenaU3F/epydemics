import numpy as np
import datetime as dt
import matplotlib.dates as mdates

from matplotlib import pyplot as plt, rc

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter

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
        fig.savefig(filename)


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
        fig.savefig(filename)


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

    axes_left.legend(loc=cases_legend_loc, prop={'size': 26})
    axes_right.legend(loc=deaths_legend_loc, prop={'size': 26})
    fig.tight_layout()
    plt.show()

    if filename is not None:
        fig.savefig(filename)


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


def config_dual_plot_structure(axes_left, axes_right):
    config_date_plot_structure(axes_left, tick_interval=60)
    config_date_plot_structure(axes_right, tick_interval=60)

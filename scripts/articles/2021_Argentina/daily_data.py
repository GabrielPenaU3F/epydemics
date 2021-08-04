import numpy as np
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager


def config_plot_background(axes):
    axes.patch.set_facecolor("#ffffff")
    axes.patch.set_edgecolor('black')
    axes.patch.set_linewidth('1')
    axes.set_facecolor("#ffffff")
    axes.grid(color='black', linestyle='--', linewidth=0.5)


def config_axis_plain_style(axes):
    axes.ticklabel_format(axis='x', style='plain')
    axes.ticklabel_format(axis='y', style='plain')


def plot_daily_data(raw_data, label):
    x = np.arange(1, len(raw_data) + 1)
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, raw_data, linewidth=1, color='#6F17A6', linestyle='-', label=label)
    config_plot_background(axes)
    config_axis_plain_style(axes)
    axes.legend(loc='upper left', prop={'size': 20})
    axes.tick_params(axis='both', which='major', labelsize=14)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=20, labelpad=15)
    plt.show()


DataManager.load_dataset('owid')

ylabel = 'Daily confirmed cases'
arg_data = DataManager.get_raw_daily_data('Argentina', dataset='total_cases', start=1, end=515)
br_data = DataManager.get_raw_daily_data('Brazil', dataset='total_cases', start=1, end=515)

plot_daily_data(arg_data, ylabel)
plot_daily_data(br_data, ylabel)

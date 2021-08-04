import numpy as np
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


def plot_gamma_per_rho(x, gamma_per_rhos):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, gamma_per_rhos, linewidth=1, color='#61b15a', linestyle='-', label='\u03B3 / \u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('\u03B3 / \u03C1', fontsize=20, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 20})
    plt.show()


def plot_rho(x, rhos):
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, rhos, linewidth=1, color='#db6400', linestyle='-', label='\u03C1')
    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('\u03C1 (1/day)', fontsize=20, labelpad=15)
    axes.legend(loc='upper right', prop={'size': 20})
    plt.show()


def plot_parameters_over_time(parameter_tuples, start_from):
    x_right_lim = start_from + len(parameter_tuples)
    x = np.arange(start_from, x_right_lim)
    rhos = [tup[0] for tup in parameter_tuples]
    gamma_per_rhos = [tup[1] for tup in parameter_tuples]
    plot_rho(x, rhos)
    plot_gamma_per_rho(x, gamma_per_rhos)


DataManager.load_dataset('owid')

lugar = 'Argentina'

# Fourth wave, initial stage
start_from = 10
start = 426
end = 449

# Fourth wave, mitigation stage
# start_from = 10
# start = 449
# end = 515

param_tuples = ep.analyze_model_parameters_over_time(lugar, start=start, end=end, start_from=start_from, output=False)
# plot_parameters_over_time(param_tuples, start_from)

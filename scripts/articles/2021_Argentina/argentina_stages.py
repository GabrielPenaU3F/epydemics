import numpy as np
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.domain.unit_converter import DaysConverter
from src.interface import epydemics as ep


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


def plot_mtbis(mtbis, unit):
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


def plot_mtbi_inverses(mtbis, data):

    inverses = np.power(mtbis, -1)
    x_right_lim = start_from + len(inverses)
    x = np.arange(start_from, x_right_lim)

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, inverses, linewidth=1, color='#0008AC', linestyle='-', label='1/MTBI')
    axes.plot(x, data, linewidth=1, color='#C70F0B', linestyle='-', label='Daily data')

    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=20, labelpad=15)
    axes.legend(loc='upper right', prop={'size': 20})
    plt.show()


def plot_mtbd_inverses(mtbds, data):

    inverses = np.power(mtbds, -1)
    x_right_lim = start_from + len(inverses)
    x = np.arange(start_from, x_right_lim)

    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(x, inverses, linewidth=1, color='#0008AC', linestyle='-', label='1/MTBD')
    axes.plot(x, data, linewidth=1, color='#C70F0B', linestyle='-', label='Daily deaths')

    pm = PlotManager()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('Number of deaths', fontsize=20, labelpad=15)
    axes.legend(loc='upper right', prop={'size': 20})
    plt.show()


DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'

# Daily cases, first wave, initial stage
# dataset = 'total_cases'
# start_from = 30
# start = 1
# end = 229

# Daily cases, first wave, mitigation stage
# dataset = 'total_cases'
# start_from = 30
# start = 229
# end = 281

# Deaths, first wave, initial stage
# dataset = 'total_deaths'
# start_from = 30
# start = 1
# end = 207

# Deaths, first wave, mitigation stage
# dataset = 'total_deaths'
# start_from = 30
# start = 207
# end = 295

# Fourth wave, initial stage
# dataset = 'total_cases'
# start_from = 10
# start = 426
# end = 449

# Fourth wave, mitigation stage
# dataset = 'total_cases'
# start_from = 10
# start = 449
# end = 515

# Deaths, fourth wave, mitigation stage
dataset = 'total_deaths'
start_from = 10
start = 458
end = 509

data = DataManager.get_raw_daily_data('Argentina', dataset=dataset, start=start + start_from - 1, end=end)


# fit_tuples = ep.analyze_model_parameters_over_time(country, dataset=dataset, start=start, end=end,
#                                                    start_from=start_from, output=False, fit_output='full')
# rsqs = []
# param_tuples = []
# for i in range(len(fit_tuples)):
#     rsqs.append(fit_tuples[i].get_rsq())
#     param_tuples.append(fit_tuples[i].get_params())
#
# print('Minimum RSQ: ' + str(np.min(rsqs)))
# print('Maximum RSQ: ' + str(np.max(rsqs)))
# print('Mean RSQ: ' + str(np.mean(rsqs)))
# plot_parameters_over_time(param_tuples, start_from)

mtbes = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end,
                          start_from=start_from, output=False, formula='approx_conditional')
# plot_mtbis(mtbis, 'sec')
# plot_mtbi_inverses(mtbes, data)
plot_mtbd_inverses(mtbes, data)

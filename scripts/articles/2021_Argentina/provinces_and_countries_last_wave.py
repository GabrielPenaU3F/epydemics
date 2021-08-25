import numpy as np
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.domain.unit_converter import DaysConverter
from src.interface import epydemics as ep
from scipy import signal as sg


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


# Apply n series MA filters of length L=7
def find_maxs_and_mins(location, L, n):
    ma_kernel = np.ones(L) / L

    y = DataManager.get_raw_daily_data(location)
    for i in range(n):
        y = np.convolve(y, ma_kernel, mode='same')

    mins, _ = sg.find_peaks(-y)
    maxs, _ = sg.find_peaks(y)
    fig, axes = plt.subplots(figsize=(12, 8))
    axes.plot(y, color='#6F17A6', linewidth=0.5)
    axes.plot(mins, y[mins], "x", color='#193894', markersize=7, label='Minimums')
    axes.plot(maxs, y[maxs], "x", color='#B90F0F', markersize=7, label='Maximums')
    pm = PlotManager()
    pm.config_axis_plain_style(axes)
    pm.config_plot_background(axes)
    axes.tick_params(axis='both', which='major', labelsize=14)
    axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=20, labelpad=15)
    axes.legend(loc='upper left', prop={'size': 20})
    print('Maximums: ' + str(maxs))
    print('Minimums: ' + str(mins))
    plt.show()


# DataManager.load_dataset('mapache_arg')
# location = 'Río Negro'

DataManager.load_dataset('owid')
location = 'Uruguay'

# Filtering
# L = 12
# n = 20
# find_maxs_and_mins(location, L, n)

# Last wave, initial stage
# start_from = 10
# start = 338
# end = 447

# Last wave, mitigation stage
start_from = 10
start = 447
end = None

fit_tuples = ep.analyze_model_parameters_over_time(location, start=start, end=end, start_from=start_from, output=False,
                                                   fit_output='full')
rsqs = []
for i in range(len(fit_tuples)):
    rsqs.append(fit_tuples[i].get_rsq())

print('Minimum RSQ: ' + str(np.min(rsqs)))
print('Maximum RSQ: ' + str(np.max(rsqs)))
print('Mean RSQ: ' + str(np.mean(rsqs)))
#
# mtbis = ep.calculate_mtbi(location, start=start, end=end, start_from=start_from,
#                           output=False, formula='approx_conditional')
# plot_mtbis(mtbis, start_from, 'sec')


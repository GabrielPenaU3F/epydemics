import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar, end=515)
# inc_data = DataManager.get_raw_daily_data(lugar, dataset='total_deaths', end=509)
x = np.arange(1, len(inc_data) + 1)
pm = PlotManager.get_instance()

# Apply n series MA filters of length L=7
n = 7
L = 7
ma_kernel = np.ones(L) / L

y = inc_data.copy()
for i in range(n):
    y = np.convolve(y, ma_kernel, mode='same')

mins, _ = sg.find_peaks(-y)
maxs, _ = sg.find_peaks(y)
fig, axes = plt.subplots(figsize=(12, 8))
axes.plot(y, color='#6F17A6', linewidth=0.5)
axes.plot(mins, y[mins], "x", color='#193894', markersize=7, label='Minimums')
axes.plot(maxs, y[maxs], "x", color='#B90F0F', markersize=7, label='Maximums')
pm.config_axis_plain_style(axes)
pm.config_plot_background(axes)
axes.tick_params(axis='both', which='major', labelsize=14)
axes.set_xlabel('Time (days)', fontsize=20, labelpad=15)
axes.set_ylabel('Number of cases', fontsize=20, labelpad=15)
axes.legend(loc='upper left', prop={'size': 20})

print('Maximums: ' + str(maxs))
print('Minimums: ' + str(mins))

plt.show()

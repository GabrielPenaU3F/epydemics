import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar)
x = np.arange(1, len(inc_data) + 1)
pm = PlotManager.get_instance()

'''
fig, axes = plt.subplots(5, 1)
axes[0].plot(x, inc_data, linewidth=0.7, color='#263859', linestyle='-', label='Daily cases')
pm.config_axis_plain_style(axes[0])
pm.config_plot_background(axes[0])
axes[0].legend()

n = 7
# n = 45
for ax in axes[1:]:
    ma_kernel = np.ones(n) / n
    y_filt = np.convolve(inc_data, ma_kernel, mode='same')
    ax.plot(x, y_filt, linewidth=1, linestyle='-', label='Filtered data (n = ' + str(n) + ')')
    pm.config_axis_plain_style(ax)
    pm.config_plot_background(ax)
    ax.legend()
    n += 2
    # n += 8
'''

'''
n = 7
y = inc_data
for i in range(1, len(axes)):
    ax = axes[i]
    j = 3
    ma_kernel = np.ones(n) / n
    for k in range(j):
        y = np.convolve(y, ma_kernel, mode='same')
    ax.plot(x, y, linewidth=1, linestyle='-', label='Filtered data (' + str(i * j) + ' series MA filters)')
    pm.config_axis_plain_style(ax)
    pm.config_plot_background(ax)
    ax.legend()
'''

# Apply n series MA filters of length L=7
n = 7
L = 7
ma_kernel = np.ones(L) / L

y = inc_data.copy()
for i in range(n):
    y = np.convolve(y, ma_kernel, mode='same')

peaks, _ = sg.find_peaks(-y)
fig, axes = plt.subplots()
axes.plot(y, color='#2C3696', linewidth=0.5)
axes.plot(peaks, y[peaks], "x", color='red', markersize=7)
pm.config_axis_plain_style(axes)
pm.config_plot_background(axes)

plt.show()

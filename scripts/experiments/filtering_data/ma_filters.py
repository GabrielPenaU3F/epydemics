import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'
fig, axes = plt.subplots(5, 1)

inc_data = DataManager.get_raw_daily_data(lugar)
x = np.arange(1, len(inc_data) + 1)
pm = PlotManager.get_instance()
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

ma_kernel = np.ones(7)/7
filtered_data = np.convolve(inc_data, ma_kernel, mode='same')

minimums = sg.argrelmin(filtered_data)
print(minimums)

# diffs1 = np.abs(np.diff(filtered_data)[200:])
# minimums = np.argsort(diffs1)[:2]
# print(minimums)

plt.show()
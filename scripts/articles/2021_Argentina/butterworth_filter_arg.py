import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg
from sklearn.metrics import r2_score

from src.data_manipulation.data_manager import DataManager

import src.interface.epydemics as ep
from src.data_io.plot_manager import PlotManager
from src.repository.model_repository import ModelRepository

DataManager.load_dataset('owid')

lugar = 'Argentina'
start = 1
end = 515

inc_data = DataManager.get_raw_daily_data(lugar, start=start, end=end)
pm = PlotManager()

# Filtering

# Filtering with a low-pass Butterworth

fs = 1
wp0 = (1/18) - 1/64
ws0 = (1/18)

N, Wn = sg.buttord(wp=wp0, ws=ws0, gpass=1, gstop=3, fs=fs)
filter_sos = sg.butter(N, Wn, btype='low', output='sos')
y = sg.sosfiltfilt(filter_sos, x=inc_data)

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
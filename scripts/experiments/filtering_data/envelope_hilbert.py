import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'
fig, ax = plt.subplots()

inc_data = DataManager.get_raw_daily_data(lugar)
x = np.arange(1, len(inc_data) + 1)
pm = PlotManager.get_instance()
ax.plot(x, inc_data, linewidth=0.7, color='#263859', linestyle='-', label='Incidence')

analytic_signal = sg.hilbert(inc_data)
amplitude_envelope = np.abs(analytic_signal)

ax.plot(x, amplitude_envelope, linewidth=1, color='red', linestyle='-', label='Envelope')

pm.config_axis_plain_style(ax)
pm.config_plot_background(ax)
ax.legend()

plt.show()
from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager


DataManager.load_dataset('owid')
lugar = 'Argentina'
start = 1
inc_data = DataManager.get_raw_daily_data(lugar, start=start)

fs = 1
w0 = 1/7  # Frequency to be removed from signal
Q = 15  # Quality factor
b, a = signal.iirnotch(w0, Q, fs)
filter_sos = signal.tf2sos(b, a)
filtered_inc = signal.sosfilt(filter_sos, x=inc_data)

freq, h = signal.freqz(b, a, fs=fs)
fig, ax = plt.subplots()
ax.plot(freq, 20*np.log10(abs(h)), color='blue')
ax.set_title("Frequency Response")
ax.set_ylabel("Amplitude (dB)", color='blue')
ax.set_xlabel("Frequency (Hz)")
ax.grid()
plt.show()

x = np.arange(1, len(filtered_inc) + 1)
mins, _ = signal.find_peaks(-filtered_inc)
fig, ax_fincidencia = plt.subplots()
pm = PlotManager.get_instance()
ax_fincidencia.plot(x, filtered_inc, linewidth=1, color='#1174F7', linestyle='-', label='Filtered incidence')
ax_fincidencia.plot(mins, filtered_inc[mins], "x", color='red', markersize=7)
pm.config_axis_plain_style(ax_fincidencia)
pm.config_plot_background(ax_fincidencia)
ax_fincidencia.legend()
plt.show()
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from sklearn.metrics import r2_score

from src.data_manipulation.data_manager import DataManager

import src.interface.epydemics as ep
from src.data_io.plot_manager import PlotManager
from src.repository.model_repository import ModelRepository

DataManager.load_dataset('owid')

lugar = 'Brazil'
start = 1
fig, axes = plt.subplots(2, 3)

inc_data = DataManager.get_raw_daily_data(lugar, start=start)
spectrum = ep.show_daily_data_spectrum(lugar, start=start, xscale='freq', output=None)


ax_modelo = axes[0, 0]
fit = ep.fit_model(lugar, start=start, output=False)
pm = PlotManager.get_instance()
x = fit.get_x_data()
real_data = fit.get_y_data()
explained = fit.get_explained_data()
params = fit.get_params()
rsq = fit.get_rsq()
ax_modelo.plot(x, real_data, linewidth=1, color='#263859', linestyle='--', label='Real data')
ax_modelo.plot(x, explained, linewidth=1, color='#ca3e47', linestyle='-',
               label='Model: \n \u03C1 = ' + str(round(params[0], 4)) +
                     '\n \u03B3 / \u03C1 = ' + str(round(params[1], 4)) +
                     '\n R2 = ' + str(round(rsq, 4))
               )
pm.config_axis_plain_style(ax_modelo)
pm.config_plot_background(ax_modelo)
ax_modelo.legend()

noisy_mins, _ = signal.find_peaks(-inc_data)
ax_incidencia = axes[0, 1]
ax_incidencia.plot(x, inc_data, linewidth=1, color='#1174F7', linestyle='-', label='Incidence')
ax_incidencia.plot(noisy_mins, inc_data[noisy_mins], "x", color='red', markersize=7)
pm.config_axis_plain_style(ax_incidencia)
pm.config_plot_background(ax_incidencia)
ax_incidencia.legend()

ax_spectrum = axes[0, 2]
spectrum_mod = np.abs(spectrum)[:int(len(spectrum)/2)]
w = np.linspace(0, 1/2, len(spectrum_mod), endpoint=None)
ax_spectrum.plot(w, spectrum_mod, linewidth=1, color='#6F17A6', linestyle='-', label='Spectrum absolute value')
pm.config_plot_background(ax_spectrum)
pm.config_spectrum_plot_axis(ax_spectrum, xscale='freq')
ax_spectrum.legend()

# Filtering

# Filtering with a least-squares bandstop FIR, adjusted to the high frequency peaks in Argentina

'''
fs = 1
bands = [x/16 for x in range(0, 8)]
gains = [1, 1, 0, 1, 0, 1, 1, 0]
filter = signal.firls(25, bands, gains, fs=fs)
filtered_inc = signal.filtfilt(filter, a=1, x=inc_data)
'''


# Filtering with a low-pass Butterworth

fs = 1
wp0 = (1/30) - 1/64
ws0 = (1/30)

N, Wn = signal.buttord(wp=wp0, ws=ws0, gpass=1, gstop=3, fs=fs)
filter_sos = signal.butter(N, Wn, btype='low', output='sos')
filtered_inc = signal.sosfiltfilt(filter_sos, x=inc_data)

ax_fspectrum = axes[1, 2]
filtered_spectrum = np.abs(np.fft.fft(filtered_inc))[:int(len(spectrum)/2)]
w = np.linspace(0, 1/2, len(filtered_spectrum), endpoint=None)
ax_fspectrum.plot(w, filtered_spectrum, linewidth=1, color='#6F17A6', linestyle='-',
                  label='Filtered spectrum absolute value')
pm.config_plot_background(ax_fspectrum)
pm.config_spectrum_plot_axis(ax_fspectrum, xscale='freq')
ax_fspectrum.legend()


mins, _ = signal.find_peaks(-filtered_inc)
ax_fincidencia = axes[1, 1]
ax_fincidencia.plot(x, filtered_inc, linewidth=1, color='#1174F7', linestyle='-', label='Filtered incidence')
ax_fincidencia.plot(mins, filtered_inc[mins], "x", color='red', markersize=7)
pm.config_axis_plain_style(ax_fincidencia)
pm.config_plot_background(ax_fincidencia)
ax_fincidencia.legend()

ax_fmodelo = axes[1, 0]
filtered_cumdata = np.cumsum(filtered_inc)
model = ModelRepository.retrieve_model('contagion')
fparams = model.fit_model(x, filtered_cumdata, x0=(1, 0.5))
fexplained = model.mean_value_function(x, *fparams)
frsq = r2_score(real_data, fexplained)

ax_fmodelo.plot(x, real_data, linewidth=1, color='#263859', linestyle='--',
                label='Real data')
ax_fmodelo.plot(x, fexplained, linewidth=1, color='#ca3e47', linestyle='-',
                label='Model (filtered): \n \u03C1 = ' + str(round(fparams[0], 4)) +
                      '\n \u03B3 / \u03C1 = ' + str(round(fparams[1], 4)) +
                      '\n R2 (Filtered model vs real data) = ' + str(round(frsq, 4))
                )
pm.config_axis_plain_style(ax_fmodelo)
pm.config_plot_background(ax_fmodelo)
ax_fmodelo.legend()

'''
# La respuesta de los filtros

# Filtro pasabanda

freq, response = signal.freqz(filter)
fig, ax_filter = plt.subplots()
ax_filter.plot(0.5*freq/np.pi, np.abs(response))



# Filtro Butterworth

freq, response = signal.sosfreqz(filter_sos)

fig, axes = plt.subplots()
amps = np.abs(response)
axes.plot(freq/np.pi, 20*np.log10(amps/np.max(amps)))
pm.config_plot_background(axes)
axes.set_xlabel('Frecuencia (0 - Nyquist)')
axes.set_ylabel('Amplitud (dB)')

'''

plt.show()
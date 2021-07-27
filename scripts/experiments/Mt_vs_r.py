import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager
from src.domain.fitter import Fitter
from src.domain.unit_converter import DaysConverter

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar)
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

# fig, axes = plt.subplots()
# axes.plot(y, color='#2C3696', linewidth=0.5)
# axes.plot(mins, y[mins], "x", color='red', markersize=7)
# axes.plot(maxs, y[maxs], "x", color='green', markersize=7)
# pm.config_axis_plain_style(axes)
# pm.config_plot_background(axes)
# plt.show()

print('Minimums: ' + str(mins))
print('Maximums: ' + str(maxs))

# First wave, initial stage
# start = 1
# end = 1 + maxs[0]

# Second wave, initial stage
start = 1 + mins[0]
end = 1 + maxs[1]

# Third wave, initial stage
# start = 1 + mins[1]
# end = 1 + maxs[2]

start_from = 30

mtbis_exact = Fitter.calculate_mtbis(lugar, dataset='', start=start, end=end,
                                     start_from=start_from, fit_x0=(1, 0.5), formula='exact_conditional')
mtbis_approx = Fitter.calculate_mtbis(lugar, dataset='', start=start, end=end,
                                      start_from=start_from, fit_x0=(1, 0.5), formula='approx_conditional')
residuals = Fitter.compute_last_residuals_over_time(lugar, dataset='', start=start, end=end,
                                                    start_from=start_from, fit_x0=(1, 0.5), residual_type='true')

converter = DaysConverter.get_instance()
converted_mtbis_exact = converter.convert_days_to('sec', mtbis_exact)
converted_mtbis_approx = converter.convert_days_to('sec', mtbis_approx)


x_right_lim = start_from + len(mtbis_exact)
x = np.arange(start_from, x_right_lim)

fig, axes = plt.subplots(3, 1)
axes[0].plot(x, converted_mtbis_exact, linewidth=1, color='red', linestyle='-', label='MTBI (r)')
axes[1].plot(x, converted_mtbis_approx, linewidth=1, color='blue', linestyle='-', label='MTBI (M(t))')
axes[2].plot(x, residuals, linewidth=1, color='purple', linestyle='-', label='Residuals M(t)-r')

pm.config_plot_background(axes[0])
pm.config_plot_background(axes[1])
pm.config_plot_background(axes[2])
pm.config_mtbi_plot_axis(axes[0], 'sec')
pm.config_mtbi_plot_axis(axes[1], 'sec')
pm.config_axis_plain_style(axes[2])
axes[0].legend()
axes[1].legend()
axes[2].legend()

plt.show()

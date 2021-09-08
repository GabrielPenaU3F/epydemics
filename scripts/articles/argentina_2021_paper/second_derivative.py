import numpy as np
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


def second_derivative(t, rho, gamma):
    return ((gamma/rho) - 1) * (rho**2) * (1 + rho * t)**(gamma/rho - 2)


DataManager.load_dataset('owid')

location = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 426
end = 449
daily_data = DataManager.get_raw_daily_data(location, dataset, start, end)
window_len = 30

# No window
fits = ep.analyze_model_parameters_over_time(location, dataset=dataset, start=start, end=end,
                                             start_from=start_from, output=False, fit_output='full')
rhos = np.array([fit.get_params()[0] for fit in fits])
gprs = [fit.get_params()[1] for fit in fits]
gammas = np.array([rhos[i] * gprs[i] for i in range(len(fits))])

# With window
# fits_windowed = perform_fits_with_window(daily_data, window_len, start_from, filtering=False)
# rhos_windowed = np.array([fit.get_params()[0] for fit in fits_windowed])
# gprs_windowed = [fit.get_params()[0] for fit in fits_windowed]
# gammas_windowed = np.array([rhos_windowed[i] * gprs_windowed[i] for i in range(len(fits_windowed))])

t = np.arange(start_from, start_from + len(fits))

sec_ders = second_derivative(t, rhos, gammas)
# sec_ders_windowed = second_derivative(t, rhos_windowed, gammas_windowed)

fig, ax = plt.subplots()

ax.plot(t, sec_ders)
ax.set_title('Second derivative')
pm = PlotManager()
pm.config_plot_background(ax)
pm.config_axis_plain_style(ax)

plt.show()

from analyzers.contagion_fitter import ContagionFitter
from data_io.url_data_manager import URLDataManager
from plotter import Plotter
from matplotlib import pyplot as plt

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'

manager = URLDataManager(url)

data_raw = manager.get_cases_from_country('Germany')
data_corrected = manager.get_cases_from_country('Germany')

data_raw.delete_nans()
data_corrected.delete_nans()

constant_days = 3
constant_tolerance = 0.3
jump_tolerance = 1.5
data_corrected.apply_relative_difference_correction(constant_days, constant_tolerance, jump_tolerance)

fitter = ContagionFitter()
plotter = Plotter()

a_raw, b_raw = fitter.fit(data_raw.get_days(), data_raw.get_values())
a_corrected, b_corrected = fitter.fit(data_corrected.get_days(), data_corrected.get_values())

print("Parameters (raw): ")
print("ρ = " + str(a_raw))
print("γ/ρ = " + str(b_raw))

print("Parameters (corrected): ")
print("ρ = " + str(a_corrected))
print("γ/ρ = " + str(b_corrected))

fig, axes = plt.subplots(1, 2)

x_raw = data_raw.get_days()
y_raw = data_raw.get_values()
prediction_raw = ContagionFitter().mean_value_function(x_raw, a_raw, b_raw)
axes[0].plot(x_raw, y_raw, linewidth=1, color='#263859', linestyle='--',
             label='Raw data (' + data_raw.get_country_name() + ')')
axes[0].plot(x_raw, prediction_raw, linewidth=1, color='red', linestyle='-',
             label='Model curve')

x_corrected = data_corrected.get_days()
y_corrected = data_corrected.get_values()
prediction_corrected = ContagionFitter().mean_value_function(x_corrected, a_corrected, b_corrected)
axes[1].plot(x_corrected, y_corrected, linewidth=1, color='#263859', linestyle='--',
             label='Corrected data (' + data_corrected.get_country_name() + ')')
axes[1].plot(x_corrected, prediction_corrected, linewidth=1, color='red', linestyle='-',
             label='Model curve')

plotter.format_plot(axes[0])
plotter.format_plot(axes[1])
plt.show()

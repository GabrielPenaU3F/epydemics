import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar, end=515)
deaths_data = DataManager.get_raw_daily_data(lugar, dataset='total_deaths', end=509)
x_cases = np.arange(1, len(inc_data) + 1)
x_deaths = np.arange(6, len(deaths_data) + 6)
pm = PlotManager.get_instance()

filtered_cases = apply_ma_filter(inc_data, 7, 7)
filtered_deaths = apply_ma_filter(deaths_data, 9, 7)

mins_cases, _ = sg.find_peaks(-filtered_cases)
maxs_cases, _ = sg.find_peaks(filtered_cases)
mins_deaths, _ = sg.find_peaks(-filtered_deaths)
maxs_deaths, _ = sg.find_peaks(filtered_deaths)

# fig, axes = plt.subplots(figsize=(12, 8))
#
# # Cases plot
#
# axes.plot(x_cases, filtered_cases, color='#193894', linewidth=2, label='Daily cases')
# axes.plot(mins_cases, filtered_cases[mins_cases], "x", color='#193894', markersize=7)
# axes.plot(maxs_cases, filtered_cases[maxs_cases], "o", color='#193894', markersize=7)
#
# pm.config_axis_plain_style(axes)
# pm.config_plot_background(axes)
# axes.tick_params(axis='both', which='major', labelsize=24)
# axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
# axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
# axes.legend(loc='upper left', prop={'size': 24})
#
# # Deaths plot
#
# axes_right = axes.twinx()
# axes_right.plot(x_deaths, filtered_deaths, color='#B90F0F', linewidth=2, label='Daily deaths')
# axes_right.plot(6 + mins_deaths, filtered_deaths[mins_deaths], "x", color='#B90F0F', markersize=7)
# axes_right.plot(6 + maxs_deaths, filtered_deaths[maxs_deaths], "o", color='#B90F0F', markersize=7)
#
# pm.config_axis_plain_style(axes_right)
# pm.config_plot_background(axes_right)
# axes_right.tick_params(axis='both', which='major', labelsize=24)
# axes_right.set_ylabel('Number of deaths', fontsize=32, labelpad=15)
# axes_right.legend(loc='lower right', prop={'size': 24})
#
# fig.tight_layout()
# filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_ma_maxs_mins_cases_vs_deaths.pdf'
# fig.savefig(filename)
# plt.show()

zeropad = np.zeros(np.abs(len(filtered_cases) - len(filtered_deaths)), dtype='int32')
pad_deaths = np.concatenate((zeropad, filtered_deaths), axis=0)

mortality = pad_deaths / (1 + filtered_cases)

fig, axes = plt.subplots(figsize=(12, 8))
axes.plot(x_cases, mortality, color='#B90F0F', linewidth=2, label='Mortality rate')

pm.config_axis_plain_style(axes)
pm.config_plot_background(axes)
axes.tick_params(axis='both', which='major', labelsize=24)
axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
axes.set_ylabel('Mortality rate', fontsize=32, labelpad=15)
axes.legend(loc='upper right', prop={'size': 32})

fig.tight_layout()
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_mortality_rate.pdf'
fig.savefig(filename)
plt.show()

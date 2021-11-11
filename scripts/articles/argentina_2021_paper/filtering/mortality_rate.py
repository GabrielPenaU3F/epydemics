import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar, end=515)
deaths_data = DataManager.get_raw_daily_data(lugar, dataset='total_deaths', end=509)
x_cases = np.arange(1, len(inc_data) + 1)
x_deaths = np.arange(6, len(deaths_data) + 6)
pm = PlotManager.get_instance()

filtered_cases = apply_ma_filter(inc_data, 7, 7)
filtered_deaths = apply_ma_filter(deaths_data, 9, 7)

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

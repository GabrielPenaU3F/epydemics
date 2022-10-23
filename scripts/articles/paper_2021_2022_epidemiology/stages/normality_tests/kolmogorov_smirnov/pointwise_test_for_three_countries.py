import numpy as np

from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats

from scripts.articles.argentina_2021_paper.useful_functions import calculate_mtbis_with_window
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_indicators_with_and_without_window, \
    config_date_plot_structure
from src.interface import epydemics as ep
from src.data_manipulation.data_manager import DataManager

import datetime as dt

DataManager.load_dataset('owid')

# Argentina

country = 'Argentina'
dataset = 'total_cases'
start_from = 45
start = 1
end = 229
mtbi_unit = 'sec'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
daily_data = dataframe['daily_data']

mtbis_arg = []
mtbi_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                                   start_from=start_from, output=False, formula='approx_conditional')
mtbis_arg.append(mtbi_nowindow)

for window_len in np.arange(15, 45):
    mtbi_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
    mtbis_arg.append(mtbi_window)

# ------------------ #

# Germany

country = 'Germany'
dataset = 'total_cases'
start_from = 45
start = 523
end = 652
mtbi_unit = 'sec'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
daily_data = dataframe['daily_data']

mtbis_ger = []
mtbi_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                                  start_from=start_from, output=False, formula='approx_conditional')
mtbis_ger.append(mtbi_nowindow)
for window_len in np.arange(15, 45):
    mtbi_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
    mtbis_ger.append(mtbi_window)

# -------------- #

# USA

country = 'United States'
dataset = 'total_cases'
start_from = 45
start = 230
end = 344
mtbi_unit = 'sec'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
daily_data = dataframe['daily_data']

mtbis_usa = []
mtbi_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                                  start_from=start_from, output=False, formula='approx_conditional')
mtbis_usa.append(mtbi_nowindow)

for window_len in np.arange(15, 45):
    mtbi_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
    mtbis_usa.append(mtbi_window)

# Now generate the datasets we need

mtbis_arg = np.array(mtbis_arg)
mtbis_ger = np.array(mtbis_ger)
mtbis_usa = np.array(mtbis_usa)

# i-th row has a dataset of MTBIs at day i. We shall test normality in each of them
datasets_arg = mtbis_arg.transpose()
datasets_ger = mtbis_ger.transpose()
datasets_usa = mtbis_usa.transpose()
reject_bool_arg = []
reject_bool_ger = []
reject_bool_usa = []

# Kolmogorov - Smirnov test

filename_test = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ks_test.pdf'
filename_pvs = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ks_pvs.pdf'

alpha = .05

arg_pvs = []
for day in range(1, len(datasets_arg) + 1):
    dataset_arg = datasets_arg[day - 1]
    dataset_arg = (dataset_arg - np.mean(dataset_arg)) / np.std(dataset_arg)
    statistic, pv = stats.kstest(dataset_arg, stats.norm.cdf)
    arg_pvs.append(pv)
    if pv < alpha:
        reject_bool_arg.append(True)
    else:
        reject_bool_arg.append(False)

ger_pvs = []
for day in range(1, len(datasets_ger) + 1):
    dataset_ger = datasets_ger[day - 1]
    dataset_ger = (dataset_ger - np.mean(dataset_ger)) / np.std(dataset_ger)
    statistic, pv = stats.kstest(dataset_ger, stats.norm.cdf)
    ger_pvs.append(pv)
    if pv < alpha:
        reject_bool_ger.append(True)
    else:
        reject_bool_ger.append(False)

usa_pvs = []
for day in range(1, len(datasets_usa) + 1):
    dataset_usa = datasets_usa[day - 1]
    dataset_usa = (dataset_usa - np.mean(dataset_usa)) / np.std(dataset_usa)
    statistic, pv = stats.kstest(dataset_usa, stats.norm.cdf)
    usa_pvs.append(pv)
    if pv < alpha:
        reject_bool_usa.append(True)
    else:
        reject_bool_usa.append(False)

x_arg = np.arange(1, len(reject_bool_arg) + 1)
x_ger = np.arange(1, len(reject_bool_ger) + 1)
x_usa = np.arange(1, len(reject_bool_usa) + 1)
ones = np.ones(len(x_arg))
twos = 2 * np.ones(len(x_ger))
threes = 3 * np.ones(len(x_usa))

arg_kcolors = ['red' if kbool is True else 'green' for kbool in reject_bool_arg]
ger_kcolors = ['red' if kbool is True else 'green' for kbool in reject_bool_ger]
usa_kcolors = ['red' if kbool is True else 'green' for kbool in reject_bool_usa]

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Can reject normality',
                          markerfacecolor='r', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Cannot reject normality',
                          markerfacecolor='g', markersize=15)]

fig, axes = plt.subplots(figsize=(12, 8))

axes.scatter(x_arg, ones, c=arg_kcolors)
axes.scatter(x_ger, twos, c=ger_kcolors)
axes.scatter(x_usa, threes, c=usa_kcolors)

axes.set_yticks([1, 2, 3])
axes.set_yticklabels(['Argentina', 'Germany', 'USA'], fontdict={'fontsize': 32})
axes.set_xlabel('Day', fontsize=32, labelpad=15)
axes.legend(handles=legend_elements, prop={'size': 24}, loc='upper right')
fig.savefig(filename_test, dpi=600)

fig, axes = plt.subplots(figsize=(12, 8))
axes.plot(x_arg, arg_pvs, linewidth=2, linestyle='-', color='#0114A6', label='Argentina')
axes.plot(x_ger, ger_pvs, linewidth=2, linestyle='-', color='#E8B92C', label='Germany')
axes.plot(x_usa, usa_pvs, linewidth=2, linestyle='-', color='#BA002B', label='United States')
axes.plot(x_arg, [.05 for i in range(len(x_arg))], linewidth=1, linestyle='--', color='#02B541', label='.05 threshold')
axes.set_xlabel('Day', fontsize=32, labelpad=15)
axes.set_ylabel('P-value', fontsize=32, labelpad=15)
axes.grid(True, which="both")
axes.legend(prop={'size': 24}, loc='upper right')
fig.tight_layout()
fig.savefig(filename_pvs, dpi=600)

plt.show()

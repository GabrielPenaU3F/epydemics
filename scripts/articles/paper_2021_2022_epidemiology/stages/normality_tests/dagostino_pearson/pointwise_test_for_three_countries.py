import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
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
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/usa_avg_mtbi.pdf'

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

# D'Agostino - Pearson test
alpha = .05

for day in range(1, len(datasets_arg) + 1):
    dataset_arg = datasets_arg[day - 1]
    dataset_arg = (dataset_arg - np.mean(dataset_arg)) / np.std(dataset_arg)
    statistic, pv = stats.normaltest(dataset_arg)
    if pv < alpha:
        reject_bool_arg.append(True)
    else:
        reject_bool_arg.append(False)

for day in range(1, len(datasets_ger) + 1):
    dataset_ger = datasets_ger[day - 1]
    dataset_ger = (dataset_ger - np.mean(dataset_ger)) / np.std(dataset_ger)
    statistic, pv = stats.normaltest(dataset_ger)
    if pv < alpha:
        reject_bool_ger.append(True)
    else:
        reject_bool_ger.append(False)

for day in range(1, len(datasets_usa) + 1):
    dataset_usa = datasets_ger[day - 1]
    dataset_usa = (dataset_usa - np.mean(dataset_usa)) / np.std(dataset_usa)
    statistic, pv = stats.normaltest(dataset_usa)
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

plt.scatter(x_arg, ones, c=arg_kcolors)
plt.scatter(x_ger, twos, c=ger_kcolors)
plt.scatter(x_usa, threes, c=usa_kcolors)

plt.yticks([1, 2, 3], ['Argentina', 'Germany', 'USA'])
plt.title("D'Agostino-Pearson test")
plt.savefig('dagostino_pearson.png', dpi=600)
plt.show()

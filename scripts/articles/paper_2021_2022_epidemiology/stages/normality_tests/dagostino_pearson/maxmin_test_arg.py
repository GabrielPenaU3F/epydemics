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

mtbis_arg = np.array(mtbis_arg)
# i-th row has a dataset of MTBIs at day i. We shall test normality in each of them
datasets_arg = mtbis_arg.transpose()

# D'Agostino - Pearson test
alpha = .05

arg_mins = np.array([np.min(ith_day_mtbi) for ith_day_mtbi in datasets_arg])
arg_maxs = np.array([np.max(ith_day_mtbi) for ith_day_mtbi in datasets_arg])
arg_means = np.array([np.mean(ith_day_mtbi) for ith_day_mtbi in datasets_arg])
arg_stds = np.array([np.std(ith_day_mtbi) for ith_day_mtbi in datasets_arg])

arg_max_errors = (arg_maxs - arg_means)/arg_stds
arg_min_errors = (arg_mins - arg_means)/arg_stds

# Max
statistic, pv = stats.normaltest(arg_max_errors)
print('------- Argentina -------')
print('Curve of the maximums:')
print("D'Agostino-Pearson statistic: " + '{:g}'.format(statistic))
print('P-value: ' + '{:g}'.format(pv))
if pv < alpha:
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")

# Min
statistic, pv = stats.normaltest(arg_min_errors)
print('------- Argentina -------')
print('Curve of the maximums:')
print("D'Agostino-Pearson statistic: " + '{:g}'.format(statistic))
print('P-value: ' + '{:g}'.format(pv))
if pv < alpha:
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")

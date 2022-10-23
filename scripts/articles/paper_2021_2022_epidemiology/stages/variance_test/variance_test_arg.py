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

# Now generate the datasets we need

mtbis_arg = np.array(mtbis_arg)

# i-th row has a dataset of MTBIs at day i. We shall test variance for each point
datasets_arg = mtbis_arg.transpose()

low_bound = 1500
alpha = .05
reject_bool_arg = []
for day in range(1, len(datasets_arg) + 1):
    dataset_arg = datasets_arg[day - 1]
    n = len(dataset_arg)
    test_stat = (n - 1) * np.var(dataset_arg, ddof=1) / low_bound
    ref_chisq = stats.chi2.isf(alpha, n - 1)
    if test_stat <= ref_chisq:
        reject_bool_arg.append(True)
    else:
        reject_bool_arg.append(False)

arg_kcolors = ['green' if kbool is True else 'red' for kbool in reject_bool_arg]
zeros = np.zeros(len(datasets_arg))
x = np.arange(1, len(zeros) + 1)
plt.scatter(x, zeros, c=arg_kcolors)
plt.title('Variance <= ' + str(low_bound))
pw_variances = [np.var(datasets_arg[i], ddof=1) for i in range(len(datasets_arg))]
# plt.plot(x, pw_variances)
print('Mean of the variances: ' + str(np.mean(pw_variances)))

plt.show()

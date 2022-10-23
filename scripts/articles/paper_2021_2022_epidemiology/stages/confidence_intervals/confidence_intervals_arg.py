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
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/arg_mtbi_confidence.pdf'


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

# i-th row has a dataset of MTBIs at day i. We shall assign a confidence interval to each of them
datasets_arg = mtbis_arg.transpose()

infs95 = []
sups95 = []
infs99 = []
sups99 = []
for day in range(1, len(datasets_arg) + 1):
    dataset_arg = datasets_arg[day - 1]
    inf95, sup95 = stats.t.interval(alpha=.95, df=len(dataset_arg) - 1,
                                    loc=np.mean(dataset_arg), scale=stats.sem(dataset_arg))
    infs95.append(inf95)
    sups95.append(sup95)

    inf99, sup99 = stats.t.interval(alpha=.99, df=len(dataset_arg) - 1,
                                    loc=np.mean(dataset_arg), scale=stats.sem(dataset_arg))
    infs99.append(inf99)
    sups99.append(sup99)

avg_mtbi = np.array([np.mean(ith_day_mtbi) for ith_day_mtbi in datasets_arg])
std_mtbi = np.array([np.sqrt(np.var(ith_day_mtbi, ddof=1)) for ith_day_mtbi in datasets_arg])
lower_bound = avg_mtbi - std_mtbi
upper_bound = avg_mtbi + std_mtbi
ci_95_rdifs = (np.array(avg_mtbi) - np.array(infs95)) / np.array(avg_mtbi)
ci_99_rdifs = (np.array(avg_mtbi) - np.array(infs99)) / np.array(avg_mtbi)

dates = dataframe['date']
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates[start_from - 1:]]

fig, axes = plt.subplots(figsize=(12, 8))
config_date_plot_structure(axes, tick_interval=15)
axes.semilogy(x, avg_mtbi, color='#010B68', linewidth=2, linestyle='-', label='MTBI (averaged)')
axes.semilogy(x, infs95, color='#3FA128', linewidth=0.7, linestyle='--', label='95% Confidence')
axes.semilogy(x, sups95, color='#3FA128', linewidth=0.7, linestyle='--')
axes.semilogy(x, infs99, color='#B80000', linewidth=0.7, linestyle='--', label='99% Confidence')
axes.semilogy(x, sups99, color='#B80000', linewidth=0.7, linestyle='--')
axes.fill_between(x, lower_bound, upper_bound, facecolor='#6788B5', alpha=0.15, label='Standard deviation')
axes.set_xlabel('Date', fontsize=32, labelpad=15)
axes.set_ylabel('MTBI (sec)', fontsize=32, labelpad=15)
axes.grid(True, which="both")
axes.set_ylim((1, 10**3))
axes.yaxis.get_offset_text().set_fontsize(24)
axes.legend(prop={'size': 24})
fig.tight_layout()
fig.savefig(filename, dpi=600)

print('95% Min (rel): ' + str(np.min(ci_95_rdifs)))
print('95% Max (rel): ' + str(np.max(ci_95_rdifs)))
print('95% Mean (rel): ' + str(np.mean(ci_95_rdifs)))
print('99% Min (rel): ' + str(np.min(ci_99_rdifs)))
print('99% Mean (rel): ' + str(np.mean(ci_99_rdifs)))
print('99% Max (rel): ' + str(np.max(ci_99_rdifs)))

plt.show()

import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import calculate_mtbis_with_window
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_indicators_with_and_without_window, \
    config_date_plot_structure
from src.interface import epydemics as ep
from src.data_manipulation.data_manager import DataManager

import datetime as dt

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 45
start = 1
end = 229
mtbi_unit = 'sec'
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/arg_avg_mtbi.pdf'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
dates = dataframe['date']
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates[start_from - 1:]]
daily_data = dataframe['daily_data']

fig, axes = plt.subplots(figsize=(12, 8))
config_date_plot_structure(axes, tick_interval=15)
ylabel = 'MTBI (sec)'
axes.set_xlabel('Date', fontsize=32, labelpad=15)
axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

mtbis = []
mtbis_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                                   start_from=start_from, output=False, formula='approx_conditional')
mtbis.append(mtbis_nowindow)
for window_len in np.arange(15, 45):
    mtbi_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
    mtbis.append(mtbi_window)

mtbis = np.array(mtbis)
avg_mtbi = np.array([np.mean(col) for col in mtbis.transpose()])
std_mtbi = np.array([np.sqrt(np.var(col, ddof=1)) for col in mtbis.transpose()])

axes.semilogy(x, avg_mtbi, linewidth=2,  color='#B80000', label='MTBI (averaged)')
axes.set_ylabel(ylabel, fontsize=32, labelpad=15)
axes.grid(True, which="both")
axes.set_ylim((1, 10**3))

# axes.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useMathText=True)
axes.yaxis.get_offset_text().set_fontsize(24)

lower_bound = avg_mtbi - std_mtbi
upper_bound = avg_mtbi + std_mtbi
axes.fill_between(x, lower_bound, upper_bound, facecolor='#D17373', alpha=0.3, label='Standard deviation')

axes.legend(prop={'size': 24})
fig.tight_layout()

fig.savefig(filename, dpi=600)

plt.show()


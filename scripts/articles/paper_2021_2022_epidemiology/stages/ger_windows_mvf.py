import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

from scripts.articles.paper_2021_2022_epidemiology.useful_functions import config_date_plot_structure
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep

import datetime as dt

DataManager.load_dataset('owid')

country = 'Germany'
dataset = 'total_cases'
start_from = 45
start = 523
end = 652
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ger_avg_mvf.pdf'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
dates = dataframe['date']
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
daily_data = dataframe['daily_data']

fig, axes = plt.subplots(figsize=(12, 8))
config_date_plot_structure(axes, tick_interval=15)
ylabel = 'Cumulative number of cases'
axes.set_xlabel('Date', fontsize=32, labelpad=15)
axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

fit = ep.fit_model(country, dataset, model='contagion', start=start, end=end, x0=(0.1, 1), output=False)
mvf = fit.get_explained_data()
real_data = fit.get_y_data()

axes.plot(x, real_data, linewidth=2, color='black', linestyle='--', label='Real data')
axes.plot(x, mvf, linewidth=2, color='#B90502', label='Mean value function')
axes.set_ylabel(ylabel, fontsize=32, labelpad=15)
axes.grid(True, which="both")

axes.ticklabel_format(axis='y', style='plain', useMathText=True)
axes.yaxis.get_offset_text().set_fontsize(24)

axes.legend(prop={'size': 24})
fig.tight_layout()
fig.savefig(filename, dpi=600)
rsq = r2_score(real_data, mvf)
print(rsq)
plt.show()



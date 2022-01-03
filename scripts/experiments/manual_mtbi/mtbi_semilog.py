import datetime as dt

import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import calculate_mtbis_with_window
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import config_date_plot_structure, \
    config_plot_background, config_axis_plain_style
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


def plot_mtbes_semilog(x, mtbes_nowindow, mtbes_window, mtbe_legend, unit, tick_interval, dataset='total_cases'):
    fig, axes = plt.subplots(figsize=(12, 8))

    ylabel = 'MTBI (' + str(unit) + ')'
    if dataset == 'total_deaths':
        'MTBD (' + str(unit) + ')'

    config_date_plot_structure(axes, tick_interval=tick_interval)

    # No window
    axes.semilogy(x, mtbes_nowindow, color='#1D8024', linewidth=2, label='Full stage history')
    axes.set_xlabel('Date', fontsize=32, labelpad=15)
    axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

    # Window
    axes.semilogy(x, mtbes_window, color='#B80000', linewidth=2, label='Time window')
    axes.set_ylabel(ylabel, fontsize=32, labelpad=15)

    axes.yaxis.get_offset_text().set_fontsize(24)

    axes.legend(loc=mtbe_legend, prop={'size': 24})
    fig.tight_layout()
    plt.show()


DataManager.load_dataset('owid')

# Argentina
country = 'Argentina'
start = 1
end = 229
#
# # Germany
# country = 'Germany'
# start = 523
# end = 652
#
# # USA
# country = 'United States'
# start = 230
# end = 344

dataset = 'total_cases'
start_from = 30
mtbi_unit = 'sec'
window_len = 30
mtbi_legend = 'upper right'
tick_interval = 30

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
daily_data = dataframe['daily_data'].values
dates = dataframe['date'].values
mtbis_nowindow = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit=mtbi_unit,
                                   start_from=start_from, output=False, formula='approx_conditional')
mtbis_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates[start_from - 1:]]

plot_mtbes_semilog(x, mtbis_nowindow, mtbis_window, mtbi_legend, mtbi_unit, tick_interval, dataset)

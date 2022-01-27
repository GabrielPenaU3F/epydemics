import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import stats

from scripts.articles.argentina_2021_paper.useful_functions import calculate_mtbis_with_window
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_indicators_with_and_without_window, \
    config_date_plot_structure
from src.interface import epydemics as ep
from src.data_manipulation.data_manager import DataManager

import datetime as dt

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 60
start = 1
end = 229
mtbi_unit = 'sec'

dataframe = DataManager.get_raw_daily_data(country, dataset, start, end, dates=True)
dates = dataframe['date']
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates[start_from - 1:]]
daily_data = dataframe['daily_data']
daily_cases = daily_data.to_numpy()[start_from - 1:]

# fig, axes = plt.subplots(figsize=(12, 8))
# config_date_plot_structure(axes, tick_interval=15)
# ylabel = 'MTBI (sec)'

matrix = []
windows = np.arange(30, 60)
for window_len in windows:

    mtbi_window = calculate_mtbis_with_window(daily_data, window_len, start_from, mtbi_unit, filtering=False)
    cases_estimation = np.power(mtbi_window, -1)
    row = (daily_cases - cases_estimation)[140:]
    # mu_e = np.mean(errors)
    # s2_e = np.var(errors, ddof=1)
    # errors = (errors - mu_e)/s2_e
    matrix.append(row)

matrix = np.array(matrix)
a = 2

row_mus = []
row_sigmas = []
for row in matrix:
    row_mus.append(np.mean(row))
    row_sigmas.append(np.var(row, ddof=1))
row_mus = np.array(row_mus)
row_sigmas = np.array(row_sigmas)
row_stats = np.vstack((row_mus, row_sigmas)).transpose()

col_mus = []
col_sigmas = []
for col in matrix.transpose():
    col_mus.append(np.mean(col))
    col_sigmas.append(np.var(col, ddof=1))
col_mus = np.array(col_mus + [0, 0])
col_sigmas = np.array(col_sigmas + [0 ,0])
col_stats = np.vstack((col_mus, col_sigmas))

matrix = np.hstack((matrix, row_stats))
matrix = np.vstack((matrix, col_stats))

pd.DataFrame(matrix).to_csv('E:/Universidad/Investigación/Coronavirus/Python/script_outputs/matriz.csv')
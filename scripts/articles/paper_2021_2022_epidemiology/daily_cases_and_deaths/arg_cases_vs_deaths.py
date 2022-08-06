import numpy as np
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_daily_cases_vs_deaths
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

lugar = 'Argentina'
# cases_end = 638
# deaths_end = 633

# Updated February 3 2022
cases_end = 702
deaths_end = 697

cases_dataframe = DataManager.get_raw_daily_data(lugar, dataset='total_cases', end=cases_end, dates=True)
cases_data = cases_dataframe['daily_data'].values
dates = cases_dataframe['date'].values
deaths_data = DataManager.get_raw_daily_data(lugar, dataset='total_deaths', end=deaths_end)
offset = len(cases_data) - len(deaths_data)

deaths_data = np.concatenate((np.zeros(offset), deaths_data))

filtered_cases = apply_ma_filter(cases_data, 7, 7)
filtered_deaths = apply_ma_filter(deaths_data, 9, 7)

mins_cases, _ = sg.find_peaks(-filtered_cases)
maxs_cases, _ = sg.find_peaks(filtered_cases)
mins_deaths, _ = sg.find_peaks(-filtered_deaths)
maxs_deaths, _ = sg.find_peaks(filtered_deaths)

cases_legends_loc = 'upper left'
deaths_legends_loc = 'lower right'
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/arg_filtered_cases_vs_deaths.pdf'

plot_daily_cases_vs_deaths(dates, filtered_cases, mins_cases, maxs_cases,
                           filtered_deaths, mins_deaths, maxs_deaths,
                           cases_legends_loc, deaths_legends_loc, filename)

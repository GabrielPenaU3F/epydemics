import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter, plot_daily_cases_vs_deaths
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'

inc_data = DataManager.get_raw_daily_data(lugar, end=515)
deaths_data = np.concatenate((np.zeros(6), DataManager.get_raw_daily_data(lugar, dataset='total_deaths', end=509)))
x = np.arange(1, len(inc_data) + 1)

filtered_cases = apply_ma_filter(inc_data, 7, 7)
filtered_deaths = apply_ma_filter(deaths_data, 9, 7)

mins_cases, _ = sg.find_peaks(-filtered_cases)
maxs_cases, _ = sg.find_peaks(filtered_cases)
mins_deaths, _ = sg.find_peaks(-filtered_deaths)
maxs_deaths, _ = sg.find_peaks(filtered_deaths)

filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_ma_maxs_mins_cases_vs_deaths.pdf'

plot_daily_cases_vs_deaths(x, filtered_cases, mins_cases, maxs_cases,
                           filtered_deaths, mins_deaths, maxs_deaths,
                           filename)

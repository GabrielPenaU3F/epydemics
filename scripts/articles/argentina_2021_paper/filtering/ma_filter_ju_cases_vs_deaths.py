import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter, plot_daily_cases_vs_deaths
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('mapache_arg')

lugar = 'Jujuy'

# cases_data = DataManager.get_raw_daily_data_without_holes(lugar, dataset='nue_casosconf_diff', start=1, end=431,
#                                                           mode='dataframe')
# deaths_data = DataManager.get_raw_daily_data_without_holes(lugar, dataset='nue_fallecidos_diff', start=1, end=378,
#                                                            mode='dataframe')

cases_data = DataManager.get_raw_daily_data_without_holes(lugar, dataset='nue_casosconf_diff', start=1, end=431,
                                                          mode='array')
deaths_data = DataManager.get_raw_daily_data_without_holes(lugar, dataset='nue_fallecidos_diff', start=1, end=378,
                                                           mode='array')
x = np.arange(1, len(cases_data) + 1)

filtered_cases = apply_ma_filter(cases_data, 7, 13)
filtered_deaths = apply_ma_filter(deaths_data, 12, 13)

mins_cases, _ = sg.find_peaks(-filtered_cases)
maxs_cases, _ = sg.find_peaks(filtered_cases)
mins_deaths, _ = sg.find_peaks(-filtered_deaths)
maxs_deaths, _ = sg.find_peaks(filtered_deaths)

filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ju_ma_maxs_mins_cases_vs_deaths.pdf'

plot_daily_cases_vs_deaths(x, filtered_cases, mins_cases, maxs_cases,
                           filtered_deaths, mins_deaths, maxs_deaths,
                           filename)

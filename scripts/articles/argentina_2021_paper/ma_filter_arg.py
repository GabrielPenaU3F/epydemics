import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter, plot_maxs_and_mins
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

lugar = 'Argentina'
daily_data = DataManager.get_raw_daily_data(lugar, end=515)
L = 7
filename_n_3 = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_ma_n_3.pdf'
filename_n_5 = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_ma_n_5.pdf'
filename_n_7 = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_ma_n_7.pdf'

plot_maxs_and_mins(daily_data, filtering=True, n=3, L=L, filename=filename_n_3)
plot_maxs_and_mins(daily_data, filtering=True, n=5, L=L, filename=filename_n_5)
plot_maxs_and_mins(daily_data, filtering=True, n=7, L=L, filename=filename_n_7)

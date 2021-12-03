def plot_filtered_cases(y, n, L, country):

    y = apply_ma_filter(y, n, L)

    mins, _ = sg.find_peaks(-y)
    maxs, _ = sg.find_peaks(y)
    fig, axes = plt.subplots(figsize=(12, 8))
    pm = PlotManager.get_instance()
    pm.config_plot_background(axes)
    pm.config_axis_plain_style(axes)
    axes.tick_params(axis='both', which='major', labelsize=24)
    axes.plot(y, color='#6F17A6', linewidth=2)
    axes.scatter(mins, y[mins], marker='x', s=128, color='#193894', linewidths=3, label='Minimums')
    axes.scatter(maxs, y[maxs], marker='o', s=32, color='#B90F0F', linewidths=2,  label='Maximums')
    axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
    axes.set_ylabel('Number of cases', fontsize=32, labelpad=15)
    axes.set_title(country, fontsize=40)

    print(country)
    print('Maximums: ' + str(maxs))
    print('Minimums: ' + str(mins))
    print('-------\n')

    fig.tight_layout()
    plt.show()

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sg

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter, plot_maxs_and_mins
from src.data_manipulation.data_manager import DataManager
from src.data_io.plot_manager import PlotManager

DataManager.load_dataset('owid')

n = 7
L = 7
for index, lugar in enumerate(['Spain', 'Italy', 'Portugal', 'United Kingdom', 'Germany', 'Switzerland', 'France',
                               'Hungary', 'Bulgaria', 'Romania', 'Czechia', 'Slovakia', 'Slovenia', 'Greece',
                               'Serbia', 'Norway', 'Sweden', 'Finland', 'Denmark', 'Netherlands', 'Belgium']):
    daily_data = DataManager.get_raw_daily_data(lugar)
    plot_filtered_cases(daily_data, n, L, lugar)

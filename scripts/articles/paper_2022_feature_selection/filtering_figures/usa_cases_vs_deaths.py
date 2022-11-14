import numpy as np
import pandas as pd

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_daily_cases_vs_deaths, \
    config_dual_plot_structure
from scripts.experiments.countries_feature_selection.codigo_original_2021.useful_functions import get_full_dataframe
from src.data_manipulation.data_manager import DataManager
from matplotlib import pyplot as plt, rc

DataManager.load_dataset('owid')

rc('font', **{'family': 'serif', 'serif': ['Arial']})
plt.rcParams['pdf.fonttype'] = 42

full_df = get_full_dataframe()
df = full_df[full_df['location'] == 'United States']
df = df[df['new_cases'].notna()]
df = df[df['new_deaths'].notna()]

# Find the peaks

n = 7
L = 7
nonfiltered_cases = df['new_cases'].to_numpy()
nonfiltered_deaths = df['new_deaths'].to_numpy()
filtered_cases = apply_ma_filter(df['new_cases'], n, L)
filtered_deaths = apply_ma_filter(df['new_deaths'], n, L)

fig, axes_left = plt.subplots(figsize=(8, 5))
dates = df['date'].values
axes_left.plot(dates, filtered_cases, linestyle='-', linewidth=1, color='#0C3F8A', label='Cases')
axes_right = axes_left.twinx()
axes_right.plot(dates, filtered_deaths, linestyle='-', linewidth=1, color='#BF0F00', label='Deaths')

# Dates formatting
axes_left.set_xlim(-30, len(df) + 30)
f = pd.date_range(dates[0], dates[-1], 7).strftime('%Y-%m-%d')
axes_left.set_xticks(f)
axes_left.set_xticklabels(f, rotation=70, ha='center')

# Finish plot formatting
axes_left.yaxis.get_offset_text().set_fontsize(16)
axes_right.yaxis.get_offset_text().set_fontsize(16)
axes_left.set_ylabel('Number of cases', fontsize=14)
axes_right.set_ylabel('Number of deaths', fontsize=14)
axes_left.set_title('United States', fontsize=20, pad=15)
axes_left.grid(linewidth=0.3)
axes_left.legend(loc='upper left', fontsize=16)
axes_right.legend(loc='upper right', fontsize=16)
fig.tight_layout()
plt.show()

fig_filename = \
    'E:/Universidad/Investigación/Coronavirus/SeleccionAtributos/resources/results/figs_publication/fig_usa_cases_deaths.pdf'
fig.savefig(fig_filename)

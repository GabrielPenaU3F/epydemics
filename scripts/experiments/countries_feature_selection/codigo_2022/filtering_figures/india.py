import numpy as np
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.experiments.countries_feature_selection.codigo_original_2021.useful_functions import find_peak_location, \
    get_full_dataframe

full_df = get_full_dataframe()
df = full_df[full_df['location'] == 'India']
df = df[df['new_cases'].notna()]
df = df.drop(columns=['new_deaths'])

# Find the peaks

n = 7
L = 7
nonfiltered_data = df['new_cases'].to_numpy()
filtered_data = apply_ma_filter(df['new_cases'], n, L)
peak_xs = find_peak_location(filtered_data)
if peak_xs.size != 0:  # check if it's empty
    peak_values = filtered_data[peak_xs]

fake_peak_idx = np.array([1, 4, 5, 7]) - 1
real_peak_idx = np.array([2, 3, 6]) - 1

fake_peak_xs = np.take(peak_xs, fake_peak_idx)
fake_peak_values = np.take(peak_values, fake_peak_idx)
real_peak_xs = np.take(peak_xs, real_peak_idx)
real_peak_values = np.take(peak_values, real_peak_idx)

fig, axes = plt.subplots(figsize=(8, 5))
dates = df['date'].values
axes.plot(dates, filtered_data, linestyle='-', linewidth=1, color='#0C3F8A', label='Filtered data')
axes.plot(dates, nonfiltered_data, linestyle='--', linewidth=0.5, color='#F2B616', label='Real data')
axes.scatter(fake_peak_xs, fake_peak_values, marker='o', color='#C93412', label='Fake peaks')
axes.scatter(real_peak_xs, real_peak_values, marker='o', color='#36B56B', label='Real peaks')

# Dates formatting
axes.set_xlim(-30, len(df) + 30)
f = pd.date_range(dates[0], dates[-1], 7).strftime('%Y-%m-%d')
axes.set_xticks(f)
axes.set_xticklabels(f, rotation=70, ha='center')

# Finish plot formatting
axes.yaxis.get_offset_text().set_fontsize(16)
axes.set_ylabel('Number of cases', fontsize=14)
axes.set_title('India', fontsize=20)
axes.grid(linewidth=0.3)
axes.legend(loc='upper left', fontsize=16)
fig.tight_layout()
plt.show()

fig_filename = \
    'E:/Universidad/Investigación/Coronavirus/SeleccionAtributos/resources/results/figs_publication/fig_india_filtering.png'
fig.savefig(fig_filename)

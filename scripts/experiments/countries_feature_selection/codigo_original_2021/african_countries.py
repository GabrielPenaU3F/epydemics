import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.experiments.countries_feature_selection.useful_functions import split_dataframes_from_continent, find_peak_location

dfs = split_dataframes_from_continent('Africa')

output_df = pd.DataFrame(columns=['country', 'peak_date', 'peak_magnitude'])
print('Total number of countries: ' + str(len(dfs)))
df_count = 0
for df in dfs:
    country = df['location'].iloc[0]
    n = 10
    L = 7
    nonfiltered_cases = df['new_cases'].copy()
    filtered_cases = apply_ma_filter(df['new_cases'], n, L)
    df['new_cases'] = filtered_cases
    # Problema: en África, algunos países llegan muy pronto al pico y otros tardan mucho más.
    # Hay países que ya están llegando al segundo cuando otros recien van por el primero.
    first_240 = filtered_cases[:240]
    peak_xs = find_peak_location(first_240)
    if peak_xs.size != 0:  # check if it's empty
        df_count += 1
        peak_values = first_240[peak_xs]
        max_peak_x = peak_xs[np.argmax(peak_values)]
        max_peak_value = first_240[max_peak_x]

        fig, axes = plt.subplots(figsize=(8, 5))
        axes.plot(first_240)
        axes.plot(nonfiltered_cases[:240], linestyle='--')
        axes.scatter(peak_xs, peak_values, marker='x')
        axes.scatter(max_peak_x, max_peak_value, marker='o', color='red')
        axes.set_title(country)
        fig.tight_layout()
        plt.show()
        max_peak_date = df['date'].loc[max_peak_x]
        output_df = output_df.append({'country': country, 'peak_date': max_peak_date, 'peak_magnitude': max_peak_value},
                                     ignore_index=True)
        fig_filename = 'E:/Universidad/Investigación/Coronavirus/Primer pico de países del mundo/figs/Africa/fig_' \
                       + str(country) + '.png'
        fig.savefig(fig_filename)

print('Number of countries with peak: ' + str(df_count))
print(output_df)
output_df.to_csv('E:/Universidad/Investigación/Coronavirus/africa_first_peaks.csv')

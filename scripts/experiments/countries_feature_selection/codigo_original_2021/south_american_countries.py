import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.experiments.countries_feature_selection.useful_functions import split_dataframes_from_continent, find_peak_location

dfs = split_dataframes_from_continent('South America')

output_df = pd.DataFrame(columns=['country', 'peak_date', 'peak_magnitude'])
print('Total number of countries: ' + str(len(dfs)))
df_count = 0
for df in dfs:
    country = df['location'].iloc[0]
    n = 7
    L = 7
    nonfiltered_cases = df['new_cases'].copy()
    filtered_cases = apply_ma_filter(df['new_cases'], n, L)
    df['new_cases'] = filtered_cases
    first_250 = filtered_cases[:250]
    peak_xs = find_peak_location(first_250)
    if peak_xs.size != 0:  # check if it's empty
        df_count += 1
        peak_values = first_250[peak_xs]
        max_peak_x = peak_xs[np.argmax(peak_values)]
        max_peak_value = first_250[max_peak_x]

        fig, axes = plt.subplots(figsize=(8, 5))
        axes.plot(first_250)
        axes.plot(nonfiltered_cases[:250], linestyle='--')
        axes.scatter(peak_xs, peak_values, marker='x')
        axes.scatter(max_peak_x, max_peak_value, marker='o', color='red')
        axes.set_title(country)
        fig.tight_layout()
        plt.show()
        max_peak_date = df['date'].loc[max_peak_x]
        output_df = output_df.append({'country': country, 'peak_date': max_peak_date, 'peak_magnitude': max_peak_value},
                                     ignore_index=True)
        fig_filename = 'E:/Universidad/Investigación/Coronavirus/Primer pico de países del mundo/figs/South America/fig_' \
                       + str(country) + '.png'
        fig.savefig(fig_filename)

print('Number of countries with peak: ' + str(df_count))
print(output_df)
output_df.to_csv('E:/Universidad/Investigación/Coronavirus/south_america_first_peaks.csv')

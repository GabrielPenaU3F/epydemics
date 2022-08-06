import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.experiments.countries_feature_selection.useful_functions import get_country_dataframe, find_peak_location

country = 'Tunisia'
start = 1
end = 300

df = get_country_dataframe(country)
n = 7
L = 7
nonfiltered_cases = df['new_cases'].copy()
filtered_cases = apply_ma_filter(df['new_cases'], n, L)
df['new_cases'] = filtered_cases
subset = filtered_cases[:end]
peak_xs = find_peak_location(subset)
if peak_xs.size != 0:  # check if it's empty
    peak_values = subset[peak_xs]
    max_peak_x = peak_xs[np.argmax(peak_values)]
    max_peak_value = subset[max_peak_x]

    fig, axes = plt.subplots(figsize=(8, 5))
    axes.plot(subset)
    axes.plot(nonfiltered_cases[:end], linestyle='--')
    axes.scatter(peak_xs, peak_values, marker='x')
    axes.scatter(max_peak_x, max_peak_value, marker='o', color='red')
    axes.set_title(country)
    fig.tight_layout()
    plt.show()
    max_peak_date = df['date'].loc[max_peak_x]
    output_df = pd.DataFrame.from_dict({'country': [country], 'peak_date': [max_peak_date],
                                        'peak_magnitude': [max_peak_value]})
    print(output_df)
    fig_filename = 'E:/Universidad/Investigación/Coronavirus/Primer pico de países del mundo/figs/fig_' \
                   + str(country) + '.png'
    fig.savefig(fig_filename)
else:
    print('No peak')

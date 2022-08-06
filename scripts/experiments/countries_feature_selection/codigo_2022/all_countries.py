import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.experiments.countries_feature_selection.codigo_original_2021.useful_functions import \
    find_peak_location, split_dfs_by_country

dfs = split_dfs_by_country()
print('Total number of countries: ' + str(len(dfs)))

df_count = 0
output_df = pd.DataFrame(columns=['location', 'peak_date', 'peak_magnitude',
                                  'mask_use', 'mobility', 'vaccination_1_dose', 'vaccination_full'])

# Find the peaks

for df in dfs:
    # For cases
    # required_col_name = 'new_cases'
    # For deaths
    required_col_name = 'new_deaths'
    country = df['location'].iloc[0]
    n = 7
    L = 7
    nonfiltered_data = df[required_col_name].copy()
    filtered_data = apply_ma_filter(df[required_col_name], n, L)
    peak_xs = find_peak_location(filtered_data)
    if peak_xs.size != 0:  # check if it's empty
        df_count += 1
        peak_values = filtered_data[peak_xs]

        fig, axes = plt.subplots(figsize=(8, 5))
        axes.plot(filtered_data)
        axes.plot(nonfiltered_data, linestyle='--', linewidth=0.5)
        axes.scatter(peak_xs, peak_values, marker='o', color='red')
        n_peaks = np.arange(1, len(peak_values) + 1)
        for i, txt in enumerate(n_peaks):
            axes.annotate(txt, (peak_xs[i], peak_values[i]))
        axes.set_title(country)
        # plt.show()
        fig.tight_layout()

        for peak_x in peak_xs:
            peak_date = df['date'].loc[peak_x]
            peak_value = filtered_data[peak_x]
            output_df = output_df.append({'location': country, 'peak_date': peak_date, 'peak_magnitude': peak_value},
                                         ignore_index=True)

        # For cases
        '''fig_filename = \
            'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/figs/fig_' \
            + str(country) + '.png'
        '''
        # For deaths
        fig_filename = \
            'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/figs/muertos/fig_' \
            + str(country) + '.png'
        fig.savefig(fig_filename)

print('Number of countries with peak: ' + str(df_count))

# Match with mask use and the rest of the data

data = pd.read_csv('E:/Universidad/Investigación/Coronavirus/Datos/IHME/ihme_data_20_a_22_fixed.csv')

output_df.reset_index(inplace=True)
for index in output_df.index:
    location = output_df['location'].iloc[index]
    if location not in data['location_name'].unique():
        print(str(location) + ' not found')
        output_df.at[index, 'mask_use'] = np.nan
        output_df.at[index, 'mobility'] = np.nan
        output_df.at[index, 'vaccination_1_dose'] = np.nan
        output_df.at[index, 'vaccination_full'] = np.nan
    else:
        try:
            country_data = data[data['location_name'] == location]
            row = country_data[country_data['date'] == output_df['peak_date'].iloc[index]]

            mask_use = row['mask_use_mean'].values[0] * 100
            mobility = row['mobility_mean'].values[0]
            vac_1dose = row['cumulative_all_vaccinated'].values[0]
            vac_full = row['cumulative_all_fully_vaccinated'].values[0]

            if not np.isnan(mask_use):
                output_df.at[index, 'mask_use'] = float('{:.2f}'.format(mask_use))
            else:
                output_df.at[index, 'mask_use'] = np.nan

            if not np.isnan(mobility):
                output_df.at[index, 'mobility'] = round(mobility)
            else:
                output_df.at[index, 'mobility'] = np.nan

            if not np.isnan(vac_1dose):
                output_df.at[index, 'vaccination_1_dose'] = round(vac_1dose)
            else:
                output_df.at[index, 'vaccination_1_dose'] = np.nan

            if not np.isnan(vac_full):
                output_df.at[index, 'vaccination_full'] = round(vac_full)
            else:
                output_df.at[index, 'vaccination_full'] = np.nan

        except IndexError:
            print('Debuggear para ver error')

# For cases
# output_df.to_csv(
# 'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks.csv')

# For deaths
output_df.to_csv(
    'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_muertos.csv')

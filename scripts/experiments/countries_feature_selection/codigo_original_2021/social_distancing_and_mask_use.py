import pandas as pd

data = pd.read_csv('E:/Universidad/Investigación/Coronavirus/Datos/data_download_file_reference_2020.csv')
output_df = pd.read_csv('E:/Universidad/Investigación/Coronavirus/Primer pico de países del mundo/All.csv')

for index in output_df['index']:
    country = output_df['country'].iloc[index]
    if country not in data['location_name'].unique():
        print(str(country) + ' not found')
    else:
        try:
            country_data = data[data['location_name'] == country]
            row = country_data[country_data['date'] == output_df['peak_date'].iloc[index]]
            mask_use = row['mask_use_mean'].values[0] * 100
            social_distancing = row['mobility_mean'].values[0]
            output_df.at[index, 'mask_use'] = float('{:.2f}'.format(mask_use))
            output_df.at[index, 'social_distancing'] = round(social_distancing)
        except IndexError:
            print('Debuggear para ver error')

output_df.to_csv('E:/Universidad/Investigación/Coronavirus/Primer pico de países del mundo/All_final.csv')

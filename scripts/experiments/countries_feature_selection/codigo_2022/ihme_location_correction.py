import numpy as np
import pandas as pd

from scripts.experiments.countries_feature_selection.codigo_original_2021.useful_functions import get_full_dataframe

full_df = get_full_dataframe()
countries = full_df['location'].unique()

ihme_data = pd.read_csv('E:/Universidad/Investigación/Coronavirus/Datos/IHME/ihme_data_20_a_22.csv')

ihme_data = ihme_data.replace(['Bolivia (Plurinational State of)'], 'Bolivia')
ihme_data = ihme_data.replace(['Cabo Verde'], 'Cape Verde')
ihme_data = ihme_data.replace(["Côte d'Ivoire"], "Cote d'Ivoire")
ihme_data = ihme_data.replace(["Democratic Republic of the Congo"], 'Democratic Republic of Congo')
ihme_data = ihme_data.replace(['Hong Kong Special Administrative Region of China'], 'Hong Kong')
ihme_data = ihme_data.replace(['Iran (Islamic Republic of)'], 'Iran')
ihme_data = ihme_data.replace(['Republic of Moldova'], 'Moldova')
ihme_data = ihme_data.replace(['Russian Federation'], 'Russia')
ihme_data = ihme_data.replace(['Republic of Korea'], 'South Korea')
ihme_data = ihme_data.replace(['Syrian Arab Republic'], 'Syria')
ihme_data = ihme_data.replace(['Taiwan (Province of China)'], 'Taiwan')
ihme_data = ihme_data.replace(['Syrian Arab Republic'], 'Syria')
ihme_data = ihme_data.replace(['Timor-Leste'], 'Timor')
ihme_data = ihme_data.replace(['United States of America'], 'United States')
ihme_data = ihme_data.replace(['Venezuela (Bolivarian Republic of)'], 'Venezuela')
ihme_data = ihme_data.replace(['Viet Nam'], 'Vietnam')
ihme_data = ihme_data.replace(['Global'], 'World')

ihme_locations = ihme_data['location_name'].unique()

diff = np.setdiff1d(countries, ihme_locations, assume_unique=True)
print('Difference:')
print(diff)

print('IHME Locs:')
print(np.sort(ihme_locations))

ihme_data.to_csv('E:/Universidad/Investigación/Coronavirus/Datos/IHME/ihme_data_20_a_22_fixed.csv')

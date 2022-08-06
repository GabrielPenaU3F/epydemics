import pandas as pd

owid_full_data = pd.read_csv(
    'E:/Universidad/Investigación/Coronavirus/Python/epydemics/resources/data/owid_dataset.csv')
# For cases
# data = pd.read_csv(
#     'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_v2.csv')

# For deaths
data = pd.read_csv(
    'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_muertos_v2.csv',
    encoding='utf-7')


locs_owid = owid_full_data.keys().tolist()
locs_to_delete = ['Unnamed: 0', 'location', 'date', 'new_cases', 'new_deaths']
new_cols = list(sorted(set(locs_owid) - set(locs_to_delete), key=locs_owid.index))
for newcol in new_cols:
    data[newcol] = None

for index in data.index:
    for col in new_cols:
        location = data['location'].iloc[index]
        date = data['peak_date'].iloc[index]
        owid_col = owid_full_data[col]
        data[col].iat[index] = owid_col[
            (owid_full_data['location'] == location) &
            (owid_full_data['date'] == date)
        ].values[0]
    print(index)

# For cases
# data.to_csv(
# 'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_v3.csv')

# For deaths
data.to_csv(
    'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_muertos_v3.csv',
    sep=',', encoding='utf-8', index=False)

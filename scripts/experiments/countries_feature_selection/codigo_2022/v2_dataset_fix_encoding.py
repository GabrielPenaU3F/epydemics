import pandas as pd

# For cases
# df = pd.read_csv(
#     'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_v2.csv')

# For deaths
df = pd.read_csv(
     'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_muertos_v2.csv')

# Re-save

# For cases
# df.to_csv(
# 'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_v2.csv')

# For deaths
df.to_csv(
    'E:/Universidad/Investigación/Coronavirus/Picos/Todos los picos de todos los países/all_peaks_muertos_v2.csv',
    sep=',', encoding='utf-8', index=False)

import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_daily_data_and_filtered_curve
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

location = 'Argentina'
dataset = 'total_cases'
end = 638
n = 7
L = 7

arg_data = DataManager.get_raw_daily_data(location, dataset=dataset, start=1, end=end)
arg_cumdata = [0] + np.cumsum(arg_data)

arg_filtered = apply_ma_filter(arg_data, n, L)
filtered_cumdata = [0] + np.cumsum(arg_filtered)
x = np.arange(1, 1 + len(filtered_cumdata))

fig, axes = plt.subplots(figsize=(12, 8))

axes.plot(x, arg_cumdata, color='red', label='Sin filtrar')
axes.plot(x, filtered_cumdata, color='blue', label='Filtrada')
# diff = [arg_cumdata[i] - filtered_cumdata[i] for i in range(len(filtered_cumdata))]
# diff_rel = [(arg_cumdata[i] - filtered_cumdata[i]) / arg_cumdata[i] for i in range(len(filtered_cumdata))]
# print('Diferencia relativa máxima: ' + str(np.max(diff_rel)))
# axes.plot(x, diff, color='red', label='Diferencia absoluta')
# axes.plot(x, diff_rel, color='blue', label='Diferencia relativa')
axes.legend(prop={'size': 18})
plt.show()

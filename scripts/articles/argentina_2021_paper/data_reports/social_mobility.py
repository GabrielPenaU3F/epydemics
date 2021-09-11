import numpy as np
import pandas
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import apply_ma_filter
from src.data_io.plot_manager import PlotManager


filepath = 'E:/Universidad/Investigación/Coronavirus/Datos/movilidad_arg.csv'
filepath_ihme = 'E:/Universidad/Investigación/Coronavirus/Datos/movilidad_arg_ihme.csv'
data = pandas.read_csv(filepath)

# Set the indexes starting from 1 and prepare for printing
pandas.set_option("display.max_rows", None, "display.max_columns", None)

# print(data)
# March 03, 2020 corresponds to index 17 of this dataset
# July 29, 2021 corresponds to index 531 of this dataset

rows = data.iloc[17: 531]
x = np.arange(1, len(rows) + 1)
fig, axes = plt.subplots(figsize=(12, 8))

# axes.plot(x, rows['retail_and_recreation'], color='#ED02B6', linewidth=1, label='Mobility percent')
# axes.plot(x, rows['grocery_and_pharmacy'], color='#ED02B6', linewidth=1, label='Mobility percent')
# axes.plot(x, rows['parks'], color='#ED02B6', linewidth=1, label='Mobility percent')
# axes.plot(x, rows['transit_stations'], color='#ED02B6', linewidth=1, label='Mobility percent')
# axes.plot(x, rows['workplaces'], color='#ED02B6', linewidth=1, label='Mobility percent')
# axes.plot(x, rows['residential'], color='#ED02B6', linewidth=1, label='Mobility percent')

# mob = np.array(rows['residential'])
# mob_filt = apply_ma_filter(mob, 7, 7)
# axes.plot(x, -mob, color='#ACADAC', linewidth=0.5, label='Mobility percent (noisy)')
# axes.plot(x, -mob_filt, color='#ED02B6', linewidth=1, label='Mobility percent')

data_ihme = pandas.read_csv(filepath_ihme)
mob_ihme = data_ihme['mobility']
x = np.arange(1, len(rows) + 1)
axes.plot(x, mob_ihme, color='#ED02B6', linewidth=2, label='Mobility percent')

pm = PlotManager()
pm.config_axis_plain_style(axes)
pm.config_plot_background(axes)
axes.tick_params(axis='both', which='major', labelsize=24)
axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
axes.set_ylabel('Percent relative to baseline', fontsize=32, labelpad=15)
axes.legend(loc='upper right', prop={'size': 32})

fig.tight_layout()
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_mobility_ihme.pdf'
fig.savefig(filename)
plt.show()

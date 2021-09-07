import numpy as np
import pandas
from matplotlib import pyplot as plt

from src.data_io.plot_manager import PlotManager

filepath_1 = 'E:/Universidad/Investigación/Coronavirus/Datos/Vacunación_Arg/covid_1raDosis_acumulado.csv'
filepath_2 = 'E:/Universidad/Investigación/Coronavirus/Datos/Vacunación_Arg/covid_2daDosis_acumulado_mod.csv'

data_1 = pandas.read_csv(filepath_1)
data_2 = pandas.read_csv(filepath_2)
vacs_1 = data_1['total_1ra_dosis_aplicadas_acumulado']
vacs_2 = data_2['total_2da_dosis_aplicadas_acumulado']

# December 29, 2020, the day the first vaccine was applied, corresponds to
# Day 302 with respect to March 03
x = np.arange(302, len(vacs_1) + 302)
fig, axes = plt.subplots(figsize=(12, 8))

axes.plot(x, vacs_1, color='#C0C0C0', linewidth=2, label='Number of first doses applied')
axes.plot(x, vacs_2, color='#EABE3F', linewidth=2, label='Number of second doses applied')

pm = PlotManager()
pm.config_axis_plain_style(axes)
pm.config_plot_background(axes)
axes.tick_params(axis='both', which='major', labelsize=24)
axes.set_xlabel('Time (days)', fontsize=32, labelpad=15)
axes.set_ylabel('Number of doses', fontsize=32, labelpad=15)
axes.legend(loc='upper left', prop={'size': 32})

fig.tight_layout()
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_vaccination.pdf'
fig.savefig(filename)
plt.show()

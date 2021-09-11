import numpy as np
import pandas

from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep
from scripts.articles.argentina_2021_paper.useful_functions import show_mtbi_vs_mobility_scatterplots, \
    show_correlation_coefficients

DataManager.load_dataset('owid')

filepath_ihme = 'E:/Universidad/Investigación/Coronavirus/Datos/movilidad_arg_ihme.csv'
country = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 426
end = 449

mtbis = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                          start_from=start_from, output=False, formula='approx_conditional')
scaled_mtbis = np.array(mtbis) * 0.5 * (10**6) - 40

data_ihme = pandas.read_csv(filepath_ihme)
# start + start_from - 2 because pandas indexes start from 0, while ours start from 1
mob_ihme = data_ihme['mobility'].iloc[start + start_from - 2: end].values

show_correlation_coefficients(mtbis, mob_ihme)
show_mtbi_vs_mobility_scatterplots(scaled_mtbis, mob_ihme, start + start_from - 1, legend_loc='lower left')

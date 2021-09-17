import pandas

from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep
from scripts.articles.argentina_2021_paper.useful_functions import show_mtbi_vs_mobility_scatterplot, \
    show_correlation_coefficients, apply_ma_filter

DataManager.load_dataset('owid')

filepath_ihme = 'E:/Universidad/Investigación/Coronavirus/Datos/movilidad_arg_ihme.csv'
country = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 281
end = 315

mtbis = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                          start_from=start_from, output=False, formula='approx_conditional')

data_ihme = pandas.read_csv(filepath_ihme)
# start + start_from - 2 because pandas indexes start from 0, while ours start from 1
mob_ihme = data_ihme['mobility'].iloc[start + start_from - 2: end].values

show_correlation_coefficients(mtbis, mob_ihme)
show_mtbi_vs_mobility_scatterplot(mtbis, mob_ihme, start + start_from - 1, legend_loc='upper right')

from src.data_manipulation.data_manager import DataManager
from scripts.articles.argentina_2021_paper.useful_functions import plot_mtbis
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

country = 'Chile'
dataset = 'total_cases'
start_from = 10
start = 447
end = 472
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ch_4w_initial_mtbi.pdf'
mtbi_legend = 'upper right'

mtbis = ep.calculate_mtbi(country, dataset=dataset, start=start, end=end,
                          start_from=start_from, output=False, formula='approx_conditional')
plot_mtbis(mtbis, 'sec', start + start_from - 1, mtbi_filename, mtbi_legend)
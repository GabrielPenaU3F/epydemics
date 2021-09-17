from src.data_manipulation.data_manager import DataManager
from scripts.articles.argentina_2021_paper.useful_functions import plot_indicators

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 30
start = 1
end = 229
mtbi_unit = 'sec'
rho_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_rho.pdf'
gpr_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_gamma_per_rho.pdf'
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_mtbi.pdf'
rho_legend = 'upper right'
gpr_legend = 'upper left'
mtbi_legend = 'upper right'

plot_indicators(country, dataset, start, end, start_from, mtbi_unit,
                rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend)

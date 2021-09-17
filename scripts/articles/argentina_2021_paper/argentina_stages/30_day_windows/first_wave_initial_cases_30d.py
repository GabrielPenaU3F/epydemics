from scripts.articles.argentina_2021_paper.useful_functions import plot_indicators_with_window
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')
country = 'Argentina'
dataset = 'total_cases'
window_len = 30
start_from = 30
start = 1
end = 229
mtbi_unit = 'sec'
rho_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_30d_rho.pdf'
gpr_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_30d_gamma_per_rho.pdf'
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_1w_initial_30d_mtbi.pdf'
rho_legend = 'upper left'
gpr_legend = 'upper right'
mtbi_legend = 'upper right'

plot_indicators_with_window(country, dataset, start, end, start_from, window_len, mtbi_unit,
                            rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend)


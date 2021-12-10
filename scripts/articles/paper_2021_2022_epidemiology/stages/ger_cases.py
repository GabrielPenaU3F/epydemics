from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_indicators_with_and_without_window
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

country = 'Germany'
dataset = 'total_cases'
start_from = 30
start = 523
end = 652
mtbi_unit = 'sec'
window_len = 30

rho_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ger_rho.pdf'
gpr_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ger_gamma_per_rho.pdf'
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ger_mtbi.pdf'

rho_legend = 'upper right'
gpr_legend = 'upper right'
mtbi_legend = 'upper right'

tick_interval = 20

plot_indicators_with_and_without_window(country, dataset, start, end, start_from, mtbi_unit, window_len, tick_interval,
                                        rho_filename, rho_legend, gpr_filename, gpr_legend, mtbi_filename, mtbi_legend)

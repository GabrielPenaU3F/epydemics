from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_indicators_with_and_without_window
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

country = 'United States'
dataset = 'total_cases'
start_from = 30
start = 344
end = 418
mtbi_unit = 'sec'
window_len = 30

rho_filename = None
gpr_filename = None
mtbi_filename = None

rho_legend = 'upper center'
gpr_legend = 'upper right'
mtbi_legend = 'upper left'

tick_interval = 15

plot_indicators_with_and_without_window(country, dataset, start, end, start_from, mtbi_unit, window_len, tick_interval,
                                        rho_filename, rho_legend, gpr_filename, gpr_legend, mtbi_filename, mtbi_legend)

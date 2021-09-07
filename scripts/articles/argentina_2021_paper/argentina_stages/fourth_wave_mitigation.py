from src.data_manipulation.data_manager import DataManager
from scripts.articles.argentina_2021_paper.useful_functions import plot_indicators

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 449
end = 514
rho_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_4w_mitigation_rho.pdf'
gpr_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_4w_mitigation_gamma_per_rho.pdf'
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_4w_mitigation_mtbi.pdf'
rho_legend = 'upper left'
gpr_legend = 'upper right'
mtbi_legend = 'upper left'

plot_indicators(country, dataset, start, end, start_from,
                rho_filename, gpr_filename, rho_legend, gpr_legend, mtbi_filename, mtbi_legend)

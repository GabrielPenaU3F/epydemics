from scripts.articles.argentina_2021_paper.useful_functions import plot_mtbi_inverse_vs_data
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 10
start = 449
end = 514
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_4w_mitigation_mtbi_inverse_vs_data.pdf'
mtbi_legend = 'upper right'

plot_mtbi_inverse_vs_data(country, dataset, start, end, start_from, mtbi_filename, mtbi_legend)

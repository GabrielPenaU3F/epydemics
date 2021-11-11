from scripts.articles.argentina_2021_paper.useful_functions import plot_mtbi_inverse_vs_data
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

# Minimums: [295 376]
# Maximums: [207 321 458]

country = 'Argentina'
dataset = 'total_deaths'
start_from = 10
start = 458
end = 509
mtbi_unit = 'day'
mtbi_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_deaths_3w_mitigation_mtbi_inverse_vs_data.pdf'
mtbi_legend = 'upper right'

plot_mtbi_inverse_vs_data(country, dataset, start, end, start_from,
                          mtbi_unit, mtbi_filename, mtbi_legend)

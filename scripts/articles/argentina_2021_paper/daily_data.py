from scripts.articles.argentina_2021_paper.useful_functions import plot_daily_data
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

dataset = 'total_cases'
ylabel = 'Daily confirmed cases'
ar_end = 514
br_end = 520
ar_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_daily_cases.pdf'
br_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/br_daily_cases.pdf'


arg_data = DataManager.get_raw_daily_data('Argentina', dataset=dataset, start=1, end=ar_end)
br_data = DataManager.get_raw_daily_data('Brazil', dataset=dataset, start=1, end=br_end)

plot_daily_data(arg_data, ylabel, filename=ar_filename)
plot_daily_data(br_data, ylabel, filename=br_filename)

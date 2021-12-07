from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_daily_data_and_filtered_curve
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

location = 'Germany'
dataset = 'total_cases'
ylabel = 'Daily number of cases'
end = 674
n = 18
L = 7
legend_loc = 'upper left'
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ger_daily_cases.pdf'


usa_data = DataManager.get_raw_daily_data(location, dataset=dataset, start=1, end=end, dates=True)

plot_daily_data_and_filtered_curve(usa_data, ylabel, filename, n, L, legend_loc)

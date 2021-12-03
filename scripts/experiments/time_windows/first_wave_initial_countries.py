from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

from scripts.articles.argentina_2021_paper.useful_functions import calculate_mtbis_with_window, plot_mtbis
from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')
country = 'Switzerland'
dataset = 'total_cases'
start_from = 30
start = 31
end = 97
mtbi_unit = 'sec'

daily_data = DataManager.get_raw_daily_data(country, dataset, start, end)
mtbes = ep.calculate_mtbi(daily_data, start_from, mtbi_unit)
plot_mtbis(mtbes, mtbi_unit, start + start_from - 1,
           filename=None, legend_loc='upper right', dataset='total_cases')

from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/'

DataManager.load_dataset('owid')

# Plots the daily cases curve from Argentina
epydemics.show_daily_data_curve('Argentina')

# Daily deaths curve can also be shown
# epydemics.show_daily_data_curve('Germany', dataset='total_deaths')

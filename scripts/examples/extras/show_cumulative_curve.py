from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/'

DataManager.load_dataset('owid')

# Plots the cumulative data curve from Germany
epydemics.show_cumulative_data_curve('Germany')

# Deaths curve can also be shown
epydemics.show_cumulative_data_curve('Germany', dataset='total_deaths')

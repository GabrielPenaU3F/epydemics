from src.data_io.data_manager import DataManager

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/'
from src.interface import epydemics

DataManager.load_dataset('owid_dataset.csv')

# Shows the list of countries
epydemics.show_available_locations()

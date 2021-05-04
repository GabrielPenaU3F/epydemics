from src.data_manipulation.data_manager import DataManager

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/'
from src.interface import epydemics

DataManager.load_dataset('owid')

# Shows the list of available locations
epydemics.show_available_locations()

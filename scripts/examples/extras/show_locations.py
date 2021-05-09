from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/'

DataManager.load_dataset('owid')

# Shows the list of available locations
epydemics.show_available_locations()

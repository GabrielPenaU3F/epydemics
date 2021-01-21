from src.data_io.data_manager import DataManager
from src.interface.data_displayer import show_available_countries

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/full_dataset.csv'
DataManager.load_dataset()

# You could also specify the relative path where your file is located:
# DataManager.load_dataset('../../resources/data/full_dataset.csv')

# Shows the list of countries
show_available_countries()

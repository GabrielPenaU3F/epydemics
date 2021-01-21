from pyepidemics_covid19 import initialize
from src.data_io.data_manager import DataManager
from src.interface.data_displayer import show_available_countries

# Reads the data from disk
DataManager.load_dataset('../../resources/data/full_dataset.csv')

# Shows the list of countries

show_available_countries()

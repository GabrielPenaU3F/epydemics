from src.data_io.data_manager import DataManager

# Reads the data from disk
# Currently using the default data path, which is: 'resources/data/full_dataset.csv'
from src.interface import pyepidemics_interface as pyepidemics

DataManager.load_dataset()

# You could also specify the relative path where your file is located:
# DataManager.load_dataset('../../resources/data/full_dataset.csv')

# Shows the list of countries
pyepidemics.show_available_countries()

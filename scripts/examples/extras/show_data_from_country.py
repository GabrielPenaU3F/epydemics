from src.data_io.data_manager import DataManager
from src.interface import pyepidemics_interface as pyepidemics


DataManager.load_dataset()

# Show the data from a given country
# pyepidemics.show_data_from_country('Argentina')

# Deaths dataset can also be shown
pyepidemics.show_data_from_country('Argentina', dataset='total_deaths')

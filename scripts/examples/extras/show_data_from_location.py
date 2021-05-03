from src.data_io.data_manager import DataManager
from src.interface import epydemics


DataManager.load_dataset('owid_dataset.csv')

# Show the data from a given location present in the dataset
# pyepidemics.show_data_from_location('Argentina')

# Deaths dataset can also be shown
epydemics.show_data_from_location('Argentina', dataset='total_deaths')

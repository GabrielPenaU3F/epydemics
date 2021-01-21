from src.data_io.data_manager import DataManager
from src.interface import data_displayer as ds


DataManager.load_dataset()

# Show the data from a given country

ds.show_data_from_country('Argentina')

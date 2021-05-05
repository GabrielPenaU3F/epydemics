from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid')

epydemics.calculate_mtbi('Argentina', plot_unit='min')

# TODO: implement minimum checking
# TODO: optimize

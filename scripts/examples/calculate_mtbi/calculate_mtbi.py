from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('mapache_arg')

epydemics.calculate_mtbi('Buenos Aires', plot_unit='min', start=350, formula='exact_conditional')

# TODO: optimize

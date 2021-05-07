from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid')
epydemics.calculate_mtbi('Argentina', end=300, formula='approx_conditional', plot_unit='sec')

# DataManager.load_dataset('mapache_arg')
# epydemics.calculate_mtbi('Córdoba', plot_unit='sec', end=250, formula='approx_conditional')

# TODO: optimize

from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# DataManager.load_dataset('owid')
# epydemics.calculate_mtbi('Argentina', start=370, formula='approx_conditional', plot_unit='sec')

DataManager.load_dataset('mapache_arg')
epydemics.calculate_mtbi('CABA', plot_unit='sec', start=370, formula='exact_conditional')

# TODO: optimize

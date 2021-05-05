from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid')

epydemics.calculate_mtbi('Argentina')

# TODO: implement unit conversion
# TODO: implement minimum checking
# TODO: optimize

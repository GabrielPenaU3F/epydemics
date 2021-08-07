from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

DataManager.load_dataset('owid')

epydemics.show_daily_data_spectrum('Argentina', xscale='freq')

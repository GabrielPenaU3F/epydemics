from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

DataManager.load_dataset('owid')

epydemics.fit_model('Argentina', model='veronica_s_shaped', end=270, x0=(0.01, 1, 200))


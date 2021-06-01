from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as ep

DataManager.load_dataset('owid')

ep.fit_model("United States", start=225, end=360)
ep.calculate_mtbi("United States", start=225, end=360, unit='day', formula='approx_conditional')
ep.calculate_mtbi("United States", start=225, end=360, unit='day', formula='exact_conditional')
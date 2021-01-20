from analyzers.contagion_fitter import ContagionFitter
from data_io.url_data_manager import URLDataManager
from plotter import Plotter

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'

manager = URLDataManager(url)

arg_data = manager.get_cases_from_country('Argentina')
arg_data.locf_nans()

fitter = ContagionFitter()
plotter = Plotter()

start_from = 29

mtbs = fitter.calculate_mtb(arg_data, start_from)
plotter.plot_mtb(arg_data, mtbs, start_from)

from analyzers.contagion_fitter import ContagionFitter
from data_io.url_data_manager import URLDataManager
from plotter import Plotter

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'

manager = URLDataManager(url)

arg_data = manager.get_cases_from_country('Argentina')
arg_data.locf_nans()

fitter = ContagionFitter()
plotter = Plotter()

a, b = fitter.fit(arg_data.get_days(), arg_data.get_values())

print("Parameters: ")
print("ρ = " + str(a))
print("γ/ρ = " + str(b))

plotter.plot_data_vs_prediction(arg_data, a, b)

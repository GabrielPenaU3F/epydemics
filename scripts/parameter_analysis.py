from analyzers.parameter_analyzer import ParameterAnalyzer
from data_io.url_data_manager import URLDataManager
from plotter import Plotter

url = 'https://covid.ourworldindata.org/data/ecdc/total_cases.csv'

manager = URLDataManager(url)

arg_data = manager.get_cases_from_country('Argentina')
arg_data.locf_nans()

start_from = 29

analyzer = ParameterAnalyzer()
a_params, b_params = analyzer.analyze_parameters_over_time(arg_data, start_from)

plotter = Plotter()
plotter.plot_parameters_over_time(arg_data, a_params, b_params, start_from)

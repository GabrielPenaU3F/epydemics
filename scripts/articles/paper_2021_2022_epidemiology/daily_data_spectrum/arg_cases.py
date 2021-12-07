import numpy as np

from scripts.articles.paper_2021_2022_epidemiology.useful_functions import plot_spectrum
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep

DataManager.load_dataset('owid')

location = 'Argentina'
dataset = 'total_cases'
end = 638
xscale = 'freq'
legend_loc = 'upper right'
filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_cases_spectrum.pdf'

arg_spectrum = np.abs(ep.show_daily_data_spectrum(location, dataset, start=1, end=end, output=False))

plot_spectrum(arg_spectrum, xscale, filename, legend_loc)

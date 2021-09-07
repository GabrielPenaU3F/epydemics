import numpy as np
from matplotlib import pyplot as plt

from scripts.articles.argentina_2021_paper.useful_functions import plot_spectrum
from src.data_io.plot_manager import PlotManager
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep



DataManager.load_dataset('owid')

ar_end = 514
br_end = 520
ar_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/ar_spectrum.pdf'
br_filename = 'E:/Universidad/Investigación/Coronavirus/Python/script_outputs/br_spectrum.pdf'

ar_spectrum = np.abs(ep.show_daily_data_spectrum('Argentina', end=ar_end, output=False))
br_spectrum = np.abs(ep.show_daily_data_spectrum('Brazil', end=br_end, output=False))

plot_spectrum(ar_spectrum, xscale='freq', filename=ar_filename)
plot_spectrum(br_spectrum, xscale='freq', filename=br_filename)

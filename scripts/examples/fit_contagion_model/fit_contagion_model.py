from src.data_io.data_manager import DataManager
from src.interface import pyepidemics_interface as pyepidemics

DataManager.load_dataset()

# This will fit the data from the indicated country, show the results via console and plot the lines
pyepidemics.fit_contagion_model('Argentina')

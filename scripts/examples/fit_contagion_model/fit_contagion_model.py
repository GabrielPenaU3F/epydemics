from src.data_io.data_manager import DataManager
from src.interface import pyepidemics_interface as pyepidemics

DataManager.load_dataset()

# Example 1: This will fit the data from the indicated country, show the results via console and plot the lines
# pyepidemics.fit_contagion_model('Argentina')

# Example 2: You can also fit the number of deaths
# pyepidemics.fit_contagion_model('Argentina', dataset='total_deaths')

# Example 3: The fit may start or end at any fixed day

pyepidemics.fit_contagion_model('Argentina', start=200)
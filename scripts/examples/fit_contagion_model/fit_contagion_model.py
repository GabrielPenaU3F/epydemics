from src.data_io.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset('owid_dataset.csv')

# Example 1: This will fit the data from the indicated country, show the results via console and plot the lines
epydemics.fit_contagion_model('Argentina')

# Example 2: You can also fit the number of deaths
# epydemics.fit_contagion_model('Argentina', dataset='total_deaths')

# Examples 3-5: The fit may start or end at any fixed day
# epydemics.fit_contagion_model('Argentina', end=200)
# epydemics.fit_contagion_model('Argentina', start=200)
# epydemics.fit_contagion_model('Argentina', start=200, end=300)

# You may want only the numbers or only the plots. This can be done too.
# Example 6: No plots, just the fit data via console.
# epydemics.fit_contagion_model('Argentina', plot=False)
# Example 7: No console output, just the plots.
# epydemics.fit_contagion_model('Argentina', output=False)


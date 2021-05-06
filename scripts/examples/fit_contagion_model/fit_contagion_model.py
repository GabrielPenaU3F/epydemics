from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

# Example 1: consider the Our World In Data dataset. First, we load it. The following lines do exactly the same:
# DataManager.load_dataset(source='owid', filename='owid_dataset.csv')
# DataManager.load_dataset('owid', 'owid_dataset.csv')
# DataManager.load_dataset(source='owid')
# DataManager.load_dataset('owid')
# DataManager.load_dataset()

# Example 1.1: This will fit the data from the indicated country, show the results via console and plot the lines
# epydemics.fit_contagion_model('Argentina')

# Example 1.2: You can also fit the number of deaths
# epydemics.fit_contagion_model('Argentina', dataset='total_deaths')

# Examples 1.3-5: The fit may start or end at any fixed day
# epydemics.fit_contagion_model('Argentina', end=200)
# epydemics.fit_contagion_model('Argentina', start=200)
# epydemics.fit_contagion_model('Argentina', start=200, end=300)

# You may want only the numbers or only the plots. This can be done too.
# Example 1.6: No plots, just the fit data via console.
# epydemics.fit_contagion_model('Argentina', plot=False)
# Example 1.7: No console output, just the plots.
# epydemics.fit_contagion_model('Argentina', output=False)

# Example 2: now consider the Mapache Dataset from Argentina. Load it:
DataManager.load_dataset('mapache_arg')

# Example 2.1: Fit the cases in CABA
epydemics.fit_contagion_model('Buenos Aires')

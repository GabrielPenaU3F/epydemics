from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# Example 1: consider the Our World In Data dataset. First, we load it. The following lines do exactly the same:
# DataManager.load_dataset(source='owid', filename='owid_dataset.csv')
# DataManager.load_dataset('owid', 'owid_dataset.csv')
# DataManager.load_dataset(source='owid')
DataManager.load_dataset('owid')
# DataManager.load_dataset()

# Example 1.1: This will fit_model the data from the indicated country, show the results via console and plot the lines
epydemics.fit_model('Argentina')

# Example 1.2: You can also fit_model the number of deaths
# epydemics.fit_model('Argentina', dataset='total_deaths')

# Examples 1.3-5: The fit_model may start or end at any fixed day
# epydemics.fit_model('Argentina', end=200)
# epydemics.fit_model('Argentina', start=200)
# epydemics.fit_model('Argentina', start=200, end=300)


# You may want to obtain the fit_model object, but not show the results. This can be done too.
# Example 1.6: No console output, just the plots.
# epydemics.fit_model('Argentina', output=False)

# Example 2: now consider the Mapache Dataset from Argentina. Load it:
# DataManager.load_dataset('mapache_arg')

# Example 2.1: Fit the cases in CABA
# epydemics.fit_model('CABA')

# Example 2.2: Fit the cases in CABA to the Goel-Okumoto model
# epydemics.fit_model('Córdoba', model='goel_okumoto', start=200, end=260, x0=(1, 0.01))

# Example 2.3: Fit the cases in Córdoba to teh Delayed S-Shaped model
# epydemics.fit_model('Córdoba', model='delayed_s_shaped', end=270, x0=(1000, 0.001))

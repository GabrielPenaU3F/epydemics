from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics

# Example 1: consider the Our World In Data dataset. First, we load it.
# DataManager.load_dataset('owid')

# Example 1.1: This will plot the model parameters versus time
# epydemics.analyze_model_parameters_over_time('Argentina')

# Example 1.2: You can also fit the number of deaths
# epydemics.analyze_model_parameters_over_time('Argentina', dataset='total_deaths')

# Examples 1.3-5: The fit may start or end at any fixed day
# epydemics.analyze_model_parameters_over_time('Argentina', end=200)
# epydemics.analyze_model_parameters_over_time('Argentina', start=200)
# epydemics.analyze_model_parameters_over_time('Argentina', start=200, end=300)

# Example 2: now consider the Mapache Dataset from Argentina. Load it:
DataManager.load_dataset('mapache_arg')

# Example 2.1: This will plot the model parameters versus time in Córdoba
epydemics.analyze_model_parameters_over_time('Córdoba')

from src.data_io.data_manager import DataManager
from src.interface import epydemics

DataManager.load_dataset()

# Example 1: This will plot the model parameters versus time
epydemics.analyze_model_parameters_over_time('Argentina')

# Example 2: You can also fit the number of deaths
# epydemics.fit_contagion_model('Argentina', dataset='total_deaths')

# Examples 3-5: The fit may start or end at any fixed day
# epydemics.fit_contagion_model('Argentina', end=200)
# epydemics.fit_contagion_model('Argentina', start=200)
# epydemics.fit_contagion_model('Argentina', start=200, end=300)

from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# Example 1: Consider the Our World In Data dataset. First, we load it.
DataManager.load_dataset('owid')

# Example 1.1: This will plot the fit residuals M(t) - r versus time
epydemics.show_fit_residuals('Argentina')

# Example 1.2: You can also see the absolute residuals
epydemics.show_fit_residuals('Argentina', type='abs')

# Example 1.3: You can also see the square residuals
epydemics.show_fit_residuals('Argentina', type='square')

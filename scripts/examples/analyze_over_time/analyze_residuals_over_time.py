from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics

# You might want to observe the behavior of the last residual when performing
# multiple fits over time.
# Example 1: Consider the Our World In Data dataset. First, we load it.
DataManager.load_dataset('owid')

# Example 1.1: This will plot the last residual M(t) - r versus time over a set of fits
# epydemics.analyze_last_residual_over_time('Argentina')

# Example 1.2: You can also see the absolute residuals
# epydemics.analyze_last_residual_over_time('Argentina', type='abs')

# Example 1.3: You can also see the square residuals
# epydemics.analyze_last_residual_over_time('Argentina', type='square')

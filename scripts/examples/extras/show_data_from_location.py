from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics


DataManager.load_dataset('owid')

# Show the data from a given location present in the dataset
epydemics.show_data_from_location('Peru')

# Deaths dataset can also be shown
# epydemics.show_data_from_location('Argentina', dataset='total_deaths')

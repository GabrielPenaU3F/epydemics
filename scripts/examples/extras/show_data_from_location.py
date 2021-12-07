from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics


DataManager.load_dataset('owid')

# Show the data from a given location present in the dataset
epydemics.show_data_from_location('Germany')

# Deaths dataset can also be shown
# epydemics.show_data_from_location('Argentina', dataset='total_deaths')

# Of course, other datasets are also availiable
# DataManager.load_dataset('mapache_arg')
# epydemics.show_data_from_location('Buenos Aires', dataset='nue_casosconf_diff')
# epydemics.show_data_from_location('Buenos Aires', dataset='nue_fallecidos_diff')


from src.data_manipulation.data_manager import DataManager

# This will retrieve the data from a source and save it in a csv file for further use. Default sources are
# Our World In Data ('owid')
# Sistemas Mapache Argentina ('mapache_arg')

# You can specify which data source you want to pull from. Default is None, which will update all the default sources.
# The filename may also be specified if needed
DataManager.update_data()
# DataManager.update_data(source='owid')
# DataManager.update_data(source='mapache_arg')
# DataManager.update_data(source='owid', filename='owid_dataset.csv')
# DataManager.update_data(source='mapache_arg', filename='mapache_arg_dataset.csv')

from src.data_io.data_manager import DataManager

# This will retrieve the data from a source and save it in a csv file for further use. Default source is
# Our World In Data ('owid')
# DataManager.update_data()

# You can specify which data source you want to pull from. Default is 'owid'. The filename may also be specified
DataManager.update_data(source='owid', filename='owid_dataset.csv')
DataManager.update_data(source='mapache_arg', filename='mapache_dataset.csv')

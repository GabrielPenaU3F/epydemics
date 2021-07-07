from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

# data = DataManager.get_raw_cumulative_data('Peru', end=180)
r = DataManager.get_single_datum('Argentina', 201)
print(r)
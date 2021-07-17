from src.data_manipulation.data_manager import DataManager

DataManager.load_dataset('owid')

r = DataManager.get_single_datum('Uruguay', 450)
print(r)
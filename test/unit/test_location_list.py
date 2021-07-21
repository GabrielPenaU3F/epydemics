import unittest

from src.data_manipulation.data_manager import DataManager


class LocationListTests(unittest.TestCase):

    def test_starwars_location_list_is_correct(self):
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')
        starwars_locations = ['Coruscant', 'Tatooine', 'Nar Shaddaa']
        actual_locations = list(DataManager.get_location_list())
        self.assertCountEqual(starwars_locations, actual_locations)


if __name__ == '__main__':
    unittest.main()

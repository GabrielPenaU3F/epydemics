import unittest

import numpy as np
from numpy import testing

from src.data_manipulation.data_manager import DataManager


class GetRawDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_get_raw_cumulative_data_end_5(self):
        expected = np.array([52, 204, 213, 384, 389])
        raw_data = DataManager.get_raw_cumulative_data('Tatooine', end=5)
        testing.assert_array_equal(raw_data, expected)

    def test_get_raw_cumulative_data_start_5_end_10(self):
        expected = np.array([389, 562, 669, 768, 930, 1087])
        raw_data = DataManager.get_raw_cumulative_data('Tatooine', start=5, end=10)
        testing.assert_array_equal(raw_data, expected)

    def test_get_raw_cumulative_data_start_65(self):
        expected = np.array([6622, 6625, 6746, 6844, 6853, 6899])
        raw_data = DataManager.get_raw_cumulative_data('Tatooine', start=65)
        testing.assert_array_equal(raw_data, expected)

    def test_get_raw_incidence_data_end_5(self):
        expected = np.array([52, 152, 9, 171, 5])
        raw_data = DataManager.get_raw_daily_data('Tatooine', end=5)
        testing.assert_array_equal(raw_data, expected)

    def test_get_raw_incidence_data_start_5_end_10(self):
        expected = np.array([5, 173, 107, 99, 162, 157])
        raw_data = DataManager.get_raw_daily_data('Tatooine', start=5, end=10)
        testing.assert_array_equal(raw_data, expected)

    def test_get_raw_incidence_data_start_65(self):
        expected = np.array([25, 3, 121, 98, 9, 46])
        raw_data = DataManager.get_raw_daily_data('Tatooine', start=65)
        testing.assert_array_equal(raw_data, expected)

    def test_get_datum_1(self):
        expected = 99
        datum = DataManager.get_single_datum('Nar Shaddaa', 1, dataset='custom_data')
        self.assertEqual(expected, datum)
    def test_get_datum_10(self):
        expected = 1027
        datum = DataManager.get_single_datum('Nar Shaddaa', 10, dataset='custom_data')
        self.assertEqual(expected, datum)

    def test_get_single_datum_when_start_is_1(self):
        expected = 1024
        datum = DataManager.get_single_datum('Coruscant', 8, dataset='custom_data', start=1)
        self.assertEqual(expected, datum)

    def test_get_single_datum_when_start_is_not_1(self):
        expected = 959
        datum = DataManager.get_single_datum('Coruscant', 8, dataset='custom_data', start=4)
        self.assertEqual(expected, datum)


if __name__ == '__main__':
    unittest.main()

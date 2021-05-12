import unittest

import numpy as np
from numpy import testing

from src.data_manipulation.data_manager import DataManager


class GetRawDataTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('owid')

    def test_get_raw_cumulative_data_end_5(self):
        expected = np.array([1, 1, 1, 2, 8])
        raw_data = DataManager.get_raw_cumulative_data('Argentina', end=5)
        testing.assert_array_equal(expected, raw_data)

    def test_get_raw_cumulative_data_start_5_end_10(self):
        expected = np.array([8, 12, 12, 17, 19, 19])
        raw_data = DataManager.get_raw_cumulative_data('Argentina', start=5, end=10)
        testing.assert_array_equal(expected, raw_data)

    def test_get_raw_incidence_data_end_5(self):
        expected = np.array([1, 0, 0, 1, 6])
        raw_data = DataManager.get_raw_incidence_data('Argentina', end=5)
        testing.assert_array_equal(expected, raw_data)

    def test_get_raw_incidence_data_start_5_end_10(self):
        expected = np.array([6, 4, 0, 5, 2, 0])
        raw_data = DataManager.get_raw_incidence_data('Argentina', start=5, end=10)
        testing.assert_array_equal(expected, raw_data)


if __name__ == '__main__':
    unittest.main()

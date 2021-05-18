import unittest

import numpy as np
from numpy import testing

from src.data_manipulation.data_manager import DataManager
from src.exceptions.exceptions import InvalidArgumentException


class GetFittableLocationDataTests(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_cases_from_first_5_days_from_nar_shaddaa(self):
        expected = [99, 148, 242, 323, 499]
        df = DataManager.get_fittable_location_data('Nar Shaddaa', end=5)
        self.assertListEqual(df['custom_data'].to_list(), expected)

    def test_dates_from_first_5_days_from_nara_shaddaa(self):
        expected = ['2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07']
        df = DataManager.get_fittable_location_data('Nar Shaddaa', end=5)
        self.assertListEqual(df['custom_date'].to_list(), expected)

    # Remember: the cumulative values at start-1 are substracted from all these values,
    def test_cases_from_days_3_to_7_from_nar_shaddaa(self):
        expected = np.array([242, 323, 499, 545, 608]) - 148
        df = DataManager.get_fittable_location_data('Nar Shaddaa', start=3, end=7)
        testing.assert_array_equal(np.array(df['custom_data'].to_list()), expected)

    def test_dates_from_days_3_to_7_from_nar_shaddaa(self):
        expected = ['2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09']
        df = DataManager.get_fittable_location_data('Nar Shaddaa', start=3, end=7)
        self.assertListEqual(df['custom_date'].to_list(), expected)

    def test_cases_from_last_5_days_from_nar_shaddaa(self):
        expected = np.array([4944, 4954, 5154, 5281, 5310]) - 4747
        df = DataManager.get_fittable_location_data('Nar Shaddaa', start=46)
        testing.assert_array_equal(df['custom_data'].to_list(), expected)

    def test_location_not_on_list(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_fittable_location_data('Argentina')
        self.assertEqual(error.exception.strerror, 'The requested location was not found')

    def test_start_cannot_exceed_dataset_length(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_fittable_location_data('Nar Shaddaa', start=1000)
        self.assertEqual(error.exception.strerror, 'Start argument cannot exceed dataset length')

    def test_end_cannot_exceed_dataset_length(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_fittable_location_data('Nar Shaddaa', end=1000)
        self.assertEqual(error.exception.strerror, 'End argument cannot exceed dataset length')

    def test_start_cannot_exceed_end(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_fittable_location_data('Nar Shaddaa', start=20, end=10)
        self.assertEqual(error.exception.strerror, 'Start argument cannot exceed end argument')


if __name__ == '__main__':
    unittest.main()

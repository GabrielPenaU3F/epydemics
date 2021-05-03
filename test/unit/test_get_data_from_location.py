import unittest

from src.data_manipulation.data_manager import DataManager
from src.exceptions.exceptions import InvalidArgumentException


class GetDataFromLocationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset()

    def test_cases_from_first_5_days_from_argentina(self):
        expected = [1, 1, 1, 2, 8]
        df = DataManager.get_location_data('Argentina', end=5)
        self.assertListEqual(expected, df['total_cases'].to_list())

    def test_deaths_from_first_5_days_from_argentina(self):
        expected = [1, 1, 1, 1, 1]
        df = DataManager.get_location_data('Argentina', end=5, dataset='total_deaths')
        self.assertListEqual(expected, df['total_deaths'].to_list())

    def test_dates_from_first_5_days_from_argentina(self):
        expected = ['2020-03-03', '2020-03-04', '2020-03-05', '2020-03-06', '2020-03-07']
        df = DataManager.get_location_data('Argentina', end=5)
        self.assertListEqual(expected, df['date'].to_list())

    # Remember: the cumulative values at start-1 are substracted from all these values,
    # so we get [0,1,7,11,11] instead of [1,2,8,12,12]
    def test_cases_from_days_3_to_7_from_argentina(self):
        expected = [0, 1, 7, 11, 11]
        df = DataManager.get_location_data('Argentina', start=3, end=7)
        self.assertListEqual(expected, df['total_cases'].to_list())

    def test_dates_from_days_3_to_7_from_argentina(self):
        expected = ['2020-03-05', '2020-03-06', '2020-03-07', '2020-03-08', '2020-03-09']
        df = DataManager.get_location_data('Argentina', start=3, end=7)
        self.assertListEqual(expected, df['date'].to_list())

    def test_country_not_on_list(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_location_data('Coruscant')
        self.assertEqual(error.exception.strerror, 'The requested country is not on the list')

    def test_start_cannot_exceed_dataset_length(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_location_data('Argentina', start=1000, end=7)
        self.assertEqual(error.exception.strerror, 'Start and end arguments cannot exceed dataset length')

    def test_end_cannot_exceed_dataset_length(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_location_data('Argentina', end=1000)
        self.assertEqual(error.exception.strerror, 'Start and end arguments cannot exceed dataset length')

    def test_dataset_cannot_be_different_from_cases_or_deaths(self):
        with self.assertRaises(InvalidArgumentException) as error:
            DataManager.get_location_data('Argentina', dataset='new_cases')
        self.assertEqual(error.exception.strerror, 'Supported datasets are total_cases and total_deaths only')



if __name__ == '__main__':
    unittest.main()

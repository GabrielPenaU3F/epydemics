import unittest

from src.data_io.data_manager import DataManager


class GetDataFromCountryTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset()

    def test_cases_from_first_5_days_from_argentina(self):
        expected = [1, 1, 1, 2, 8]
        df = DataManager.get_country_data('Argentina', end=5)
        self.assertListEqual(expected, df['total_cases'].to_list())

    def test_deaths_from_first_5_days_from_argentina(self):
        expected = [1, 1, 1, 1, 1]
        df = DataManager.get_country_data('Argentina', end=5, dataset='total_deaths')
        self.assertListEqual(expected, df['total_deaths'].to_list())

    def test_dates_from_first_5_days_from_argentina(self):
        expected = ['2020-03-03', '2020-03-04', '2020-03-05', '2020-03-06', '2020-03-07']
        df = DataManager.get_country_data('Argentina', end=5)
        self.assertListEqual(expected, df['date'].to_list())

    # Remember: the cumulative values at start-1 are substracted from all these values,
    # so we get [0,1,7,11,11] instead of [1,2,8,12,12]
    def test_cases_from_days_3_to_7_from_argentina(self):
        expected = [0, 1, 7, 11, 11]
        df = DataManager.get_country_data('Argentina', start=3, end=7)
        self.assertListEqual(expected, df['total_cases'].to_list())

    def test_dates_from_days_3_to_7_from_argentina(self):
        expected = ['2020-03-05', '2020-03-06', '2020-03-07', '2020-03-08', '2020-03-09']
        df = DataManager.get_country_data('Argentina', start=3, end=7)
        self.assertListEqual(expected, df['date'].to_list())


if __name__ == '__main__':
    unittest.main()
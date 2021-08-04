import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as ep
from src.exceptions.exceptions import InvalidArgumentException


class FitResidualsStarwarsTest(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')
        cls.fit = ep.fit_model('Tatooine', output=False)

    def test_first_10_residuals_true(self):
        '''
        data = self.__class__.fit_model.get_y_data()
        mean_values = np.rint(self.__class__.fit_model.get_explained_data())
        expected_residuals = [mean_values[i] - data[i] for i in range(10)]
        print(expected_residuals)
        '''
        expected_residuals = np.array([97, 77, 193, 144, 257, 201, 209, 223, 173, 127])
        residuals = ep.show_fit_residuals('Tatooine', output=False, type='true')[0:10]
        testing.assert_array_equal(residuals, expected_residuals)

    def test_residuals_5_to_15_abs(self):
        '''
        data = self.__class__.fit_model.get_y_data()
        mean_values = np.rint(self.__class__.fit_model.get_explained_data())
        expected_residuals = [mean_values[i] - data[i] for i in range(4, 14)]
        print(expected_residuals)
        '''
        expected_residuals = np.array([257, 201, 209, 223, 173, 127, 93, 18, 30, 46])
        residuals = ep.show_fit_residuals('Tatooine', output=False, type='abs')[4:14]
        testing.assert_array_equal(residuals, expected_residuals)

    def test_residuals_30_to_40_square(self):
        '''
        data = self.__class__.fit_model.get_y_data()
        mean_values = np.rint(self.__class__.fit_model.get_explained_data())
        expected_residuals = [(mean_values[i] - data[i])**2 for i in range(29, 39)]
        print(expected_residuals)
        '''
        expected_residuals = np.array([1936, 17424, 11664, 1369, 1600, 8649, 25600, 12100, 13456, 2116])
        residuals = ep.show_fit_residuals('Tatooine', output=False, type='square')[29:39]
        testing.assert_array_equal(residuals, expected_residuals)

    def test_invalid_type_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ep.show_fit_residuals('Tatooine', output=False, type='cube')
        self.assertEqual(error.exception.strerror, 'The residual type is invalid')


if __name__ == '__main__':
    unittest.main()

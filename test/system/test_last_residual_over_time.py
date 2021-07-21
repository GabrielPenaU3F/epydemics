import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as ep
from src.domain.fitter import Fitter
from src.domain.models.model import ContagionModel
from src.exceptions.exceptions import InvalidArgumentException


class LastResidualOverTimeStarwarsTest(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_10_residuals_over_time_starting_from_30_true(self):

        '''
        data = DataManager.get_raw_cumulative_data('Tatooine')[29:39]
        params_over_time = Fitter.fit_parameters_over_time('Tatooine', 'custom_data', 1, None, 30, (1, 0.5))[0:9]
        model = ContagionModel()
        t = np.arange(30, 39)
        mean_values = np.rint([model.mean_value_function(t[i], params_over_time[i][0], params_over_time[i][1])
                               for i in range(len(params_over_time))])
        expected_residuals = [mean_values[i] - data[i] for i in range(len(mean_values))]
        print(expected_residuals)
        '''

        expected_residuals = np.array([23, -43, -5, 67, 66, 21, -28, 29, 32])
        residuals = ep.analyze_last_residual_over_time('Tatooine', output=False, type='true')[0:9]
        testing.assert_array_equal(residuals, expected_residuals)

    def test_invalid_type_must_raise_exception(self):
        with self.assertRaises(InvalidArgumentException) as error:
            ep.analyze_last_residual_over_time('Tatooine', output=False, type='cube')
        self.assertEqual(error.exception.strerror, 'The residual type is invalid')


if __name__ == '__main__':
    unittest.main()

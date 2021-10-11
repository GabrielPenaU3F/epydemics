import unittest

import numpy as np
from numpy import testing

from src.data_manipulation.data_manager import DataManager
from src.domain.predictor import Predictor
from src.interface import epydemics as ep


class PredictorsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_mtbi_linear_regression_coefficients(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        expected_coefs = np.array([1259.8800, 0.3651, -0.1396, -0.7508])
        actual_coefs, score = Predictor().linear_regression(mtbis, 5, 3)
        testing.assert_array_almost_equal(actual_coefs, expected_coefs, decimal=4)


if __name__ == '__main__':
    unittest.main()

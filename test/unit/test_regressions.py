import unittest

import numpy as np
from numpy import testing

from src.data_manipulation.data_manager import DataManager
from src.domain.regression_manager import RegressionManager
from src.interface import epydemics as ep


class RegressionsTests(unittest.TestCase):

    regression_manager = None

    @classmethod
    def setUpClass(cls):
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')
        cls.regression_manager = RegressionManager()

    def test_mtbi_linear_regression_coefficients(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        expected_coefs = np.array([1259.8800, 0.3651, -0.1396, -0.7508])
        actual_coefs, score = self.__class__.regression_manager.linear_regression(mtbis, 5, 3)
        testing.assert_array_almost_equal(actual_coefs, expected_coefs, decimal=4)

    def test_mtbi_linear_regression_prediction(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        mtbis_test = mtbis[0:30]
        reg = self.__class__.regression_manager.linear_regression(mtbis_test, 5, 3, output='full')
        testing.assert_almost_equal(reg.predict(), 838.6780, decimal=4)

    def test_mtbi_lasso_regression_coefficients(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        expected_coefs = np.array([1244.4663, 0.2251, 0, -0.7317])
        actual_coefs, score = self.__class__.regression_manager.lasso_regression(mtbis, 5, 3, alpha=0.2)
        testing.assert_array_almost_equal(actual_coefs, expected_coefs, decimal=4)

    def test_mtbi_lasso_regression_prediction(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        mtbis_test = mtbis[0:30]
        reg = self.__class__.regression_manager.lasso_regression(mtbis_test, 5, 3, alpha=0.2, output='full')
        testing.assert_almost_equal(reg.predict(), 838.7207, decimal=4)

    def test_mtbi_ridge_regression_coefficients(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        expected_coefs = np.array([1251.4475, 0.3610, -0.1354, -0.7406])
        actual_coefs, score = self.__class__.regression_manager.ridge_regression(mtbis, 5, 3, alpha=0.2)
        testing.assert_array_almost_equal(actual_coefs, expected_coefs, decimal=4)

    def test_mtbi_ridge_regression_prediction(self):
        mtbis = ep.calculate_mtbi('Coruscant', unit='sec', output=False)
        mtbis_test = mtbis[0:30]
        reg = self.__class__.regression_manager.ridge_regression(mtbis_test, 5, 3, alpha=0.2, output='full')
        testing.assert_almost_equal(reg.predict(), 838.6769, decimal=4)


if __name__ == '__main__':
    unittest.main()

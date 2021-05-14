import unittest

from numpy import testing

from src.data_manipulation.data_manager import DataManager
from src.domain.fitter import Fitter


class AnalyzeParametersOverTimeOWIDTests(unittest.TestCase):

    arg_until_40 = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset()
        cls.arg_until_40 = Fitter.perform_range_fits('Argentina', 'total_cases', 1, 40, 30, fit_x0=(0.1, 1))

    def test_arg_until_40_parameters_over_time_rhos(self):
        param_tuples = self.__class__.arg_until_40
        expected_rhos = [0.180, 0.207, 0.226, 0.231, 0.262, 0.292, 0.328, 0.364, 0.405, 0.428, 0.474]
        rhos = [param_tuples[i][0] for i in range(len(param_tuples))]
        testing.assert_array_almost_equal(expected_rhos, rhos, decimal=3)

    def test_arg_until_40_parameters_over_time_gamma_by_rhos(self):
        param_tuples = self.__class__.arg_until_40
        expected_gamma_by_rhos = [4.605, 4.270, 4.080, 4.032, 3.787, 3.596, 3.414, 3.257, 3.116, 3.044, 2.922]
        gamma_by_rhos = [param_tuples[i][1] for i in range(len(param_tuples))]
        testing.assert_array_almost_equal(expected_gamma_by_rhos, gamma_by_rhos, decimal=3)


if __name__ == '__main__':
    unittest.main()

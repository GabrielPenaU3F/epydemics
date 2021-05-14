import unittest

from numpy import testing

from src.data_manipulation.data_manager import DataManager
from src.domain.fitter import Fitter


class AnalyzeParametersOverTimeMapacheTests(unittest.TestCase):

    baires_until_40 = None

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('mapache_arg')
        cls.baires_until_40 = Fitter.perform_range_fits('Buenos Aires', '', 1, 40, 30, fit_x0=(0.1, 1))

    def test_baires_until_200_parameters_over_time_rhos(self):
        param_tuples = self.__class__.baires_until_40
        expected_rhos = [0.760, 0.807, 0.864, 0.901, 0.937, 0.972, 0.956, 0.914, 0.894, 0.886, 0.889]
        rhos = [param_tuples[i][0] for i in range(len(param_tuples))]
        testing.assert_array_almost_equal(expected_rhos, rhos, decimal=3)

    def test_baires_until_40_parameters_over_time_gamma_per_rhos(self):
        param_tuples = self.__class__.baires_until_40
        expected_gamma_per_rhos = [2.200, 2.149, 2.093, 2.060, 2.031, 2.004, 2.016, 2.048, 2.064, 2.071, 2.068]
        gamma_per_rhos = [param_tuples[i][1] for i in range(len(param_tuples))]
        testing.assert_array_almost_equal(expected_gamma_per_rhos, gamma_per_rhos, decimal=3)


if __name__ == '__main__':
    unittest.main()

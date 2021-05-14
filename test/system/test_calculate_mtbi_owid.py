import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
from src.domain.fitter import Fitter


class CalculateMTBIOWIDTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('owid')

    def test_mtbi_owid_arg_exact(self):
        expected_mtbis_seg = np.array([633, 640, 610, 551, 595, 594, 607, 615, 625, 594, 630])
        mtbis_seg = np.round(86400 * np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                                     start=1, end=40, start_from=30, fit_x0=(0.1, 1),
                                                                     formula='exact_conditional')))
        testing.assert_array_equal(expected_mtbis_seg, mtbis_seg)

    def test_mtbi_owid_arg_approx(self):
        expected_mtbis_day = np.array([0.0069, 0.0069, 0.0067, 0.0063, 0.0064,
                                       0.0064, 0.0065, 0.0066, 0.0067, 0.0066, 0.0067])
        mtbis_day = np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                    start=1, end=40, start_from=30, fit_x0=(0.1, 1),
                                                    formula='approx_conditional'))
        testing.assert_array_almost_equal(expected_mtbis_day, mtbis_day, decimal=4)

    def test_mtbi_owid_arg_50_days_from_30(self):
        expected_mtbis_day = np.array([0.0069, 0.0069, 0.0067, 0.0063, 0.0064,
                                       0.0064, 0.0065, 0.0066, 0.0067, 0.0066, 0.0067,
                                       0.0067, 0.0067, 0.0068, 0.0067, 0.0067, 0.0066,
                                       0.0066, 0.0067, 0.0067, 0.0067])
        mtbis = np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                start=1, end=50, start_from=30, fit_x0=(0.1, 1),
                                                formula='approx_conditional'))
        testing.assert_array_almost_equal(expected_mtbis_day, mtbis, decimal=4)

    def test_mtbi_owid_arg_50_days_from_40(self):
        expected_mtbis = np.array([0.0067, 0.0067, 0.0067, 0.0068, 0.0067,
                                   0.0067, 0.0067, 0.0066, 0.0067, 0.0067, 0.0067])
        mtbis = np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                start=1, end=50, start_from=40, fit_x0=(0.1, 1),
                                                formula='approx_conditional'))
        testing.assert_array_almost_equal(expected_mtbis, mtbis, decimal=4)


if __name__ == '__main__':
    unittest.main()

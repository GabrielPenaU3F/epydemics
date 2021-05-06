import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
from src.fitters.fitter import Fitter


class CalculateMTBIOWIDTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('owid')

    def test_mtbi_owid_arg(self):
        expected_mtbis_seg = np.array([633, 640, 610, 551, 595, 594, 607, 615, 625, 594, 630])
        mtbis_seg = np.round(86400 * np.array(Fitter.calculate_mtbis(
            'Argentina', dataset='total_cases', start=1, end=40, start_from=30, fit_x0=(0.1, 1))))
        testing.assert_array_equal(expected_mtbis_seg, mtbis_seg)


if __name__ == '__main__':
    unittest.main()

import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics


class CalculateMTBIStarwarsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_mtbi_coruscant_day_1_to_40_specifying_only_end(self):
        expected_mtbis = np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                   0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', end=40,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_1_to_40_specifying_start_and_end(self):
        expected_mtbis = np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                   0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=1, end=40,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_1_to_40_from_30_specifying_end_and_start_from(self):
        expected_mtbis = np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                   0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start_from=30, end=40,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_1_to_40_from_30_specifying_everything(self):
        expected_mtbis = np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                   0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=1, end=40, start_from=30,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_20_to_60_specifying_start_and_end(self):
        expected_mtbis = np.array([0.0103, 0.0100, 0.0099, 0.0098, 0.0096, 0.0095,
                                   0.0094, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=20, end=60,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_20_to_60_from_30_specifying_everything(self):
        expected_mtbis = np.array([0.0103, 0.0100, 0.0099, 0.0098, 0.0096, 0.0095,
                                   0.0094, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=20, end=60, start_from=30,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_20_to_60_from_35_specifying_everything(self):
        expected_mtbis = np.array([0.0095, 0.0094, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=20, end=60, start_from=35,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_30_to_the_end_specifying_only_start(self):
        expected_mtbis = np.array([0.0074, 0.0074, 0.0075, 0.0075, 0.0076, 0.0078,
                                   0.0079, 0.0080, 0.0082, 0.0083, 0.0084])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=30, formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_30_to_the_end_from_30_specifying_start_and_start_from(self):
        expected_mtbis = np.array([0.0074, 0.0074, 0.0075, 0.0075, 0.0076, 0.0078,
                                   0.0079, 0.0080, 0.0082, 0.0083, 0.0084])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=30, start_from=30,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)

    def test_mtbi_coruscant_day_30_to_the_end_from_35_specifying_start_and_start_from(self):
        expected_mtbis = np.array([0.0078, 0.0079, 0.0080, 0.0082, 0.0083, 0.0084])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', start=30, start_from=35,
                                                  formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)


if __name__ == '__main__':
    unittest.main()

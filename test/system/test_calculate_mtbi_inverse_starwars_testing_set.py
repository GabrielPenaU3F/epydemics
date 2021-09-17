import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as ep


class CalculateMTBIInverseStarwarsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_mtbi_inverses_coruscant_from_1_to_40_starting_from_30(self):
        expected_inverses = np.power(np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                               0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Coruscant', end=40, mtbi_unit='day', fit_x0=(0.1, 1),
                                                           formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.01)

    def test_mtbi_inverses_coruscant_day_20_to_60(self):
        expected_inverses = np.power(np.array([0.0103, 0.0100, 0.0099, 0.0098, 0.0096, 0.0095,
                                               0.0094, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Coruscant', start=20, end=60, mtbi_unit='day',
                                                           fit_x0=(0.1, 1), formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.01)

    def test_mtbi_inverses_coruscant_day_20_to_60_from_35(self):
        expected_inverses = np.power(np.array([0.0095, 0.0094, 0.0092, 0.0091, 0.0090, 0.0089, 0.0088]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Coruscant', start=20, end=60, start_from=35,
                                                           mtbi_unit='day', formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.01)

    def test_mtbi_inverses_coruscant_day_30_to_the_end(self):
        expected_inverses = np.power(np.array([0.0074, 0.0074, 0.0075, 0.0075, 0.0076, 0.0078,
                                               0.0079, 0.0080, 0.0082, 0.0083, 0.0084]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Coruscant', start=30, mtbi_unit='day',
                                                           formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.01)

    def test_mtbi_inverses_coruscant_day_30_to_the_end_from_35(self):
        expected_inverses = np.power(np.array([0.0078, 0.0079, 0.0080, 0.0082, 0.0083, 0.0084]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Coruscant', start=30, start_from=35, mtbi_unit='day',
                                                           formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.01)


if __name__ == '__main__':
    unittest.main()

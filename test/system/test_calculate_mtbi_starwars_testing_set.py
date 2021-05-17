import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as epydemics


class CalculateMTBIStarwarsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset(source='custom', filename='starwars_test_data.csv')

    def test_mtbi_coruscant_day_1_to_40_from_30_specifying_only_end(self):
        expected_mtbis = np.array([0.0107, 0.0106, 0.0106, 0.0106, 0.0107,
                                   0.0109, 0.0110, 0.0111, 0.0112, 0.0114, 0.0115])
        mtbis = np.array(epydemics.calculate_mtbi('Coruscant', end=40, formula='approx_conditional', output=False))
        testing.assert_array_almost_equal(mtbis, expected_mtbis, decimal=4)


if __name__ == '__main__':
    unittest.main()

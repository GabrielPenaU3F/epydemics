import unittest
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal

from src.data_io.data_manager import DataManager


class SliceDataTests(unittest.TestCase):

    test_df = None

    @classmethod
    def setUpClass(cls) -> None:
        ones = np.ones(4, dtype=np.int64)
        matrix = np.array([ones, 2*ones, 3*ones, 4*ones])
        cls.test_df = pd.DataFrame(matrix)

    # The input indexes run from 1 instead of 0 (i.e., the slice data function works as in R)

    def test_obtain_rows_0_and_1_asking_for_rows_1_to_2(self):
        expected = pd.DataFrame([[1, 1, 1, 1], [2, 2, 2, 2]])
        expected.set_index(np.array([1, 2]), inplace=True, drop=True)
        rows_0_and_1 = DataManager.slice_data_by_index(self.__class__.test_df, 1, 2)
        assert_frame_equal(expected, rows_0_and_1)

    def test_obtain_rows_1_to_3_asking_for_rows_2_to_4(self):
        expected = pd.DataFrame([[2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
        expected.set_index(np.array([1, 2, 3]), inplace=True, drop=True)
        rows_1_to_3 = DataManager.slice_data_by_index(self.__class__.test_df, 2, 4)
        assert_frame_equal(expected, rows_1_to_3)


if __name__ == '__main__':
    unittest.main()

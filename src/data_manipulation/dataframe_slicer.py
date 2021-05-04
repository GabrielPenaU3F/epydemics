import numpy as np


class DataframeSlicer:

    @classmethod
    def slice_rows_by_index(cls, data, start, end):
        sliced_data = data.iloc[start-1:end, :]
        correct_index = np.arange(1, len(sliced_data) + 1)
        sliced_data.set_index(correct_index, inplace=True, drop=True)
        return sliced_data

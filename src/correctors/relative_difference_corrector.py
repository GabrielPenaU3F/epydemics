# Must not be applied when data has lots of holes (NAs), or must be fixed
import numpy as np


class RelativeDifferenceCorrector:

    # Constant days must be >= 2
    def __init__(self, constant_days, constant_tolerance, jump_tolerance):
        self.constant_days = constant_days
        self.constant_tolerance = constant_tolerance
        self.jump_tolerance = jump_tolerance

    # Data must be corrected if two conditions are met:
    #   1) A series of constant_days with values under constant_tolerance is found
    #   2) Following it, a jump exceeding jump_tolerance is found

    def correct_data(self, values):
        for i in range(self.constant_days, len(values) - len(values) % self.constant_days, self.constant_days):
            condition_1 = self.check_condition_1(values[i - self.constant_days: i - 1])
            condition_2 = self.check_condition_2(values[i - 1], values[i])
            if condition_1 and condition_2:
                self.apply_correction(values, i)
        return values

    def check_reldiff_tolerance(self, val1, val2, tol):
        return np.abs(val1 - val2) / min(val1, val2) < tol

    def apply_correction(self, values, jump_index):
        initial_index = jump_index - self.constant_days
        # Linear interpolation
        yf = int(values[jump_index])
        yi = int(values[initial_index])
        m = (yf - yi) / self.constant_days
        for k in range(initial_index + 1, jump_index):
            values[k] = int(yi + m * (k - initial_index))

    def check_condition_1(self, sublist):
        for j in range(1, len(sublist)):
            if not self.check_reldiff_tolerance(sublist[j], sublist[j - 1], self.constant_tolerance):
                return False
        return True

    def check_condition_2(self, val1, val2):
        if not self.check_reldiff_tolerance(val1, val2, self.jump_tolerance):
            return True
        else:
            return False

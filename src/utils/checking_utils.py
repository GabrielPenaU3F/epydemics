import numpy as np


def check_if_minimum_was_reached(array):
    return np.argmin(array) < len(array) - 1

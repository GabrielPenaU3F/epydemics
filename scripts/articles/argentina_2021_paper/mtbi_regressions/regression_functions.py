import numpy as np


def exponential_function(t, A, b, K):
    return A * np.exp(b * t) + K

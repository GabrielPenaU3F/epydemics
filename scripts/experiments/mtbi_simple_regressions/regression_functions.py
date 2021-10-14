import numpy as np


def exponential_function(t, A, b, c):
    return A * np.exp(-b * (t - c))


def poly_function(t, *params):
    length = len(params)
    poly = 0
    for i in range(length):
        poly += params[i] * (t ** i)
    return poly

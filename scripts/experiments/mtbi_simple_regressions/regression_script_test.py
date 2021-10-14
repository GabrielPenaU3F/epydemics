import numpy as np
from scipy import optimize as opt

from scripts.experiments.mtbi_simple_regressions.regression_functions import poly_function

np.random.seed(123)

x = np.linspace(0, 1, 100)
y = 2 * (x**2) - x + 1

params, cov = opt.curve_fit(poly_function, x, y, method='lm', p0=(1.5, -1.2, 0.5))
print(params)

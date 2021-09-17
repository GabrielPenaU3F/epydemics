import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy import optimize as opt

from scripts.articles.argentina_2021_paper.mtbi_regressions.regression_functions import exponential_function
from scripts.articles.argentina_2021_paper.useful_functions import show_mtbi_curve_regression
from src.data_manipulation.data_manager import DataManager
from src.interface import epydemics as ep


DataManager.load_dataset('owid')

country = 'Argentina'
dataset = 'total_cases'
start_from = 30
start = 1
end = 229

mtbis = np.array(ep.calculate_mtbi(country, dataset=dataset, start=start, end=end, unit='sec',
                 start_from=start_from, output=False, formula='approx_conditional'))
t = np.arange(start + start_from - 1, start + start_from - 1 + len(mtbis))

# params, cov = opt.curve_fit(exponential_function, t, mtbis, method='lm')
# explained = exponential_function(t, *params)

deg = 4
poly_coefs = Polynomial.fit(t, mtbis, deg).convert().coef
explained = np.polyval(poly_coefs, t)

show_mtbi_curve_regression(mtbis, explained, start + start_from - 1)

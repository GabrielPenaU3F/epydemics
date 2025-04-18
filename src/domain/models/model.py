from abc import ABC, abstractmethod
from scipy.integrate import quad
from scipy.optimize import differential_evolution

import numpy as np
import scipy.optimize as opt


class Model(ABC):

    def __init__(self, **kwargs):
        self.bounds = None
        self.pretrain_bounds = None

    def fit(self, x, y, x0):
        # params, cov = opt.curve_fit(self.mean_value_function, x, y, p0=x0, method='lm')
        lower, upper = zip(*self.bounds)
        bounds = (np.array(lower), np.array(upper))
        result = opt.least_squares(
            lambda params: self.mean_value_function(x, *params) - y,
            x0,
            method='trf',
            bounds=bounds,
            max_nfev=2000  # podés aumentar el límite de evaluaciones
        )
        return result.x  # devuelve el mejor vector encontrado, converja o no

    def pretrain(self, x, y):

        def residuals(params):
            y_pred = self.mean_value_function(x, *params)
            return y - y_pred

        de_result = differential_evolution(
            lambda p: np.sum(residuals(p) ** 2),
            self.pretrain_bounds,
            maxiter=100,
            popsize=5,
            tol=1e-3,
            polish=False
        )
        return de_result.x

    @abstractmethod
    def mean_value_function(self, x, *params):
        pass


class ContagionModel(Model):

    def mean_value_function(self, x, *params):
        rho, gamma_per_rho = params
        return ((1 + rho * x) ** gamma_per_rho - 1) / gamma_per_rho


class GoelOkumotoModel(Model):

    def mean_value_function(self, x, *params):
        a, b = params
        return a * (1 - np.exp(-b * x))


class DelayedSShapedModel(Model):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pretrain_bounds = [(0.0, 100), (0.0, 1.0)]
        self.bounds = [(0, np.inf), (0, np.inf)]

    def mean_value_function(self, x, *params):
        a, b = params
        return a * (1 - (1 + b * x) * np.exp(-b * x))


class VeronicaSShapedModel(Model):

    def mean_value_function(self, x, *params):
        m, b, t_0 = params
        c = (-2 + np.sqrt(4 + 8 * m * t_0)) / (4 * t_0)
        F_t = (-1 / c) * (1 / (1 + c * x) - 1)
        return (b / m) * (np.exp(m * F_t) - 1)

class PenaSigmoidModel(Model):

    def __init__(self):
        super().__init__()
        self.pretrain_bounds = [(0, 2), (0, 10000), (-1, 1000)]
        self.bounds = [(0, np.inf), (0, np.inf), (-np.inf, np.inf)]

    # def fit(self, x, y, x0):
    #     params, cov = opt.curve_fit(self.mean_value_function, x, y, p0=x0, method='trf',
    #                                 bounds=(0, np.inf))
    #     return params

    def mean_value_function(self, x, *params):
        beta = 1
        m = 0
        gamma, l, M = params
        return (beta/gamma) * (np.exp(gamma * self.Kappa(x, m, l, gamma, M)) - 1)

    def rho(self, x, m, l, c, M):
        return M - (M - m) * ((M - c) / (M - m)) ** (x / l)

    def kappa(self, x, m, l, c, M):
        rho = self.rho(x, m, l, c, M)
        return 1 / (1 + rho * x)

    def Kappa(self, x, m, l, c, M):
        integrand = lambda x: self.kappa(x, m, l, c, M)
        if np.isscalar(x):
            return quad(integrand, 0, x)[0]
        else:
            Kx = np.zeros_like(x, dtype=float)
            for i, ti in enumerate(x):
                Kx[i] = quad(integrand, 0, ti)[0]
            return Kx

from abc import ABC, abstractmethod

import numpy as np
import scipy.optimize as opt


class Model(ABC):

    def fit(self, x, y, x0):
        params, cov = opt.curve_fit(self.mean_value_function, x, y, p0=x0, method='lm')
        return params

    @abstractmethod
    def mean_value_function(self, x, *params):
        pass


class ContagionModel(Model):

    def mean_value_function(self, x, *params):
        a, b = params
        return ((1 + a * x)**b - 1)/b


class GoelOkumotoModel(Model):

    def mean_value_function(self, x, *params):
        a, b = params
        return a * (1 - np.exp(-b * x))


class DelayedSShapedModel(Model):

    def mean_value_function(self, x, *params):
        a, b = params
        return a * (1 - (1 + b * x) * np.exp(-b * x))


class VeronicaSShapedModel(Model):

    def mean_value_function(self, x, *params):
        m, b, t_0 = params
        c = (-2 + np.sqrt(4 + 8 * m * t_0)) / (4 * t_0)
        F_t = (-1 / c) * (1 / (1 + c * x) - 1)
        return (b / m) * (np.exp(m * F_t) - 1)

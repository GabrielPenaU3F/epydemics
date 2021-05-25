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
        a = params[0]
        b = params[1]
        return ((1 + a * x)**b - 1)/b


class GoelOkumotoModel(Model):

    def mean_value_function(self, x, *params):
        a = params[0]
        b = params[1]
        return a * (1 - np.exp(-b * x))


class DelayedSShapedModel(Model):

    def mean_value_function(self, x, *params):
        a = params[0]
        b = params[1]
        return a * (1 - (1 + b * x) * np.exp(-b * x))

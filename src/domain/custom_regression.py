from abc import ABC, abstractmethod

import numpy as np


class CustomRegression:

    type = None
    regression = None
    data = None
    score = None
    regression_vars = None
    response_var = None

    def __init__(self, type, reg, data, X, y):
        self.type = type
        self.regression = reg
        self.data = data
        self.regression_vars = X
        self.response_var = y
        self.score = reg.score(X, y)

    def predict(self):
        K = self.regression_vars.shape[1]
        data = np.flip(self.data)
        x = data[0: K].reshape(1, -1)
        return self.regression.predict(x)[0]

    def get_regression_object(self):
        return self.regression

    def get_data(self):
        return self.data

    def get_r2_score(self):
        return self.score

    def get_regression_vars(self):
        return self.regression_vars

    def get_response_var(self):
        return self.response_var

    def get_coefficients(self):
        coefs = self.regression.coef_
        intercept = self.regression.intercept_
        return np.insert(coefs, 0, intercept)

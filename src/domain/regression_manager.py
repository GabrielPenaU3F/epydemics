import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge

from src.domain.custom_regression import CustomRegression


class RegressionManager:

    # m is the number of data to consider, i.e., the number of rows in the Y matrix
    # K is the order of the filter, i.e., K + 1 is the number of coefficients
    def linear_regression(self, data, m, K, output='coef'):
        X, y = self.build_regression_matrices(data, m, K)
        lreg = LinearRegression().fit(X, y)
        return self.do_regression('linear', lreg, data, X, y, output)

    def do_regression(self, type, reg, data, X, y, output):
        if output == 'full':
            return CustomRegression(type, reg, data, X, y)
        elif output == 'coef':
            coefs = np.concatenate((np.array([reg.intercept_]), reg.coef_))
            score = reg.score(X, y)
            return coefs, score

    def lasso_regression(self, data, m, K, alpha, output='coef'):
        X, y = self.build_regression_matrices(data, m, K)
        lasreg = Lasso(alpha).fit(X, y)
        return self.do_regression('lasso', lasreg, data, X, y, output)

    def ridge_regression(self, data, m, K, alpha, output='coef'):
        X, y = self.build_regression_matrices(data, m, K)
        rreg = Ridge(alpha).fit(X, y)
        return self.do_regression('ridge', rreg, data, X, y, output)

    def build_regression_matrices(self, data, m, K):
        data_flip = np.flip(data)
        X = np.empty(shape=(m, K))
        for i in range(m):
            row = data_flip[1 + i:1 + i + K]
            X[i] = row
        y = data_flip[0:m]
        return X, y

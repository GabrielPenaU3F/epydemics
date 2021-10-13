import numpy as np
from sklearn.linear_model import LinearRegression

from src.domain.custom_regression import CustomLinearRegression


class RegressionManager:

    def linear_regression(self, data, m, K, output='coef'):
        # m is the number of data to consider, i.e., the number of rows in the Y matrix
        # K is the order of the filter, i.e., K + 1 is the number of coefficients
        X, y = self.build_regression_matrices(data, m, K)

        lreg = LinearRegression().fit(X, y)

        if output == 'full':
            return CustomLinearRegression(lreg, data, X, y)
        elif output == 'coef':
            coefs = np.concatenate((np.array([lreg.intercept_]), lreg.coef_))
            score = lreg.score(X, y)
            return coefs, score

    def build_regression_matrices(self, data, m, K):
        data_flip = np.flip(data)
        X = np.empty(shape=(m, K))
        for i in range(m):
            row = data_flip[1 + i:1 + i + K]
            X[i] = row
        y = data_flip[0:m]
        return X, y

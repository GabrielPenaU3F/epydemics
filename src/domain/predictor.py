import numpy as np
from sklearn.linear_model import LinearRegression


class Predictor():

    def linear_regression(self, data, m, K):
        # m is the number of data to consider, i.e., the number of rows in the Y matrix
        # K is the order of the filter, i.e., K + 1 is the number of coefficients
        mtbis_flip = np.flip(data)
        K = 3
        m = 5
        X = np.empty(shape=(m, K))
        for i in range(m):
            row = mtbis_flip[1 + i:1 + i + K]
            X[i] = row
        y = mtbis_flip[0:m]

        lreg = LinearRegression().fit(X, y)
        coefs = np.concatenate((np.array([lreg.intercept_]), lreg.coef_))
        score = lreg.score(X, y)
        return coefs, score

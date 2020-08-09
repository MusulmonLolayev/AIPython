from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

import numpy as np

class KnnOptimalRegression(BaseEstimator, RegressorMixin):
    def __init__(self, metric='euclidean'):
        self.metric = metric

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)

        self._X = X
        self._y = y

        return self

    def predict(self, X):

        # Input validation
        X = check_array(X)

        res = [self.predict_by_optimal_k(X[i]) for i in range(X.shape[0])]

        return res

    def predict_by_optimal_k(self, x):

        m = self._X.shape[0]

        dists = [np.sqrt(np.sum(np.square(x - self._X[i]))) for i in range(m)]

        dist_args = np.argsort(dists)

        f_min = None

        s = 0
        for k in range(m // 2):
            s += self._y[dist_args[k]]
            y = s / (k + 1)
            f = np.sum(np.square(self._y - y))
            if f_min == None or f_min > f:
                f_min = f
                y_opt = y

        return y_opt
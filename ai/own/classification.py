import numpy as np
import time
from scipy.spatial import distance
from sklearn.base import ClassifierMixin, BaseEstimator
from sklearn.metrics import euclidean_distances
from sklearn.utils import check_array, check_X_y
from sklearn.utils.multiclass import unique_labels
from sklearn.utils.validation import check_is_fitted
from sklearn import linear_model
from sklearn import svm
from sklearn.neighbors import KNeighborsRegressor

from ai.own.estimations import DivideIntervals
from ai.own.functions import GeneralValues, GeneralCriterion2D
from usingpackages.ctypesapi.cml import find_standard, find_noisy
from sklearn.neural_network import MLPRegressor

class NearestNeighborClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, metric='euclidean'):

        self.metric = metric

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X_ = X
        self.y_ = y

        self.find_standard()
        self.computingDistances()

        return self

    def computingDistances(self):
        # Computing distances for standard objects
        self.ro = np.zeros(shape=(self.X_.shape[0]))
        for i in range(self.X_.shape[0]):
            if self.standard[i]:
                for j in range(self.X_.shape[0]):
                    if i != j and self.y_[i] != self.y_[j]:
                        dis = distance.pdist(self.X_[[i, j]], metric=self.metric)
                        if self.ro[i] == 0 or dis < self.ro[i]:
                            self.ro[i] = dis


    def find_standard(self):
        # Calling find_standart
        self.standard = find_standard(self.X_, self.y_)

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        for i in range(X.shape[0]):
            m = 1e36
            k = -1
            for j in range(self.X_.shape[0]):
                if self.standard[j]:
                    _X = np.array([X[i], self.X_[j]]);
                    dis = distance.pdist(_X, metric=self.metric)
                    #dis *= 1.0 / self.ro[j]
                    if dis < m:
                        m = dis
                        k = j
            closest[i] = k

        return self.y_[closest]

class NearestNeighborClassifier_(BaseEstimator, ClassifierMixin):
    def __init__(self, metric='euclidean', noisy = False):

        self.metric = metric
        self.Is_noisy = noisy

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X_ = X
        self.y_ = y

        self.computingDistances()

        if self.Is_noisy:
            self.noisy = find_noisy(X, y, metric=self.metric)

        return self

    def computingDistances(self):
        # Computing distances for standard objects
        self.ro = np.zeros(shape=(self.X_.shape[0]))
        for i in range(self.X_.shape[0]):
            self.ro[i] = np.min(euclidean_distances(self.X_[i].reshape(1, -1),
                                                        self.X_[self.y_ != self.y_[i]]))

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        for i in range(X.shape[0]):
            m = 1e36
            k = -1
            for j in range(self.X_.shape[0]):
                if not self.Is_noisy or self.Is_noisy and not self.noisy[j]:
                    _X = np.array([X[i], self.X_[j]]);
                    dis = distance.pdist(_X, metric=self.metric)
                    dis *= 1.0 / self.ro[j]
                    if dis < m:
                        m = dis
                        k = j
            closest[i] = k

        return self.y_[closest]

class TemplateClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, metric='euclidean', noisy = False):

        self.metric = metric
        self.Is_noisy = noisy

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X_ = X
        self.y_ = y

        if self.Is_noisy:
            self.noisy = find_noisy(X, y, metric=self.metric)

        # Return the classifier
        return self

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        for i in range(X.shape[0]):
            m = 1e36
            k = -1
            for j in range(self.X_.shape[0]):
                if not self.Is_noisy or self.Is_noisy and not self.noisy[j]:
                    d = np.min(euclidean_distances(X[i].reshape(1, -1), self.X_[j].reshape(1, -1)))
                    if d < m:
                        m = d
                        k = j
            closest[i] = k

        return self.y_[closest]

class RegressionClassifier(BaseEstimator, ClassifierMixin):

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X = X
        self.y = y

        self._y = GeneralValues(X, y)

        _, ln = np.unique(self.y, return_counts=True)
        self.divided = GeneralCriterion2D(self._y, self.y, ln=ln)

        print(self.divided)

        d = [0, 0]

        m = None
        n = 0

        for i in range(self.y.shape[0]):
            if self._y[i] <= self._y[self.divided[2]]:
                d[self.y[i]] += 1

            q = self._y[i] - self._y[self.divided[2]]
            if m is None or q > 0 and m > q:
                m = q
                n = self._y[i]

        self.border = (self._y[self.divided[2]] + n) / 2

        nyu = d / ln

        f = nyu[0] / nyu.sum()

        if f > 0.5:
            self.check = [0, 1]
        else:
            self.check = [1, 0]

        #self.reg = linear_model.Ridge(alpha=.01)
        #self.reg = linear_model.LinearRegression()
        #self.reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
        #self.reg = linear_model.Lasso(alpha=0.0001)
        #self.reg = linear_model.LassoLars(alpha=.0001)
        #self.reg = linear_model.BayesianRidge()
        #self.reg = linear_model.LogisticRegression()
        #self.reg = linear_model.PassiveAggressiveRegressor(max_iter=1000, random_state=0, tol=1e-10)
        #self.reg = linear_model.SGDRegressor(loss='squared_epsilon_insensitive')
        #self.reg = svm.SVR()
        #self.reg = KNeighborsRegressor(n_neighbors=2 * min(ln) - 3)
        self.reg = KNeighborsRegressor(n_neighbors=self._y.shape[0] / 2)
        #self.reg = MLPRegressor()

        self.reg.fit(self.X, self._y)

        # Return the classifier
        return self

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        res = self.reg.predict(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        for i in range(X.shape[0]):
            c = 0
            if self.border < res[i]:
                c = 1
            closest[i] = self.check[c]

        return closest

class EstimationClassifier(BaseEstimator, ClassifierMixin):

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X = X
        self.y = y

        self.GeneralValues()

        _, ln = np.unique(self.y, return_counts=True)
        self.divided = GeneralCriterion2D(self._y, self.y, ln=ln)

        d = [0, 0]

        m = None
        n = 0

        for i in range(self.y.shape[0]):
            if self._y[i] <= self._y[self.divided[2]]:
                d[self.y[i]] += 1

            q = self._y[i] - self._y[self.divided[2]]
            if m is None or q > 0 and m > q:
                m = q
                n = self._y[i]

        self.border = (self._y[self.divided[2]] + n) / 2

        nyu = d / ln

        f = nyu[0] / nyu.sum()

        if f > 0.5:
            self.check = [0, 1]
        else:
            self.check = [1, 0]

        # Return the classifier
        return self

    def GeneralValues(self):

        self._X = np.empty(shape=self.X.shape, dtype=int)
        self._y = np.empty(shape=self.y.shape)

        self.ests = np.empty(self.X.shape[1])

        self.group_index = []
        self.group_estimation = []
        self.interval = []

        for i in range(self.X.shape[1]):
            from ai.own.estimations import DivideIntervals
            group_index, group_estimation, interval = \
                DivideIntervals(self.X[:, i], self.y, return_intervals=True)

            self.group_index.append(group_index)
            self.group_estimation.append(group_estimation)
            self.interval.append(interval)

            self._X[group_estimation >= 0.5, i] = 0
            self._X[group_estimation < 0.5, i] = 1

            from ai.own.estimations import EstimationNominalFeture
            self.ests[i] = EstimationNominalFeture(self._X[:, i], self.y)

        unique, ln = np.unique(self.y, return_counts=True)

        for i in range(self._X.shape[0]):
            s = 0
            for j in range(self._X.shape[1]):
                d = len(self._X[np.logical_and(self.y == 0, self._X[:, j] == self._X[i, j]), j]) / ln[0] - \
                    len(self._X[np.logical_and(self.y == 1, self._X[:, j] == self._X[i, j]), j]) / ln[1]
                s += self.ests[j] * d

            self._y[i] = s

    def Modify(self, intervals, k):
        res = []
        for i in range(len(intervals)):
            _min = self.X[intervals[i][3], k]
            l = i
            for j in range(i, len(intervals)):
                if _min > self.X[intervals[j][3], k]:
                    _min = self.X[intervals[j][3], k]
                    l = j

            helper = intervals[l].copy()
            intervals[l] = intervals[i].copy()
            intervals[i] = helper

            item = [self.X[intervals[i][3], k], self.X[intervals[i][4], k], intervals[i][2]]
            res.append(item)

        res[-1][1] = 1

        for i in range(len(res) - 1):
            res[i][1] = (res[i][1] + res[i + 1][0]) / 2
            res[i + 1][0] = res[i][1]

        return res

    def Compute(self, x):
        _x = np.empty(shape=x.shape)
        for i in range(x.shape[0]):
            res = self.Modify(self.interval[i], i)
            for item in res:
                if item[0] <= x[i] and x[i] <= item[1]:
                    _x[i] = item[2]
                    break
        _x[_x > .5] = 1
        _x[_x <= .5] = 0

        unique, ln = np.unique(self.y, return_counts=True)

        s = 0
        for j in range(_x.shape[0]):
            d = len(self._X[np.logical_and(self.y == 0, self._X[:, j] == _x[j]), j]) / ln[0] - \
                len(self._X[np.logical_and(self.y == 1, self._X[:, j] == _x[j]), j]) / ln[1]
            s += self.ests[j] * d

        return s

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        for i in range(X.shape[0]):
            c = 0
            res = self.Compute(X[i])
            print(res)
            if self.border > res:
                c = 1
            closest[i] = self.check[c]

        return closest

class RegressionClassifier1(BaseEstimator, ClassifierMixin):

    def Modify(self, intervals):
        res = np.empty(shape=(len(intervals), 3))
        for i in range(len(intervals)):
            _min = self._y[intervals[i][3]]
            l = i
            for j in range(i, len(intervals)):
                if _min > self._y[intervals[j][3]]:
                    _min = self._y[intervals[j][3]]
                    l = j

            helper = intervals[l].copy()
            intervals[l] = intervals[i].copy()
            intervals[i] = helper

            res[i][0] = self._y[intervals[i][3]]
            res[i][1] = self._y[intervals[i][4]]
            res[i][2] = intervals[i][2]

        for i in range(len(res) - 1):
            res[i][1] = (res[i][1] + res[i + 1][0]) / 2
            res[i + 1][0] = res[i][1]

        return res

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X = X
        self.y = y

        self._y = GeneralValues(X, y)

        """
        _, ln = np.unique(self.y, return_counts=True)

        #self.divided = GeneralCriterion2D(self._y, self.y, ln=ln)
        #print(self.divided)

        _, _, self.intervals = DivideIntervals(self._y, self.y, return_intervals=True)

        self.groups = self.Modify(self.intervals)

        print(self.groups)

        s = 0
        for item in self.intervals:
            print(item)
            if item[2] > 0.5:
                s += item[2] * (item[1] - item[0] + 1)
            else:
                s += (1 - item[2]) * (item[1] - item[0] + 1)

        s = s / self.y.shape[0]

        print('s = ', s)

        self.check = np.zeros(shape=(self.groups.shape[0]))
        self.check[self.groups[:, 2] < .5] = 1
        print(self.check)
        """

        #self.reg = linear_model.Ridge(alpha=.01)
        #self.reg = linear_model.LinearRegression()
        #self.reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
        #self.reg = linear_model.Lasso(alpha=0.0001)
        #self.reg = linear_model.LassoLars(alpha=.0001)
        #self.reg = linear_model.BayesianRidge()
        #self.reg = linear_model.LogisticRegression()
        #self.reg = linear_model.PassiveAggressiveRegressor(max_iter=1000, random_state=0, tol=1e-10)
        #self.reg = linear_model.SGDRegressor(loss='squared_epsilon_insensitive')
        #self.reg = svm.SVR()
        #self.reg = KNeighborsRegressor(n_neighbors=2 * min(ln) - 3)
        self.reg = KNeighborsRegressor(n_neighbors=1)
        #self.reg = MLPRegressor()

        self.reg.fit(self.X, self._y)

        # Return the classifier
        return self

    def predict(self, X):
        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        res = self.reg.predict(X)

        closest = np.empty(shape=(X.shape[0]), dtype=int)

        """
        for i in range(X.shape[0]):

            if res[i] < self.groups[0][1]:
                closest[i] = self.check[0]
            elif res[i] >= self.groups[-1][0]:
                closest[i] = self.check[-1]
            else:
                for j in range(1, self.groups.shape[0] - 1):
                    if self.groups[j][0] <= res[i] and res[i] < self.groups[j][1]:
                        closest[i] = self.check[j]
        """

        for i in range(X.shape[0]):
            closest[i] = self.y[np.argmin(np.abs(res[i] - self._y))]

        return closest
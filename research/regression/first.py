import numpy as np
from sklearn.preprocessing import minmax_scale
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split

from datamining.own.classification import RegressionClassifier, EstimationClassifier
from datamining.own.estimations import DivideIntervals, EstimationNominalFeture
from datamining.own.functions import GeneralValues


def main():
    data = np.loadtxt("Regres_m_Just_scales.dat")
    y = data[:, data.shape[1] - 1].astype(int)
    X = data[:, 0 : data.shape[1] - 1]

    minmax_scale(X, copy=False)

    """rc = RegressionClassifier()
    rc.fit(X, y)
    print(rc.score(X, y))"""


    nnc = EstimationClassifier()
    nn = MLPClassifier()
    svm = SVC()

    """nnc.fit(X, y)
    print(nnc.score(X, y))
    return 0"""

    k = 10
    mean1 = 0
    mean2 = 0
    mean3 = 0
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=None, shuffle=True)

        nnc.fit(X_train, y_train)
        svm.fit(X_train, y_train)
        nn.fit(X_train, y_train)

        mean1 += nnc.score(X_test, y_test)
        mean2 += svm.score(X_test, y_test)
        mean3 += nn.score(X_test, y_test)

    mean1 /= k
    mean2 /= k
    mean3 /= k

    print(mean1, mean2, mean3)

if __name__ == '__main__':
    main()
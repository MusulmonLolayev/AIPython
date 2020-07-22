import numpy as np
from sklearn.preprocessing import minmax_scale
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split

from datamining.own.classification import RegressionClassifier, EstimationClassifier, RegressionClassifier1
from datamining.own.estimations import DivideIntervals, EstimationNominalFeture
from datamining.own.functions import GeneralValues
from projects.magdiss_fris1.func.methods import ToFormNumpy


def main():
    path = r"D:\tanlanmalar\Spame.txt"

    X, types, y = ToFormNumpy(path)

    minmax_scale(X, copy=False)

    """rc = RegressionClassifier()
    rc.fit(X, y)
    print(rc.score(X, y))"""


    nnc = RegressionClassifier()
    nn = MLPClassifier()
    svm = SVC()

    """nnc.fit(X, y)
    print(nnc.score(X, y))
    return 0"""

    k = 2
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
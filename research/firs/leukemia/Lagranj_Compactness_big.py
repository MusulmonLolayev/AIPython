import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from usingpackages.ctypesapi.cml import find_noisy, compactness
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from uz.nuu.datamining.own.estimations import Lagranj_nd, Lagranj, Lagranj1
from uz.nuu.datamining.own.functions import Normalizing_Estmation
import numpy as np
import pandas as pd


def ReadFromCSVWithHeaderClass(path):
    data = pd.read_csv(path)

    X = np.array(data.T)

    y = np.empty(shape=(X.shape[0]), dtype=np.int)

    for i in range(X.shape[0]):
        if "ALL" in data.columns.values[i]:
            y[i] = 0
        else:
            y[i] = 1

    """y = np.array(data.columns.values)
    y["ALL" in y] = 0
    y["AML" in y] = 1

    print(y)"""

    types = np.full(shape=(X.shape[1]), fill_value=1)

    return X, types, y


def main():
    path = r"D:\Nuu\AI\Selections\leukemia\leukemia_big.csv"

    X, types, y = ReadFromCSVWithHeaderClass(path)

    #minmax_scale(X, copy=False)
    Normalizing_Estmation(X, y)

    _, ln = np.unique(y, return_counts=True)

    w = Lagranj1(X, y)

    while X.shape[1] > 13:
        cond = w != w.min()
        X = X[:, cond]
        w = w[cond]

        #print(X.shape)
        compactness(X, y, types=types, metric=1)

    """nnc1 = NearestNeighborClassifier_(noisy=True)
    nnc2 = NearestNeighborClassifier()
    nnc3 = TemplateClassifier(noisy=True)
    nn = MLPClassifier()
    svm = SVC()

    k = 10
    mean1 = 0
    mean2 = 0
    mean3 = 0
    mean4 = 0
    mean5 = 0
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.45, random_state=None, shuffle=True)

        nnc1.fit(X_train, y_train)
        nnc2.fit(X_train, y_train)
        nnc3.fit(X_train, y_train)
        svm.fit(X_train, y_train)
        nn.fit(X_train, y_train)

        mean1 += nnc1.score(X_test, y_test)
        mean2 += nnc2.score(X_test, y_test)
        mean3 += nnc3.score(X_test, y_test)
        mean4 += svm.score(X_test, y_test)
        mean5 += nn.score(X_test, y_test)

    mean1 /= k
    mean2 /= k
    mean3 /= k
    mean4 /= k
    mean5 /= k

    print(mean1, mean2, mean3, mean4, mean5)"""

if __name__ == '__main__':
    main()
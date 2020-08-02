import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC
import numpy as np
import pandas as pd

from Test.read_data import ToFormNumpy
from ai.own.classification import NearestNeighborClassifier_, NearestNeighborClassifier
from usingpackages.ctypesapi.cml import compactness, find_standard, find_noisy


def main():
    path = r"D:\tanlanmalar\GIPER_MY.txt"

    X, types, y = ToFormNumpy(path)

    y -= 1

    minmax_scale(X, copy=False)
    # Normalizing_Estmation(X, y)

    print(compactness(X, y, types))
    res = find_standard(X, y, types)
    res = find_noisy(X, y, types)

    s = 0
    for i in range(res.shape[0]):
        if res[i] == True and y[i] == 1:
            print(i + 1)
            s += 1

    print(s)


    return 0


    #nnc = NearestNeighborClassifier_(noisy=True)
    #nnc = NearestNeighborClassifier()
    #nnc = TemplateClassifier(noisy=True)
    nn = MLPClassifier()
    svm = SVC()

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
import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormNumpy
from usingpackages.ctypesapi.cml import find_noisy, compactness
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from uz.nuu.datamining.own.estimations import Lagranj_nd, Lagranj, Lagranj1
from uz.nuu.datamining.own.functions import Normalizing_Estmation
import numpy as np
import pandas as pd

def main():
    path = r"D:\Tanlanmalar\german.txt"

    X, types, y = ToFormNumpy(path)

    minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    nnc1 = NearestNeighborClassifier_(noisy=True)
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

    print(mean1, mean2, mean3, mean4, mean5)

if __name__ == '__main__':
    main()
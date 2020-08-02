from projects.magdiss_fris1.func.methods import ToFormNumpy
from usingpackages.ctypesapi.cml import find_noisy, compactness
from ai.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from ai.own.estimations import Lagranj, Lagranj1
from ai.own.functions import Normalizing_Estmation
import numpy as np
import pandas as pd


def main():
    # X, types, y = ToFormNumpy("D:\\german.txt")
    X, types, y = ToFormNumpy("D:\\german1.txt")
    # X, types, y = ToFormNumpy("D:\\tanlanmalar\\german.txt")

    #minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    y -= 1

    _, ln = np.unique(y, return_counts=True)

    w = Lagranj1(X, y)

    print(w)

    res= compactness(X, y, types=types, metric=1)

    print(res)

    while X.shape[1] > 2:
        cond = w != w.min()
        X = X[:, cond]
        w = w[cond]

        res = compactness(X, y, types=types, metric=1)
        print(res)


if __name__ == '__main__':
    main()
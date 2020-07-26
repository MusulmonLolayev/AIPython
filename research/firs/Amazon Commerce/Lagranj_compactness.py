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
    path = r"D:\Nuu\AI\Selections\Amazon_initial_50_30_10000\data.txt"

    X, types, y = ToFormNumpy(path)

    minmax_scale(X, copy=False)

    _, ln = np.unique(y, return_counts=True)

    w = Lagranj1(X, y)

    compactness(X, y, types=types, metric=1)

    while X.shape[1] > 2:
        cond = w != w.min()
        X = X[:, cond]
        w = w[cond]

        compactness(X, y, types=types, metric=1)


if __name__ == '__main__':
    main()
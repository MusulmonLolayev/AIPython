import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from usingpackages.ctypesapi.cml import find_noisy, compactness
from ai.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from ai.own.estimations import Lagranj, Lagranj1
from ai.own.functions import Normalizing_Estmation
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

    types = np.full(shape=(X.shape[1]), fill_value=1)

    return X, types, y

def main():
    path = r"D:\Nuu\AI\Selections\gene-expression\data1.csv"

    X, types, y = ReadFromCSVWithHeaderClass(path)

    #minmax_scale(X, copy=False)
    Normalizing_Estmation(X, y)

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
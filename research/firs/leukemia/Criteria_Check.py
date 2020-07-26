import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from usingpackages.ctypesapi.cml import find_noisy, compactness
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from uz.nuu.datamining.own.estimations import Lagranj_nd, Lagranj, Lagranj1, GeneralCriterion2D
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

    types = np.full(shape=(X.shape[1]), fill_value=1)

    return X, types, y


def main():
    path_train = r"D:\Nuu\AI\Selections\leukemia\leukemia_big.csv"
    path_test = r"D:\Nuu\AI\Selections\leukemia\leukemia_big.csv"

    X_train, types_train, y_train = ReadFromCSVWithHeaderClass(path_train)
    X_test, types_test, y_test = ReadFromCSVWithHeaderClass(path_test)

    for i in range(X_train.shape[1]):
        b = X_train[:, i].copy()
        res = GeneralCriterion2D(b, y_train)
        print(i + 1, res)

if __name__ == '__main__':
    main()
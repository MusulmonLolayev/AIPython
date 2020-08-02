import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from ai.own.classification import NearestNeighborClassifier, NearestNeighborClassifier_, TemplateClassifier
from ai.own.estimations import Lagranj1
from ai.own.functions import Normalizing_Estmation
from usingpackages.ctypesapi.cml import find_noisy, compactness
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
    path_train = r"D:\Nuu\AI\Selections\gene-expression\data_train.csv"
    path_test = r"D:\Nuu\AI\Selections\gene-expression\data_test.csv"

    X_train, types_train, y_train = ReadFromCSVWithHeaderClass(path_train)
    X_test, types_test, y_test = ReadFromCSVWithHeaderClass(path_test)

    #minmax_scale(X_train, copy=False)
    #minmax_scale(X_test, copy=False)
    Normalizing_Estmation(X_train, y_train, types_train)

    print(X_train)

    _, ln = np.unique(y_train, return_counts=True)

    w = Lagranj1(X_train, y_train)

    value = w.max()
    cond = w == value
    while len(cond[cond == True]) <= X_train.shape[1]:
        value = np.max(w[w < value])
        cond = w >= value

        compactness(X_train[:, cond], y_train)

    return 0

    #cond = [356, 2266, 2358, 2641, 4049, 6280]
    #cond = [356, 2266, 2358, 2641, 2724, 4049]
    #cond = [356, 2266, 2641, 3772, 4049, 4261]
    #cond = [4847]

    #X_train = X_train[:, cond]
    #X_test = X_test[:, cond]

    nnc1 = NearestNeighborClassifier_(noisy=True)
    nnc2 = NearestNeighborClassifier()
    nnc3 = TemplateClassifier(noisy=True)
    nn = MLPClassifier()
    svm = SVC()

    nnc1.fit(X_train, y_train)
    nnc2.fit(X_train, y_train)
    nnc3.fit(X_train, y_train)
    svm.fit(X_train, y_train)
    nn.fit(X_train, y_train)

    mean1 = nnc1.score(X_test, y_test)
    mean2 = nnc2.score(X_test, y_test)
    mean3 = nnc3.score(X_test, y_test)

    mean4 = svm.score(X_test, y_test)
    mean5 = nn.score(X_test, y_test)

    print("NearestNeighborClassifier_", mean1)
    print("NearestNeighborClassifier", mean2)
    print("TemplateClassifier", mean3)
    print("SVC", mean4)
    print("MLPClassifier", mean5)

if __name__ == '__main__':
    main()
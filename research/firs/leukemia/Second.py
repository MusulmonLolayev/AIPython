import time
from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from usingpackages.ctypesapi.cml import find_noisy
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from uz.nuu.datamining.own.estimations import Lagranj_nd
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

    path = r"D:\Nuu\AI\Selections\leukemia\leukemia_small.csv"

    X, types, y = ReadFromCSVWithHeaderClass(path)

    minmax_scale(X, copy=False)
    #minmax_scale(X, copy=False)

    """w = Lagranj_nd(X)

    value = w.max()
    cond = w == value
    while len(cond[cond == True]) < 661:
        value = np.max(w[w < value])
        cond = w >= value


    print(len(cond[cond == True]))

    X_Test = X[:, w >= value]
    types_Test = types[w >= value]

    metric = 1

    noisy = find_noisy(X_Test, y, types=types_Test, metric=metric)

    cond = np.logical_not(noisy)

    X_Test = X_Test[cond]
    y_Test = y[cond]

    print(X.shape)

"""

    noisy = find_noisy(X, y, types=types)

    cond = np.logical_not(noisy)
    X = X[cond]
    y = y[cond]

    k = 10
    k_fold = KFold(n_splits=k, shuffle=True, random_state=None)

    """
    # Neighbors
    nnc = NearestNeighborClassifier()

    nnc_ = NearestNeighborClassifier_()

    knc = KNeighborsClassifier(n_neighbors=30)


    begin = time.time()
    max_mean1 = 0
    #max_mean1 = CVS(nnc, X_Test, y_Test, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    end = time.time()
    print("Time: ", (end - begin) * 1000)

    max_mean2 = 0
    max_mean2 = CVS(nnc_, X_Test, y_Test, cv=k_fold, n_jobs=4, scoring='accuracy').mean()

    begin = time.time()
    max_mean3 = 0
    max_mean3 = CVS(knc, X_Test, y_Test, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    end = time.time()
    print("Time: ", (end - begin) * 1000)

    print(max_mean1, max_mean2, max_mean3)
"""

    nnc = NearestNeighborClassifier_()
    nnc.fit(X, y)

    svm = SVC(kernel="linear")
    #svm.fit(X, y)

    nn = MLPClassifier(hidden_layer_sizes=(100, 200))
    #nn.fit(X, y)

    max_mean = CVS(nnc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()

    print(max_mean)
if __name__ == '__main__':
    main()
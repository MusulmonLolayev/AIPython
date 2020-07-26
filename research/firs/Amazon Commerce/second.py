from ctypes import *
import time

from numpy.ctypeslib import ndpointer
from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormNumpy
import numpy as np

from usingpackages.ctypesapi.cml import compactness, find_noisy
from uz.nuu.datamining.own.estimations import Lagranj_nd


def Lagranj(X):
    w = np.empty(shape=(X.shape[1]))
    for i in range(X.shape[1]):
        ww = set()
        for j in range(X.shape[0]):
            ww.add(X[j, i])
        w[i] = len(ww)
    return w

def main():
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    X, types, y = ToFormNumpy(r"D:\Nuu\AI\Selections\Amazon_initial_50_30_10000\data.txt")

    metric = 1

    minmax_scale(X, copy=False)

    #w = Lagranj_nd(X, y)
    w = Lagranj(X)
    value = w.max()

    value = w.max()
    cond = w == value
    while len(cond[cond == True]) < 661:
        value = np.max(w[w < value])
        cond = w >= value

    X_Test = X[:, w >= value]

    k = 10
    k_fold = KFold(n_splits=k, shuffle=True, random_state=None)

    svm = SVC(kernel="linear")

    #svm.fit(X_Test, y)

    nn = MLPClassifier()
    nn.fit(X_Test, y)

    max_mean = CVS(nn, X_Test, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    print(max_mean)

if __name__ == '__main__':
    main()
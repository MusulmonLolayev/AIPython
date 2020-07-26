from ctypes import *
import time

from numpy.ctypeslib import ndpointer
from sklearn.preprocessing import minmax_scale
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
    X_Test = np.array(X[:, w == value])
    types_Test = np.array(types[w == value])

    i = 0

    while X_Test.shape[1] < 2000:

        value = np.max(w[w < value])

        X_Test = X[:, w >= value]
        types_Test = types[w >= value]

        noisy = find_noisy(X_Test, y, types=types_Test, metric=metric)


        cond =  np.logical_not(noisy)

        print("\nnoisy = ", len(noisy[noisy == True]))

        compactness(X_Test[cond], y[cond],
                    types=types_Test, metric=metric)

        i += 1

if __name__ == '__main__':
    main()
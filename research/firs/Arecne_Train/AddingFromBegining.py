from ctypes import *
import time

from numpy.ctypeslib import ndpointer
from sklearn.preprocessing import minmax_scale
from Test.read_data import ToFormNumpy
import numpy as np

from usingpackages.ctypesapi.cml import cml, _doublepp, compactness
from uz.nuu.datamining.own.estimations import Lagranj_nd
from ai.own.fris import Fris


def main():
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\arcene_train.txt")

    minmax_scale(X, copy=False)

    w = Lagranj_nd(X, y)

    print(w.shape)

    X_Test = np.array(X[:, w == w.min()])
    types_Test = np.array(types[w == w.min()])

    print(X_Test)

    res = compactness(X_Test, y, types=types_Test, metric=1)
    #print(res[0], res[1], res[2])

if __name__ == '__main__':
    main()
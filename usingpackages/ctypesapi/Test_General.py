from ctypes import *
import time

from numpy.ctypeslib import ndpointer
from sklearn.preprocessing import minmax_scale
from Test.read_data import ToFormNumpy
import numpy as np

from usingpackages.ctypesapi.cml import cml, _doublepp, compactness
from datamining.own.fris import Fris


def main():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    # X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    minmax_scale(X, copy=False)

    res = compactness(X, y, types=types, metric=1)

    print(res[0], res[1], res[2])

if __name__ == '__main__':
    main()
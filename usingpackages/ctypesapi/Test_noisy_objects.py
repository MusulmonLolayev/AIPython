from ctypes import *

import time

import time

from numpy.ctypeslib import ndpointer
from sklearn.preprocessing import minmax_scale
from Test.read_data import ToFormNumpy
import numpy as np

from usingpackages.ctypesapi.cml import find_noisy


def main():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    # X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")

    metric = 1

    minmax_scale(X, copy=False)

    noisy = find_noisy(X, y, types=types, metric=metric)

    #for item in noisy:
    #    print(item)

    print(len(noisy))

if __name__ == '__main__':
    main()
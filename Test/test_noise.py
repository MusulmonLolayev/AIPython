import time
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy
from uz.nuu.datamining.own.noisyobjects import noisyobjects1
import numpy as np


def main():
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    # X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    minmax_scale(X, copy=False)

    begin = time.time()

    res = noisyobjects1(X, y, ln=[30, 12], types = types)

    end = time.time()
    print("Time: ", (end - begin) * 1000)

    indexes = np.empty(shape=(X.shape[0]), dtype=bool)
    indexes[res == 0] = False
    indexes[res > 0] = True

    print(len(indexes[indexes == True]))


if __name__ == '__main__':
    main()
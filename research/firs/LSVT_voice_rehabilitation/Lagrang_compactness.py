import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

from Test.read_data import ToFormNumpy
from usingpackages.ctypesapi.cml import find_noisy, compactness
from ai.own.estimations import Lagranj_nd, Lagranj, Lagranj1
from ai.own.functions import Normalizing_Estmation
import numpy as np
import pandas as pd

def main():
    path = r"D:\Nuu\AI\Selections\LSVT_voice_rehabilitation\data.txt"

    X, types, y = ToFormNumpy(path)

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
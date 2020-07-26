from usingpackages.ctypesapi.cml import find_noisy, compactness, find_shell
import numpy as np
import pandas as pd
from Test.read_data import ToFormNumpy
from sklearn.preprocessing import minmax_scale


def count(data, y):
    res = [0, 0]

    for i in range(y.shape[0]):
        if data[i] == True:
            res[y[i]] += 1

    for i in range(y.shape[0]):
        if data[i] == True and y[i] == 0:
            print(i + 1, end=", ")
    print(res[0])

    for i in range(y.shape[0]):
        if data[i] == True and y[i] == 1:
            print(i + 1, end=", ")
    print(res[1])

def main():
    path = r"D:\Tanlanmalar\MATBIO_MY.txt"

    X, types, y = ToFormNumpy(path)

    y -= 1

    print(X.shape)

    #minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    count(find_shell(X, y), y)

if __name__ == '__main__':
    main()
import numpy as np
import pandas

from Test.read_data import ToFormNumpy
from ai.own.regression import KnnOptimalRegression


def main():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")

    reg = KnnOptimalRegression()

    reg.fit(X, y)

    print(reg.predict(X))

if __name__ == '__main__':
    main()
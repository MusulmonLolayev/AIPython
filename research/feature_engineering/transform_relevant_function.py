import numpy as np

from Test.read_data import ToFormNumpy

def main():

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\german.txt")
    _, ln = np.unique(y, return_counts=True)
    for j in range(X.shape[1]):
        if types[j] == 0:
            gradation = {}
            for i in range(X.shape[0]):
                if not (X[i, j] in gradation):
                    nyu1 = np.count_nonzero(X[y == 0, j] == X[i, j]) / ln[0]
                    nyu2 = np.count_nonzero(X[y == 1, j] == X[i, j]) / ln[1]

                    gradation[X[i, j]] = nyu1 / (nyu1 + nyu2)

                if y[i] == 0:
                    X[i, j] = gradation[X[i, j]]
                else:
                    X[i, j] = 1 - gradation[X[i, j]]


    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            print(X[i, j], end=' ')
        print(y[i] + 1)


if __name__ == '__main__':
    main()
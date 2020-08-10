import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import minmax_scale
from sklearn.cluster import DBSCAN

def main():

    colums = [0, 2, 4, 6, 7, 8]
    headers = ['Age', 'Creatinine phosphokinase', 'Ejection fraction', 'Platelets',
               'Serum creatinine', 'Serum sodium']

    X = np.loadtxt('G:/data.txt')

    _X = X.copy()

    minmax_scale(X, copy=False)

    x = 1
    y = 4

    x_coor = colums[x]
    y_coor = colums[y]

    marker = ["o", "s"]
    size = 7

    clustering = DBSCAN(eps=0.1, min_samples=4).fit(X[:, [x_coor, y_coor]])

    print(clustering.labels_)

    #return 0

    black = clustering.labels_ == 0

    red = np.logical_not(black)

    plt.xlabel(headers[x])
    plt.ylabel(headers[y])

    plt.plot(_X[black, x_coor], _X[black, y_coor], marker[0], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='black',
             markeredgewidth=1.5)
    plt.plot(_X[red, x_coor], _X[red, y_coor], marker[1], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='red',
             markeredgewidth=1.5)

    plt.show()

if __name__ == '__main__':
    main()
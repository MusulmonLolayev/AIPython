import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import minmax_scale

def main():

    colums = [0, 2, 4, 6, 7, 8]
    headers = ['Age', 'Creatinine phosphokinase', 'Ejection fraction', 'Platelets',
               'Serum creatinine', 'Serum sodium']

    X = np.loadtxt('G:/data.txt')

    #minmax_scale(X, copy=False)

    card = np.array([i + 1 for i in range(X.shape[0])])

    x = 1
    y = 4

    x_coor = colums[x]
    y_coor = colums[y]

    marker = ["o", "s"]
    size = 7

    black = np.logical_and(card != 2, card != 10)
    red = np.logical_not(black)

    plt.xlabel(headers[x])
    plt.ylabel(headers[y])

    plt.plot(X[black, x_coor], X[black, y_coor], marker[0], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='black',
             markeredgewidth=1.5)
    plt.plot(X[red, x_coor], X[red, y_coor], marker[1], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='red',
             markeredgewidth=1.5)

    [plt.annotate(str(i + 1), (X[i, x_coor], X[i, y_coor])) for i in [1, 9, 60]]

    plt.show()

if __name__ == '__main__':
    main()
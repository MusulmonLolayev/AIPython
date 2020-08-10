import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import minmax_scale

def AcceptableInterval(x, y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = np.median(x)
        value_y = np.median(y)

    R = x / value_x - y / value_y

    return R, value_x, value_y

def main():

    colums = [0, 2, 4, 6, 7, 8]
    headers = ['Age', 'Creatinine phosphokinase', 'Ejection fraction', 'Platelets',
               'Serum creatinine', 'Serum sodium']

    X = np.loadtxt('G:/data.txt')

    _X = X.copy()

    minmax_scale(X, copy=False)

    card = np.array([i + 1 for i in range(X.shape[0])])

    x = 1
    y = 4

    x_coor = colums[x]
    y_coor = colums[y]

    R, value_x, value_y = AcceptableInterval(X[:, x_coor], X[:, y_coor])

    marker = ["o", "s"]
    size = 7

    percentage = 3
    q_left = np.percentile(R, percentage)
    q_right = np.percentile(R, 100 - percentage)

    black = np.logical_and(q_left <= R, R <= q_right)
    red = np.logical_not(black)

    plt.xlabel(headers[x])
    plt.ylabel(headers[y])

    plt.plot(_X[black, x_coor], _X[black, y_coor], marker[0], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='black',
             markeredgewidth=1.5)
    plt.plot(_X[red, x_coor], _X[red, y_coor], marker[1], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='red',
             markeredgewidth=1.5)

    #[plt.annotate(str(i + 1), (X[i, x_coor], X[i, y_coor])) for i in [1, 9, 60]]

    plt.show()

if __name__ == '__main__':
    main()
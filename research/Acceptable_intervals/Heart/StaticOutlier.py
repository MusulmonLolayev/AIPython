import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import minmax_scale

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


    mean_x = X[:, x_coor].mean()
    mean_y = X[:, y_coor].mean()


    percentage = 3

    std_x = percentage * np.std(X[:, x_coor])
    std_y = percentage * np.std(X[:, y_coor])

    print(std_x, std_y)

    marker = ["o", "s"]
    size = 7

    black = np.logical_and(
        np.logical_and(mean_x - std_x <= X[:, x_coor], X[:, x_coor] <= mean_x + std_x),
        np.logical_and(mean_y - std_y <= X[:, y_coor], X[:, y_coor] <= mean_y + std_y))

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
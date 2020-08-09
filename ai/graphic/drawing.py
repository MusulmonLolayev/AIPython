from matplotlib.pyplot import imshow, title
import matplotlib.pyplot as plt


def drawobjects(a, classes=None, className=None, objectLabel=None, isVisibleLabel=False):
    g1_x = []
    g1_y = []

    g2_x = []
    g2_y = []

    x = []
    y = []

    for item in range(len(a)):
        if classes[item] == 1:
            g1_x.append(a[item][0])
            g1_y.append(a[item][1])
        else:
            g2_x.append(a[item][0])
            g2_y.append(a[item][1])
        x.append(a[item][0])
        y.append(a[item][1])

    g1 = (g1_x, g1_y)
    g2 = (g2_x, g2_y)

    data = (g1, g2)
    colors = ("red", "green")
    groups = ("Birinchi sinf", "Ikkinchi sinf")

    # Create plot
    fig = plt.figure()
    fig.suptitle("Obyektlarning ikki o'lchovli fazoda joylashish o'rni")
    ax = fig.add_subplot(1, 1, 1)

    for data, color, group in zip(data, colors, groups):
        x1, y1 = data
        ax.scatter(x1, y1, alpha=0.8, c=color, edgecolors='none', s=10, label=group)

    if isVisibleLabel:
        for i in range(len(x)):
            ax.annotate(str(i + 1), (x[i], y[i]))

    plt.title('Obyektlar oynasi')
    plt.legend(loc=2)
    plt.show()

def mscatter(X, y, marker = ["o", "s"], colors = ["black", "red"], size=8,
             labels = None, title = "Obyektlarning ikki o'lchovli fazoda joylashish o'rni", save_name = None):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for i in range(X.shape[0]):
        plt.scatter(X[i, 0], X[i, 1], marker=marker[y[i]], s=size, c=colors[y[i]])
        #ax.annotate(str(i + 1), (X[i, 0], X[i, 1]))

    if save_name == None:
        plt.show()
    else:
        plt.savefig(fname=save_name)
    plt.close()

def mscatter1(X, y, marker = ["o", "s"], colors = ["black", "red"], size=8,
             labels = None, title = "Obyektlarning ikki o'lchovli fazoda joylashish o'rni", save_name = None):

    plt.plot(X[y == 0, 0], X[y == 0, 1], marker[0], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='black', markeredgewidth=1.5)
    plt.plot(X[y == 1, 0], X[y == 1, 1], marker[1], ms=size, markerfacecolor="None", alpha=1, markeredgecolor='black', markeredgewidth=1.5)

    plt.show()
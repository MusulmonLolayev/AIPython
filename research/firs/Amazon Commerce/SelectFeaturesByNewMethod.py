import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormNumpy
from usingpackages.ctypesapi.cml import find_noisy, compactness
from ai.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from ai.own.functions import Normalizing_Estmation
import numpy as np


def Lagranj_nd(X, y):

    unique, ln = np.unique(y, return_counts=True)

    w = np.empty(shape=(X.shape[1]))

    q = 0

    for j in range(X.shape[1]):
        mean = np.empty(shape=(ln.shape[0]))
        for i in range(ln.shape[0]):
            mean[i] = X[y == unique[i], j].mean()

        teta = 0
        gamma = 0
        for i in range(ln.shape[0]):

            teta += np.sum(np.abs(X[y == unique[i], j] - mean[i])) / len(y[y == unique[i]])

            l = i
            dis = -1
            for r in range(ln.shape[0]):
                diff  = abs(mean[i] - mean[r])
                if i != r and (dis == -1 or diff < dis):
                    l = r
                    dis = diff

            gamma += np.sum(np.abs(X[y == unique[l], j] - mean[i])) / len(y[y == unique[l]])

        w[j] = gamma - teta
    return w

def main():
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    X, types, y = ToFormNumpy(r"D:\Nuu\AI\Selections\Amazon_initial_50_30_10000\data.txt")

    #y[y == 2] = 1

    minmax_scale(X, copy=False)
    #minmax_scale(X, copy=False)

    w = Lagranj_nd(X, y)

    unique, ln = np.unique(y, return_counts=True)

    number_class = len(unique)

    #return 0

    value = w.max()
    cond_opt = w == value

    comp_opt = compactness(X[:, cond_opt], y, types)
    print(len(cond_opt[cond_opt == True]), comp_opt, sep="\t")

    while len(cond_opt[cond_opt == True]) < X.shape[1]:
        value = np.max(w[w < value])

        cond_current = np.logical_or(w == value, cond_opt)

        comp_current = compactness(X[:, cond_current], y, types)

        if comp_opt[number_class] < comp_current[number_class]:
            cond_opt = cond_current
            comp_opt = comp_current
            print(len(cond_opt[cond_opt == True]), comp_opt, sep="\t")

    return 0

    X = X[:, cond]
    types = types[cond]

    metric = 1

    #nnc = NearestNeighborClassifier_(noisy=True)
    nnc = NearestNeighborClassifier()
    # nnc = TemplateClassifier(noisy=True)
    nn = MLPClassifier()
    svm = SVC()

    k = 10
    mean1 = 0
    mean2 = 0
    mean3 = 0
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.5, random_state=None, shuffle=True)

        nnc.fit(X_train, y_train)
        svm.fit(X_train, y_train)
        nn.fit(X_train, y_train)

        mean1 += nnc.score(X_test, y_test)
        mean2 += svm.score(X_test, y_test)
        mean3 += nn.score(X_test, y_test)

    mean1 /= k
    mean2 /= k
    mean3 /= k

    print(mean1, mean2, mean3)

if __name__ == '__main__':
    main()
from uz.nuu.datamining.own.functions import Distance, Table, inf_object
import numpy as np
from scipy.spatial import distance

def noisyobjects(a, classes, ln=None, types=None):
    """
        Shovqin obyektlarning indexni topish funksiyasi
    """
    tables = inf_object(a, classes, types)
    print("Got information location of objects")
    res = []
    for i in range(len(a)):
        if tables[i].count_it / ln[classes[i]-1] > tables[i].count_vs / ln[2-classes[i]] :
            for j in range(len(a)):
                if classes[j] != classes[i]:
                    dis = Distance(a[i], a[j], types)
                    if dis < tables[j].dis_from_vs:
                        tables[j].count_vs -= 1
            res.append(i)
    return res



def noisyobjects1(X, y, ln=None, types=None, metric='euclidean'):
    # Shell objects
    cc = np.zeros(shape=(X.shape[0]))
    r1 = np.zeros(shape=(X.shape[0]))
    r3 = np.zeros(shape=(X.shape[0]))

    count = 0

    for i in range(X.shape[0]):
        s = np.core.inf
        k = 0
        for j in range(X.shape[0]):
            if y[i] != y[j]:
                s1 = distance.pdist(X[[i, j]], metric=metric)
                if s > s1:
                    s = s1
                    k = j
        cc[k] += 1
        r3[i] = s

    for i in range(X.shape[0]):
        if cc[i] > 0:
            for j in range(X.shape[0]):
                if i != j and y[i] == y[j] and r3[i] > distance.pdist(X[[i, j]]):
                    r1[i] += 1
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            count += 1
        else:
            cc[i] = 0

    return cc

def noisyobjects2(X, y, ln=None, types=None, metric='euclidean'):
    # Shell objects
    cc = np.zeros(shape=(X.shape[0]))
    lk = np.zeros(shape=(X.shape[0]))
    r1 = np.zeros(shape=(X.shape[0]))
    r3 = np.zeros(shape=(X.shape[0]))
    etalon = np.zeros(shape=(X.shape[0]))

    for i in range(X.shape[0]):
        s = np.core.inf
        k = 0
        for j in range(X.shape[0]):
            if y[i] != y[j]:
                s1 = distance.pdist(X[[i, j]], metric=metric)
                if s > s1:
                    s = s1
                    k = j
        cc[k] += 1
        lk[k] = 1
        r3[i] = s

    for i in range(X.shape[0]):
        if cc[i] > 0:
            for j in range(X.shape[0]):
                if r3[i] > distance.pdist(X[[i, j]]) and i != j and y[i] == y[j]:
                    r1[i] += 1
    count = 0
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            count += 1
            etalon[i] -= cc[i]
        else:
            cc[i] = 0
    return cc, lk, r1, r3, etalon
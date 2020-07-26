from scipy.spatial import distance
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy
from uz.nuu.datamining.own.estimations import Lagranj, DecomposionEstimation
from uz.nuu.datamining.own.functions import Normalizing_Estmation

from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import numpy as np

def clearNoisy(X, y, ln=None):
    if ln == None:
        _, ln = np.unique(y, return_counts=True)

    metric = 'euclidean'

    # Shell objects
    # cc is number of which object in against class is close to this object
    cc = np.zeros(shape=(X.shape[0]), dtype=int)
    pnk = np.zeros(shape=(X.shape[0]), dtype=int)
    #
    lk = np.zeros(shape=(X.shape[0]), dtype=int)
    # r1 is number of which object in this object's class is in radius of r1
    r1 = np.zeros(shape=(X.shape[0]), dtype=int)
    # r3 radius of object that to check which objects are in this and what class they are
    r3 = np.zeros(shape=(X.shape[0]), dtype=float)
    #
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

    # size of noisy objects
    count = 0
    indx = np.empty(shape=(len(y)), dtype=bool)
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            count += 1
            etalon[i] -= cc[i]
            np.append(indx, [i])
            indx[i] = False
        else:
            cc[i] = 0
            indx[i] = True

    print(len(indx[indx == False]))
    return indx

def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")

    y[y == 2] = 1

    _, ln = np.unique(y, return_counts=True)

    #print(ln)

    #minmax_scale(X, copy=False)
    Normalizing_Estmation(X, y)

    indx = clearNoisy(X, y)

    X = X[indx]
    y = y[indx]

    #print(X.shape)
    #print(y.shape)

    #return None

    selection_Name = r'\Gasterology2'
    preproccesing_name = r'own'

    path = r"D:\Nuu\Data mining\Articles\Cross Validation\Computing" + selection_Name + \
           r"\res " + preproccesing_name + ".txt"

    file = open(path, 'w')

    # Cross Validation
    k = 10
    k_fold = KFold(n_splits=k, shuffle=True, random_state=None)

    #Nerual network
    mlp = MLPClassifier(hidden_layer_sizes=(100, 200), activation='logistic')

    # Knn
    n_neighbors = 2 * min(ln) - 3
    # mertic Euclidean
    knc = KNeighborsClassifier(n_neighbors=n_neighbors, p=2)

    #SVM
    svc = SVC(kernel="linear", degree=5)

    # RDF
    rdf = RandomForestClassifier(max_depth=1000)

    #print("MLP")
    max_mean1 = CVS(mlp, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    #print("KNN")
    max_mean2 = CVS(knc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    #print("SVM")
    max_mean3 = CVS(svc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()

    print(X.shape[1], max_mean1, max_mean2, max_mean3)
    # 25
    w = Lagranj(X, y, types)

    while X.shape[1] > 2:
        # Cross Validation
        k = 5
        k_fold = KFold(n_splits=k, shuffle=True, random_state=42)

        # Nerual network
        mlp = MLPClassifier(hidden_layer_sizes=(50, 200), activation='relu', max_iter=1000, alpha=1e-5,
                            solver='adam', verbose=False, tol=1e-8, random_state=1,
                            learning_rate_init=.1)

        # Knn
        n_neighbors = 2 * min(ln) - 3
        # mertic Euclidean
        knc = KNeighborsClassifier(n_neighbors=n_neighbors, p=2)

        # SVM
        svc = SVC(gamma='scale')


        max_mean1 = sum(CVS(mlp, X, y, cv=k_fold, n_jobs=4, scoring='accuracy')) / k
        max_mean2 = sum(CVS(knc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy')) / k
        max_mean3 = sum(CVS(svc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy')) / k

        print(X.shape[1], max_mean1, max_mean2, max_mean3)
        file.write(str(X.shape[1]) + "\t" + str(max_mean1)+ "\t" + str(max_mean2)+ "\t" + str(max_mean3)+ "\n")

        cond = w != w.min()
        X = X[:, cond]
        w = w[cond]

    file.close()

if __name__ == '__main__':
    main()
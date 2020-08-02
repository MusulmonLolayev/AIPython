from scipy.spatial import distance
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy

from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import numpy as np

from ai.own.functions import Normalizing_Estmation


def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    #X, types, y = ToFormNumpy("D:\\german.txt") #71.2
    #X, types, y = ToFormNumpy("D:\\german1.txt") #91.7
    #X, types, y = ToFormNumpy("D:\\german2.txt") #91.7
    #X, types, y = ToFormNumpy("D:\\german3.txt") #94.4
    #X, types, y = ToFormNumpy("D:\\german4.txt") #95.4
    #X, types, y = ToFormNumpy("D:\\german5.txt") #97.7
    X, types, y = ToFormNumpy("D:\\german6.txt") #98.1
    #X, types, y = ToFormNumpy("D:\\german7.txt") #97.3
    #X, types, y = ToFormNumpy("D:\\german8.txt") #94.5
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\german.txt")

    #y[y == 2] = 1

    _, ln = np.unique(y, return_counts=True)


    #minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    # Cross Validation
    k = 10
    k_fold = KFold(n_splits=k, shuffle=True, random_state=None)

    #Nerual network
    mlp = MLPClassifier(hidden_layer_sizes=(100, 200))

    # Knn
    n_neighbors = 2 * min(ln) - 3
    # mertic Euclidean
    #knc = KNeighborsClassifier(n_neighbors=n_neighbors)
    knc = KNeighborsClassifier(n_neighbors=1)

    #SVM
    svc = SVC()

    #print("MLP")
    max_mean1 = CVS(mlp, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    #print("KNN")
    max_mean2 = CVS(knc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    #print("SVM")
    max_mean3 = CVS(svc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()

    print(max_mean1, max_mean2, max_mean3)
    # 25


if __name__ == '__main__':
    main()
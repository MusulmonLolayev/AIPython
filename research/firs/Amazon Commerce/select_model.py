import time
from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormNumpy
from usingpackages.ctypesapi.cml import find_noisy
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier, \
    NearestNeighborClassifier_
from uz.nuu.datamining.own.functions import Normalizing_Estmation
import numpy as np

from sklearn.feature_selection import SelectKBest, chi2

def main():
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    X, types, y = ToFormNumpy(r"D:\Nuu\AI\Selections\Amazon_initial_50_30_10000\data.txt")

    minmax_scale(X, copy=False)
    #minmax_scale(X, copy=False)

    X = SelectKBest(chi2, k=2000).fit_transform(X, y)


    metric = 1

    # nnc = NearestNeighborClassifier_(noisy=True)
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

        #nnc.fit(X_train, y_train)
        svm.fit(X_train, y_train)
        nn.fit(X_train, y_train)

        #mean1 += nnc.score(X_test, y_test)
        mean2 += svm.score(X_test, y_test)
        mean3 += nn.score(X_test, y_test)

    mean1 /= k
    mean2 /= k
    mean3 /= k

    print(mean1, mean2, mean3)

if __name__ == '__main__':
    main()
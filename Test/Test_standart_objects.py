from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormArray, ToFormNumpy
import numpy as np

from sklearn.model_selection import cross_val_score as CVS, KFold, train_test_split
from usingpackages.ctypesapi.cml import find_standard
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, NearestNeighborClassifier_, \
    TemplateClassifier
from uz.nuu.datamining.own.functions import Normalizing_Estmation


def main():

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")

    y -= 1

    minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    #nnc = NearestNeighborClassifier_()
    nnc = NearestNeighborClassifier()
    #nnc = TemplateClassifier()
    nn = MLPClassifier()
    svm = SVC()

    k = 10
    mean1 = 0
    mean2 = 0
    mean3 = 0
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = 0.5, random_state = None, shuffle=True)

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
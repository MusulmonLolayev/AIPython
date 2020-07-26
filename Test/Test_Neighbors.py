import time
from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier
from uz.nuu.datamining.own.functions import Normalizing_Estmation


def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\Asian Religion.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\arcene_train.txt")


    minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y, types=types)

    k = 10
    k_fold = KFold(n_splits=k, shuffle=True, random_state=None)

    # Neighbors
    nnc = NearestNeighborClassifier()

    knc = TemplateClassifier()

    begin = time.time()
    max_mean1 = CVS(nnc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    end = time.time()
    print("Time: ", (end - begin) * 1000)

    print(max_mean1)

    begin = time.time()
    max_mean2 = CVS(knc, X, y, cv=k_fold, n_jobs=4, scoring='accuracy').mean()
    end = time.time()
    print("Time: ", (end - begin) * 1000)


    print(max_mean1, max_mean2)

if __name__ == '__main__':
    main()
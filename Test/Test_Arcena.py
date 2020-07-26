import time
from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy
from uz.nuu.datamining.own.classification import NearestNeighborClassifier, TemplateClassifier
from uz.nuu.datamining.own.functions import Normalizing_Estmation
import numpy as np

def main():

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\arcene_train.txt")

    X_Test = np.loadtxt(r"D:\Nuu\AI\Selections\Arcena Data Set\arcene_test.data")


    minmax_scale(X, copy=False)
    minmax_scale(X_Test, copy=False)
    #Normalizing_Estmation(X, y, types=types)

    nnc = NearestNeighborClassifier()


    begin = time.time()

    nnc.fit(X, y)

    print(nnc.predict(X_Test))

    end = time.time()
    print("Time: ", (end - begin) * 1000)

if __name__ == '__main__':
    main()
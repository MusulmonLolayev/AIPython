from concurrent.futures import ThreadPoolExecutor
from time import time

from sklearn.decomposition import PCA, KernelPCA
from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, minmax_scale

from Test.read_data import ToFormArray, ToFormNumpy
from uz.nuu.datamining.graphic.drawing import drawobjects, mscatter
from uz.nuu.datamining.own.estimations import Lagranj
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, Normalizing_Estmation, Normalizing_Estmation1
from uz.nuu.datamining.own.reduction import SammonProjection
import numpy as np

def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasteralogy.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")

    y[y == 2] = 1

    # 25
    w, cond = Lagranj(X, y, types)

    X = X[:, cond]

    count = 0
    i = 0
    while i < count:
        X = X[:, w != w.min()]
        w = w[w != w.min()]
        i += 1

    print(X.shape)
    #minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    path = r'D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj\Gasterology\Gasterology' + str(X.shape) + '.txt'
    path2 = r'D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj\Gasterology\Gasterology(transform)' + str(X.shape) + '.txt'

    file = open(path, 'w')
    file2 = open(path2, 'w')

    #pca = KernelPCA(n_components=2, kernel='poly')
    pca = PCA(n_components=2)
    pca.fit(X, y=y)

    transform = pca.transform(X)

    mscatter(transform, y=y)

    k = 5

    k_fold = KFold(n_splits=k, shuffle=True, random_state=42)

    mlp = MLPClassifier(hidden_layer_sizes=(50, 200), activation='relu', max_iter=1000, alpha=1e-5,
                        solver='adam', verbose=False, tol=1e-4, random_state=1,
                        learning_rate_init=.1)

    #max_mean = sum(CVS(mlp, X, y, cv=k_fold, n_jobs=-1, scoring='accuracy')) / k
    #print('Баҳо = ', max_mean)

    #max_mean = sum(CVS(mlp, transform, y, cv=k_fold, n_jobs=-1, scoring='accuracy')) / k
    #print('Баҳо = ', max_mean)

    file.write(str(X.shape[0]) + " " + str(X.shape[1]) + "\n")
    file2.write(str(X.shape[0]) + " " + "2" + "\n")

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            file.write(str(X[i, j]).replace('.', ',') + " ")

        file2.write(str(transform[i, 0]).replace('.', ',') + " ")
        file2.write(str(transform[i, 1]).replace('.', ',') + " ")

        if i < X.shape[0] - 1:
            file.write(str(y[i]) + "\n")
            file2.write(str(y[i]) + "\n")
        else:
            file.write(str(y[i]))
            file2.write(str(y[i]))
    file.close()

if __name__ == '__main__':
    main()
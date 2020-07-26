import numpy as np
from sklearn.decomposition import PCA, KernelPCA
from sklearn.manifold import Isomap

from Test.read_data import ToFormArray
from uz.nuu.datamining.graphic.drawing import drawobjects
from uz.nuu.datamining.own.estimations import GeneralCriterion2D
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, OwnForm


def main():
    #a, types, classes = ToFormArray(r"D:\\german.txt")
    #a, types, classes = ToFormArray(r"D:\\Nuu\\Data mining\\Researchs\\Umid aka Moliya\\Data set\\use\\umumiy.txt")
    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #a, types, classes = ToFormArray("D:\\tanlanmalar\\german (numerical).txt")
    #a, types, classes = ToFormArray("D:\\tanlanmalar\\giper_my.txt")
    #a, types, classes = ToFormArray("D:\\tanlanmalar\\MATBIO_MY.txt")

    ln = [0, 0]

    for i in range(len(classes)):
        classes[i] -= 1
        ln[classes[i]] += 1

    wop = []

    res = []

    Normalizing_Min_Max(a, types)
    isNormalize = False


    for i in range(len(a[0])):
        b = []
        for j in range(len(a)):
            b.append(a[j][i])
        sort = []
        res.append(GeneralCriterion2D(b, classes, ln=ln, sort=sort))
        c0 = a[res[i][1]][i]
        c1 = a[res[i][2]][i]
        #border = (a[res[i][2]][i] + b[res[i][4]]) / 2
        c2 = a[res[i][3]][i]

        if isNormalize == True:
            for j in range(len(a)):
                #a[j][i] = (a[j][i] - border) / (c2 - c0)
                a[j][i] = res[i][0] * (a[j][i] - c1) / (c2 - c0)
                #a[j][i] = res[i][0] * (a[j][i] - border) / (c2 - c0)


        #wop.append(border)
        wop.append(a[res[i][2]][i])

    #print(wop)
    X = np.array(a)

    #pca = PCA(n_components = 2, wop = wop)
    pca = PCA(n_components = 2)


    pca.fit(X, y=classes)

    transform = pca.transform(X)

    array = []
    for i in range(len(transform)):
        row = []
        for j in range(len(transform[0])):
            row.append(transform[i][j])
        print(str(row[0]) + " " + str(row[1]) + " " + str(classes[i]))
        array.append(row)

    drawobjects(transform, classes=classes, isVisibleLabel = False)
    #print(sammon.error)

if __name__ == '__main__':
    main()
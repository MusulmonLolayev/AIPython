from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import minmax_scale
from sklearn.svm import SVC

from Test.read_data import ToFormNumpy
from ai.own.classification import NearestNeighborClassifier_

from ai.own.estimations import Lagranj_nd


def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")
    #X, types, y = ToFormNumpy(r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Gastown1.txt")
    X, types, y = ToFormNumpy(r"D:\Nuu\AI\Selections\Amazon_initial_50_30_10000\data.txt")

    #minmax_scale(X, copy=False)

    w = Lagranj_nd(X, y)

    cond = w > 0

    print(len(cond[cond == True]))

"""
    nnc = NearestNeighborClassifier_(noisy=True)
    # nnc = NearestNeighborClassifier()
    # nnc = TemplateClassifier(noisy=True)
    nn = MLPClassifier()
    svm = SVC()

    k = 10
    mean1 = 0
    mean2 = 0
    mean3 = 0
    for i in range(k):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=None, shuffle=True)

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
"""

if __name__ == '__main__':
    main()
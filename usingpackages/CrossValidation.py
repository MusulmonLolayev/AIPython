import numpy as np
from sklearn.preprocessing import minmax_scale

from sklearn.model_selection import cross_val_score as CVS, KFold
from sklearn.neural_network import MLPClassifier

from Test.read_data import ToFormNumpy


def main():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    minmax_scale(X, copy=False)

    #X, types, y = ToFormNumpy(r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Lagranj\Spame\data\own\(4595, 57).txt")



    k = 5

    k_fold = KFold(n_splits=k, shuffle=True, random_state=42)

    mlp = MLPClassifier(hidden_layer_sizes=(50, 200), activation='relu', max_iter=1000, alpha=1e-5,
                        solver='adam', verbose=False, tol=1e-4, random_state=1,
                        learning_rate_init=.1)

    max_mean = sum(CVS(mlp, X, y, cv=k_fold, n_jobs=4, scoring='accuracy')) / k

    print('Score = ', max_mean)

if __name__ == '__main__':
    main()
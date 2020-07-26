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

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasteralogy.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")


    y = y - 1

    #minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)


    drawobjects(X[:, [3, 5]], classes=y, isVisibleLabel=True)


if __name__ == '__main__':
    main()
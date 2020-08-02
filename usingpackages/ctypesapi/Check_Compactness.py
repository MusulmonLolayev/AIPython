from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormArray, ToFormNumpy
from Test.write_file import writeNP
from usingpackages.ctypesapi.cml import compactness
from uz.nuu.datamining.graphic.drawing import mscatter
from uz.nuu.datamining.own.estimations import Lagranj, DecomposionEstimation
from ai.own.fris import Fris
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, Normalizing_Estmation, Normalizing_Estmation1
import numpy as np

def main():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")

    y -= 1

    minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    compactness(X, y, types=types, metric=1)

if __name__ == '__main__':
    main()
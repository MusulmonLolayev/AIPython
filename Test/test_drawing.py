from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormArray, ToFormNumpy
from uz.nuu.datamining.graphic.drawing import mscatter, mscatter1
from uz.nuu.datamining.own.estimations import Lagranj, DecomposionEstimation
from datamining.own.fris import Fris
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, Normalizing_Estmation, Normalizing_Estmation1
import numpy as np

def main():

    X, types, y = ToFormNumpy(r"D:/test.txt")

    mscatter1(X, y, marker=['v', 's'], size=6, colors=['black', 'black'])

if __name__ == '__main__':
    main()
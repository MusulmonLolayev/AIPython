from sklearn.preprocessing import minmax_scale

from Test.read_data import ToFormNumpy
from Test.write_file import writeNP
from uz.nuu.datamining.graphic.drawing import mscatter
from ai.own.fris import Fris


def main():

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")

    y -= 1

    minmax_scale(X, copy=False)
    #Normalizing_Estmation(X, y)

    group, comp1 = Fris(X, y, types=types, file=None)

if __name__ == '__main__':
    main()
from Test.read_data import ToFormNumpy
from uz.nuu.datamining.own.reduction import ReductionOptimal


def main():

    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\gasterlogy1394.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")

    #y -= 1
    #y[y == 2] = 1

    for i in range(X.shape[1]):
        for j in range(i + 1,  X.shape[1]):
            ReductionOptimal(X[:, i], X[:, j], y)

if __name__ == '__main__':
    main()
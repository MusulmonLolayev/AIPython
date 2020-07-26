from Test.read_data import ToFormArray
from uz.nuu.datamining.own.functions import Normalizing_Min_Max
from uz.nuu.datamining.own.reduction import SammonProjection


def main():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\german.txt")
    #a, types, classes = ToFormArray("D:\\tanlanmalar\\imun2.txt")

    Normalizing_Min_Max(a, types)
    #print(a)

    projection = SammonProjection(a, 100, outputDimension = 2, types = types)
    print(projection)

if __name__ == '__main__':
    main()
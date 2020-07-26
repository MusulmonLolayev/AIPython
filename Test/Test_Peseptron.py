from Test.read_data import ToFormArray
from uz.nuu.datamining.graphic.drawing import drawobjects
from uz.nuu.datamining.nerualnetwork import NND
from uz.nuu.datamining.own.estimations import GeneralCriterion2D, FindOptimalInterval, IntervalEstimation
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, sortByClass


def main():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    for i in range(len(a)):
        classes[i] -= 1
    ln = [30, 12]
    Normalizing_Min_Max(a, types)
    nnd = NND(companents = 2)
    transformation = nnd.transformation(a, classes)
    b = []
    for i in transformation:
        b.append(i[0])
    print(GeneralCriterion2D(b, classes, ln = ln))
    b = []
    for i in transformation:
        b.append(i[1])
    print(GeneralCriterion2D(b, classes, ln = ln))

    x = []
    y = []
    for l in range(len(a)):
        x.append(transformation[l][0])
        y.append(transformation[l][1])

    values_copy = x.copy()
    sortedClass = sortByClass(values_copy, classes)
    # for i in range(len(sortedClass)):
    #   print(i, values_copy[i])
    res = []
    FindOptimalInterval(sortedClass, classes, res, ln = ln)

    for item in res:
        print(item)
    print(IntervalEstimation(res, len(a)))

    values_copy = y.copy()
    sortedClass = sortByClass(values_copy, classes)
    # for i in range(len(sortedClass)):
    #   print(i, values_copy[i])
    res = []
    FindOptimalInterval(sortedClass, classes, res, ln=ln)

    for item in res:
        print(item)
    print(IntervalEstimation(res, len(a)))

    drawobjects(transformation, classes=classes)

if __name__ == '__main__':
    main()
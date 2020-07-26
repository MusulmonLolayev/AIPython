from Test.read_data import ToFormArray
from uz.nuu.datamining.own.estimations import FindOptimalInterval
from uz.nuu.datamining.own.functions import sortByClass


def main():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")

    for i in range(len(a)):
        classes[i] -= 1
    ln = [30, 12]

    x = []
    y = []
    for l in range(len(a)):
        x.append(a[l][0])
        y.append(a[l][5])

    values_copy = y.copy()
    sortedClass = sortByClass(values_copy, classes)
    #for i in range(len(sortedClass)):
     #   print(i, values_copy[i])
    res = []
    FindOptimalInterval(sortedClass, classes, res, ln = ln)

    for item in res:
        print(item)

if __name__ == '__main__':
    main()
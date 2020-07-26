from Test.read_data import ToFormArray
from uz.nuu.datamining.own.estimations import GeneralCriterion2D


def main():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\MATBIO_MY.txt")
    ln = [0, 0]
    for i in range(len(classes)):
        classes[i] -= 1
        ln[classes[i]] += 1
    for j in range(len(a[0])):
        b = []
        for i in range(len(a)):
            b.append(a[i][j])
        sort = []
        res = GeneralCriterion2D(b, classes = classes, ln=ln, sort=sort)
        print(res[0], a[sort[res[2]]][j])
if __name__ == '__main__':
    main()
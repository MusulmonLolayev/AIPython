
from Test.read_data import ToFormArray, ToFormNumpy
from uz.nuu.datamining.exercises.exercise import exercise34, exercise4, exercise11


def main1():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    for i in range(len(a)):
        classes[i] -= 1

    i = input("Agar w larni kiritmoqchi bulsangiz 1 ni kiring, tasodifiy bo'lsa ixtiyoriy tugmani kiriting:")
    w = None
    if i == '1':
        w = []
        for i in range(len(a[0])):
            w.append(float(input('w[' + str(i + 1) + '] = ')))
    res = exercise34(a, classes, w = w)

    print("Max = ", res[0])
    print("t = ", res[1])

def main2():
    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    for i in range(len(a)):
        classes[i] -= 1

    res = sorted(exercise4(a, classes, types = types))
    for i in res:
        print(i, classes[i] + 1)

def main3():
    X, types, y = ToFormNumpy("D:\\tanlanmalar\\uzb_kor.txt")
    for i in range(X.shape[1]):
        exercise11(X[:, i], y)


if __name__ == '__main__':
    #main1()
    #main2()
    main3()

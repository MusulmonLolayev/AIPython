from Test.read_data import ToFormArray
from uz.nuu.datamining.own.estimations import GeneralCriterion2D, FindOptimalInterval, IntervalEstimation
from uz.nuu.datamining.own.functions import Normalizing_Min_Max, sortByClass
from uz.nuu.datamining.own.reduction import ReductionLeastSquare_2


def main():
    #a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    #ln = [30, 12]
    #names = ["(CBL) основная длина", "(LUJ) длина верхней челюсти", "(WID) ширина верхней челюсти", "(LUC) длина верхнего карнивора", "(LFM) длина первого верхнего моляра", "(WFM) ширина первого верхнего моляра"]
    #for i in range(len(a)):
     #  classes[i] -= 1

    #a, types, classes = ToFormArray("D:\\tanlanmalar\\imun2.txt")
    #names = ["Индекс_коморбидности", "Возраст", "АЛТ", "АСТ", "Билирубин_общий", "Непрямой_билирубин", "Креатинин", "Мочевина", "Глюкоза", "первый_курс", "всего_курсов", "стадия", "Class"]
    #ln = [36, 24]

    #a, types, classes = ToFormArray("D:\\tanlanmalar\\GIPER_MY.txt")
    #names = []
    #for i in range(len(a[0])):
    #    names.append("x" + str(i + 1))
    #ln = [404, 162]


    a, types, classes = ToFormArray("D:\\tanlanmalar\\IT_BORI_42_6.txt")
    names = []
    for i in range(len(a[0])):
        names.append("x" + str(i + 1))
    ln = [700, 300]

    for i in range(len(a)):
        classes[i] -= 1

    Normalizing_Min_Max(a, types)

    for i in range(len(a[0])):
        for j in range(i + 1, len(a[0])):
            x = []
            y = []
            for l in range(len(a)):
                x.append(a[l][i] + 0.00001)
                y.append(a[l][j] + 0.00001)
            #delta, res = ReductionLeastSquare(x, y, classes, ln=ln)
            #delta, res = ReductionLeastSquare_2(x, y, classes, ln=ln)

            #crit = GeneralCriterion2D(res, classes, ln=ln)
            #print("(", names[i], ",", names[j], ")", '\t', crit[0])
            #print(crit)

            #x = res.copy()
            sorted_class = sortByClass(x, classes)
            res = []
            crit = FindOptimalInterval(sorted_class, classes, res, ln=ln)
            for item in res:
                print(item)
            print("Count intervals: ", len(res))
            print("Crit: ", IntervalEstimation(res, len(x)))

if __name__ == '__main__':
    main()
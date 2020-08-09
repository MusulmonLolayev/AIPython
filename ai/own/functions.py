"""
This function is for calculate distance by Evklid modification
"""
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def Distance(a, b, types = None):
    distance = 0
    if types == None:
        for i, j in zip(a, b):
            distance += (i - j) ** 2
        distance = distance ** 0.5
    else:
        r = 0
        for i, j, k in zip(a, b, types):
            if k == 1:
                distance += (i - j) ** 2
            elif i != j:
                r += 1
        distance = distance ** 0.5 + r * (2 ** 0.5)
    return distance

class Table:
    def __init__(self, vs_ind, rad, count_vs=0, count_it=0, dis_from_vs=0, ind_from_vs = -1):
        self.rad = rad
        self.vs_ind = vs_ind
        self.count_it = count_it

        self.dis_from_vs = dis_from_vs
        self.ind_from_vs = ind_from_vs
        self.count_vs = count_vs

def sortByClass(values, classes):
    """
        Ushbu tartiblash algoritmi ikkita parametrga ega: birinchi parametr alomatning
    qiymatlari bo'lib list hisoblanadi; ikkinchisi esa, alomatning qaysi sinfga tegishli ekanligini anglatadi.
        Natija sifatida kirib keluvchi listning tartiblanishidan hosil bo'lgan indexlari qaytariladi.
        Agar ikkita har xil sinf vakili kelsa, u holda sinflarning tartibiga qarab joylashtiriladi.
    """
    result = []
    sorted_values = []
    for i in range(len(values)):
        min_val = 1.0e15
        min_index = i
        for j in range(len(values)):
            if values[j] < min_val:
                min_val = values[j]
                min_index = j

        sorted_values.append(values[min_index])
        values[min_index] = 1.0e15
        result.append(min_index)

    for i in range(len(sorted_values)):
        values[i] = sorted_values[i]
    return result

def inf_object(a, classes, types = None):
    m = len(a)
    inf_table = []
    for i in range(m):
        rad_min = 1e100
        ind_min = i
        for j in range(m):
            if classes[i] != classes[j]:
                dis = Distance(a[i], a[j], types)
                if dis < rad_min:
                    rad_min = dis
                    ind_min = j
        inf_table.append(Table(ind_min, rad_min))
    for i in range(m):
        rad_min = 1e100
        ind_min = i
        for j in range(m):
            if classes[i] == classes[j]:
                dis = Distance(a[i], a[j], types)
                if dis < inf_table[i].rad:
                    inf_table[i].count_it += 1
            else:
                if i == inf_table[j].vs_ind:
                    if inf_table[j].rad < rad_min:
                        rad_min = inf_table[j].rad
                        ind_min = j
        inf_table[i].dis_from_vs = rad_min
        inf_table[i].ind_from_vs = j
    for i in range(m):
        for j in range(m):
            if classes[i] != classes[j]:
                dis = Distance(a[i], a[j], types)
                if dis < inf_table[i].dis_from_vs:
                    inf_table[i].count_vs += 1
    return inf_table

def Normalizing_Min_Max(a, types = None):
    for j in range(len(a[0])):
        if types == None or types[j] != 0:
            _min = a[0][j]
            _max = a[0][j]
            for i in range(len(a)):
                if _min > a[i][j]:
                    _min = a[i][j]
                if _max < a[i][j]:
                    _max = a[i][j]
            diff = _max - _min
            for i in range(len(a)):
                a[i][j] = (a[i][j] - _min) / diff

def Normalizing_Min_Max(a, res, types = None):
    for j in range(len(a[0])):
        if types == None or types[j] != 0:
            _min = a[0][j]
            _max = a[0][j]
            for i in range(len(a)):
                if _min > a[i][j]:
                    _min = a[i][j]
                if _max < a[i][j]:
                    _max = a[i][j]
            diff = _max - _min
            for i in range(len(a)):
                a[i][j] = (a[i][j] - _min) / diff

def Length(classes):
    res = []
    groups = []
    for i in classes:
        t = True
        print(i)
        for j in groups:
            if j == i:
                t = False

        if t:
            groups.append(i)

    for i in groups:
        res.append(0)

    return res#, groups

def OwnForm(a, forObject = 0, types = None):
    b = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            if types[j] == 0:
                if a[i][j] == a[forObject][j]:
                    row.append(0)
                else:
                    row.append(1)
            else:
                row.append(abs(a[i][j] - a[forObject][j]))
        b.append(row)
    return b

def Normalizing_Estmation(X, y, ln = None, types = None):
    if ln is None:
        ln = np.unique(y, return_counts=True)[1]
    if types is None:
        types = np.full(shape=(X.shape[1]), fill_value=1)

    for j in range(X.shape[1]):
        if types[j] == 1:
            b = X[:, j].copy()
            res = GeneralCriterion2D(b, y, ln=ln)
            print(res[0])
            if X[int(res[3]), j] != X[int(res[1]), j]:
                X[:, j] = res[0] * (X[:, j] - X[int(res[2]), j]) / (X[int(res[3]), j] - X[int(res[1]), j])
                #print(X[int(res[1]), j], X[int(res[2]), j], X[int(res[3]), j], res[0])
                #X[:, j] = (X[:, j] - X[int(res[2]), j]) / (X[int(res[3]), j] - X[int(res[1]), j])
            else:
                print("warning : ", X[int(res[3]), j], X[int(res[1]), j])
        else:
            X[:, j] = (X[:, j] - min(X[:, j])) / (max(X[:, j]) - min(X[:, j]))

def Normalizing_Estmation1(X, y, ln = None):
    if ln == None:
        ln = np.unique(y, return_counts=True)[1]
    with ThreadPoolExecutor(max_workers=X.shape[1]) as executor:
        for j in range(X.shape[1]):
            b = X[:, j].copy()
            future = executor.submit(GeneralCriterion2D, b, y, ln=ln)
            res = future.result()
            X[:, j] = res[0] * (X[:, j] - X[int(res[2]), j]) / (X[int(res[3]), j] - X[int(res[1]), j])

def GeneralCriterion2D(values, classes, ln=None):
    """
        Ushbu funksiya, sinflararo o'xshashlik va sinflararo farq kriteriyasini hisoblash uchun xizmat qiladi:
        values - miqdoriy alomatning qiymatlari, list;
        classes - miqdoriy alomatning sinfi, list;
        ln - sinflardagi obyektlar soni, list;
        Qaytuvchi natija:
        max_value - kriteriyaning qiymati;
        min_index - miqdoriy alomatning minimum qiymati indeksi;
        opt_index - miqdoriy alomatning kriteriya bo'yicha optimal chegarasining indexi;
        max_index - miqdoriy alomatning maximum qiymati indeksi;
    """
    # Tartiblash uchun kiruvchi qiymatlardan nusxalash

    if ln is None:
        print(classes)
        _, ln = np.unique(classes, return_counts=True)

    values_copy = values.copy()
    sortedClass = sortByClass(values_copy, classes)
    # u[x, y] is count of x index of interval and y class. x is index of interval's and y is index of class. Where are x = {0, 1}.
    u = [[0, 0], [0, 0]]
    # Result values
    # Default of max value of Kriteriya is 0
    max_value = 0
    opt_index = sortedClass[0]
    min_index = sortedClass[0]
    max_index = sortedClass[len(values) - 1]
    # maxraj
    m1 = ln[0] * (ln[0] - 1) + ln[1] * (ln[1] - 1)
    m2 = 2 * ln[0] * ln[1]
    # for begin from 0 to len(vaules) - 1, beacuse each interval need min one object
    for x in range(0, len(values) - 1):
        # Count object's in fisrt interval by class
        u[0][classes[sortedClass[x]]] += 1

        # Calculate len of object's by class in second interval
        u[1][0] = ln[0] - u[0][0]
        u[1][1] = ln[1] - u[0][1]

        # if current object and next object aren't eqvivalent
        if values[sortedClass[x]] != values[sortedClass[x + 1]]:
            sum1 = 0.0
            sum2 = 0.0
            # Furmulation
            for y in range(0, 2):
                for z in range(0, 2):
                    sum1 += u[y][z] * (u[y][z] - 1)
                    sum2 += u[y][z] * (ln[1 - z] - u[y][1 - z])
            current_max = (sum1 / m1) * (sum2 / m2)
            # Check current max than more max value
            if current_max > max_value:
                max_value = current_max
                opt_index = sortedClass[x]
                opt_index1 = sortedClass[x + 1]
    return max_value, min_index, opt_index, max_index

def GeneralValues(X, y):
    _X = np.empty(shape=X.shape, dtype=int)
    _y = np.empty(shape=y.shape)

    ests = np.empty(X.shape[1])

    for i in range(X.shape[1]):
        from ai.own.estimations import DivideIntervals
        group_index, group_estimation = DivideIntervals(X[:, i], y)

        _X[group_estimation <= 0.5, i] = 0
        _X[group_estimation > 0.5, i] = 1

        from ai.own.estimations import EstimationNominalFeture
        ests[i] = EstimationNominalFeture(_X[:, i], y)

    unique, ln = np.unique(y, return_counts=True)

    for i in range(_X.shape[0]):
        s = 0
        for j in range(_X.shape[1]):
            d = len(_X[np.logical_and(y == 0, _X[:, j] == _X[i, j]), j]) / ln[0] - \
                len(_X[np.logical_and(y == 1, _X[:, j] == _X[i, j]), j]) / ln[1]
            s += ests[j] * d

        _y[i] = s

    return _y

def AcceptableInterval(x, y, method='mean'):

    value_x = None
    value_y = None

    if method == 'mean':
        value_x = x.mean()
        value_y = y.mean()
    else:
        value_x = x.median()
        value_y = y.median()

    R = x / value_x - y / value_y

    return R.min(), R.max()
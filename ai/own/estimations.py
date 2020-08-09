import numpy as np

# The function is calculate Kriteriya 1
from ai.own.functions import sortByClass


def GeneralCriterion2D(values, classes, ln=None, sort=[]):
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
        _, ln = np.unique(classes, return_counts=True)

    values_copy = values.copy()
    sortedClass = sortByClass(values_copy, classes)
    [sort.append(i) for i in sortedClass]
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
    return max_value, min_index, opt_index, max_index

def Margin(values, classes):
    """
        Ushbu funksional ikkinchi sinf vakillarini birinchi joylashgan deb tassavur qilingan holda,
    ikkita sinf orasidagi masofani topadi.
    """
    min_k1 = 1e100
    max_k2 = -1e100
    max_v = -1e100
    min_v = 1e100
    for i, j in zip(values, classes):
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i
        if j == 0 and min_k1 > i:
            min_k1 = i
        if j == 1 and max_k2 < i:
            max_k2 = i
    return (min_k1 - max_k2) / (max_v - min_v)

class InfSepratedInterval:

    def __init__(self, begin = 0, end = 0, cr_1 = 0, cr_2 = 0, cr = 0):
        self.begin = begin
        self.end = end
        self.crit_val1 = cr_1
        self.crit_val2 = cr_2
        self.crit = cr
    def __str__(self):
        return "[{0}, {1}], {2}, {3}, {4}".format(self.begin, self.end, self.crit, self.crit_val1, self.crit_val2)

def FindOptimalInterval(sorted_class, classes, res, range_a = 0, range_b = None, ln = None):
    if range_b is None:
        range_b = len(classes)
    if range_a == range_b:
        inf = [0, 0]
        inf[classes[sorted_class[range_a]]] += 1
        crit = abs(inf[0] / ln[0] - inf[1] / ln[1])
        crit1 = inf[0] / (inf[0] + inf[1])
        crit2 = inf[1] / (inf[0] + inf[1])
        ob = InfSepratedInterval(range_a, range_b, crit1, crit2, crit)
        return ob

    max_crit = -1
    ob = InfSepratedInterval()
    #print(range_a, range_b)
    for i in range(range_a, range_b):
        inf = [0, 0]
        for j in range(i, range_b):
            inf[classes[sorted_class[j]]] += 1
            currect = abs(inf[0] / ln[0] - inf[1] / ln[1])
            if max_crit < currect:
                max_crit = currect
                ob.begin = i
                ob.end = j
                ob.crit = currect
                ob.crit_val1 = inf[0] / (inf[0] + inf[1])
                ob.crit_val2 = inf[1] / (inf[0] + inf[1])
    #print("max_crit = ", max_crit)
    if ob.begin == range_a and ob.end == range_b:
        return None
    else:
        res.append(ob)
        # left side
        if ob.begin > range_a:
            left = FindOptimalInterval(sorted_class, classes, res, range_a = range_a, range_b = ob.begin - 1, ln = ln)
            if left != None:
                res.append(left)
        # right side
        if ob.end < range_b and  ob.end < len(classes) - 1:
            right = FindOptimalInterval(sorted_class, classes, res, range_a = ob.end + 1, range_b = range_b, ln = ln)
            if right != None:
                res.append(right)

def Check(x, y, a, b):
    _, ln = np.unique(y, return_counts=True)
    d = [0, 0]
    for i in range(a, b + 1):
        d[y[x[i]]] += 1

    print('d', d)
    nyu = [d[0] / ln[0], d[1] / ln[1]]
    w_current = f = nyu[0] / (nyu[0] + nyu[1])

    print(w_current)

def DivideIntervals(x, y, return_intervals=False):
    a = 0
    b = y.shape[0]
    # index of sorted x
    _x = np.argsort(x)
    _, ln = np.unique(y, return_counts=True)
    intervals = []

    #Check(_x, y, 23, 59)
    def inner(a, b):
        rng_opt = None
        w_opt = 0
        for i in range(a, b):
            if i == 0 or i > 0 and x[_x[i]] != x[_x[i - 1]]:
                j = i
                d = [0, 0]
                while j < b:
                    d[y[_x[j]]] += 1
                    if j == b - 1 or j < b - 1 and x[_x[j]] != x[_x[j + 1]]:
                        nyu = [d[0] / ln[0], d[1] / ln[1]]
                        w_current = abs(nyu[0] - nyu[1])
                        if w_current >= w_opt:
                            f = nyu[0] / (nyu[0] + nyu[1])
                            rng_opt = [i, j, f, _x[i], _x[j]]
                            w_opt = w_current

                    j += 1
        if rng_opt:
            intervals.append(rng_opt)
            # Go to left side
            if rng_opt[0] > a:
                inner(a, rng_opt[0])
            # Go to right side
            if rng_opt[1] < b:
                inner(rng_opt[1] + 1, b)

    inner(a, b)

    group_index = np.empty(shape=(y.shape[0]))
    group_estimation = np.empty(shape=(y.shape[0]))
    for i in range(len(intervals)):
        for item in range(intervals[i][0], intervals[i][1] + 1):
            group_index[_x[item]] = i
            group_estimation[_x[item]] = intervals[i][2]
    if return_intervals:
        return group_index, group_estimation, intervals
    return group_index, group_estimation


def EstimationNominalFeture(x, y):
    uniq_class, ln = np.unique(y, return_counts=True)
    uniq_grad = np.unique(x)
    g = np.empty(shape=(uniq_grad.shape[0], ln.shape[0]))
    l = np.empty(shape=(ln.shape[0]))
    for i in range(uniq_grad.shape[0]):
        for j in range(uniq_class.shape[0]):
            g[i][j] = len(x[np.logical_and(x == uniq_grad[i], y == uniq_class[j])])

    for i in range(uniq_class.shape[0]):
        l[i] = len(np.unique(x[y == uniq_class[i]]))

    dominator = 1
    for item in ln:
        dominator *= item

    s = 0
    for item in g:
        p = 1
        for i in item:
            p *= i
        s += p

    lymada = 1 - s / dominator

    d = [0, 0]
    if uniq_grad.shape[0] > 2:
        d[0] = (ln[0] - l[0] + 1) * (ln[0] - l[0])
        d[1] = (ln[1] - l[1] + 1) * (ln[1] - l[1])
    else:
        d[0] = ln[0] * (ln[0] - 1)
        d[1] = ln[1] * (ln[1] - 1)

    betta = 0
    if d[0] + d[1] > 0:
        for i in range(uniq_grad.shape[0]):
            for j in range(uniq_class.shape[0]):
                betta += g[i][j] * (g[i][j] - 1)
        betta /= (d[0] + d[1])

    return betta * lymada

def IntervalEstimation(intervals, m):
    res = 0
    for item in intervals:
        mul = item.crit_val1
        if item.crit_val1 < 0.5:
            mul = 1 - mul
        res += mul * (item.end - item.begin + 1)
    res /= m
    return res

def DecomposionEstimation(a_group, b_group, obj_count):
    group = 0
    a = np.empty((0, 1), dtype=int)
    for i in a_group:
        group += 1
        for j in i:
            a = np.append(a, np.array(group))

    group = 0
    b = np.empty((0, 1), dtype=int)
    for i in b_group:
        group += 1
        for j in i:
            b = np.append(b, np.array(group))


    c = np.empty((0, 1), dtype=int)
    grad = 0
    check_grad = np.empty((0, 3), dtype=int)

    for i in range(obj_count):
        t = True
        for j in check_grad:
            if j[0] == a[i] and j[1] == b[i]:
                # Set exits gradation
                c = np.append(c, np.array(j[2]))
                t = False
                break
        if t:
            # add new gradation
            grad += 1
            c = np.append(c, np.array(grad))
            check_grad = np.append(check_grad, [[a[i], b[i], grad]], axis=0)
    a_sum = 0
    b_sum = 0
    c_sum = 0
    for i, j, l in zip(np.unique(a, return_counts=True)[1],
                       np.unique(b, return_counts=True)[1],
                       np.unique(c, return_counts=True)[1]):
        a_sum += i * i
        b_sum += j * j
        c_sum += l * l
    return 2 * c_sum / (a_sum + b_sum)

def Lagranj1(X, y):

    K1 = y == 0
    K2 = y == 1

    means1 = np.mean(X[K1], axis = 0)
    means2 = np.mean(X[K2], axis = 0)

    tetas = np.empty((0, 1))
    lyamdas = np.empty((0, 1))

    for j in range(X.shape[1]):
        teta = (np.sum(np.abs(X[K1, j] - means1[j])) + np.sum(np.abs(X[K2, j] - means2[j]))) / X.shape[0]
        lyamda = (np.sum(np.abs(X[K2, j] - means1[j])) + np.sum(np.abs(X[K1, j] - means2[j]))) / X.shape[0]

        tetas = np.append(tetas, teta)
        lyamdas = np.append(lyamdas, lyamda)


    surat = lyamdas - tetas
    cond = surat > 0
    maxraj = np.sum(surat[cond])
    w = surat / maxraj
    w[surat < 0] = 0
    return w

def Lagranj(X, y, types, ln):

    # preproccesing
    X1 = np.empty(shape=X.shape[0], dtype=np.int)
    lyamdas = np.empty(shape=(X.shape[1]))
    tetas = np.empty(shape=(X.shape[1]))

    m1 = ln[0] * ln[1]
    m2 = ln[0] * (ln[0] - 1) + ln[1] * (ln[1] - 1)

    for j in range(X.shape[1]):
        if types[j] == 0:
            X1 = X[:, j]
        else:
            b = X[:, j].copy()
            res = GeneralCriterion2D(b, y, ln=ln, sort=[])
            print(j, res[0], X[res[2], j])
            X1[X[:, j] <= X[res[2], j]] = 0
            X1[X[:, j] > X[res[2], j]] = 1

        unique = np.unique(X1)

        g = np.empty(shape=(len(unique), 2), dtype=np.int)
        for i in range(len(unique)):
            g[i, 0] = len(X1[(X1 == unique[i]) & (y == 0)])
            g[i, 1] = len(X1[(X1 == unique[i]) & (y == 1)])


        lyamdas[j] = 1 - sum(g[:, 0] * g[:, 1]) / m1
        tetas[j] = 1 - sum(g[:, 0] * (g[:, 0] - 1) + g[:, 1] * (g[:, 1] - 1)) / m2

    surat = lyamdas - tetas
    cond = surat > 0
    maxraj = np.sum(surat[cond])
    w = surat / maxraj
    w[surat < 0] = 0
    return w
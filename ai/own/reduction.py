from random import randrange
from ai.own.estimations import GeneralCriterion2D, Margin, FindOptimalInterval
from math import log

import numpy as np

from ai.own.functions import sortByClass, Distance

T = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, 1, 1],
    [-1, -1, -1],
    [1, 1, -1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, 1, -1]])

def ReductionOptimal(x1, x2, y, IsNormalize=False):
    _, ln = np.unique(y, return_counts=True)

    x3 = x1 * x2

    res1 = GeneralCriterion2D(x1, y, ln=ln)
    res2 = GeneralCriterion2D(x2, y, ln=ln)
    res3 = GeneralCriterion2D(x3, y, ln=ln)

    if not IsNormalize:
        x1 = (x1 - x1[res1[2]]) / (x1[res1[3]] - x1[res1[1]])
        x2 = (x2 - x2[res2[2]]) / (x2[res2[3]] - x2[res2[1]])
        x3 = (x3 - x3[res3[2]]) / (x3[res3[3]] - x3[res3[1]])

    res_opt = -2
    t_opt = None

    for i in range(T.shape[0]):
        t = T[i]
        d = t[0] * x1 + t[1] * x2 + t[2] * x3
        res_current = Mar(d, y)
        if res_opt < res_current:
            res_opt = res_current
            t_opt = i

    s = 0
    s_opt = None
    res_opt_By_s = res_opt
    t = T[t_opt]
    while s <= 1:
        d = s * (t[0] * x1 + t[1] * x2) +  (1 - s) * t[2] * x3
        res_current = Mar(d, y)
        if res_opt_By_s < res_current:
            res_opt_By_s = res_current
            s_opt = s
        s += 0.1

    t = T[t_opt]
    s = s_opt

    d2 = None

    d1 = t[0] * x1 + t[1] * x2 + t[2] * x3
    res1 = GeneralCriterion2D(d1, y, ln=ln)

    if s != None:
        d2 = s * (t[0] * x1 + t[1] * x2) + (1 - s) * t[2] * x3
        res2 = GeneralCriterion2D(d2, y, ln=ln)

    if s_opt == None or res1[0] > res2[0]:
        s_opt = None
        print(res1, t_opt, s_opt, res_opt)
    elif res1[0] < res2[0]:
        res_opt = res_opt_By_s
        print(res2, t_opt, s_opt, res_opt)
    else:
        margin1 = Mar(d1, y)
        margin2 = Mar(d2, y)
        if margin1 > margin2:
            s_opt = None
            print(res1, t_opt, s_opt, res_opt)
        else:
            res_opt = res_opt_By_s
            print(res2, t_opt, s_opt, res_opt)

def ReductionOptimal2(x1, x2, y, IsNormalize=False):
    _, ln = np.unique(y, return_counts=True)

    x3 = x1 * x2

    res1 = GeneralCriterion2D(x1, y, ln=ln)
    res2 = GeneralCriterion2D(x2, y, ln=ln)
    res3 = GeneralCriterion2D(x3, y, ln=ln)

    if not IsNormalize:
        x1 = (x1 - x1[res1[2]]) / (x1[res1[3]] - x1[res1[1]])
        x2 = (x2 - x2[res2[2]]) / (x2[res2[3]] - x2[res2[1]])
        x3 = (x3 - x3[res3[2]]) / (x3[res3[3]] - x3[res3[1]])

    res_opt = [0]
    t_opt = None

    for i in range(T.shape[0]):
        t = T[i]
        d = t[0] * x1 + t[1] * x2 + t[2] * x3
        res_current = GeneralCriterion2D(d, y, ln=ln)
        if res_opt[0] < res_current[0]:
            res_opt = res_current
            t_opt = i

    s = 0
    s_opt = None
    res_opt_By_s = res_opt
    t = T[t_opt]
    while s <= 1:
        d = s * (t[0] * x1 + t[1] * x2) +  (1 - s) * t[2] * x3
        res_current = GeneralCriterion2D(d, y, ln=ln)
        if res_opt_By_s[0] < res_current[0]:
            res_opt_By_s = res_current
            s_opt = s
        s += 0.1

    if res_opt[0] > res_opt_By_s[0] or s_opt == None:
        s_opt = None
        d1 = t[0] * x1 + t[1] * x2 + t[2] * x3
        margin = Mar(d1, y)
        print(res_opt, t_opt, s_opt, margin)
    elif res_opt[0] < res_opt_By_s[0]:
        res_opt = res_opt_By_s
        d2 = s * (t[0] * x1 + t[1] * x2) + (1 - s) * t[2] * x3
        margin = Mar(d2, y)
        print(res_opt, t_opt, s_opt, margin)
    else:
        t = T[t_opt]
        s = s_opt

        d1 = t[0] * x1 + t[1] * x2 + t[2] * x3
        d2 = s * (t[0] * x1 + t[1] * x2) + (1 - s) * t[2] * x3

        margin1 = Mar(d1, y)
        margin2 = Mar(d2, y)

        if margin1 > margin2:
            s_opt = None
            print(res_opt, t_opt, s_opt, margin1)
        else:
            res_opt = res_opt_By_s
            print(res_opt, t_opt, s_opt, margin2)

def Mar(x, y):
    return (min(x[y == 0]) - max(x[y == 1])) / (max(x) - min(x))

def ReductionOptimal1(x, y, classes, crit_x = None, crit_y = None, ln = None):
    """
        Ushbu funksiya ikkita miqdoriy alomatni son o'qiga nochiziqli akslantiradi.
    """
    if crit_x == None:
        crit_x = GeneralCriterion2D(x, classes, ln)

        min_a = x[crit_x[1]]
        opt_a = x[crit_x[2]]
        max_a = x[crit_x[3]]
        sub = max_a - min_a;

        for i in range(len(x)):
            x[i] = (x[i] - opt_a) / sub
    if crit_y == None:
        crit_y = GeneralCriterion2D(y, classes, ln)
        min_b = y[crit_y[1]]
        opt_b = y[crit_y[2]]
        max_b = y[crit_y[3]]

        sub = max_b - min_b;
        for i in range(len(x)):
            y[i] = (y[i] - opt_b) / sub
    # print(crit_a, crit_b)

    d = []
    for i, j in zip(x, y):
        d.append(i * j)
    crit_d = GeneralCriterion2D(d, classes, ln)
    d_min = d[crit_d[1]]
    d_opt = d[crit_d[2]]
    d_max = d[crit_d[3]]
    coef = crit_d[0] / (d_max - d_min)
    for i in range(len(d)):
        d[i] = (d[i] - d_opt) * coef

    # max_value, min_index, opt_index, max_index, T_opt, s_opt, func_opt
    crit_c = [0, 0, 0, 0, 0, None, 0]

    for item in range(len(T)):
        c = []
        for i in range(len(x)):
            c.append(T[item][0] * x[i] + T[item][1] * y[i] + T[item][2] * d[i])
        res = GeneralCriterion2D(c, classes, ln)
        # print(res)
        func_opt = Margin(y, classes)
        if res[0] > crit_c[0] or res[0] == crit_c[0] and crit_c[6] < func_opt:
            crit_c[0] = res[0]
            crit_c[1] = res[1]
            crit_c[2] = res[2]
            crit_c[3] = res[3]
            crit_c[4] = item
            crit_c[6] = func_opt
    s = 0
    while s <= 1:
        c = []
        item = crit_c[4]
        for i in range(len(x)):
            c.append(s * (T[item][0] * x[i] + T[item][1] * y[i]) + (1 - s) * T[item][2] * d[i])
        res = GeneralCriterion2D(c, classes, ln)
        # print(res)
        func_opt = Margin(y, classes)
        if res[0] > crit_c[0] or res[0] == crit_c[0] and crit_c[6] < func_opt:
            crit_c[0] = res[0]
            crit_c[1] = res[1]
            crit_c[2] = res[2]
            crit_c[3] = res[3]
            crit_c[6] = func_opt
        s += 0.1
    return crit_c

def ReductionLeastSquare(x, y, classes, ln = None):
    x_sorted = x.copy()
    x_sortedClass = sortByClass(x_sorted, classes)
    x_res = []
    FindOptimalInterval(x_sortedClass, classes, x_res, ln = ln)

    y_sorted = y.copy()
    y_sortedClass = sortByClass(y_sorted, classes)
    y_res = []
    FindOptimalInterval(y_sortedClass, classes, y_res, ln = ln)

    def Func(ind, is_x_or_y = True):
        t = True
        if is_x_or_y:
            for i in range(len(x_res)):
                if x_sorted[x_res[i].begin] <= x[ind] and x[ind] <= x_sorted[x_res[i].end] or x_sorted[x_res[i].begin] == x[ind] or x[ind] == x_sorted[x_res[i].end]:
                    t = False
                    if classes[ind] == 0:
                        return x_res[i].crit_val1
                    else:
                        return x_res[i].crit_val2
        else:
            for i in range(len(y_res)):
                if y_sorted[y_res[i].begin] <= y[ind] and y[ind] <= y_sorted[y_res[i].end] or y_sorted[y_res[i].begin] == y[ind] and y[ind] == y_sorted[y_res[i].end]:
                    t = False
                    if classes[ind] == 0:
                        return y_res[i].crit_val1
                    else:
                        return y_res[i].crit_val2
        print("T = ", t)

    a1 = 0
    b1 = 0
    c1 = 0
    a2 = 0
    b2 = 0
    c2 = 0
    for i in range(len(x)):
        a1 += log(x[i]) ** 2
        b1 += log(x[i]) * log(y[i])
        c1 += Func(i) * Func(i, False) * log(x[i])

        #a2 += log(x[i]) * log(y[i])
        b2 += log(y[i]) ** 2
        c2 += Func(i) * Func(i, False) * log(y[i])
    a2 = b1

    delta = [0, 0]
    sub = a2 * b1 - a1 * b2

    if sub == 0:
        sub += 1e-10
        print("a = ", a2, b1, a1, b2)

    delta[0] = (b1 * c2 - c1 * b2) / sub
    delta[1] = (a1 * c2 - a2 * c1) / sub

    res = []
    for i in range(len(x)):
        res.append((x[i] ** delta[0]) / (y[i] ** delta[1]))
    return delta, res

def ReductionLeastSquare_2(x, y, classes, ln = None):
    x_sorted = x.copy()
    x_sortedClass = sortByClass(x_sorted, classes)
    x_res = []
    FindOptimalInterval(x_sortedClass, classes, x_res, ln = ln)

    y_sorted = y.copy()
    y_sortedClass = sortByClass(y_sorted, classes)
    y_res = []
    FindOptimalInterval(y_sortedClass, classes, y_res, ln = ln)

    xy = []
    for item in range(len(x)):
        xy.append(x[item] * y[item])
    xy_sorted = xy.copy()
    xy_sortedClass = sortByClass(xy_sorted, classes)
    xy_res = []
    FindOptimalInterval(xy_sortedClass, classes, xy_res, ln = ln)

    def Func(ind, is_x_or_y = 'x'):
        t = True
        if is_x_or_y == 'x':
            for i in range(len(x_res)):
                if x_sorted[x_res[i].begin] <= x[ind] and \
                                x[ind] <= x_sorted[x_res[i].end] or \
                                x_sorted[x_res[i].begin] == x[ind] or \
                                x[ind] == x_sorted[x_res[i].end]:
                    t = False
                    if classes[ind] == 0:
                        return x_res[i].crit_val1
                    else:
                        return x_res[i].crit_val2
        elif is_x_or_y == 'y':
            for i in range(len(y_res)):
                if y_sorted[y_res[i].begin] <= y[ind] and \
                                y[ind] <= y_sorted[y_res[i].end] or \
                                        y_sorted[y_res[i].begin] == y[ind] and \
                                        y[ind] == y_sorted[y_res[i].end]:
                    t = False
                    if classes[ind] == 0:
                        return y_res[i].crit_val1
                    else:
                        return y_res[i].crit_val2
        else:
            for i in range(len(xy_res)):
                if xy_sorted[xy_res[i].begin] <= xy[ind] and \
                                xy[ind] <= xy_sorted[xy_res[i].end] or \
                                        xy_sorted[xy_res[i].begin] == xy[ind] and \
                                        xy[ind] == xy_sorted[xy_res[i].end]:
                    t = False
                    if classes[ind] == 0:
                        return xy_res[i].crit_val1
                    else:
                        return xy_res[i].crit_val2
        print("T = ", t)

    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    a2 = 0
    b2 = 0
    c2 = 0
    d2 = 0
    a3 = 0
    b3 = 0
    c3 = 0
    d3 = 0
    for i in range(len(x)):
        a1 += x[i] ** 2
        b1 += x[i] * y[i]
        c1 += x[i] * x[i] * y[i]
        #temp = Func(i, 'x') + Func(i, 'y') + Func(i, 'xy')
        temp = Func(i, 'x') + Func(i, 'y') + Func(i, 'x') * Func(i, 'x')
        d1 += x[i] * temp


        #a2 = b1
        b2 += y[i] ** 2
        c2 += x[i] * y[i] * y[i]
        d2 += y[i] * temp

        #a3 = c1
        #b3 = c2
        c3 += (x[i] * y[i]) ** 2
        d3 += x[i] * y[i] * temp

    a2 = b1
    a3 = c1
    b3 = c2

    maxraj = a1 * b2 * c3 - a1 * b3 * c2 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1

    delta = [0, 0, 0]

    if maxraj == 0:
        maxraj += 1e-10

    delta[0] = (b1 * c2 * d3 - b1 * c3 * d2 - b2 * c1 * d3 + b2 * c3 * d1 + b3 * c1 * d2 - b3 * c2 * d1) / maxraj
    delta[1] = -(a1 * c2 * d3 - a1 * c3 * d2 - a2 * c1 * d3 + a2 * c3 * d1 + a3 * c1 * d2 - a3 * c2 * d1) / maxraj
    delta[2] = (a1 * b2 * d3 - a1 * b3 * d2 - a2 * b1 * d3 + a2 * b3 * d1 + a3 * b1 * d2 - a3 * b2 * d1) / maxraj

    res = []
    for i in range(len(x)):
        res.append(delta[0] * x[i] + delta[1] * y[i] + delta[2] * xy[i])
    return delta, res

def FuncValues(x, border_a, border_b, classes, is_a = True, is_b = True):
    count = 0
    ln = [0, 0]
    for i in range(len(x)):
        t = (border_a < x[i] or is_a and border_a == x[i]) and (x[i] < border_b or is_b and x[i] == border_b)
        if t:
            count += 1
            ln[classes[i]] += 1
    return ln[0] / count, ln[1] / count;

class SammonProjection:
    def __init__(self, inputdata, Iteration, outputDimension = 1, types = None):
        self.inputdata = inputdata
        self.Iteration = Iteration
        self.outputDimension = outputDimension
        self.types = types
        self.error = -1


    def transformation(self, projection = []):
        s = 0
        sumDij = 0

        m = len(self.inputdata)
        distanceMatrix = []
        if len(projection) == 0:
            self.projection = []
            for i in range(m):
                row = []
                for j in range(self.outputDimension):
                    row.append(randrange(m))
                    self.projection.append(row)
        else:
            self.projection = projection

        for i in range(m):
            row = []
            for j in range(m):
                if i == j:
                    row.append(0)
                else:
                    row.append(Distance(self.inputdata[i], self.inputdata[j], self.types))
            distanceMatrix.append(row)

        for iter in range(self.Iteration):
            print(iter)
            for i in range(m):
                for j in range(m):
                    if i != j:
                        dij = distanceMatrix[i][j]
                        dijProjection = Distance(self.projection[i], self.projection[j])
                        if dijProjection == 0:
                            dijProjection = 1e-10

                        e = iter / self.Iteration
                        delta = e * (dij - dijProjection) / dijProjection

                        s += (dij - dijProjection) * (dij - dijProjection) / dij
                        sumDij += dij

                        for l in range(self.outputDimension):
                            correction = delta * (self.projection[i][l] - self.projection[j][l])
                            self.projection[i][l] += correction
                            self.projection[j][l] -= correction
        self.error = (s / sumDij) * 100
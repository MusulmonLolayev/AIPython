import random
from math import sqrt

import numpy as np


def generateTmatrix(n):
    t = []
    for i in range(2 ** n):
        row = []
        b = bin(i)
        b = b.replace('0b', '')
        while len(b) < n:
            b = '0' + b
        for j in b:
            if j == '0':
                row.append(-1)
            else:
                row.append(1)
        t.append(row)
    return t

def MaxMinByClass(R, classes):
    Min_K1 = None
    Max_K2 = None
    for i in range(len(R)):
        if classes[i] == 0:
            if Min_K1 == None or Min_K1 > R[i]:
                Min_K1 = R[i]
        else:
            if Max_K2 == None or Max_K2 < R[i]:
                Max_K2 = R[i]
    return Min_K1, Max_K2

def exercise34(a, classes, w = None):
    # Obyektlar soni aniqlash
    m = len(a)
    # alomatlar sonini aniqlash
    n = len(a[0])
    # Agar w vaznlar yo'q bulsa ularni randomdan olish qulaylim uchun
    if w == None:
        w = []
        for i in range(n):
            w.append(random.random() + 0.00001)
    # t i j larni gereratsiya qilish martitasi
    t = generateTmatrix(n)
    # t i j larning o'lchami
    len_t = len(t)
    #Obyektlarning R(S) funksiya qiymarni saqlash toplami
    R = []
    # Min(R(S)) - Max(R(S)) = Max tanlash uchun qiymat
    Max = None
    # t ij lar faqat -1 bir bo'lsin birinchi holda
    Max_T_Ind = 0
    # t i j larning hamma hollarini qarash
    for l in range(len_t):
        # R ni tozalab qo'yish
        R.clear()
        # har bir obyekt uchun R(S)=Sum(ti*wi*xi) topish
        for i in range(m):
            # summa bo'lgani uchun nol deb olindi
            s = 0
            # alomatlar bo'yicha ti * wi * xi larning summasi
            for j in range(n):
                s += t[l][j] * w[j] * a[i][j]
            # R ga qo'shib qo'yish
            R.append(s)
        # Min va Max larni topish
        Min_K1, Max_K2 = MaxMinByClass(R, classes)
        print(R)
        print(Min_K1, Max_K2)
        print(t[l])
        # Ayirmani olish
        temp = Min_K1 - Max_K2
        print("Max = ", temp)
        # Agar olingan natija berilganlardan katta bo'lsa O'zlashtirish
        if Max == None or temp > Max:
            Max = temp
            Max_T_Ind = l
    # natijani qaytarish
    return Max, t[Max_T_Ind]

def Evklid(a, b):
    s = 0
    for i, j in zip(a, b):
        s += (i - j) ** 2
    return sqrt(s)
def Chebyoshev(a, b):
    max1 = 0
    for i, j in zip(a, b):
        d = abs(i - j)
        if d > max1:
            max1 = d
    return max1

def exercise4(a, classes, types = None):
    # qobiq obyekt indexlarini saqalash uchun toplam
    r = set()

    # Obyektlar soni aniqlash
    m = len(a)
    # alomatlar sonini aniqlash
    n = len(a[0])

    # har bir obyekt uchun qidirish
    for i in range(m):
        # eng yaqin masofani anilash uchun
        min = None
        # eng yaqin obyekt indexsi
        l = None
        # i chi obyektga qarama-qarshi sinfdagi eng yaqin obyektni topish
        for j in range(m):
            if classes[i] != classes[j]:
                # i va j obyekt orasidagi masofa
                temp = Chebyoshev(a[i], a[j])
                # Agar masofa yaqin bo'lsa almashtirish kerak
                if min == None or min > temp:
                    min = temp
                    l = j
        # l obyektga eng yaqin qarama-qarshi sinfdagi obyektni topish
        min = None
        k = None
        for j in range(m):
            if classes[l] != classes[j]:
                # l va j obyekt orasidagi masofa
                temp = Chebyoshev(a[l], a[j])
                # Agar masofa yaqin bo'lsa almashtirish kerak
                if min == None or min > temp:
                    min = temp
                    k = j
        r.add(k)
    return r

def exercise11(X, y):
    _, ln = np.unique(y, return_counts=True)

    unique, _= np.unique(X, return_counts=True)

    z = []
    _z = []
    for i in unique:
        row = []
        _row = []

        s = 0
        for j in X[y == 1]:
            if j == i:
                s += 1
        _s = s
        row.append(s)

        s = 0
        for j in X[y == 2]:
            if j == i:
                s += 1
        row.append(s)
        _row.append(s)
        _row.append(_s)
        z.append(row)
        _z.append(_row)


    s = 0
    for i in z:
        for j in i:
            s += j * (j - 1)

    _s = 0
    for i in range(len(z)):
        for j in range(2):
            _s += z[i][j] * _z[i][j]


    print(z)
    print(_z)

    print(s, _s)

    m1 = ln[0] * (ln[0] - 1) + ln[1] * (ln[1] - 1)

    m2 = 2 * ln[0] * ln[1]


    res = s / m1 - _s / m2

    print(res)
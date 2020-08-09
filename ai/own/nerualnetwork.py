import random
from math import exp
import math


class NND:
    def __init__(self, companents = 1, eps = 0.001, tau = None):
        self.companents = companents
        self.tau = tau
        self.eps = eps
        if self.tau == None:
            self.tau = []
            for i in range(self.companents):
                self.tau.append(random.random())

    def transformation(self, a, classes):
        # natija uchun, m obyekt va comoanents ta alomat bo'ladi
        result = []
        # Vaznlar, companents ta qator va n ta ustun bo'ladi
        w = []
        # a ning ulchamlari
        m = len(a)
        n = len(a[0])
        #vaznlarni nol bilan to'ldirish
        for i in range(self.companents):
            row = []
            for j in range(n):
                #row.append(0)
                row.append(random.random())
            w.append(row)

        # har bir obyekt uchun yangi alomatlarni hisoblash
        for i in range(m):
            t = False
            while not t:
                # alomat
                row = []
                for j in range(self.companents):
                    s = 0
                    for l in range(n):
                        s += w[j][l] * a[i][l] - self.tau[j]
                    row.append(s)

                t = self.Check(row, classes[i])
                if t:
                    result.append(row)
                else:
                    # u holda qiymatlarni oshirish
                    for j in range(self.companents):
                        for l in range(n):
                            if classes[i] == 0:
                                w[j][l] += a[i][l]
                            else:
                                w[j][l] -= a[i][j]
        return result

    def Activation(self, x):
        return 1.0 / (1 + pow(2.7, x))

    def Check(self, a, obj_class):
        for i in range(len(a)):
            if a[i] < self.eps:
                return False
        return True
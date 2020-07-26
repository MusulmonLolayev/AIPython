# Berilganlarni kiritish
from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b * b - 4 * a * c
try:
    if D < 0:
        print("Tenglamaga haqiyqiy yechimga ega emas!")
    elif D == 0:
        x = b / (2 * a)
        print("Tenglama bitta yechimga ega:")
        print("x = ", x)
    else:
        x1 = (b + sqrt(D)) / (2 * a)
        x2 = (b - sqrt(D)) / (2 * a)
        print("tenglama ikkita yechimga ega:")
        print("x1 = ", x1, "\nx2 = ", x2)
except ZeroDivisionError as exp:
    print("Nolga bo'lish mumkin emas.\nXatolik: ", exp)
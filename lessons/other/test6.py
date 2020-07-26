# Berilganlarni kiritish
from cmath import sqrt
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
except ValueError as exp:
    print("Berilgalarni kiritishda xato:\n", exp)
D = b * b - 4 * a * c
if D < 0:
    print("Tenglamaga haqiyqiy yechimga ega emas!")
elif D == 0:
    print("Tenglama bitta yechimga ega:")
    x = b / (2 * a)
    print("x = ", x)
else:
    print("tenglama ikkita yechimga ega:")
    x1 = (b + sqrt(D)) / (2 * a)
    x2 = (b - sqrt(D)) / (2 * a)
    print("x1 = ", x1, "\nx2 = ", x2)

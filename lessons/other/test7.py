# Berilganlarni kiritish
from math import sqrt
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    D = b * b - 4 * a * c
    if D < 0:
        raise \
            ValueError("Diskreminant "
            "noldan kichik bo‘lmasligi kerak")
    elif D == 0:
        x = b / (2 * a)
        print("Tenglama bitta yechimga ega:")
        print("x = ", x)
    else:
        x1 = (b + sqrt(D)) / (2 * a)
        x2 = (b - sqrt(D)) / (2 * a)
        print("tenglama ikkita yechimga ega:")
        print("x1 = ", x1, "\nx2 = ", x2)
except ValueError as exp:
    print(exp)
except ZeroDivisionError as exp:
    print("Nolga bo'lish mumkin emas:\n", exp)
except Exception as exp:
    print("Xarolik bor:\n", exp)
finally: print("Dastur yakunlandi")
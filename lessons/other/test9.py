# a va b sonlar ustida arfimetik
# amalrni bajaruvchi funksiyalar
def Qoshish(a, b):
    return a + b
def Ayrish(a, b):
    return a - b
def Kopaytirish(a, b):
    return a * b
def Bolish(a, b):
    return a // b
def Qoldiq(a, b):
    return a % b
def Daraja(a, b):
    return a ** b
# Operation funksiyasi
def Operation(func, a, b):
    return func(a, b)

try:
    a = int(input("a = "))
    b = int(input("b = "))

    print("a + b = ", Operation(Qoshish, a, b))
    print("a - b = ", Operation(Ayrish, a, b))
    print("a * b = ", Operation(Kopaytirish, a, b))
    print("a // b = ", Operation(Bolish, a, b))
    print("a % b = ", Operation(Qoldiq, a, b))
    print("a ^ b = ", Operation(Daraja, a, b))

except ValueError as exp:
    print("Berilganlarni kirishtishda xatolik.\n", exp)
except ZeroDivisionError as exp:
    print("Nolga bo'lish mumkin emas.\n", exp)
except Exception as exp:
    print("Xatolik bo'ldi.\n", exp)
finally:
    print("Dastur yukunlandi.")
from math import sqrt
# Biribchi funksiya, 3 ta kesmani funksiya bo'lishiga tekshirish
def IsTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
# Yuzasini topsih
def Uchburchak_Yuzasi(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        raise ValueError("Kesmaning uzunligi noldan katta bo'lishi kerak")
    if IsTriangle(a, b, c):
        print(Uchburchak_Yuzasi(a, b, c))
    if IsTriangle(a, b, d):
        print(Uchburchak_Yuzasi(a, b, d))
    if IsTriangle(a, c, d):
        print(Uchburchak_Yuzasi(a, c, d))
    if IsTriangle(b, c, d):
        print(Uchburchak_Yuzasi(b, c, d))
except ValueError as exp:
    print("Berilganlarni kirishtishda xatolik.\n", exp)
except ZeroDivisionError as exp:
    print("Nolga bo'lish mumkin emas.\n", exp)
except Exception as exp:
    print("Xatolik bo'ldi.\n", exp)
finally: print("Dastur yukunlandi.")
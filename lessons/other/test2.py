# Berilganlarni kiritish
x = float(input("x = "))
# Shart operatori
if x < -1:
    y = 0
elif x > 1:
    y = (x + 3) / abs(x)
else:
    y = 5 * x ** 3 + 6 * x * x - 2 * x

print("y = ", y)
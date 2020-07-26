# Berilganlarni kiritish
n = int(input("n = "))
m = int(input("m = "))
s = 0
for i in range(1, n + 1):
    p = 1
    for j in range(6, m + 1):
        p *= (i + j)
    s += p
print("s = ", s)
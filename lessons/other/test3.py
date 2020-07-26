# Berilganlarni kiritish
n = int(input("n = "))
m = int(input("m = "))
# Yig'indi uchun
s = 0
# Qadamlarni sanash uchun
i = 2
while i <= n:
    p = 1
    j = 3
    while j <= m:
        p *= float(i * i) / j
        j += 1
    s += p
    i += 1
print("s = ", s)
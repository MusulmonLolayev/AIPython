import random

n = 28

a = 11
b = 16

for i in range(n):
    for j in range(9):
        print(str(random.randint(a, b)) + ", " + str(random.randint(a, b)), end='\t')
    print()

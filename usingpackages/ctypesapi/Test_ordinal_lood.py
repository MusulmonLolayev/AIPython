import time

arr = [1, 2, 3, 4, 5]
begin = time.time()

for i in arr:
    print(i)

end = time.time()
print(end - begin)
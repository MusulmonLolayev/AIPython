from ctypes import *
import time

mydll = cdll.LoadLibrary("C:\\Project1.dll")
n = 1000000000

begin = time.time()
i = 0
while i < n:
    i += 1
end = time.time()
print(end - begin)

begin = time.time()
mydll.loop(n)
end = time.time()
print(end - begin)
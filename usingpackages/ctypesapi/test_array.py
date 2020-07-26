from ctypes import *

import time

mydll = cdll.LoadLibrary(r"C:\Users\Windows1\source\repos\Project1\Debug\Project1.dll")


IntArray5 = c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)

ia2 = IntArray5()

begin = time.time()

ptr = mydll.array(ia, ia2, 5)

end = time.time()
print(end - begin)

print()
begin = time.time()
for item in ia2:
    print(item)
end = time.time()
print(end - begin)

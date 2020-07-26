from ctypes import *
import time

mydll = cdll.LoadLibrary("C:\\ClassLibrary2.dll")

ob = mydll.ClassLibrary2.Class1

print(ob.sum(4, 6))
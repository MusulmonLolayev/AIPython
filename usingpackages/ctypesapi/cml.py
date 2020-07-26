from ctypes import *

import numpy as np
from numpy.ctypeslib import ndpointer

_doublepp = ndpointer(dtype=np.uintp, ndim=1, flags='C_CONTIGUOUS')

cml = CDLL(r"D:\Nuu\AI\Programms\C\Machine Learning\Debug\Machine Learning.dll")

# Init ctypes types
# Just one varable
INT = c_int
# 1 dimension array
PINT = POINTER(INT)
# 2 dimension array
PPINT = POINTER(PINT)
# 3 dimension array
PPPINT = POINTER(PPINT)

BOOL = c_bool
# 1 dimension array
PBOOL = POINTER(BOOL)
# 2 dimension array
PPBOOL = POINTER(PBOOL)
# 3 dimension array
PPPBOOL = POINTER(PPBOOL)

# Just one varable
DOUBLE = c_double
# 1 dimension array
PDOUBLE = POINTER(DOUBLE)
# 2 dimension array
PPDOUBLE = POINTER(PDOUBLE)
# 3 dimension array
PPPDOUBLE = POINTER(PPDOUBLE)

class MLData(Structure):
    _fields_= [
        ('X', PPDOUBLE),
        ('y', POINTER(c_int)),
        ('types', POINTER(c_int)),
        ('m', c_int),
        ('n', c_int),
        ('metric', c_int)
    ]

def createMLData(X, y, types = None, metric = 1):
    if types is None:
        types = np.full(shape=(X.shape[1]), fill_value=1)

    X_c = double2ArrayToPointer(X)

    y_c = IntArray2ToPointer(y)
    types_c = IntArray2ToPointer(types)

    return MLData(X_c, y_c, types_c, X.shape[0], X.shape[1], 1)

def IntArray1ToPointer(arr):
    return arr.ctypes.data_as(POINTER(c_int))

def BoolArray1ToPointer(arr):
    return arr.ctypes.data_as(POINTER(c_bool))

def IntArray2ToPointer(arr):
    return arr.ctypes.data_as(POINTER(c_int))

def double2ArrayToPointer(arr):
    """ Converts a 2D numpy to ctypes 2D array.

    Arguments:
        arr: [ndarray] 2D numpy float64 array
    Return:
        arr_ptr: [ctypes double pointer]
    """

    # Init needed data types
    ARR_DIMX = DOUBLE * arr.shape[1]
    ARR_DIMY = PDOUBLE * arr.shape[0]

    # Init pointer
    arr_ptr = ARR_DIMY()

    # Fill the 2D ctypes array with values
    for i, row in enumerate(arr):
        arr_ptr[i] = ARR_DIMX()

        for j, val in enumerate(row):
            arr_ptr[i][j] = val

    return arr_ptr

def find_noisy(X, y, types = None, metric = 1):
    if types is None:
        types = np.zeros(shape=(X.shape[1]))
        types += 1

    data = createMLData(X, y, types=types, metric=metric)

    foo = cml.find_noisy
    foo.argtypes = [POINTER(MLData), POINTER(c_bool)]
    foo.restype = None

    noisy = np.full(shape=(X.shape[0]), fill_value=False, dtype=np.bool)

    foo(data, BoolArray1ToPointer(noisy))

    return noisy

def find_standard(X, y, types = None, metric = 1):

    if types is None:
        types = np.full(shape=(X.shape[1]), fill_value=False)

    data = createMLData(X, y, types=types, metric=metric)

    foo = cml.find_standard
    foo.argtypes = [POINTER(MLData), POINTER(c_bool)]
    foo.restype = None

    standard = np.full(shape=(X.shape[0]), fill_value=False, dtype=np.bool)

    foo(data, BoolArray1ToPointer(standard))

    return standard

def find_shell(X, y, types = None, metric = 1):

    if types is None:
        types = np.full(shape=(X.shape[1]), fill_value=False)

    data = createMLData(X, y, types=types, metric=metric)

    foo = cml.find_shell
    foo.argtypes = [POINTER(MLData), POINTER(c_bool)]
    foo.restype = None

    shell = np.full(shape=(X.shape[0]), fill_value=False, dtype=np.bool)

    foo(data, BoolArray1ToPointer(shell))

    return shell

def compactness(X, y, types = None, metric = 1):

    if types is None:
        types = np.full(shape=(X.shape[1]), fill_value=1)

    data = createMLData(X, y, types=types, metric=metric)

    foo = cml.compactness
    foo.argtypes = [POINTER(MLData)]
    foo.restype = POINTER(c_double)

    res_f = foo(data)

    comp = []

    unique = np.unique(y)

    ln = len(unique)

    for item in range(ln + 1):
        comp.append(res_f[item])

    return comp
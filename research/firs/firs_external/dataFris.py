import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import math
from sklearn import datasets

class Iris:
    def GetData(self):
        iris = datasets.load_iris()
        x = iris.data[:, [2,3]]
        y = iris.target
        return x, y

def Degenerate():
    np.random.seed(123)
    disp = 1/5
    def normal(centerx, centery, disp, N):
        x = disp * np.random.randn(N) + centerx
        y = disp * np.random.randn(N) + centery
        return np.column_stack((x, y))

    def getData():
        d1 = 0.6
        d2 = 2
        np.random.seed(365)
        N = 15
        x1 = normal(-2,0,d1,N)
        y1 = np.array([0] * N)
        x2 = normal(5,0,d2,N)
        y2 = np.array([1] * N)
        x = np.row_stack((x1,x2))
        y = np.concatenate((y1,y2))
        return x, y

    return getData()

def FrisData():
    X = [
        [-4.41827821165084 ,1.10447552559827 ,   1 ], 
        [-2.49997149059698 ,2.74067831708538 ,   1 ], 
        [-1.38566096880835 ,-0.0803609785820420  , 1 ], 
        [-3.37449367225388 ,-2.02687809259256 , 1 ], 
        [-6.02627061018126 ,-1.56140660880744 , 1 ], 
        [-2.59870786594534 ,-5.04539013895670 , 1 ], 
        [-0.144403678714688 ,-2.87318988129279 , 1 ], 
        [2.54968884864770 ,-3.40918734746960 , 1 ], 
        [-0.116193285758014 ,1.64047299177508 , 1 ], 
        [1.32253675503237 ,-0.785620802498897 , 1 ], 
        [1.94316540007920 ,2.79709910299872 , 1 ], 
        [7.14798290058560 ,1.31605347277333 , 2 ], 
        [7.13387770410726 ,0.907002774901556 , 2 ], 
        [7.59934918789239 ,1.07626513264160 , 2 ], 
        [7.57113879493571 ,0.681319631248162 , 2 ], 
        [8.37513499420093 ,0.794161203074859 , 2 ], 
        [8.26229342237423 ,0.483846880551443 , 2 ], 
        [8.75597529911603 ,0.765950810118185 , 2 ], 
        [8.58671294137599 ,1.18910670446830 , 2 ], 
        [8.13534665406920 ,1.52763141994839 , 2 ], 
        [8.37513499420093 ,1.82384054599347 , 2 ], 
        [7.61345438437073 ,1.78152495655845 , 2 ]
    ]
    X = np.array(X,dtype=float)
    n = X.shape[1]-1
    return X[:,0:n], X[:,n]-1

class DataBuilder:
    def Build(self, name):
        if name == "iris":
            x, y = Iris().GetData()
            return x, y
        elif name == "degenerate":
            x, y = Degenerate()
            print(x)
            return x, y
        elif name == "fris":
            x, y = FrisData()
            return x,y
        else:
            assert("Unknown data")

if __name__ == '__main__':
    x, y = DataBuilder().Build("fris")
    plt.scatter(x[:,0], x[:,1], c=y)
    plt.show()

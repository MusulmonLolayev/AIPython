import numpy as np

def connected_areas(X, y, ln=None, types=None, metric='euclidean'):
    ng = np.zeros(shape=(X.shape[0]))
    nobl = 0
    for i in range(len(ln)):
        bk = np.zeros(shape=(X.shape[0]))
        for j in range(X.shape[0]):
            if y[j] == i:
                pass
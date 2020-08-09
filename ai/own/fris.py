import numpy as np

def distance(X, types=None, metric='euclidean'):
    distance = 0
    if len(types[types == 0]) > 0:
        r = 0
        for i, j, k in zip(X[0], X[1], types):
            if k == 1:
                distance += (i - j) ** 2
            elif i != j:
                r += 1
        distance = distance ** 0.5 + r * (2 ** 0.5)
    else:
        for i, j in zip(X[0], X[1]):
            distance += (i - j) ** 2
        distance = distance ** 0.5
    return distance

def Fris(X, y, types = None, ln = None, file = None):

    if ln == None:
        _, ln = np.unique(y, return_counts=True)

    metric = 'euclidean'
    #if types != None and len(types[types == 0]) > 0:
    #    metric =

    # Shell objects
    # cc is number of which object in against class is close to this object
    cc = np.zeros(shape=(X.shape[0]), dtype=int)
    pnk = np.zeros(shape=(X.shape[0]), dtype=int)
    #
    lk = np.zeros(shape=(X.shape[0]), dtype=int)
    # r1 is number of which object in this object's class is in radius of r1
    r1 = np.zeros(shape=(X.shape[0]), dtype=int)
    # r3 radius of object that to check which objects are in this and what class they are
    r3 = np.zeros(shape=(X.shape[0]), dtype=float)
    #
    etalon = np.zeros(shape=(X.shape[0]))

    for i in range(X.shape[0]):
        s = np.core.inf
        k = 0
        for j in range(X.shape[0]):
            if y[i] != y[j]:
                #s1 = distance.pdist(X[[i, j]], metric=metric)
                s1 = distance(X[[i, j]], metric=metric, types=types)
                if s > s1:
                    s = s1
                    k = j
        cc[k] += 1
        lk[k] = 1
        r3[i] = s

    for i in range(X.shape[0]):
        if cc[i] > 0:
            for j in range(X.shape[0]):
                if r3[i] > distance(X[[i, j]], metric=metric, types=types) and i != j and y[i] == y[j]:
                    r1[i] += 1

    # size of noisy objects
    count = 0
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            count += 1
            etalon[i] -= cc[i]
        else:
            cc[i] = 0
        cc[i] = 0

    print("Number of noisy objects: ", count)
    file.write("Number of noisy objects: " +  str(count) + "\n")

    ng = np.zeros(shape=(X.shape[0]), dtype=int)
    pr = np.zeros(shape=(X.shape[0]))
    nobl = 0

    # By classes
    for i in range(len(ln)):
        bk = np.zeros(shape=(X.shape[0]), dtype=int)
        # By by objects
        for j in range(X.shape[0]):
            # if cc[j] is 0, then this object isn't noisy
            if y[j] == i and cc[j] == 0:
                for l in range(X.shape[0]):
                    r3[l] = distance(X[[j, l]], metric=metric, types=types)

                s = 1e100
                k1 = -2
                for l in range(X.shape[0]):
                    if y[l] != i and s > r3[l] and cc[l] == 0:
                        s = r3[l]
                        k1 = l

                lk[j] = k1
                j1 = j
                s1 = s

                for l in range(X.shape[0]):
                    if y[l] == y[j] and cc[l] == 0:
                        sss = distance(X[[k1, l]], metric=metric, types=types)
                        if s1 > sss and s > distance(X[[j, l]], metric=metric, types=types):
                            s1 = sss
                            j1 = l



                bk[j1] += 1
                pr[j] = distance(X[[j, lk[j]]], metric=metric, types=types)

        k = -1

        for u in range(X.shape[0]):
            if y[u] == i and bk[u] > 0:
                k += 1
                bk[k] = u
                if k != u:
                    bk[u] = 0
        k += 1

        print("Number of shell objects in class " + str(i + 1) + " : " + str(k))
        file.write("Number of shell objects in class " + str(i + 1) + " : " + str(k) + '\n')

        pnk[i] = k

        x1 = np.zeros(shape=(X.shape[0], k), dtype=int)
        zz = np.zeros(shape=(k), dtype=int)

        for u in range(X.shape[0]):
            if y[u] == i:
                for q in range(k):
                    if pr[u] > distance(X[[u, bk[q]]], metric=metric, types=types):
                        x1[u, q] = 1
                    else:
                        x1[u, q] = 0

        ind = 1
        j1 = 0
        while ind == 1:
            ind = 0;
            ind1 = nobl

            for u in range(X.shape[0]):
                if y[u] == i and ng[u] == 0 and cc[u] == 0:
                    ind = 1
                    if j1 == 0:
                        nobl += 1
                        for q in range(k):
                            zz[q] = x1[u, q]
                        ng[u] = nobl
                        j1 = 1
                    else:
                        q = 0
                        while q < k:
                            if x1[u, q] == 1 and zz[q] == 1:
                                for l in range(k):
                                    if x1[u, l] == 1:
                                        zz[l] = 1
                                ng[u] = nobl
                                q = k + 5
                                j1 = 1
                            q += 1
            if ind1 == nobl:
                j1 = j1 - 1


    bk = np.zeros(shape=(nobl), dtype=int)
    zz = np.zeros(shape=(nobl), dtype=int)

    k = 0
    r2 = np.zeros(shape=(X.shape[0]), dtype=float)
    r3 = np.zeros(shape=(X.shape[0]), dtype=float)

    group = []

    for i in range(nobl):
        row = []
        bk[i] = 0
        zz[i] = i
        for j in range(X.shape[0]):
            if ng[j] == i + 1 and cc[j] == 0:
                k = y[j]
                bk[i] = bk[i] + 1
                row.append(j)

        group.append(row)

        r3[k] = r3[k] + bk[i] * bk[i]
        r2[k] = r2[k] + bk[i]


    print("Number of connected groups : " + str(nobl))
    file.write("Number of connected groups : " + str(nobl) + "\n")
    for i in range(nobl):
        print("Group " + str(i + 1) + "\t" + str(bk[i]) + "\t" + str(group[i]))
        file.write("Group " + str(i + 1) + "\t" + str(bk[i]) + "\t" + str(group[i]) + "\n")

    s = 0

    for i in range(len(ln)):
        sss = r3[i] / (r2[i] * r2[i])
        print("Compactness of class " + str(i + 1) + " : " + str(sss))
        file.write("Compactness of class " + str(i + 1) + " : " + str(sss) + "\n")

        s += r2[i] * (r3[i] / (r2[i] * r2[i]))

    s /= X.shape[0]
    print("Compactness of data set: " + str(s))
    file.write("Compactness of data set: " + str(s) + "\n")

    # ordinal sort
    for i in range(nobl - 1):
        for j in range(j + 1, nobl):
            if bk[i] < bk[j]:
                kr = bk[j]
                bk[j] = bk[i]
                bk[i] = kr
                k = zz[j]
                zz[j] = zz[i]
                zz[i] = k

    etalon[cc == 0] = 1
    etalon[cc != 0] = -5

    for i in range(nobl):
        if bk[i] >= 1:
            for j in range(X.shape[0]):
                if ng[j] == (i + 1) and cc[j] == 0:
                    r3[j] = distance(X[[j, lk[j]]], types=types)
                    r1[j] = j
                else:
                    r3[j] = -1
                    r1[j] = j
            lon(r3, r2, r1)

            j = X.shape[0]
            k1 = 1
            while r2[X.shape[0] - k1] == -1:
                k1 += 1
            j = j - k1

            while j >= 0 and j <= X.shape[0] - k1:
                if test(r1[j], etalon, cc, X, pr, y, types=types) == 1:
                    etalon[r1[j]] = 0

                j = j - 1
    for i in range(2):
        r3[i]=0;

    kk = 0
    s = 0

    for i in range(nobl):
        s=s+bk[i];
        j=0;
        while ((ng[j] - 1) != zz[i] & j < X.shape - 1):
            j += 1
        if zz[i] >= 0:
            for j in range(X.shape[0]):
                if etalon[j] == 1 and (ng[j]-1) == zz[i] and cc[j] == 0:
                    r3[y[j]] = r3[y[j]] + 1
                    kk += 1

    #return group, s, count, np.array([int(r3[0]), int(r3[1])])
    print("Etalon:", r3[0], r3[1]);
    return group, s, count

def lon(r3, r2, r1):
    for j in range(r3.shape[0]):
        for k in range(r3.shape[0]):
            if r2[j] < r3[k]:
                r2[j] = r3[k]
                r1[j] = k
        k2 = r1[j]
        r3[k2] = -1e36

def test(p, etalon, cc, x, pr, f, types):
    etalon[p] = 0;
    for i in range(x.shape[0]):
        if etalon[i] == 0:
            s = 1e40
            k = 1000
            for j in range(x.shape[0]):
                if etalon[j] == 1 and cc[j] == 0:
                    if distance(x[[j, i]], types=types) / pr[j] < s:
                        s = distance(x[[j, i]], types=types) / pr[j]
                        k = j
            if f[k] != f[i]:
                etalon[p] = 1
                return 0
    return 1
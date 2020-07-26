import numpy as np

def getData(path):
    data = []
    with open(path, "r") as file:
        line = file.readline()
        array = line.split(' ')
        m = int(array[0])
        n = int(array[1])
        for line in file:
            # print(line.replace('\n', '').split(' '))
            data.append(line.replace('\n', '').split(' '))
    return data

def ToFormArray(path, selected = None):
    data = getData(path)
    a = []
    types = []
    classes = []
    if selected == None:
        selected = len(data[0]) - 1
    for i in range(len(data) - 1):
        row = []
        for j in range(len(data[i])):
            if j != selected:
                row.append(float(data[i][j].replace(',', '.')))
            else:
                classes.append(int(data[i][j].replace(',', '.')))
        a.append(row)
    for item in data[len(data) - 1]:
        if item != None and item != '':
            types.append(int(item))
        else: break
    return a, types, classes

def ToFormNumpy(path):
    X, types, y = ToFormArray(path)

    X = np.array(X)
    types = np.array(types)
    y = np.array(y)

    return X, types, y

def distance(x):
    s = 0
    for i in range(x.shape[1]):
        s += (x[0, i] - x[1, i]) * (x[0, i] - x[1, i])
    s = s ** 0.5

    return s

def Fris(X, y, types = None, ln = None, IsNoisy = True):

    if ln == None:
        _, ln = np.unique(y, return_counts=True)

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

    shells = np.array([0, 0])

    for i in range(X.shape[0]):
        s = np.core.inf
        k = 0
        for j in range(X.shape[0]):
            if y[i] != y[j]:
                s1 = distance(X[[i, j]])
                if s > s1:
                    s = s1
                    k = j
        cc[k] += 1
        lk[k] = 1
        r3[i] = s

    for i in range(X.shape[0]):
        if cc[i] > 0:
            print(i)
            for j in range(X.shape[0]):
                if r3[i] > distance(X[[i, j]]) and i != j and y[i] == y[j]:
                    r1[i] += 1

    # size of noisy objects
    count = 0
    noisies = np.array([0, 0])
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            noisies[y[i]] += 1
            count += 1
            etalon[i] -= cc[i]
        else:
            cc[i] = 0

        if IsNoisy != True:
            cc[i] = 0

    if IsNoisy != True:
        count = 0

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
                    r3[l] = distance(X[[j, l]])

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
                        sss = distance(X[[k1, l]])
                        if s1 > sss and s > distance(X[[j, l]]):
                            s1 = sss
                            j1 = l

                bk[j1] += 1
                pr[j] = distance(X[[j, lk[j]]])

        k = -1

        for u in range(X.shape[0]):
            if y[u] == i and bk[u] > 0:
                #print(u)
                k += 1
                bk[k] = u
                if k != u:
                    bk[u] = 0
        k += 1

        shells[i] = k

        pnk[i] = k

        x1 = np.zeros(shape=(X.shape[0], k), dtype=int)
        zz = np.zeros(shape=(k), dtype=int)

        for u in range(X.shape[0]):
            if y[u] == i:
                for q in range(k):
                    if pr[u] > distance(X[[u, bk[q]]]):
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

    s = 0

    comp = []

    for i in range(len(ln)):
        sss = r3[i] / (r2[i] * r2[i])
        comp.append(sss)
        s += r3[i] / r2[i]

    s /= (X.shape[0] - count)

    comp.append(s)

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
                    r3[j] = distance(X[[j, lk[j]]])
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
        r3[i] = 0;

    kk = 0
    s = 0

    for i in range(nobl):
        s = s + bk[i];
        j = 0;
        while ((ng[j] - 1) != zz[i] & j < X.shape - 1):
            j += 1
        if zz[i] >= 0:
            for j in range(X.shape[0]):
                if etalon[j] == 1 and (ng[j] - 1) == zz[i] and cc[j] == 0:
                    r3[y[j]] = r3[y[j]] + 1
                    kk += 1

    return shells, noisies, comp, np.array([r3[0], r3[1]], dtype=int)

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
                    if distance(x[[j, i]]) / pr[j] < s:
                        s = distance(x[[j, i]]) / pr[j]
                        k = j
            if f[k] != f[i]:
                etalon[p] = 1
                return 0
    return 1

def sortByClass(values, classes):
    """
        Ushbu tartiblash algoritmi ikkita parametrga ega: birinchi parametr alomatning
    qiymatlari bo'lib list hisoblanadi; ikkinchisi esa, alomatning qaysi sinfga tegishli ekanligini anglatadi.
        Natija sifatida kirib keluvchi listning tartiblanishidan hosil bo'lgan indexlari qaytariladi.
        Agar ikkita har xil sinf vakili kelsa, u holda sinflarning tartibiga qarab joylashtiriladi.
    """
    result = []
    sorted_values = []
    for i in range(len(values)):
        min_val = 1e30
        min_index = i
        for j in range(len(values)):
            if values[j] < min_val:
                min_val = values[j]
                min_index = j

        sorted_values.append(values[min_index])
        values[min_index] = 1e30
        result.append(min_index)

    for i in range(len(sorted_values)):
        values[i] = sorted_values[i]
    return result

def GeneralCriterion2D(values, classes, ln=None, sort=None):
    """
        Ushbu funksiya, sinflararo o'xshashlik va sinflararo farq kriteriyasini hisoblash uchun xizmat qiladi:
        values - miqdoriy alomatning qiymatlari, list;
        classes - miqdoriy alomatning sinfi, list;
        ln - sinflardagi obyektlar soni, list;
        Qaytuvchi natija:
        max_value - kriteriyaning qiymati;
        min_index - miqdoriy alomatning minimum qiymati indeksi;
        opt_index - miqdoriy alomatning kriteriya bo'yicha optimal chegarasining indexi;
        max_index - miqdoriy alomatning maximum qiymati indeksi;
    """
    # Tartiblash uchun kiruvchi qiymatlardan nusxalash
    if sort == None:
        sort = []
    values_copy = values.copy()
    sortedClass = sortByClass(values_copy, classes)
    [sort.append(i) for i in sortedClass]
    # u[x, y] is count of x index of interval and y class. x is index of interval's and y is index of class. Where are x = {0, 1}.
    u = [[0, 0], [0, 0]]
    # Result values
    # Default of max value of Kriteriya is 0
    max_value = 0
    opt_index = sortedClass[0]
    min_index = sortedClass[0]
    max_index = sortedClass[len(values) - 1]
    # maxraj
    m1 = ln[0] * (ln[0] - 1) + ln[1] * (ln[1] - 1)
    m2 = 2 * ln[0] * ln[1]
    # for begin from 0 to len(vaules) - 1, beacuse each interval need min one object
    for x in range(0, len(values) - 1):
        # Count object's in fisrt interval by class
        u[0][classes[sortedClass[x]]] += 1

        # Calculate len of object's by class in second interval
        u[1][0] = ln[0] - u[0][0]
        u[1][1] = ln[1] - u[0][1]

        # if current object and next object aren't eqvivalent
        if values[sortedClass[x]] != values[sortedClass[x + 1]]:
            sum1 = 0.0
            sum2 = 0.0
            # Furmulation
            for y in range(0, 2):
                for z in range(0, 2):
                    sum1 += u[y][z] * (u[y][z] - 1)
                    sum2 += u[y][z] * (ln[1 - z] - u[y][1 - z])
            current_max = (sum1 / m1) * (sum2 / m2)
            # Check current max than more max value
            if current_max > max_value:
                max_value = current_max
                opt_index = sortedClass[x]
                opt_index1 = sortedClass[x + 1]
    return max_value, min_index, opt_index, max_index, opt_index1

def Normalizing_Estmation(X, y, ln = None):
    if ln == None:
        ln = np.unique(y, return_counts=True)[1]
    for j in range(X.shape[1]):
        b = X[:, j].copy()
        res = GeneralCriterion2D(b, y, ln=ln)
        if X[int(res[3]), j] != X[int(res[1]), j]:
            X[:, j] = res[0] * (X[:, j] - X[int(res[2]), j]) / (X[int(res[3]), j] - X[int(res[1]), j])
            #print(X[int(res[1]), j], X[int(res[2]), j], X[int(res[3]), j], res[0])
            #X[:, j] = (X[:, j] - X[int(res[2]), j]) / (X[int(res[3]), j] - X[int(res[1]), j])
        else:
            print("warning : ", X[int(res[3]), j], X[int(res[1]), j])

def GetIndexsOfNoisyObjects(X, y):
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

    shells = np.array([0, 0])

    for i in range(X.shape[0]):
        s = np.core.inf
        k = 0
        for j in range(X.shape[0]):
            if y[i] != y[j]:
                s1 = distance(X[[i, j]])
                if s > s1:
                    s = s1
                    k = j
        cc[k] += 1
        lk[k] = 1
        r3[i] = s

    for i in range(X.shape[0]):
        if cc[i] > 0:
            for j in range(X.shape[0]):
                if r3[i] > distance(X[[i, j]]) and i != j and y[i] == y[j]:
                    r1[i] += 1

    # size of noisy objects
    count = 0
    noisies = np.array([0, 0])
    for i in range(X.shape[0]):
        if cc[i] > r1[i]:
            noisies[y[i]] += 1
            count += 1
            etalon[i] -= cc[i]
        else:
            cc[i] = 0
    return cc == 0
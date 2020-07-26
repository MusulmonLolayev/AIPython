import numpy as np

data = np.loadtxt(r"D:\Nuu\Data mining\Selections\Gastralogiya\data.txt", dtype=object, delimiter=',')

data = data.T

indx = [i for i in range(1, data.shape[1] - 1)]

data = data[:, indx]

data = data.astype(float)

formats = ['%f' for i in range(data.shape[1] - 2)]
formats = ['%i', '%i'] + formats
data[:, 0] -= 1

i = 0

dd = []

while i < data.shape[0]:
    row = []
    for j in range(2, data.shape[1]):
        row.append(data[i, j])
    i += 1

    for j in range(2, data.shape[1]):
        row.append(data[i, j])
    row.append(data[i, 0])
    i += 1

    dd.append(row)


X = np.array(dd)
print(X.shape)

formats = ['%f' for i in range(X.shape[1] - 1)]
formats = formats + ['%i']

indx = np.array(range(2, data.shape[1]))
indx = np.append(indx, 0)

data = data[:, indx]
indx = np.array(range(0, data.shape[0]))

cond = indx % 2 != 0

data = data[cond]

formats = ['%f' for i in range(data.shape[1] - 1)]
formats = formats + ['%i']

[print(1, end=' ') for i in range(data.shape[1] - 1)]

print(np.savetxt(r'D:\gasterlogy.txt', data, delimiter=' ', fmt=formats))
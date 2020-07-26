import numpy as np

from uz.nuu.datamining.own.estimations import DecomposionEstimation


def getData(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            data.append(line.replace('\n', '').split('\t'))
    return data

path1 = r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Res1.txt"


path2 = r"D:\Nuu\Data mining\Articles\PCA operator\Computing\Res2.txt"

data1 = getData(path1)
data2 = getData(path2)

a = []
for item in data1:
    row = []
    for i in item[3].split(' '):
        row.append(int(i))
    a.append(row)
b = []
for item in data2:
    row = []
    for i in item[3].split(' '):
        row.append(int(i))
    b.append(row)

print(DecomposionEstimation(a, b, 147))
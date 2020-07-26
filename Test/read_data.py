import numpy as np
import pandas as pd

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
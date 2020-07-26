def writeNP(path, X, y, types = None):
    file = open(path, 'w')
    file.write(str(X.shape[0]) + " " + str(X.shape[1]) + "\n")
    for i, j in zip(X, y):
        for l in i:
            file.write(str(l) + " ")
        file.write(str(j) + "\n")

    for i in types:
        file.write(str(i) + " ")
    file.close()
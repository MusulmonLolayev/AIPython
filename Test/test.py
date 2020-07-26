import numpy as np
import pandas;

def main():

    data = pandas.read_csv("D:/test.csv")

    X = np.array(data)
    X = X[:, 0:]
    #print(X)

    data = pandas.read_csv("D:/survived.csv")

    y = np.array(data['Survived'])
    #print(y)

    unique, ln = np.unique(y, return_counts=True)

    print(unique)
    print(ln)



if __name__ == '__main__':
    main()
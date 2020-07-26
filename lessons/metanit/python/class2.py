# Import random in order to generate values
import random

# Creating class with name Matrix
class Matrix:
    # constructor
    def __init__(self, n, m = None, a = None):
        self.n = n
        if m is None:
            self.m = n
        else:
            self.m = m
        self.a = []

        if a is not None:
            for i in range(self.n):
                # new row
                row = []
                for j in range(self.m):
                    # add new value
                    row.append(a[i][j])
                self.a.append(row)
        else:
            for i in range(self.n):
                # new row
                row = []
                for j in range(self.m):
                    # add new value
                    row.append(random.randint(0, 100))
                self.a.append(row)

    # Print matrix in file or console
    def display(self, file=None):
        print("Matrix: ")
        for i in range(self.n):
            for j in range(self.m):
                if file is None:
                    print(self.a[i][j], end="\t")
                else:
                    print(self.a[i][j], end="\t", file=file)

            if file is None:
                print()
            else:
                print(file=file)
        print("Matrix")

    def Row_Max(self):
        print("Max element in each row")
        for i in range(self.n):
            s = self.a[i][0]
            for j in range(self.m):
                if s < self.a[i][j]:
                   s = self.a[i][j]
            print(s, end="\t")

    def Row_Min(self):
        print("Min element in each row")
        for i in range(self.n):
            s = self.a[i][0]
            for j in range(self.m):
                if s > self.a[i][j]:
                   s = self.a[i][j]
            print(s, end="\t")

if __name__ == '__main__':
    matrix = Matrix(5, 6)
    # Print randomly data
    matrix.display()
    print()
    # Print max and min elements in rows
    matrix.Row_Max()
    print()
    matrix.Row_Min()

    # Creating object with real data
    matrix = Matrix(3, 2, [[2, 3], [5, 6], [8, 2]])
    # Print real data
    matrix.display()
    print()
    # Print max and min elements in rows
    matrix.Row_Max()
    print()
    matrix.Row_Min()
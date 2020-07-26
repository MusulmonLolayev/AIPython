class Matrix:

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        b = []
        for i in range(len(self.a)):
            row = []
            for j in range(len(self.a[0])):
                row.append(self.a[i][j] + other.a[i][j])
            b.append(row)
        return b

    def __str__(self):
        return str(self.a)

a = Matrix([[1, 2], [2, 3]])
b = Matrix([[5, 2], [8, 3]])

c = a + b

print(c)
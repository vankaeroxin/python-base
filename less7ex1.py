class Matrix:
    def __init__(self, *args):
        self.matrix = []
        for el in args:
            self.matrix.append(el)

    def __str__(self):
        for el in self.matrix:
            print(el)
        return '\n'

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        matr_sum = []
        for i, eli in enumerate(self.matrix):
            line_sum = []
            for j, elj in enumerate(eli):
                line_sum.append(elj + other[i][j])
            matr_sum.append(line_sum)
            self.matrix = matr_sum
        return self.matrix


m = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
m2 = Matrix([11, 12, 13], [14, 15, 16], [17, 18, 19])
m + m2
print(m)

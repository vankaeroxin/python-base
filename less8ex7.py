class Complex:
    def __init__(self, num):
        self.rl = num.real
        self.img = num.imag

    def __str__(self):
        return f'({self.rl}+{self.img}j)'

    def __add__(self, other):
        add = complex(self.rl + other.rl, self.img + other.img)
        return add

    def __mul__(self, other):
        a, b, c, d = self.rl, self.img, other.rl, other.img
        mul = complex(a*c - b*d, b*c + a*d)
        return mul


c1 = 2 + 3j
c2 = 3 + 3j
cmp1 = Complex(c1)
cmp2 = Complex(c2)
print(cmp1)
print(cmp2)
print(f'\nСложение через перегрузку:     {cmp1 + cmp2}\nСложение через функции Python: {c1 + c2}\n')
print(f'Умножение через перегрузку:     {cmp1 * cmp2}\nУмножение через функции Python: {c1 * c2}')

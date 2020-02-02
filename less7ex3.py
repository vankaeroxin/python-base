def cells(nums):
    return f'Количество клеток: {nums}'


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return cells(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums >= other.nums:
            return cells(self.nums - other.nums)
        else:
            return 'Ошибка вычитания'

    def __mul__(self, other):
        return cells(self.nums * other.nums)

    def __truediv__(self, other):
        try:
            return cells(self.nums // other.nums)
        except ZeroDivisionError:
            return 'Ошибка: деление на ноль'

    def make_order(self, c):
        rows = self.nums // c
        for r in range(rows):
            print(f'{"*" * c}')
        print("*" * (self.nums % c))


c1 = Cell(20)
c2 = Cell(30)
c3 = Cell(0)
print(c1 + c2)
print(c2 - c1)
print(c1 - c2)
print(c1 * c2)
print(c2 / c1)
print(c1 / c3)

c1.make_order(6)

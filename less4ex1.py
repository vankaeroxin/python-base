from sys import argv


def salary(prod, rate, bonus):
    if prod < 0 or rate < 0 or bonus < 0:
        print('Введены отрицательные значения, возможно ошибка ввода')
    return prod * rate + bonus


try:
    print(salary(float(argv[1]), float(argv[2]), float(argv[3])))
except TypeError:
    print('Ошибка ввода параметров: введено не число')
except IndexError:
    print('Ошибка ввода параметров: неверное количество, ожидается три')

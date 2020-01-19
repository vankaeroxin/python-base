from functools import reduce


def multiplicate(arg_1, arg_2):
    """
    Функция, выполняющая математическую операцию умножение
    multiplicate(2, 2)
    return 4.0

    Функция не проверяет пользовательский ввод, в случае ввода некорректных значений, будет сгенерировано
    стандартное искдючение языка
    """
    return arg_1 * arg_2


print(reduce(multiplicate, [el for el in range(10, 1001)]))

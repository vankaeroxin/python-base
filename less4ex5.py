from functools import reduce


def multiplicate(arg_1, arg_2):
    return arg_1 * arg_2


print(reduce(multiplicate, [el for el in range(10, 1001)]))

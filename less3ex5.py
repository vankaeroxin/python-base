r_list = []
fin = False


def parse_sum(arg_list):
    global fin

    for el in arg_list:
        if el == 'q':
            fin = True
        try:
            r_list.append(float(el))
        except ValueError:
            continue

    for ind, el in enumerate(r_list, 1):
        print(f'{el} ', end='')
        sym = '=' if ind == len(r_list) else '+'
        print(sym, end=' ')

    return sum(r_list)


while not fin:
    s_list = input('Введите числа через пробел или q для выхода: ').split(' ')
    print(parse_sum(s_list))

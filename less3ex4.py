def power(arg_1, arg_2):
    return arg_1 ** arg_2


def powerrec(arg_1, arg_2):
    if arg_2 == 0:
        return 1
    if arg_2 == 1:
        return arg_1
    if arg_2 < 0:
        return 1 / (arg_1 * powerrec(arg_1, -arg_2 - 1))
    return arg_1 * powerrec(arg_1, arg_2 - 1)


def powercicle(arg_1, arg_2):
    t = arg_1
    for i in range(abs(arg_2) - 1):
        t *= arg_1
    return 1 / t


while 1:
    st = input('Введите действительное положительное X и целое отрицательное Y через пробел или оставьте пустым для '
               'выхода: ')
    if not st:
        break
    if st.count(' ') != 1:
        continue

    try:
        x, y = float(st.split(' ')[0]), int(st.split(' ')[1])
    except ValueError:
        continue

    if x > 0 and y < 0:
        print(f'\n{len(str(x)) * " "}{y}')
        print(f'{x}{len(str(y)) * " "} = {pow(x, y)}\n')
        print(f'Оператор ** : {power(x, y)}')
        print(f'Цикл        : {powercicle(x, y)}')
        print(f'Рекурсия    : {powerrec(x, y)}\n')
    else:
        continue

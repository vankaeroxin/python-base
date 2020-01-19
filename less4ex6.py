import time
from itertools import cycle, count


def load_process(cyc):
    load_symbol = ['#' * el for el in range(11)]
    load_iter = cycle(load_symbol)
    cyc = int(cyc)
    print()

    if cyc < 0:
        raise ValueError

    while cyc > 0:
        for i in range(len(load_symbol)):
            print(f'[{next(load_iter)}', end=f'{"." * (len(load_symbol) - 1 - i)}]')
            time.sleep(.3)
            print('\r', end='')
        cyc -= 1

    print('\n')


while 1:
    s = input('Выберите режим работы: демонстрация работы count() - 1; cycle() - 2; для выхода наберите q: ')
    if s == '1':
        while 1:
            cnt = input('Введите через пробел начальное число и количество итераций или q для выхода: ')

            if cnt == 'q':
                break
            if cnt.count(' ') != 1:
                continue

            try:
                x, y = int(cnt.split(' ')[0]), int(cnt.split(' ')[1])
                for el in count(x):
                    if el == x + y:
                        break
                    print(el)

            except ValueError:
                continue
    elif s == '2':
        while 1:
            try:
                cyc = input('Введите количества итераций отображения процесса загрузки или q для выхода: ')
                if cyc == 'q':
                    break
                load_process(cyc)
            except ValueError:
                continue
    elif s == 'q':
        break
    else:
        continue

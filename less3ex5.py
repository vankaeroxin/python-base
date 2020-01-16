r_list = []
fin = False


def parse_sum(arg_list):
    """
    Функция принимает список из чисел и возвращает их сумму в виде числе.
    Также просходит вывод на печать эелементов в виде:

    el1 + el2 + ... eln =

    Элементы можно в текстовом формате, функция осуществит преобразование во float
    Если преобразование не удаётся, этот элемент игнорируется в подсчёте
    Если элемент равен q, присходит поднятие глобального флага q для передачи в основной код и завершение цикла
    обработки элементов
    """

    global fin

    for el in arg_list:
        if el == 'q':
            fin = True
            break
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

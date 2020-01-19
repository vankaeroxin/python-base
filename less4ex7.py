def fact_yield(n):
    """
    Функция принимает на вход целое число n и возвращает генератор для факториалов чисел от 1 до n

    В случае некорректного ввода генерируется исключение ValueError, которое необходимо обрабатывать вне функции
    """
    if n < 0:
        raise ValueError
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


def fact_ret(n):
    """
    Функция принимает на вход целое число n и возвращает факториал этого числа

    В случае некорректного ввода генерируется исключение ValueError, которое необходимо обрабатывать вне функции
    """
    if n < 0:
        raise TypeError
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


while 1:
    try:
        n = input('Введите целое положительное число до 15 или q для выхода: ')

        if n == 'q':
            break

        n = int(n)
        if n > 15:
            continue

        for i, f in enumerate(fact_yield(n), 1):
            print(f'{i}! = {f}')

        print()
        for i, f in enumerate(range(1, n + 1), 1):
            print(f'{i}! = {fact_ret(f)}')
    except TypeError:
        continue
    except ValueError:
        continue

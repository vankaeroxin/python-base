def my_func(arg_1, arg_2, arg_3):
    """
    Функция принимает три числа и возвращает сумму возвращает сумму наибольших двух в виде числа

    arg_1 = 1; arg_2 = 2.5; arg_3 = 3;
    return 5.5

    Значения можно передавать в текстовом формате, функция осуществит преобразование типов
    Если преобразование не удаётся, возвращается текстовая ошибка

    Если сумма чисел не имеет дробной части, она будет возвращена как целое:
    arg_1 = 1; arg_2 = 2.5; arg_3 = 3.5;
    return 6
    """
    try:
        list_args = [float(arg_1), float(arg_2), float(arg_3)]
        list_args.remove(min(list_args))
        s = sum(list_args)
        if s % 1:
            return s
        return int(s)
    except ValueError:
        return 'Ошибка! Проверьте корректность ввода чисел.'


while 1:
    st = input('Введите три значения через пробел или оставьте пустым для выхода: ')
    if not st:
        break
    if st.count(' ') != 2:
        continue

    print(my_func(st.split(' ')[0], st.split(' ')[1], st.split(' ')[2]))

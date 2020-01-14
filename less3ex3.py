def my_func(arg_1, arg_2, arg_3):
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

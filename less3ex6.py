def int_func(s):
    """
    Функция принимает слово из маленьких латинских букв и возвращает его же, но с прописной первой буквой

    s = 'word';
    return 'Word'

    Если слово содержит в себе другие символы, кроме маленьких латинских букв, вознакает исключение TypeError.
    Обработка типов не производится и неправильные аргументы могут привести к ошибке.
    """
    for i in s:
        if ord(i) not in range(97, 123):
            raise TypeError
    return s.title()


while 1:
    t = input('Выберите режим работы: одно слово(1) или строка(2). 0 - для выхода: ')
    if t == '1':
        st = input('Введите слово из маленьких латинских букв: ')
        try:
            print(int_func(st))
        except TypeError:
            print('Некорректный ввод')
    elif t == '2':
        st_list = input('Введите несколько слов из маленьких латинских букв разделённых пробелом: ').split(' ')
        try:
            for el in st_list:
                print(int_func(el), end=' ')
        except TypeError:
            print('Некорректный ввод')
        print()
    elif t == '0':
        break
    else:
        continue

with open('less1.txt', 'w') as w:
    pass
with open('less1.txt', 'a') as f:
    while 1:
        s = input('Введите строку для записи в файл: ')
        if not s:
            break
        f.write(s)
        f.write('\n')

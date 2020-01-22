with open('ex2.txt', 'w', encoding='utf-8') as w:
    pass
with open('ex2.txt', 'a', encoding='utf-8') as f:
    while 1:
        s = input('Введите строку для записи в файл: ')
        if not s:
            break
        f.write(s)
        f.write('\n')

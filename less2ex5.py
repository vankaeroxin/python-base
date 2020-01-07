while 1:
    min = True
    r_list = [7, 5, 3, 3, 2]
    inp = input("Введите целочисленное значение или q для выхода: ")
    if inp == 'q':
        break
    try:
        el = int(inp)
    except:
        continue
    if r_list.count(el):
        r_list.insert(r_list.index(el) + r_list.count(el), el)
    else:
        for i, j in enumerate(r_list):
            if el > j:
                r_list.insert(i, el)
                min = False
                break
        if min:
            r_list.append(el)
    print(f"Пользователь ввел число {el}. Результат:", end=' ')
    for i in r_list:
        print(f"{i}", end=' ')
    print('\n')

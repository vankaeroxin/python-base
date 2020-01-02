while 1:
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
        r_list.append(el)
    r_list.sort(reverse=True)
    print(f"Пользователь ввел число {el}. Результат:", end=' ')
    for i in r_list:
        print(f"{i}", end=' ')
    print()

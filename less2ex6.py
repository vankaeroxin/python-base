goods = []
while 1:
    n, c, k, e = "", "", "", ""
    while not n:
        n = input("Введите название товара: ")
    while not c:
        c = input("Введите цену: ")
        try:
            c = int(c)
        except:
            c = ""
            continue
    while not k:
        k = input("Введите количество: ")
        try:
            k = int(k)
        except:
            k = ""
            continue
    e = input("Введите используемые единицы (оставьте пустым для указания \"шт.\"): ")
    if not e:
        e = "шт."
    goods.append((len(goods)+1, {"название": n, "цена": c, "количество": k, "eд": e}))
    if input("Введите q для анализа данных и выхода: ") == 'q':
        break

n, c, k, e = [], [], [], []
for ind, el in enumerate(goods):
    n.append(goods[ind][1].get("название"))
    c.append(goods[ind][1].get("цена"))
    k.append(goods[ind][1].get("количество"))
    e.append(goods[ind][1].get("eд"))

n, c, k, e = set(n), set(c), set(k), set(e)
an = {"название": n, "цена": c, "количество": k, "eд": e}
for i in an:
    print(f"\"{i}\" {an[i]}")

list_str = input("Введите элементы списка через запятую: ")
quant = list_str.count(',')
list_direct = list_str.split(',')
list_tmp = []
list_reverse = []
odd = True if quant % 2 == 0 else False

for ind, el in enumerate(list_direct):
    if ind % 2 == 1:
        list_tmp.append(el)
        list_tmp.append(tmp)
    tmp = el
    if ind == quant and odd:
        list_tmp.append(el)
    list_reverse.extend(list_tmp)
    list_tmp.clear()

print(f"       Заданный список: {list_direct}")
print(f"Форматированный список: {list_reverse}")

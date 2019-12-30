list_str = input("Введите элементы списка через запятую: ")
ind = list_str.count(',')
list_direct = list_str.split(',')
list_tmp = []
list_reverse = []
j = 0
odd = True if ind % 2 == 0 else False
for i in list_direct:
    if j % 2 == 1:
        list_tmp.append(i)
        list_tmp.append(tmp)
    tmp = i
    if (j == ind) & odd:
        list_tmp.append(i)
    list_reverse.extend(list_tmp)
    list_tmp.clear()
    j += 1

print(f"       Заданный список: {list_direct}")
print(f"Форматированный список: {list_reverse}")

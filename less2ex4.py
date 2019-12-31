s_list = input("Введите слова через пробел: ").split(' ')
j = 1
for i in s_list:
    print(f"{j}: {i[:10].title()}")
    j += 1

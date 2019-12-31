s_list = input("Введите слова через пробел: ").split(' ')
for ind, el in enumerate(s_list):
    print(f"{ind}: {el[:10].title()}")

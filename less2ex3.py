worktype = 0
while worktype != 'l' and worktype != 'd':
    worktype = input("Выберите режим работы список(l) или словарь(d): ")
    print(worktype)

while worktype == 'l':
    list_season = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    try:
        s = int(input("Введите номер месяца или оставьте поле пустым для выхода: "))
        s = 0 if s < 0 else s
        1 / s
        print(f"{s}-й месяц - это {list_season[s - 1]}")
    except:
        break

while worktype == 'd':
    dict_season = {
        '1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето', '8': 'Лето',
        '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}
    try:
        s = int(input("Введите номер месяца или оставьте поле пустым для выхода: "))
        s = 0 if s < 0 else s
        1 / s
        print(f"{s}-й месяц - это {dict_season.get(str(s))}")
    except:
        break

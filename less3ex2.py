def print_data(**kwargs):
    print(kwargs)


s_dict = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город': '', 'Email': '', 'Телефон': ''}
for key in s_dict:
    el = input(f'Введите {key} : ')
    s_dict.update({key: el})

print_data(**s_dict)

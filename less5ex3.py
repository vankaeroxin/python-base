with open('ex3.txt') as f:
    f_list = f.readlines()
    salary = []
    rich = []
    for ind, el in enumerate(f_list):
        try:
            salary.append(float(el.split()[1]))
            if salary[ind] >= 20000:
                rich.append(el.split()[0])
        except:
            continue

print(f'Прочитанный список зарплат: {salary}\n')
print('Граждане с зарплатой не менее 20 тысяч: ')
for el in rich:
    print(f'    {el}')
print(f'\nСредняя зарплата: {sum(salary)/len(salary):.2f}')

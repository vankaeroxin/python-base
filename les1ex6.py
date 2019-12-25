run = int(input("Введите результат первого дня: "))
target = int(input("Введите цель, которой хотите достичь: "))
day = 1
while run < target:
    run *= 1.1
    day += 1
    '''print(run)'''
print(f"Вы достигнете результата в {day} день.")

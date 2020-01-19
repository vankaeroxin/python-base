start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [start_list[ind] for ind in range(1, len(start_list)) if start_list[ind - 1] < start_list[ind]]
print(f'Исходный список: {start_list}\nРезультат:       {result_list}')

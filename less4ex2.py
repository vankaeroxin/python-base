start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for ind, el in enumerate(start_list, 1) if start_list[ind] > el]
print(f'Исходный список: {start_list}\nРезультат:       {result_list}')


# for ind, el in enumerate(start_list, 1):
#     print(start_list[ind], el)
#    # print(ind, el)

#
# for el in start_list[1:]:
#     print(el)

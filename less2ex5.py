r_list = [7, 5, 3, 3, 2]
print(r_list.index(3))
print(r_list.count(3))
print(r_list.index(3)+r_list.count(3))
r_list.insert(r_list.index(3)+r_list.count(3), 3)
print(r_list)
print(max(r_list))
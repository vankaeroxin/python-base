with open('less2.txt') as f:
    f_list = f.readlines()
    print(f'В файле {f.name} {len(f_list)} строк')
    for el in f_list:
        print(len(el.split()))

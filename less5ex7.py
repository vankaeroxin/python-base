import json

with open('ex7.txt', encoding='utf-8') as f:
    f_list = f.readlines()
    profit_dict, cnt, profit_sum = {}, 0, 0

    for el in f_list:
        print(el.split())
        profit = int(el.split()[2])-int(el.split()[3])
        profit_dict[el.split()[0]] = profit
        if profit >= 0:
            cnt += 1
            profit_sum += profit

firm_list = [profit_dict, {'average_profit': profit_sum/cnt}]
print(firm_list)

with open("ex7.json", "w", encoding='utf-8') as write_f:
    json.dump(firm_list, write_f, sort_keys=True, indent=4)

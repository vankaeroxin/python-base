with open('ex6.txt', encoding='utf-8') as f:
    f_list = f.readlines()
    d = {}
    for el in f_list:
        sum_ = 0
        print(el.split())
        s = ''.join(el.split()[1:])
        for ch in ['(', ')', '—']:
            s = s.replace(ch, ' ')
        for item in s.split():
            try:
                sum_ += int(item)
            except ValueError:
                continue
        d[el.split()[0]] = sum_

print(d)

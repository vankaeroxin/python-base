from random import randint

with open('ex5.txt', 'w') as w:
    rnd = ' '.join([str(randint(1, 100)) for _ in range(10)])
    w.write(rnd)

with open('ex5.txt') as r:
    result = [int(el) for el in r.read().split()]
    print(f'Сумма для {result} = {sum(result)}')

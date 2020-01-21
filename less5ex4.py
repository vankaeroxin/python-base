import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20200120T201124Z.834d859953d3bb20.f36860433e50c625c964aba0d22590b62a8303f5'
lang = 'en-ru'

w = open('ex41.txt', 'w')
w.close()
w = open('ex41.txt', 'a')
with open('ex4.txt') as f:
    f_list = f.readlines()
    for ind, el in enumerate(f_list):
        text = el.split()[0]
        r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
        print(f'[{"#"*ind}', end=f'{"." * (len(f_list) - 1 - ind)}]\n')
        s = ''.join(r.json().get('text')) + ' ' + ' '.join(el.split()[1:])
        w.write(f'{s}\n')

w.close()

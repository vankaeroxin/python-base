def div(num1, num2):
    try:
        num1, num2 = float(num1), float(num2)
        if not num1 % 1:
            num1 = int(num1)
        if not num2 % 1:
            num2 = int(num2)
        return f'{num1} / {num2} = {int(num1 / num2) if int(num1 / num2) == num1 / num2 else num1 / num2}'
    except ValueError:
        return 'Ошибка! Проверьте корректность ввода чисел.'
    except ZeroDivisionError:
        return 'Ошибка! Попытка деления на ноль.'


while 1:
    st = input('Введите значения через дробь или оставьте пустым для выхода: ')
    if not st:
        break
    if st.count('/') != 1:
        continue

    print(div(st.split('/')[0], st.split('/')[1]))

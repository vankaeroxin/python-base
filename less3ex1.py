def div(num1, num2):
    """
    Функция принимает два числа и возвращает их частное в виде строки:
    делимое / делитель = частное

    num1 = 10; num2 = 5;
    return 10 / 5 = 2

    Значения можно передавать в текстовом формате, функция осуществит преобразование типов
    Если преобразование не удаётся, возвращается текстовая ошибка
    При попытке деления на ноль, возвращается текстовая ошибка

    Если любое из чисел не имеет дробной части, оно будет выведено как целое:
    num1 = 1.5; num2 = 0.75;
    return 1.5 / 0.75 = 2
    """
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

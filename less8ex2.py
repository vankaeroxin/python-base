class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while 1:
    x = input("Введите числитель: ")
    y = input("Введите знаменатель: ")

    try:
        x, y = int(x), int(y)
        if y == 0:
            raise OwnError("Деление на ноль")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f"Частное: {x / y}")

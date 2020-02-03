class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_list = []
while 1:
    try:
        inp_data = input("Введите положительное число или stop: ")
        if inp_data == 'stop':
            print(inp_list)
            break
        try:
            inp_data = int(inp_data)
        except ValueError:
            raise OwnError("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        inp_list.append(inp_data)

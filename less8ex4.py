class Org:
    owner = 'Склад'

    def __init__(self, name, serial):
        self.name = name
        self.serial = str(serial)

    def __str__(self):
        org = {}
        org['Тип товара'] = self.__class__.__name__
        org['Наименование'] = self.name
        org['Серийный номер'] = self.serial
        org['Владелец'] = self.owner
        return str(org)


class Printer(Org):
    def __init__(self, name, serial, is_color):
        super().__init__(name, serial)
        self.is_color = is_color


class Scanner(Org):
    def __init__(self, name, serial, dpi):
        super().__init__(name, serial)
        self.dpi = dpi


class Xerox(Org):
    def __init__(self, name, serial, paper_size):
        super().__init__(name, serial)
        self.paper_size = paper_size


def to_storage(org):
    org.owner = 'Склад'
    print(f'{org.__class__.__name__} передан на склад')


def from_storage(org, owner):
    org.owner = owner
    print(f'{org.__class__.__name__} передан в подразделение {owner}')


while 1:
    inp_list = input('Введите тип (Сканер[s], Принтер[p], Ксерокс[x]), наименование, серийный номер, '
                     'харакетиристику через пробел: ').split()
    try:
        if inp_list[0] == 'q':
            break
        elif inp_list[0] == 's':
            org = Scanner(inp_list[1], int(inp_list[2]), inp_list[3])
            break
        elif inp_list[0] == 'p':
            org = Printer(inp_list[1], int(inp_list[2]), inp_list[3])
            break
        elif inp_list[0] == 'x':
            org = Xerox(inp_list[1], int(inp_list[2]), inp_list[3])
            break
        else:
            continue
    except ValueError:
        print('Серийный номер может содержать только числа')
        continue


print(org)
from_storage(org, "IT")
print(org)
to_storage(org)
print(org)

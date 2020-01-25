class Worker:
    name = 'Имя'
    surname = 'Фамилия'
    position = 'Должность'
    _income = {'Wage': 0, 'Bonus': 0}

    # def __init__(self, name, surname, position, wage, bonus):
    #     self.name = name
    #     self.surname = surname
    #     self.position = position
    #     self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(super().name)
        print(super().surname)


p = Position()
p.name = 'qweqwe'
p.surname = 'ee'
p.get_full_name()


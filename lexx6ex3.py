class Worker:
    name = 'Имя'
    surname = 'Фамилия'
    position = 'Должность'
    _income = {'Wage': 0, 'Bonus': 0}

    def set_income(self, wage, bonus):
        self._income = {'Wage': wage, 'Bonus': bonus}

    # def __init__(self, name, surname, position, wage, bonus):
    #     self.name = name
    #     self.surname = surname
    #     self.position = position
    #     self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'Общий доход: {sum(self._income.values())}')


p = Position()
p.name = 'Алексей'
p.surname = 'Стаханов'
p.get_full_name()
p.set_income(200, 100)
p.get_total_income()

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} - запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - пишем ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - чертим карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} - рисуем фломастером')


s = Stationery('1')
s.draw()

p = Pen('2')
p.draw()

pc = Pencil('3')
pc.draw()

h = Handle('4')
h.draw()

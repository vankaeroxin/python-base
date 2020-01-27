class Road:
    _lenght = 2000
    _widht = 50

    def build_road(self, mass, depth):
        print(f'Масса асфальта для покрытия = {Road._lenght * Road._widht * mass * depth / 1000:.0f} тонн')


road = Road()
while 1:
    try:
        s = input('Введите массу и толщину: ').split()
        if not s:
            break
        road.build_road(int(s[0]), int(s[1]))
    except:
        continue

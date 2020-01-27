class Car:
    speed = 0
    direction = 'прямо'

    def __init__(self, color, name, is_police=False):
        self.color, self.name, self.is_police = color, name, is_police
        print(f'Определена{" полицейская " if is_police else " "}машина: {self.color} {self.name}')

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} начал движение со скростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} закончил движение')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} едет {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости для {self.name}! Пожалуйста, двигайтесь не быстрее 60.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости для {self.name}! Пожалуйста, двигайтесь не быстрее 40.')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


car = Car('Чёрная', 'Toyota', False)
townCar = TownCar('Зелёная', 'Skoda')
workCar = WorkCar('Оранжевый', 'КамАЗ')
sportCar = SportCar('Красный', 'Ferrari')
policeCar = PoliceCar('Белый', 'Ford')

sportCar.go(200)
sportCar.turn('направо')
policeCar.go(210)
policeCar.turn('направо')
sportCar.stop()
townCar.go(90)
townCar.show_speed()
townCar.stop()
workCar.go(30)
workCar.show_speed()
workCar.go(100)
workCar.show_speed()
workCar.stop()

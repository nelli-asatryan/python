class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        return "Машина" + self.name + "поехала"

    def stop(self):
        return "Машина" + self.name + "остановилась"

    def turn(self, direction):
        self.direction = direction
        if direction == 'right':
            print('Машина повернула направо')
        elif direction == 'left':
            print('Машина повернула налево')

    def shown_speed(self):
        print(f'Текущая скорость машины {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.is_police = is_police
        super().__init__(speed, color, name, is_police)

    def shown_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена')
        else:
            print(f'Скорость {self.name}: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.is_police = is_police
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.is_police = is_police
        super().__init__(speed, color, name, is_police)

    def shown_speed(self):
        if speed > 40:
            print(f'Скорость {self.name} превышена')
        else:
            print(f'Скорость {self.name}: {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.is_police = is_police
        super().__init__(speed, color, name, is_police)


a = TownCar(45, "Red", "Ferrari") #выдает ошибку по is_police
b = SportCar(65, "White", "Mercedes")
c = WorkCar(90, "Blue", "Lada")
d = PoliceCar(66, "White-Blue", "Renault")
a.stop()
b.go()
c.direction("left")
d.direction("right")
a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
print(d.__dict__)

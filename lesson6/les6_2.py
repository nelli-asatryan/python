class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def mass_of_asphalt(self, mass, depth):
        self.mass = int(mass)
        self.depth = int(depth)
        value = self._length * self._width * self.mass * self.depth
        print(f'{self._length}м * {self._width}м * {self.mass}кг * {self.depth}см '
              f'Рачсет массы асфальта для покарытия всей дороги = {value/1000}т')

s = Road(25, 29)
s.mass_of_asphalt(40, 60)
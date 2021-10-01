class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = 'ручка'

    def draw(self):
        print("Возьми меня за ручку!")


class Pencil(Stationery):
    def __init__(self, title="Карандаш"):
        super().__init__(title)

    def draw(self):
        print("Карандаш проглотил?")


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__(title)

    def draw(self):
        print("Имея маркер можно закрасить все кроме самого маркера!")


a = Pen('ручка')
b = Pencil()
c = Handle()
a.draw()
b.draw()
c.draw()
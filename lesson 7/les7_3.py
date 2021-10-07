class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            print("Исходная клетка меньше вычитаемой!")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, lenstr):
        for i in range(1, self.count + 1):
            if i % int(lenstr) == 0:
                print("*")
            else:
                print("*", end="")


cell1 = Cell(21)
cell2 = Cell(10)
cell3 = cell1 - cell2
cell4 = cell1 + cell2
cell5 = cell1 * cell2
cell6 = cell1 / cell2
cell7 = cell2 - cell1
print(cell3.count)
print(cell4.count)
print(cell5.count)
print(cell6.count)
cell5.make_order(16)


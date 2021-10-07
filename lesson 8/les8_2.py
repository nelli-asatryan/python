class MyError(Exception):
    def __init__(self, txterr):
        self.txterr = txterr


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise MyError("На 0 Делить нельзя!")
except ValueError:
    print("Вы ввели не число!")
except MyError as err:
    print(err)
else:
    print(a / b)
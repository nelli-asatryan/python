def my_full_zp():
    x = int(input("Количество отработанных часов: "))
    y = int(input("Ставка в час: "))
    z = int(input("Премия в размере: "))
    return x * y + z

#ДАЛЕЕ в другом файле

import les4_1
from les4_1 import my_full_zp
print(my_full_zp())

#------------------- вариант 2

from sys import argv

x = int(argv[1])
y = int(argv[2])
z = int(argv[3])

print(f'Количество отработанных часов: {x}')
print(f'Ставка в час: {y}')
print(f'Премия в размере: {z}')
print(f'Заработная плата сотрудника равна: {x * y + z}')

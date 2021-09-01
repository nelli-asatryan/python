# 1
from itertools import count

first_gen = count(3)
for i in first_gen:
    if i > 10:
        break
    else:
        print(int(i))

# 2
from itertools import cycle

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
count = 0
iter_list = cycle(my_list)
for i in cycle(my_list):
    if count > len(my_list)-1:
        break
    print(i)
    count += 1
from functools import reduce

def my_func(x, y):
    return x * y

my_list = []
new_list = [my_list.append(i) for i in range(100, 1001) if i % 2 == 0]

print(reduce(my_func, my_list))
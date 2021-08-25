x = float(input('Число основание: '))
y = int(input('Возвести в степень: '))
result = x**abs(y)
if y >= 0:
    print(result)
else:
    print(1/result)

#-----------------------------------------------

def my_func(x,y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(3,-2))


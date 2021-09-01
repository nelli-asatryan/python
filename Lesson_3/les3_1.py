def my_division():
    '''Возврат результата от деления num1 на num2, если mun2 !=0'''
    while True:
        try:
            num1, num2 = input('Введите числа для их деления: ').split(',')
            res = int(num1) / int(num2)
            return res
        except ZeroDivisionError:
            print("Делить на 0 нельзя")

print(my_division())
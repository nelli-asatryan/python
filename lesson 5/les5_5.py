# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('for_les5.5.txt', 'w') as nabor:
    numbers = input('Введите числа: ').split()
    nabor.writelines(numbers)
    num_list = list(map(int, numbers))
    summa = 0
    for i in num_list:
        summa += i
    print(summa)

def slozhenie():
    try:
        my_list = 0
        sum_list = 0
        while True:
            sum_list += my_list
            print(sum_list)
            my_list = sum(list(map(int, input('Введите числа: ').split())))
    except ValueError:
        print('Неккорекные символы')
        return # нужен ли этот return?
    return

print(slozhenie())

# как выбросить часть текста, введного некоректно?
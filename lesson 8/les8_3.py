class OwnException(Exception):
    def __init__(self):
        self.txt = "Некорректный тип данных! Необходимо ввести число!"


mylist = []
my_string = input('Введите число. Для выхода введите пустую строку: ')
while my_string:
    try:
        if my_string.isdigit():
            mylist.append(int(my_string))
        else:
            raise OwnException
    except OwnException as a:
        print(a.txt)

    my_string = input('Введите число. Для выхода введите пустую строку: ')

print(mylist)
# Создать программный файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('hello.txt', 'w', encoding='utf-8') as file:
    message = input('Введите строку: ') + '\n'
    while message != '\n':
        file.write(message)
        message = input('Введите строку: ') + '\n'
    print('Ввод завершен!')

with open('hello.txt', 'r') as file:
    for message in file:
        print(message, end='')


# my_list = []
# while True:
#     message = input('Введите текст: ')
#     if not message:
#         break
#     my_list.append(message + '\n')
#
# with open('hello.txt', 'w', encoding='utf-8') as file_write:
#     message = input('Введите числа: ')
#     file_write.write(message)

# with open('hello.txt', 'w') as file:
#     for message in my_list:
#         file.write(message + '\n')


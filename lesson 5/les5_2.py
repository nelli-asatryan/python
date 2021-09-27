# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке

with open('for_les5.2.2.txt', encoding='utf-8') as podschet:
# выводит всю запись целиком
    # line1 = podschet.read()
    # print(line1)
# выводит каждую след строку отдельно: количество команд = количество строк
    # line2 = podschet.readline()
    # print(line2)
# выводит каждую след строку отдельно
    line3 = podschet.readlines()
# полная печать в виде списка
    print(line3)
# почать по номеру строки
    print(line3[:2])
# количество строк
    print(len(line3))
# количество слов в строке
    for i in line3:
        print(len(i.split()))


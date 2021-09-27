# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text.txt', 'r', encoding='utf-8') as my_file:
    text = my_file.read().split('\n')
lectures = {}
for sub in text:
    key, value = sub.split(': ')
    c = 0
    for i in value.split():
        if i == '—':
            digit = 0
        else:
            digit = ''
            for symb in i:
                if symb.isdigit():
                    digit += symb
            c += int(digit)
    lectures[key] = c
print(lectures)

# with open ('text.txt', 'r', encoding='utf-8') as my_file:
#     my_dict = {}
#     # print(my_file.readlines())
#     for info in my_file.readlines():
#         info2 = info.rstrip('\n').split()
#         print(info)
#         print(info2)

def func(*args):
    args = list(map(str, input('Ввод текста: ').title().split()))
    for word in args:
        if word.isalpha():
            new_list = ' '.join(args)
            print(args)
            return new_list
        else:
            print("Недоступные символы!")
            return
    return

print(func())

# как ограничить печать цифр после слов? Если цифры идут в начале, то выдает None.
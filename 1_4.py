
i = int(input("Введите число: "))
a = i % 10
while i > 0:
    if i % 10 > a:
        a = i % 10
    i = i // 10
print(a)





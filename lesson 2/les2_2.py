# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


elements = input("Введите данные: ").split()
for i in range(1, len(elements), 2):
    elements[i-1], elements[i] = elements[i], elements[i-1]
print(elements)


#--------------------------

len_list = len(input_list)
i = 0

while i < len_list - 1 :
    input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    i +=2

#--------------------------------




















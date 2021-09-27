with open('for_les5.4.txt', 'r+', encoding='utf-8') as count_num:
    # print(count_num.readline())
    # print(count_num.readlines())

    for simb in count_num.readlines():
        a, b, c = simb.rstrip("\n").split()
        if a == 'One':
            a = 'Один'
        elif a == 'Two':
            a = 'Два'
        elif a == 'Three':
            a = 'Три'
        else:
            a = 'Четыре'
        # print(a, b, c)
        with open('for_les5.4.1.txt', 'w', encoding='utf-8') as count_num_w:
            count_num_w.write(f'{a} {b} {c}\n')






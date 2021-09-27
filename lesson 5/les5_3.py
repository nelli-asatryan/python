with open('for_les5.3.txt', 'r+', encoding='utf-8') as employee:
    my_list = []
    for everyone in employee.readlines():
        everyone.rstrip('\n')
        surname, salary = everyone.split()
        # print(everyone)
        # print(salary)
        if float(salary) < 20000.00:
            print(surname)
        my_sum = 0
        average = 0
        fl = float(salary)
        my_list.append(fl)
    print(my_list)
    for line in my_list:
        my_sum += line
        average = my_sum / len(my_list)
    # print(my_sum)
    print(average)


revenue = int(input('Введите значение прибыли за пероид (в руб.): '))
expenses = int(input('Введите значение расходов за период (в руб.): '))

if revenue > expenses:
    profit = revenue-expenses
    print(f"Вы получили прибыть в размере {profit} руб. Рентабельность компании составляет: {profit/revenue:.2%}")
    staff = int(input('Введите количество сотрудников: '))
    print(f"На одного сотрудника приходится {profit/staff:.2f} рублей прибыли")
else:
    print(f"Вы получили убыток в размере - {expenses-revenue} руб.")

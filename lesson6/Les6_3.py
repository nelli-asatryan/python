class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')


    def get_total_income(self):
        _income = self._income["wage"] + self._income["bonus"]
        print(f'Доход сотруднка с учетов премии составляет: {_income}')


p = Position('Александр', 'Попов', 'менеджер', '20', '10')
print(p.get_full_name(), p.get_total_income())
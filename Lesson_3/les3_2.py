# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.


def confid (**data):
    for key, value in data.items():
        return data

print(confid(name='Maria', surname='Ivanova', date_of_birth='01.01.2020', city='London', email='test@gmail.com', tel='9834857294'))

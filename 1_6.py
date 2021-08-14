while True:
    days = 1
    a = float(input("Старотовый результат: "))
    b = float(input("Финальный результат: "))
    if a <= 0 or b <0:
        print("Результат должен быть больше нуля. Старотовое значение !=0")
    else:
        while a < b:
            a += a+0.1
            days += 1
        print(f"Спортсмен добьется результата на {days} дней")
        break

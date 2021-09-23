
Time = int(input('Введите секунды: '))
hour = int(Time//3600)
minute = int((Time%3600)/60)
sec = int(Time%60)
if Time > 0:
    print(f"Формат изменен: {hour:02d}:{minute:02d}:{sec:02d}")
else:
    print("Нет результата: Введите положительное число")

# ---------------------------------------------

Time = int(input('Введите секунды: '))
hour = Time//3600
minute = Time//60 - hour * 60
sec = Time%60
print(f"{hour:02d}:{minute:02d}:{sec:02d}")




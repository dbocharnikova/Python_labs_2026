# Запрашиваем секунды
total_seconds=int(input("Введите количество секунд (целое, неотрицательное): "))
if total_seconds>=0:
    # Проводим вычисления (прописываем арифметические выражения)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    # Выводим результат
    print(f"{hours} ч {minutes} мин {seconds} c")
else:
    print("Ошибка. Некорректное количество секунд")
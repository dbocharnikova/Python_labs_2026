# Запрашиваем данные
total=int(input("Введите общее количество деталей (неотрицательное): "))
capacity=int(input("Введите количество деталей в контейнере (положительное): "))
# Проводим вычисления
all=total//capacity
remains=total%capacity
volume=(total+capacity-1)//capacity
# Выводим результаты
print(f"Полные контейнеры: {all}")
print(f"Остаток деталей: {remains}")
print(f"Всего контейнеров: {volume}")
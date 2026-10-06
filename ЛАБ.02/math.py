# импортируем значение pi из библеотеки math
from math import pi
print(pi)
# Проводим вычисления по формулам:
#Длина окружности: 2 * pi * radius
#Площадь круга: pi * radius ** 2
radius=float(input("Введите радиус (см, положительные): "))
long=2*pi*radius
square=pi*radius**2
# Выводим результаты
print(f"Длина окружности: {long:.2f}")
print(f"Площадь круга: {square:.2f}")

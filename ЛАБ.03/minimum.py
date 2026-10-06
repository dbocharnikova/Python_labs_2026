# Запрашиваем данные
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
# Ищем мимимальное значение через if/elif/else
if a<=b and a<=c:
    minimum=a
elif b<=a and b<=c:
    minimum=b
else:
    minimum=c
# Выводим результат
print(minimum)
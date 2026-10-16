# Запрашивем данные
data=input("Введите целые числа через пробел: ").split()
# преобразуем в список целых чисел
original=[int(x) for x in data]
# создаем новый список для преобразованных значений
new=[]
# в исходном списке применяем модуль к отрицательным числам
for number in original:
    if abs(number) not in new:
        if number<0:
            new.append(abs(number))  # модуль числа
        else:
            new.append(number) # неотрицательные числа оставляем как есть
        # выводим списки
print(f"Новый список: {new}")
print(f"Исходный список: {original}")
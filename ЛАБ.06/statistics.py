# запрашиваем числа, считываем строку и разбиваем ее по пробелам в список строк
data=input("Введите целые числа через пробел: ").split()
# проверяем на пустой ввод
if not data:
    print("Нет данных")
else:
    # преобразуем строки в целые числа
    numbers=[int(x) for x in data]
    count=len(numbers) # количество элементов
    total=sum(numbers) # сумма элементов
    # поиск минимума и максимума вручную
    minimum=numbers[0]
    maximum=numbers[0]
    for num in numbers:
        if num<minimum:
            minimum=num
        if num>maximum:
            maximum=num
            # вычисляем среднее значение
    average=total/count
    # выводим результат
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")

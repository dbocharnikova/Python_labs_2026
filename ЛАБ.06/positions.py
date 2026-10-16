# запрашиваем числа
data=input("Введите целые числа через пробел: ").split()
if not data:
    print("Нет данных")
else:
    numbers=[int(x) for x in data]
    # находим максимум вручную
    maximum=numbers[0]
    for num in numbers:
        if num>maximum:
            maximum=num
    # используем enumerate() для обхода с индексами
    positions=[]
    for i, num in enumerate(numbers):
        if num==maximum:
            positions.append(i)
    # выводим результат
    print(positions)


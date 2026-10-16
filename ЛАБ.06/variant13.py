# запрашиваем числа
data=input("Введите целые числа через пробел: ").split()
# преобразование в список целых чмсел
numbers=[int(x) for x in data]
# создание списка значений по условию (отрицательные и нечетные)
result=[]
for num in numbers:
    if num<0 and num%2!=0:
        result.append(num)
# подсчитываем количество и сумму
count=len(result)
total=sum(result)
# создаем отсортированнуб копию (по возрастанию)
copy=sorted(result)
# выводим результат
print(f"Выборка: {result}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Сортированная копия: {copy}")

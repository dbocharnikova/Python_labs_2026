# Запрашиваем число
number=int(input("Введите число от 0 до 100: "))
# Прописываем условия и вывод результата
if number<0 or number>100:
    print("Ошибка диапазона")
elif 0<=number<=4:
    print("Начало")
elif 5<=number<=94:
    print("Загрузка")
elif 95<=number<=100:
    print("Завершение")

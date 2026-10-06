# Запрашиваем данные
price=int(input("Цена одной тетради (руб., целая, неотрицательная): "))
if price>=0:
    count=int(input("Количество тетрадей (целое, неотрицательное): "))
    if count>=0:
        paid=int(input("Переданная сумма: "))
        if paid>=price*count:
            # Проводим вычисления
            cost=price*count
            change=paid-cost
            # Выводим результат
            print("")
            print(f"Стоимость: {cost} руб.")
            print(f"Сдача: {change} руб.")
        else:
            print("Ошибка. Некорректная сумма")
    else:
        print("Ошибка. Некорректное количество")
else:
    print("Ошибка. Некорректная цена")

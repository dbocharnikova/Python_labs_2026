# Запрашиваем значения
order=input("Введите название заказа: ")
customer=input("Введите имя заказчика: ")
first_name=input("Введите название первой позиции: ")
first_quantity=int(input("Введите количество первой позиции (целое, неотрицательное): "))
first_price=float(input("Введите цену первой позиции (неотрицательное, дробное): "))
second_name=input("Введите название второй позиции: ")
second_quantity=int(input("Введите количество второй позиции (целое, неотрицательное): "))
second_price=float(input("Введите цену второй позиции (неотрицательное, дробное): "))
delivery=float(input("Введите стоимость доставки (неотрицательна): "))
sum=float(input("Введите внесенную сумму (не меньше стоимости обеих позиций с доставкой): "))
# Проводим вычисления
first=first_quantity*first_price
second=second_quantity*second_price
not_delivery=first+second
with_delivery=not_delivery+delivery
quantity=first_quantity+second_quantity
change=sum-with_delivery
# Выводим заказ
print("")
print(f"Заказ: {order}")
print(f"Заказчик: {customer}")
print("")
print(f"{first_name} | {first_quantity} | {first_price:.2f} | {first:.2f}")
print(f"{second_name} | {second_quantity} | {second_price:.2f} | {second:.2f}")
print("")
print(f"Стоимость товаров без доставки: {not_delivery:.2f} руб")
print(f"Общая сумма с доставкой: {with_delivery:.2f} руб")
print(f"Общее количество единиц: {quantity}")
print(f"Сдача: {change:.2f} руб")
# Добавляем скидку
discount=int(input("Введите скидку (от 0 до 100): "))
sum_discount=not_delivery*0.01*discount
print(f"Cкидка: {sum_discount:.2f} руб")
# Выводим итог со скидкой
cost=with_delivery-sum_discount
print(f"Итог: {cost:.2f} руб")
# Запрашиваем данные
first=float(input("Введите первое число: "))
second=float(input("Введите второе число: "))
operation=input("Введите операцию (+,-,*,/): ")
# Прописываем подсчет и условия и выводим результат
if operation=="+":
    result=first+second
    print(f"{result:.2f}")
elif operation=="-":
    result=first-second
    print(f"{result:.2f}")
elif operation=="*":
    result=first*second
    print(f"{result:.2f}")
elif operation=="/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        result=first/second
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")

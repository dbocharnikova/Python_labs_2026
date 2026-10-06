# запрашиваем данные
n=int(input("Введите цело число n (n>=2): "))
# проверка целого простого числа
if n<2:
    print("Не простое")
else:
    simple=True
    divisor=2
#  прописывем бесконечный цикл и условия, ищем делитель
    while divisor*divisor<=n:
        if n%divisor==0:
            simple=False
            break
        divisor+=1
# выводим результат
    if simple:
        print("Простое")
    else:
        print("Составное")

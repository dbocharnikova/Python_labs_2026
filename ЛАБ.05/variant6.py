# запрашиваем строку
text=input("Введите строку: ")
words=text.split() # разбиваем строку по пробелам
list=[] # список подходящих слов
# обрабатываем каждое слово
for word in words:
    clean=word.strip(",.!?:").lower()
   # пропускаем пустые результаты
    if not clean:
        continue
    # проверка условия длины = 4
    if len(clean)==4:
        list.append(clean)
# выводим результат
if list:
    for i in list:
        print(i)
    print(f"Количество: {len(list)}")
else:
    print("Нет совпадений")
    print("Количество: 0")

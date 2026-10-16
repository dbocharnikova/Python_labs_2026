# запрашиваем текст
text=input("Введите текст: ")
# очищаем строку
clean=text.replace(" ", "").lower()
# проверяем на пустую строку
if not clean:
    print("Нет текста")
else:
    palindrome=True
    length=len(clean)
    # прописываем выполнение цикла 2 раза
    for i in range(length//2):
        # сравниваем символ с начала и с конца
        if clean[i] != clean[length-1-i]:
            palindrome=False # несовпадение-не палиндром
            break
    # выводим результат
    if palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")

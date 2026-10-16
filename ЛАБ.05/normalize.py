# Запрашиваем текст
text=input("Введите текст: ")
original=len(text) # высчитываем исходную длину
normalize=" ".join(text.split()) # нормализируем
new=len(normalize) # вычисляем новую длину
words=len(normalize.split()) # считаем кеоличество слов
# выводим результат
print(f"Исходная длина: {original}")
print(f"Новая длина: {new}")
print(f"Нормализированный текст: {normalize}")
print(f"Количество слов: {words}")

from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome
def main():
    # Запрашиваем целое число
    num_str=input("Введите целое число: ")
    number=int(num_str)
    # Запрашиваем строку чисел
    print(f"Сумма цифр числа {number}: {sum_digits(number)}")
    numbers_str=input("Введите числа через пробел: ")
    if numbers_str.strip():
        numbers_list=list(map(int,numbers_str.split()))
    else:
        numbers_list=[]
    avg_result=average(numbers_list)
    if avg_result is None:
        print("Среднее значение: Нет данных")
    else:
        print(f"Среднее значение: {avg_result}")
    # Запрашиваем произвольный текст
    text=input("Введите произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(text)}'")

    # Дополнительно: проверка на палиндром
    print(f"Является текст палиндромом: {is_palindrome(text)}")

# Вариант 8: Запрашиваем порог и применяем функцию к введенному ранее списку
    threshold_str=input("Введите порог (целое неотрицательное число): ")
    threshold=int(threshold_str)

    selected=select_numbers(numbers_list, threshold)
    print(f"Исходный список: {numbers_list}")
    print(f"Числа, модуль которых не больше {threshold}: {selected}")

# Точка входа.
if __name__=="__main__":
    main()

from functions import average, normalize_text, sum_digits, select_numbers

# Базовые проверки
assert sum_digits(0)==0
assert sum_digits(507)==12
assert sum_digits(-507)==12
assert average([]) is None
assert average([2, 4, 6])==4
assert normalize_text(" ПРИВЕТ  мир ")=="привет мир"
assert normalize_text("   ")==""

# Дополнительные проверки для варианта 8
assert select_numbers([-5, 0, 2, 5], 2)==[0, 2]
assert select_numbers([], 5)==[]
assert select_numbers([-3, -2, 2, 3], 2)==[-2, 2]  # Проверка границы
assert select_numbers([2, 5, 2], 2)==[2, 2]

source_list=[-5, 0, 2, 5]
source_copy=source_list.copy()  # сохраняем копию
select_numbers(source_list, 2)  # вызываем функцию
assert source_list==source_copy  # проверка оригинала

# Проверка дробного среднего
actual=average([1, 2])
expected=1.5
assert abs(actual-expected)<1e-9

print("Все проверки пройдены успешно")

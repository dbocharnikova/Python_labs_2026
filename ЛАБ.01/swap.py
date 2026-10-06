# запрашиваем значения двух аудиторий
first_room=input("Введите название первой аудитории: ")
second_room=input("Введите название второй аудитории: ")
# исходные значения
print(f"first room={first_room}, second room={second_room}")
# меняем значения местами через третью переменную
third=first_room
first_room=second_room
second_room=third
# значения после обмена
print(f"first room={first_room}, second room={second_room}")

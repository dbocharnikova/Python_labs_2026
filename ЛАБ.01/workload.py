# Запрашиваем данные по первому предмету
first_subject=str(input("Введите первый предмет: "))
first_lesson=int(input("Введите количество занятий по предмету в неделю: "))
if first_lesson<0:
    print("Ошибка. Некорректное количество занятий")
else:
    first_time=int(input("Введите продолжительность одного занятия (в минутах): "))
    if first_time<=0:
        print("Ошибка. Некорректное количество часов")
    else:
        # Запрашиваем данные по второму предмету
        second_subject=str(input("Введите второй предмет: "))
        second_lesson=int(input("Введите количество занятий по предмету в неделю: "))
        if second_lesson<0:
            print("Ошибка. Некорректное количество занятий")
        else:
            second_time=int(input("Введите продолжительность одного занятия (в минутах): "))
            if second_time<=0:
                print("Ошибка. Некорректное количество часов")
            else:
                # Запрашиваем доступное время на неделю
                time = float(input("Доступное время на неделю (в часах): "))
                if time<first_lesson*first_time+second_lesson*second_time:
                    print("Ошибка. Некорректное время")
                else:
                    # Проводим вычисления
                    first_minutes=first_lesson*first_time
                    second_minutes=second_lesson*second_time
                    minutes=first_minutes+second_minutes
                    hours=minutes/60
                    free_time=time-hours
                    weeks=hours*4
                    # Выводим карточку
                    print("")
                    print("Учебная нагрузка")
                    print(f"{first_subject}: {first_minutes} мин")
                    print(f"{second_subject}: {second_minutes} мин")
                    print(f"Общая нагрузка: {minutes} мин, {hours:.2f} ч")
                    print(f"Остаток свободного времени: {free_time:.2f} ч")
                    print(f"Нагрузка за 4 недели: {weeks:.2f} ч")

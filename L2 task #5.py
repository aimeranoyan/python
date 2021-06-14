# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

some_list = [7, 5, 3, 3, 2]
print(f"Rating - {some_list}")
figure = int(input("Enter new rate: "))
for i in range(len(some_list)):
    if some_list[i] == figure:
        some_list.insert(i + 1, figure)
        break
    elif some_list[0] < figure:
        some_list.insert(0, figure)
    elif some_list[-1] > figure:
        some_list.append(figure)
    elif some_list[i] > figure > some_list[i + 1]:
        some_list.insert(i + 1, figure)
print(f"Updated rating: {some_list}")

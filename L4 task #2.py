# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

original_list = [1, 10, 5, 300, 400, 44, 4, 6, 3, 123, 99]
new_list = [el for el in range(1, len(original_list)) if original_list[el] > original_list[el - 1]]
print(new_list)

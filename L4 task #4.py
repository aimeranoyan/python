# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор. Пример исходного списка:
# [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]. Результат: [23, 1, 3, 10, 4, 11]

sample_list = [1, 56, 7, 33, 1, 7, 8, 7, 90, 87, 90, 78, 33, 56, 11, 12]
unique_list = [el for el in sample_list if sample_list.count(el) == 1]
print(unique_list)

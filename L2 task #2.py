# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

some_list = []
some_list = [item for item in input("Enter items for list : ").split()]
for i in range(len(some_list)):
    n = 2*i
    if (len(some_list) // 2 == 1 and n == len(some_list) - 2) or i >= len(some_list) // 2:
        break
    else:
        tmp = some_list[n]
        some_list[n] = some_list[n+1]
        some_list[n+1] = tmp

print(some_list)
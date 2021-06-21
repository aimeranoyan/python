# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
with open('some_numbers.txt', 'w+') as f_n:
    r_list = random.sample(range(23, 999), 11)
    lines = " ".join(str(x) for x in r_list)

    f_n.write(lines)
    f_n.seek(0)
    num_list = f_n.read()

    print(f'Total figure: {sum(int(n) for n in num_list.split())}')
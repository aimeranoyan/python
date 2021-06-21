# Создать (не программно) текстовый файл со следующим содержимым: One — 1 / Two — 2 / Three — 3 / Four — 4.
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
with open('1234.txt', 'r') as f_num, \
        open('1234_rus.txt', 'w') as f_num_rus:
    def replace_fun(target, val):
        for i, j in val.items():
            target = target.replace(i, j)
            val = None
        return target

    num_val = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }

    lines = f_num.read()
    lines = replace_fun(lines, num_val)

    print(lines)

    f_num_rus.write(lines)

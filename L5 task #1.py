# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
with open("some_text.txt", "w") as f_text:
    lines = input("Enter something: ").split()
    for line in lines:
        f_text.writelines("%s\n" % line)
        if line == ' ':
            break

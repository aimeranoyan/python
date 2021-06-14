# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input("Your text goes here: ")
user_word = []
level = 1
for i in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f"{level}. {user_word[i]}")
        level += 1
    else:
        print(f"{level}. {user_word[i][0:10]}")
        level += 1

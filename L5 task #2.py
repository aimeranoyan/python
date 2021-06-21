# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# saving strings right in the script:
with open('meow.txt', 'w') as f_meow:
    lines = 'boom, bang, doom\nsun is shining\nthe weather is sweet: thank you, bob marley'.split('\n')
    for line in lines:
        f_meow.writelines(line)

    print(f'Amount of strings: {len(lines)}\nAmount of words in strings:')
    text = [f'{print(str(i + 1) + "> " + str(len(lines[i].split())) + " words")}' for i in range(len(lines))]

# saving strings with creating a file:
# with open('meow2.txt', 'r') as f_meow2:
# lines2 = f_meow2.readlines()
# print(f'Amount of strings: {len(lines2)}\nAmount of words in strings:')
# text = [f'{print(str(i + 1) + "> " + str(len(lines2[i].split())) + " words")}' for i in range(len(lines2))]

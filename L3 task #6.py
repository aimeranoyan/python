def int_func(*args):
    word = input('Enter a string: ').split()
    new = ''
    for i in word:
        new = f'{new} {i.upper()[0]}{i[1:]}'
    return print(new[1:])


int_func()

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

num = input('Enter month number: ')
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
          'декабрь']

for el in range(len(months)):
    if num in months[11:2]:
        print('Walking in a winter wonderland.. Yay, winter.')
        break
    elif num in months[2:5]:
        print("And it’s spring time right here!")
        break
    elif num in months[5:8]:
        print('Summertime is meant to fall in love. Are you ready?')
        break
    else:
        print("Autumn. There’s nothing sweet about it, I’m sorry. And it’s raining. Again.")
        break


num = int((input('Enter month number: ')))

dict_months = {
    1: 'зима',
    2:'зима',
    3:'весна',
    4:'весна',
    5:'весна',
    6:'лето',
    7:'лето',
    8:'лето',
    9:'осень',
    10:'осень',
    11:'осень',
    12:'зима'
}

print(dict_months.get(num))
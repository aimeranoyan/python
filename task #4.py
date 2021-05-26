number = int(input('Enter your number: '))
figure = 0
while number != 0:
    if figure < number % 10:
        figure = number % 10
    number = number // 10

print(figure)

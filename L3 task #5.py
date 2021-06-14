def my_sum():
    history_sum = 0
    Q = False
    the_type = 'Current'
    while Q == False:
        number = input('Enter the digits or Q for termination: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] in ['Q', 'q']:
                Q = True
                the_type = 'Final'
                break
            else:
                res = res + int(number[i])
        history_sum = history_sum + res
        print(f'{the_type} sum: {history_sum}')


my_sum()

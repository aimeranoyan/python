def my_func(name=input('Enter a name: '), surname=input('Enter a lastname: '), year=input('Enter the year of birth: '),
            city=input('Enter the city: '), email=input('Enter email: '), telephone=input('Enter a phone number: ')):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func())

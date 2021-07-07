# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Enter values and click "Enter" - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Not today, i see a string and boolean")
                y_or_n = input(f'Huh, again? Click "Y" or "N" ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Completed'
                else:
                    return f'Completed'


try_except = Error(1)
print(try_except.my_input())

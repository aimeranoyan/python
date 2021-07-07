# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Sum is equal to:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i\n {"-"*15}'

    def __mul__(self, other):
        print(f'Product of numbers is equal to:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i\n {"-"*15}'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i\n {"-"*15}'


z_1 = ComplexNumber(3, -5)
z_2 = ComplexNumber(100, 42)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
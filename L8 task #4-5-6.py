class TechWarehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price per unit': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Enter name: ')
            unit_p = int(input(f'Enter price per unit: '))
            unit_q = int(input(f'Enter quantity: '))
            unique = {'Model': unit, 'Price per unit': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Input error'

        print(f'To exit - Q, To continue - Enter')
        q = input(f'>. ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Whole warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return TechWarehouse.reception(self)


class Printer(TechWarehouse):
    def to_print(self):
        return f'to print {self.numb} copies'


class Scanner(TechWarehouse):
    def to_scan(self):
        return f'to scan {self.numb} copies'


class Copier(TechWarehouse):
    def to_copier(self):
        return f'to copier  {self.numb} copies'


first = Printer('Samsung', 1300, 2, 12)
second = Scanner('Apple', 1600, 4, 14)
third = Copier('Sony', 1230, 3, 11)
print(first.reception())
print(second.reception())
print(third.reception())
print(first.to_print())
print(third.to_copier())
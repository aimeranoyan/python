# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle

for el in count(99):
    if el > 107:
        break
    else:
        print(el)

original_list = ['sun', 'is', 'shining']

i = 0
for el in cycle(original_list):
    if i > 5:
        break
    print(el)
    i += 1

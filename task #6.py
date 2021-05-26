a = int(input())
b = int(input())
n = 1
while a < b:
    a = a * 1.1
    n += 1
    if a >= b:
        break
print(n)
def div(*args):
    try:
        x = int(input("Enter the dividend: "))
        y = int(input("Enter the divisor: "))
        ratio = x / y
    except ZeroDivisionError:
        return print("Don't divide by zero")
    return print(ratio)


div()

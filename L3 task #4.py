def program(x, y):
    result = 1
    for i in range(-y):
        result *= 1 / x
    return result


print(program(13, -3))

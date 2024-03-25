def delta(a: int, b: int, c: int):
    result = (b ** 2) - (4 * a * c)
    return result


print(delta(3, 5, 2))


def bhaskara(a: int, b: int, c: int):  
    delta_result = delta(a, b, c)
    if (delta_result < 0):
        return "Delta Negativo"
    x1 = (-b + (delta_result ** (1/2))) / (2 * a)
    x2 = (-b - (delta_result ** (1/2))) / (2 * a)
    return f'x1={round(x1, 2)}, x2={round(x2, 2)}'


print(bhaskara(7, 3, 4))

print(bhaskara(1, 5, 2))

print(bhaskara(3, 10, 2))

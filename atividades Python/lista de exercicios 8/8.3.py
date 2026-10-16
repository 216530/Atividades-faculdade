def tipo_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Inválido"
    if a >= b + c or b >= a + c or c >= a + b:
        return "Inválido"
    if a == b == c:
        return "Equilátero"
    if a == b or a == c or b == c:
        return "Isósceles"
    return "Escaleno"


print(tipo_triangulo(3, 3, 3))
print(tipo_triangulo(5, 5, 8))
print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(1, 2, 3))
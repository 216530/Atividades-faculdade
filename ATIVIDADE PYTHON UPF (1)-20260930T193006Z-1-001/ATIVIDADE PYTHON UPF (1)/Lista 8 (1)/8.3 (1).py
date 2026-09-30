'''
3. Elabore uma função que receba três valores
representando os lados de um triângulo
e retorno o tipo do triângulo. 
'''

def tipo_triangulo(a, b, c):
    # Testa se é triângulo
    if (a + b) <= c or (b + c) <= a or (a + c) <= b :
        return("Não forma triângulo")

    # Verifica tipo de triângulo
    if a == b and b == c :
        return("Equilátero")
    elif a != b and b != c and a != c :
        return("Escaleno")
    else :
        return("Isósceles")

print(tipo_triangulo(5, 5, 5))  # Equilátero
print(tipo_triangulo(5, 5, 3))  # Isósceles
print(tipo_triangulo(3, 4, 5))  # Escaleno
print(tipo_triangulo(1, 2, 5))  # Não é triângulo

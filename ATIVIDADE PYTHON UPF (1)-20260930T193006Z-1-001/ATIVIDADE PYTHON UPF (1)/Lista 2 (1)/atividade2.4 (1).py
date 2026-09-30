'''
Leia 3 valores inteiros e diferentes e a seguir,
encontre e exiba o maior, o menor e o intermediário.
'''

a = int(input('Insira o primeiro valor:'))
b = int(input('Insira o segundo valor:'))
c = int(input('Insira o terceiro valor:'))

if (a == b) or (a == c) or (c == b):
    print('Escreva valores diferentes!')
else:
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
meio = (a + b + c) - maior -menor
print('Maior: ', maior)
print('Menor: ', menor)
print('Meio:', meio)
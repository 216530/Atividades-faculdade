'''
Leia dois valores inteiros e diferentes
em seguida apresenta o MAIOR e o MENOR número
'''

valor1 = int(input('Digite um número inteiro:'))
valor2 = int(input('Digite outro número inteiro:'))

if valor1 != valor2:
    if valor1 > valor2:
        print(valor1,'é maior que', valor2)
    else:
        print(valor2,'é maior que', valor1)
else:
    print('Valores iguais, digite novamente')
    
    

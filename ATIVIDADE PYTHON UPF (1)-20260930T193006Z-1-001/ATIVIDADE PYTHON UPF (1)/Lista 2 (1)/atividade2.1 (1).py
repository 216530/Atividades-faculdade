'''
Leia um valor inteiro e em seguida apresenta
uma mensagem se o número é PAR ou IMPAR.
'''

valor = int(input('Digite um valor: '))

if valor % 2 == 0:
    print('Número PAR')
else:
    print('Número ÍMPAR')
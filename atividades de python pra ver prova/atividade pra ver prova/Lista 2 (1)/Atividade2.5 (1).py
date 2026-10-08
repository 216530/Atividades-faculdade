'''
Leia a idade de um nadador e a seguir classifique-o em uma das seguintes categorias:
 infantil A 5 - 7 anos 
 infantil B 8-10 anos
 juvenil A 11-13 anos 
 juvenil B 14-17 anos 
 adulto maiores de 18 anos 
'''

idade = int(input('Insira a idade do(a) nadador(a):'))

if idade >= 5 and idade <= 7:
    print('Classificação: INFANTIL A')
elif idade >= 8 and idade <= 10:
    print('Classificação: INFANTIL B')
elif idade >= 11 and idade <= 13:
    print('Classificação: JUVENIL A')
elif idade >= 14 and idade <= 17:
    print('Classificação: JUVENIL B')
elif idade > 18:
    print('Classificação: ADULTO')
else:
    print('Não possui idade mínima para nadar')
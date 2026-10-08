'''
1. Desenvolva um algoritmo que exiba a tabuada de um número qualquer escolhido pelo usuário.
'''
tabuada = int(input('Escreva qual tabuada você deseja ver(1-10): '))

for x in range(11):
    print(f'{x} x {tabuada} = {tabuada * x}')
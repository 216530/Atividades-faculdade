'''
3. Escreva um algoritmo que lê dois números e em seguida
exibe os números pares e os números ímpares existentes entre estes dois números.
'''
numIn = int(input('Escreva o primeiro algorismo: '))
numFin = int(input('Escreva o segundo algorismo: ')) 



for x in range(numIn, numFin + 1):
    if x % 2 == 0:
        print(f'Número par: {x}')
    else:
        print(f'Número ímpar:{x}')
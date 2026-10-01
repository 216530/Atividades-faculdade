'''
1. Elabore uma aplicação em Python que implemente um jogo de Adivinhar o Número de 0 a 100 com as seguintes características:

para geração do número oculto, utilizar a biblioteca Random
o jogador terá um número de chances para acertar o número. Se não conseguir, a aplicação deverá mostrar qual era o número oculto
a cada jogada, a aplicação deverá informar o número de tentativas restantes e se o número oculto é maior ou menor do o palpite do jogador
'''

import random

chances = 5
numero = random.randint(0, 100)

print('Adivinhe o número!')

while True :
    print(f'Você tem {chances} chances')
    palpite = int(input('Qual o seu palpite? '))
    if palpite == numero:
        print('Parabéns! Você acertou!')
        break
    
    elif palpite < numero:
        print('É um número maior')
        
    elif palpite > numero:
        print('É um número menor')
        
    chances -= 1
    
    if chances == 0:
        print(f'Você perdeu :( O número era {numero}')
        break
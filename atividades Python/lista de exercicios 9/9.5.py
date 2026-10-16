'''
5. Jogo de Adivinhação de Palavras. Desenvolva um jogo que possibilite ao usuário tentar adivinhar palavras com base nas dicas fornecidas. O jogo deverá funcionar da seguinte maneira:

O jogo poderá desenvolvido com uma lista de palavras Hard Coded
Você receberá uma dica sobre a palavra a ser adivinhada.
Você terá um número limitado de tentativas para adivinhar a palavra correta.
Cada vez que você faz uma tentativa, o jogo informa se a palavra que você inseriu está correta ou não.
Se você adivinhar corretamente a palavra dentro do número máximo de tentativas, você vence o jogo. Caso contrário, o jogo termina e a palavra correta é revelada.
Exemplo: Dica: Uma linguagem de programação poderosa. Palavra: python
'''

palavras = {
    'banana': 'Uma fruta amarela com pintas pretas.',
    'python': 'Uma linguagem de programação poderosa',
    'praia': 'Um lugar com areia e água salgada'
            }

import random

def jogo():
    palavra_secreta = random.choice(list(palavras.keys()))
    dica = palavras[palavra_secreta]
    tentativas = 3
    
    while tentativas > 0:
        print('Dica:', dica)
        palpite = input('Adivinhe a palavra: ').lower()
        if palpite == palavra_secreta:
            print('Parabéns, você acertou')
            return
        else:
            tentativas -= 1
            print(f'Você Errou! {tentativas} restantes')
    print('0 tentativas restantes')
    
jogo()
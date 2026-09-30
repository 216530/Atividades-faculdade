'''
2. Desenvolva uma aplicação que implemente o Jogo da Forca e que,
a cada execução, escolha uma palavra aleatória de uma lista de palavras.
O jogador poderá errar 5 vezes antes de ser "enforcado". A lista de palavras
pode ser obtida de um arquivo ou Hard-coded. Abaixo, é sugerida uma interface
no console para interação com o programa. 
'''

import random


palavras = ["python", "computador", "logica", "programacao", "algoritmo", "teclado"]


palavra_secreta = random.choice(palavras)


letras_descobertas = []
for letra in palavra_secreta:
    letras_descobertas.append("_")


erros = 0
limite_erros = 5


while erros < limite_erros and "_" in letras_descobertas:
    print() 
    palpite = input("Digite uma letra: ").lower()
    
    
    if palpite in palavra_secreta:
        
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == palpite:
                letras_descobertas[i] = palpite
        
        
        print("A palavra é:", " ".join(letras_descobertas))
        
    else:
        erros += 1
        print(f"-> Você errou pela {erros}ª vez. Tente de novo!")



if "_" not in letras_descobertas:
    print(f"Você ganhou! A palavra era: {palavra_secreta}")
else:
    print(f"Você foi enforcado! A palavra era: {palavra_secreta}")
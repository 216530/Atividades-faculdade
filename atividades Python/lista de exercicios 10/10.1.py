import random

numero = random.randint(0, 100)
chances = 7
tentativas = 0
acertou = False

print("=== JOGO DE ADIVINHAR O NUMERO ===")
print("Tente adivinhar o numero entre 0 e 100")
print("Voce tem", chances, "chances")

while tentativas < chances and not acertou:
    try:
        palpite = int(input("\nDigite seu palpite: "))
    except ValueError:
        print("Digite um numero valido!")
        continue

    if palpite < 0 or palpite > 100:
        print("O numero tem que ser entre 0 e 100!")
        continue

    tentativas += 1
    restantes = chances - tentativas

    if palpite == numero:
        acertou = True
        print("Parabens! Voce acertou em", tentativas, "tentativa(s)!")
    elif palpite < numero:
        print("O numero oculto e MAIOR que", palpite)
        print("Tentativas restantes:", restantes)
    else:
        print("O numero oculto e MENOR que", palpite)
        print("Tentativas restantes:", restantes)

if not acertou:
    print("\nSuas chances acabaram! O numero oculto era", numero)

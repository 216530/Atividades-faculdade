import random

numero = random.randint(1, 100)
tentativas = []
anterior = None

print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))

    if palpite == numero:
        tentativas.append((palpite, "Acertou!", "—"))
        print("Parabéns! Você acertou!")
        break

    dica = "Maior" if numero > palpite else "Menor"

    # proximidade
    if anterior is None:
        prox = "—"
    else:
        atual_dist = abs(numero - palpite)
        anterior_dist = abs(numero - anterior)
        prox = "Mais próximo" if atual_dist < anterior_dist else "Mais distante"

    tentativas.append((palpite, dica, prox))
    anterior = palpite

    print(f"Errado! Tente um número {dica}!")

# Resumo final
print("\n===== HISTÓRICO =====")
for i, (p, d, pr) in enumerate(tentativas, 1):
    print(f"Jogada {i}: palpite={p}, dica={d}, proximidade={pr}")

print(f"Total de tentativas: {len(tentativas)}")
